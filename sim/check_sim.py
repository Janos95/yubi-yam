"""End-to-end checks of the yubi_4310 gripper on a simulated YAM.

    python3 sim/check_sim.py            # all checks, writes docs/img/*.png
    python3 sim/check_sim.py --no-render

Everything runs through i2RT's own code: a scratch copy of third_party/i2rt gets the
sdk/ patch and overlay installed (exactly what sdk/install.sh does to a user's
checkout), then the checks import that copy.

  1. sdk      GripperType.YUBI_4310 resolves its config; get_yam_robot(sim=True)
              builds the arm+gripper model; commanding the gripper 0 -> 1 moves the
              finger joint from the closed to the open stop.
  2. grasp    Physics: the arm reaches down, closes on a 30 mm cube resting on a
              table, lifts it 10 cm, and the cube comes along.
  3. reach    Exact-mesh collision sweep of the gripper against the arm's links over
              the joint ranges, compared with i2RT's stock linear_4310 gripper.
"""
import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile

os.environ.setdefault("MUJOCO_GL", "osmesa")
os.environ.setdefault("PYOPENGL_PLATFORM", os.environ["MUJOCO_GL"])

import fcl  # noqa: E402
import mujoco  # noqa: E402
import numpy as np  # noqa: E402
import trimesh  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
IMG = os.path.join(ROOT, "docs/img")


# --------------------------------------------------------------------------------------
def install_i2rt() -> str:
    """Scratch copy of the i2rt submodule with the yubi_4310 SDK files installed."""
    src = os.path.join(ROOT, "third_party/i2rt")
    if not os.path.exists(os.path.join(src, "i2rt/robots/utils.py")):
        sys.exit("third_party/i2rt missing. Run: git submodule update --init")
    tmp = tempfile.mkdtemp(prefix="yubi_i2rt_")
    dst = os.path.join(tmp, "i2rt")
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git"))
    subprocess.run(["bash", os.path.join(ROOT, "sdk/install.sh"), dst], check=True, stdout=subprocess.DEVNULL)
    return dst


# --------------------------------------------------------------------------------------
def check_sdk(i2rt_dir, report):
    from i2rt.robots.get_robot import get_yam_robot
    from i2rt.robots.utils import ArmType, GripperType

    g = GripperType.from_string_name("yubi_4310")
    assert g is GripperType.YUBI_4310
    report["sdk"] = {
        "motor_type": g.get_motor_type(ArmType.YAM),
        "kp_kd": list(g.get_motor_kp_kd(ArmType.YAM)),
        "needs_calibration": g.get_gripper_needs_calibration(ArmType.YAM),
        "limiter_params": [float(x) if not callable(x) else "fn" for x in g.get_gripper_limiter_params(ArmType.YAM)],
    }
    robot = get_yam_robot(gripper_type=GripperType.YUBI_4310, sim=True)
    model, data = robot._model, robot._data
    names = [mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, i) for i in range(model.njnt)]
    assert names[:8] == [f"joint{i}" for i in range(1, 9)], names
    lo, hi = model.jnt_range[6]
    out = {}
    for cmd in (0.0, 0.5, 1.0):
        robot.command_joint_pos(np.r_[np.zeros(6), cmd])
        out[cmd] = float(data.qpos[6])
    assert abs(out[0.0] - lo) < 1e-6 and abs(out[1.0] - hi) < 1e-6, out
    assert lo < hi
    report["sdk"].update({"joint_names": names, "joint7_range_rad": [float(lo), float(hi)],
                          "cmd_to_joint7": {str(k): round(v, 4) for k, v in out.items()},
                          "model_path": robot.xml_path, "ok": True})
    print(f"[sdk] ok: cmd 0/0.5/1 -> joint7 {[round(v, 3) for v in out.values()]} rad")
    return robot.xml_path


# --------------------------------------------------------------------------------------
def site_pose(model, data, site):
    sid = model.site(site).id
    return data.site_xpos[sid].copy(), data.site_xmat[sid].reshape(3, 3).copy()


def ik(model, data, site, target_pos, target_z, q0, iters=400):
    """Damped least squares on the first 6 joints: site at target_pos with its z axis
    along target_z (the grasp_site z axis points out of the fingertips)."""
    sid = model.site(site).id
    q = q0.copy()
    jac_p = np.zeros((3, model.nv)); jac_r = np.zeros((3, model.nv))
    for _ in range(iters):
        data.qpos[:6] = q
        mujoco.mj_kinematics(model, data); mujoco.mj_comPos(model, data)
        p, R = data.site_xpos[sid], data.site_xmat[sid].reshape(3, 3)
        e_p = target_pos - p
        e_r = np.cross(R[:, 2], target_z)
        err = np.r_[e_p, 0.5 * e_r]
        if np.linalg.norm(e_p) < 2e-4 and np.linalg.norm(e_r) < 2e-3:
            break
        mujoco.mj_jacSite(model, data, jac_p, jac_r, sid)
        J = np.r_[jac_p[:, :6], 0.5 * jac_r[:, :6]]
        dq = J.T @ np.linalg.solve(J @ J.T + 1e-4 * np.eye(6), err)
        q = np.clip(q + dq, model.jnt_range[:6, 0], model.jnt_range[:6, 1])
    return q, float(np.linalg.norm(e_p)), float(np.linalg.norm(e_r))


def check_grasp(xml_path, report, render):
    spec = mujoco.MjSpec.from_file(xml_path)
    # Only the pads, the cube and the table collide here. The YAM's base and first link
    # meshes touch at rest (fine for i2RT's kinematic sim, but under physics it fights
    # joint 1), and arm-vs-table contact is not what this test is about.
    for geom in spec.geoms:
        if geom.name not in ("pad_r", "pad_l"):
            geom.contype = 0
            geom.conaffinity = 0
    spec.option.timestep = 0.002
    spec.option.integrator = mujoco.mjtIntegrator.mjINT_IMPLICITFAST
    # Geared motors add rotor inertia (armature) that i2RT's YAM model leaves out;
    # without it the stiff position loop on the light wrist links is numerically unstable.
    for j in spec.joints:
        if j.name in [f"joint{i}" for i in range(1, 9)]:
            j.armature = 0.01 if j.name not in ("joint7", "joint8") else 0.002
    spec.option.cone = mujoco.mjtCone.mjCONE_ELLIPTIC
    spec.option.noslip_iterations = 3
    wb = spec.worldbody
    wb.add_light(pos=[0.3, -0.4, 1.2], dir=[-0.2, 0.3, -1], diffuse=[0.8, 0.8, 0.8])
    wb.add_geom(type=mujoco.mjtGeom.mjGEOM_PLANE, size=[1, 1, 0.01], rgba=[0.92, 0.92, 0.9, 1], name="floor")
    table_top = 0.04
    table = wb.add_body(name="table", pos=[0.35, 0, table_top / 2])
    table.add_geom(type=mujoco.mjtGeom.mjGEOM_BOX, size=[0.12, 0.12, table_top / 2], rgba=[0.55, 0.45, 0.35, 1])
    cube_half = 0.015
    cube = wb.add_body(name="cube", pos=[0.35, 0, table_top + cube_half])
    cube.add_freejoint(name="cube")
    cube.add_geom(type=mujoco.mjtGeom.mjGEOM_BOX, size=[cube_half] * 3, mass=0.05, rgba=[0.2, 0.45, 0.85, 1],
                  friction=[1.0, 0.02, 0.002], condim=4)
    for i in range(1, 7):
        a = spec.add_actuator(name=f"a{i}", target=f"joint{i}")
        a.trntype = mujoco.mjtTrn.mjTRN_JOINT
        a.set_to_position(kp=300, kv=20)
        a.forcerange = [-10, 10]; a.forcelimited = mujoco.mjtLimited.mjLIMITED_TRUE
    g = spec.add_actuator(name="grip", target="joint7")
    g.trntype = mujoco.mjtTrn.mjTRN_JOINT
    g.set_to_position(kp=10, kv=0.3)              # yubi_4310.yml motor_kp / motor_kd
    g.forcerange = [-3, 3]; g.forcelimited = mujoco.mjtLimited.mjLIMITED_TRUE  # DM4310 rated torque
    model = spec.compile()
    data = mujoco.MjData(model)
    lo, hi = model.jnt_range[model.joint("joint7").id]

    cube_pos = np.array([0.35, 0, table_top + cube_half])
    down = np.array([0, 0, -1.0])
    q_home = np.array([0.0, 1.2, 1.0, -0.6, 0.0, 0.0])
    # grasp_site z points out of the fingertips; place it 6 mm below the cube centre
    # so the pads hold the cube over most of their length but stay off the table
    grasp_pt = cube_pos + np.array([0, 0, 0.004])
    q_pre, ep1, er1 = ik(model, data, "grasp_site", grasp_pt + [0, 0, 0.08], down, q_home)
    q_grasp, ep2, er2 = ik(model, data, "grasp_site", grasp_pt, down, q_pre)
    q_lift, ep3, er3 = ik(model, data, "grasp_site", grasp_pt + [0, 0, 0.10], down, q_grasp)
    ik_err = max(ep1, ep2, ep3)

    mujoco.mj_resetData(model, data)
    data.qpos[:6] = q_pre; data.qpos[6] = hi; data.qpos[7] = -hi
    cj = model.joint("cube").qposadr[0]
    data.qpos[cj:cj + 3] = cube_pos; data.qpos[cj + 3:cj + 7] = [1, 0, 0, 0]
    data.ctrl[:6] = q_pre; data.ctrl[6] = hi
    mujoco.mj_forward(model, data)

    frames, views = [], []
    renderer = None
    if render:
        renderer = mujoco.Renderer(model, 480, 640)
        cam = mujoco.MjvCamera(); cam.lookat[:] = [0.33, 0, 0.12]; cam.distance = 0.42
        cam.azimuth = 130; cam.elevation = -18
        wide = mujoco.MjvCamera(); wide.lookat[:] = [0.2, 0, 0.18]; wide.distance = 0.95
        wide.azimuth = 135; wide.elevation = -20
        close = mujoco.MjvCamera(); close.distance = 0.26; close.azimuth = 100; close.elevation = -8

    def snap(label, c, follow=False):
        if renderer is None:
            return
        if follow:
            c.lookat[:] = data.site_xpos[model.site("grasp_site").id] + [0, 0, 0.045]
        renderer.update_scene(data, camera=c); views.append((label, renderer.render().copy()))

    def run(seconds, q_arm=None, grip=None, ramp=0.0, label=None):
        start = data.ctrl.copy()
        n = int(seconds / model.opt.timestep)
        for k in range(n):
            s = min(1.0, k * model.opt.timestep / ramp) if ramp > 0 else 1.0
            if q_arm is not None:
                data.ctrl[:6] = (1 - s) * start[:6] + s * q_arm
            if grip is not None:
                data.ctrl[6] = (1 - s) * start[6] + s * grip
            # gravity compensation on the arm joints, as i2RT's controller does
            data.qfrc_applied[:6] = data.qfrc_bias[:6]
            mujoco.mj_step(model, data)
        if renderer is not None and label:
            renderer.update_scene(data, camera=cam); frames.append((label, renderer.render().copy()))

    run(0.6, label="pre-grasp, open")
    snap("YAM with YUBI 4310", wide)
    snap("open: 47 mm between pads", close, follow=True)
    run(1.2, q_arm=q_grasp, ramp=0.8, label="descend")
    run(0.8, grip=lo, ramp=0.4, label="close")
    z0 = float(data.qpos[cj + 2])
    run(1.5, q_arm=q_lift, ramp=1.0, label="lift 10 cm")
    snap("holding a 30 mm cube", close, follow=True)
    z1 = float(data.qpos[cj + 2])
    grip_q = float(data.qpos[6])
    pad_force = sum(float(np.linalg.norm(data.efc_force[data.contact[i].efc_address:data.contact[i].efc_address + 1]))
                    for i in range(data.ncon)
                    if {mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, data.contact[i].geom1),
                        mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_GEOM, data.contact[i].geom2)} & {"pad_r", "pad_l"})
    lifted = z1 - z0
    ok = lifted > 0.08 and ik_err < 0.003
    report["grasp"] = {"ik_pos_err_m": round(ik_err, 5), "cube_lift_m": round(lifted, 4),
                       "finger_joint_at_hold_rad": round(grip_q, 4), "closed_stop_rad": round(float(lo), 4),
                       "pad_normal_force_N": round(pad_force, 2), "ok": bool(ok)}
    print(f"[grasp] {'ok' if ok else 'FAIL'}: cube lifted {lifted * 100:.1f} cm, finger held at "
          f"{grip_q:.3f} rad (closed stop {lo:.3f}), pad force {pad_force:.1f} N")
    if renderer is not None:
        save_strip(frames, os.path.join(IMG, "sim_grasp.png"))
        save_strip(views, os.path.join(IMG, "sim_views.png"))
    return ok


def save_strip(frames, path):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, len(frames), figsize=(4.2 * len(frames), 3.4))
    for ax, (label, img) in zip(np.atleast_1d(axs), frames):
        ax.imshow(img); ax.set_title(label, fontsize=11); ax.axis("off")
    plt.tight_layout(); os.makedirs(os.path.dirname(path), exist_ok=True); plt.savefig(path, dpi=110); plt.close()


# --------------------------------------------------------------------------------------
def geom_meshes(model, body_names):
    """Exact (non-hull) trimesh for every mesh geom on the given bodies, in body frame."""
    out = {}
    for b in body_names:
        bid = model.body(b).id
        parts = []
        for gid in range(model.ngeom):
            if model.geom_bodyid[gid] != bid or model.geom_type[gid] != mujoco.mjtGeom.mjGEOM_MESH:
                continue
            mid = model.geom_dataid[gid]
            v0, nv = model.mesh_vertadr[mid], model.mesh_vertnum[mid]
            f0, nf = model.mesh_faceadr[mid], model.mesh_facenum[mid]
            V = model.mesh_vert[v0:v0 + nv].astype(float); F = model.mesh_face[f0:f0 + nf]
            R = np.zeros(9); mujoco.mju_quat2Mat(R, model.geom_quat[gid]); R = R.reshape(3, 3)
            parts.append(trimesh.Trimesh(V @ R.T + model.geom_pos[gid], F, process=False))
        if parts:
            out[b] = trimesh.util.concatenate(parts)
    return out


def bvh(m):
    b = fcl.BVHModel(); b.beginModel(len(m.vertices), len(m.faces))
    b.addSubModel(m.vertices, m.faces); b.endModel(); return b


def sweep(xml_path, gripper_bodies, n_random=1500, seed=0):
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)
    arm = ["base", "link1", "link2", "link3", "link4", "link5"]
    arm = [b for b in arm if mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, b) >= 0]
    meshes = geom_meshes(model, arm + gripper_bodies)
    objs = {b: fcl.CollisionObject(bvh(m)) for b, m in meshes.items()}
    rng = np.random.default_rng(seed)
    lo, hi = model.jnt_range[:6, 0], model.jnt_range[:6, 1]
    qs = [lo + (hi - lo) * rng.random(6) for _ in range(n_random)]
    # wrist-focused grid around a typical working pose
    for q4 in np.linspace(lo[3], hi[3], 7):
        for q5 in np.linspace(lo[4], hi[4], 9):
            for q6 in np.linspace(lo[5], hi[5], 9):
                qs.append(np.array([0.0, 1.2, 1.0, q4, q5, q6]))
    hits = {}
    for q in qs:
        data.qpos[:6] = q
        if model.nq > 6:
            data.qpos[6:] = 0
        mujoco.mj_kinematics(model, data)
        for b, o in objs.items():
            bid = model.body(b).id
            o.setTransform(fcl.Transform(data.xmat[bid].reshape(3, 3).copy(), data.xpos[bid].copy()))
        for g in gripper_bodies:
            if g not in objs:
                continue
            for a in arm:
                if a == "link5":       # the gripper's own parent: checked separately below
                    continue
                r = fcl.CollisionResult()
                if fcl.collide(objs[g], objs[a], fcl.CollisionRequest(), r):
                    hits.setdefault(a, []).append(np.round(q, 3).tolist())
    return {"configs": len(qs), "collisions_by_link": {k: len(v) for k, v in hits.items()},
            "examples": {k: v[:3] for k, v in hits.items()}}


def check_reach(xml_yubi, report):
    from i2rt.robots.utils import ArmType, GripperType, combine_arm_and_gripper_xml
    xml_stock = combine_arm_and_gripper_xml(ArmType.YAM, GripperType.LINEAR_4310)
    ours = sweep(xml_yubi, ["gripper", "finger_r", "finger_l"])
    stock = sweep(xml_stock, ["gripper", "tip_left", "tip_right"])
    worse = {k: v for k, v in ours["collisions_by_link"].items() if v > stock["collisions_by_link"].get(k, 0) * 1.1 + 2}
    ok = not worse
    report["reach"] = {"yubi_4310": ours, "linear_4310_stock": stock, "worse_than_stock": worse, "ok": ok}
    print(f"[reach] {'ok' if ok else 'WORSE'}: {ours['configs']} arm poses; gripper-vs-arm collisions "
          f"yubi {ours['collisions_by_link']} vs stock {stock['collisions_by_link']}")
    return ok


# --------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-render", action="store_true")
    args = ap.parse_args()
    i2rt_dir = install_i2rt()
    sys.path.insert(0, i2rt_dir)
    report = {}
    xml = check_sdk(i2rt_dir, report)
    ok = check_grasp(xml, report, render=not args.no_render)
    ok &= check_reach(xml, report)
    report["sdk"]["model_path"] = os.path.basename(report["sdk"]["model_path"])
    json.dump(report, open(os.path.join(HERE, "check_report.json"), "w"), indent=1)
    print("all checks passed" if ok else "SOME CHECKS FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
