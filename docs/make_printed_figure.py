"""Render docs/img/printed_parts.png (run after cad/printed.py).

Left: the two merged drive parts in place, inside a cut-away robot gripper.
Right: the glove's new upper plate with the Adafruit AS5600 board over the finger magnet.
"""
import os
import sys

os.environ.setdefault("MUJOCO_GL", "osmesa")
os.environ.setdefault("PYOPENGL_PLATFORM", os.environ["MUJOCO_GL"])

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import mujoco  # noqa: E402
import numpy as np  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "cad"))
import build as B  # noqa: E402
import printed as PR  # noqa: E402

TMP = os.path.join(ROOT, "docs/.fig_meshes")
os.makedirs(TMP, exist_ok=True)


def shape_stl(shape, name):
    p = os.path.join(TMP, name + ".stl")
    B.to_trimesh(shape).export(p)
    return p


def render(items, center, lookat_dir, dist, size=(900, 700)):
    spec = mujoco.MjSpec()
    spec.visual.global_.offwidth, spec.visual.global_.offheight = size
    spec.visual.headlight.ambient = [0.35, 0.35, 0.35]
    spec.visual.headlight.diffuse = [0.6, 0.6, 0.6]
    for i, (path, rgba) in enumerate(items):
        spec.add_mesh(name=f"m{i}", file=path, scale=[1e-3] * 3)
        spec.worldbody.add_geom(type=mujoco.mjtGeom.mjGEOM_MESH, meshname=f"m{i}", rgba=rgba,
                                contype=0, conaffinity=0)
    model = spec.compile(); data = mujoco.MjData(model)
    mujoco.mj_forward(model, data)
    r = mujoco.Renderer(model, size[1], size[0])
    cam = mujoco.MjvCamera()
    cam.lookat[:] = np.array(center) / 1000.0
    cam.distance = dist / 1000.0
    cam.azimuth, cam.elevation = lookat_dir
    r.update_scene(data, cam)
    return r.render()


def main():
    toyota = B.load_toyota_parts(B.TOYOTA_ASSY)
    out = os.path.join(ROOT, "cad/out/printed")
    grey, dark = (0.75, 0.75, 0.78, 0.35), (0.3, 0.3, 0.33, 1)
    robot = [(os.path.join(out, "drive_R_printed.stl"), (0.93, 0.45, 0.15, 1)),
             (os.path.join(out, "drive_L_printed.stl"), (0.20, 0.55, 0.85, 1)),
             (shape_stl(B.make_coupler(), "coupler"), (0.95, 0.80, 0.20, 1)),
             (shape_stl(B.make_motor(), "motor"), dark)]
    for nm in ["CASE", "FINGER_ATTACHMENT_L", "FINGER_ATTACHMENT_R"]:
        robot.append((shape_stl(B.one(toyota, nm), nm), grey))
    img_r = render(robot, (854, 845, 1272), (-60, -20), 190)

    glove = B.load_toyota_parts(PR.GLOVE_R)
    board = PR.load_board()
    g = [(os.path.join(out, "glove_upper_plate_as5600.stl"), (0.25, 0.25, 0.28, 1)),
         (os.path.join(out, "adafruit_as5600_reference.stl"), (0.10, 0.35, 0.75, 1)),
         (shape_stl(B.one(glove, "MAGNET_D6_AS5601"), "magnet"), (0.85, 0.15, 0.15, 1)),
         (shape_stl(B.one(glove, "FINGER_with_Gear_Glove_t30_R_SHAFT_DIA_Φ8"), "finger"), (0.85, 0.3, 0.3, 0.5))]
    del board
    img_g = render(g, (-11, 27, 1020), (-90, -25), 110)

    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
    for a, im, t in [(ax[0], img_r, "Robot gripper: merged drive parts (orange right, blue left)\n"
                      "gear + shaft + key + washer printed as one piece each"),
                     (ax[1], img_g, "Glove: new upper plate (dark) with Adafruit AS5600 (blue)\n"
                      "chip centred on the finger magnet (red), same 2 mm air gap")]:
        a.imshow(im); a.set_title(t, fontsize=10); a.axis("off")
    plt.tight_layout(rect=(0, 0, 1, 0.97))
    p = os.path.join(ROOT, "docs/img/printed_parts.png")
    plt.savefig(p, dpi=110)
    print(p)


if __name__ == "__main__":
    main()
