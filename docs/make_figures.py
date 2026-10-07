"""Render the CAD overview figure (docs/img/cad_overview.png). Run after cad/build.py.

    python3 docs/make_figures.py
"""
import json
import os

os.environ.setdefault("MUJOCO_GL", "osmesa")
os.environ.setdefault("PYOPENGL_PLATFORM", os.environ["MUJOCO_GL"])

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import mujoco  # noqa: E402
import numpy as np  # noqa: E402
import trimesh  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = json.load(open(os.path.join(ROOT, "cad/out/build_summary.json")))
O = np.array(S["derived"]["gripper_frame_origin_mm"])
R = np.diag([1.0, -1.0, -1.0])
TMP = os.path.join(ROOT, "docs/.fig_meshes")
os.makedirs(TMP, exist_ok=True)

NEW = {  # part: (label, rgba)
    "yam_flange": ("wrist flange", (0.20, 0.62, 0.40, 1)),
    "bracket_trimmed": ("trimmed bracket", (0.25, 0.48, 0.80, 1)),
    "motor_bracket": ("motor bracket", (0.93, 0.55, 0.15, 1)),
    "coupler": ("coupler", (0.95, 0.80, 0.20, 1)),
}


def to_frame(path, out):
    m = trimesh.load(path, force="mesh")
    m.vertices = ((m.vertices - O) @ R.T) / 1000.0
    m.export(out)
    return out


meshes = []
for n in NEW:
    meshes.append((n, to_frame(os.path.join(ROOT, f"cad/out/{n}.stl"), os.path.join(TMP, f"{n}.stl")), NEW[n][1]))
for n, rgba in (("context", (0.55, 0.57, 0.60, 1)), ("finger_r", (0.78, 0.25, 0.22, 1)),
                ("finger_l", (0.78, 0.25, 0.22, 1))):
    meshes.append((n, os.path.join(ROOT, f"sim/assets/{n}.stl"), rgba))
# motor envelope: base.stl minus everything else is awkward, so rebuild it as a cylinder
ax = np.array(S["sim"]["axis_r"])
stator_y = -(S["derived"]["stator_face_y"] - O[1]) / 1000.0
motor = trimesh.creation.cylinder(radius=0.0285, height=0.045,
                                  transform=trimesh.transformations.rotation_matrix(np.pi / 2, [1, 0, 0]))
motor.apply_translation([ax[0], stator_y + 0.0225, ax[2]])
motor.export(os.path.join(TMP, "motor.stl"))
meshes.append(("motor", os.path.join(TMP, "motor.stl"), (0.16, 0.17, 0.19, 1)))

xml = ["<mujoco><visual><global offwidth='900' offheight='700'/><headlight ambient='0.35 0.35 0.35' diffuse='0.5 0.5 0.5'/></visual><asset>",
       "<texture type='skybox' builtin='flat' rgb1='1 1 1' rgb2='1 1 1' width='16' height='16'/>"]
xml += [f"<mesh name='{n}' file='{p}'/>" for n, p, _ in meshes]
xml += ["</asset><worldbody><light pos='0.2 -0.3 0.4' dir='-0.4 0.6 -0.8' diffuse='0.6 0.6 0.6'/>"]
xml += [f"<geom type='mesh' mesh='{n}' rgba='{' '.join(map(str, c))}'/>" for n, _, c in meshes]
xml += ["</worldbody></mujoco>"]
model = mujoco.MjModel.from_xml_string("".join(xml))
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)
r = mujoco.Renderer(model, 700, 900)
shots = []
for title, az, el in (("camera side", 70, -15), ("back: DM4310 on its bracket", -120, -12),
                      ("wrist side: flange bolts to the YAM", -150, -62)):
    cam = mujoco.MjvCamera(); cam.lookat[:] = [0, 0.012, -0.07]; cam.distance = 0.27
    cam.azimuth, cam.elevation = az, el
    r.update_scene(data, camera=cam); shots.append((title, r.render().copy()))

fig, axs = plt.subplots(1, 3, figsize=(15, 4.6))
for a, (t, img) in zip(axs, shots):
    a.imshow(img); a.set_title(t, fontsize=12); a.axis("off")
handles = [plt.Rectangle((0, 0), 1, 1, color=c[:3]) for _, c in NEW.values()] + \
          [plt.Rectangle((0, 0), 1, 1, color=(0.16, 0.17, 0.19)), plt.Rectangle((0, 0), 1, 1, color=(0.55, 0.57, 0.6))]
fig.legend(handles, [l for l, _ in NEW.values()] + ["DM4310 (from the stock gripper)", "Toyota YUBI parts (unchanged)"],
           loc="lower center", ncol=6, frameon=False, fontsize=10)
plt.tight_layout(rect=(0, 0.07, 1, 1))
os.makedirs(os.path.join(ROOT, "docs/img"), exist_ok=True)
plt.savefig(os.path.join(ROOT, "docs/img/cad_overview.png"), dpi=100)
print("wrote docs/img/cad_overview.png")
