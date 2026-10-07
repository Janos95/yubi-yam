"""Finger travel of the YUBI gripper from the exact CAD meshes.

Rotates the two fingers about their gear shafts (opposite directions, 1:1 gears) and
reports, per angle, the pad gap and the clearance to everything else. Run after
cad/build.py:

    python3 sim/finger_sweep.py

Writes sim/finger_travel.json, which sim/build_model.py uses for the joint range.
Angle convention: q > 0 opens the gripper. q = 0 is the pose in Toyota's assembly.
"""
import json
import os

import fcl
import numpy as np
import trimesh

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
A = os.path.join(HERE, "assets")
summary = json.load(open(os.path.join(ROOT, "cad/out/build_summary.json")))["sim"]


def bvh(m):
    b = fcl.BVHModel(); b.beginModel(len(m.vertices), len(m.faces))
    b.addSubModel(m.vertices, m.faces); b.endModel(); return b


def rot_y(theta, about):
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    t = np.asarray(about) - R @ np.asarray(about)
    return R, t


def obj(model, R=np.eye(3), t=np.zeros(3)):
    return fcl.CollisionObject(model, fcl.Transform(R, t))


def dist(a, b):
    req = fcl.DistanceRequest(enable_nearest_points=False)
    res = fcl.DistanceResult()
    return fcl.distance(a, b, req, res)


base = trimesh.load(os.path.join(A, "base_body.stl"))      # no bearings: shafts ride in them
fr = trimesh.load(os.path.join(A, "finger_r_body.stl"))   # no gear/shaft: they turn in place
fl = trimesh.load(os.path.join(A, "finger_l_body.stl"))
pr = trimesh.load(os.path.join(A, "pad_r.stl"))
pl = trimesh.load(os.path.join(A, "pad_l.stl"))
Mb, Mfr, Mfl, Mpr, Mpl = map(bvh, (base, fr, fl, pr, pl))
ar, al = summary["axis_r"], summary["axis_l"]

# Which rotation sign opens? Right finger sits at -x; opening swings its tip to -x.
rows = []
for deg in np.arange(-30.0, 60.01, 0.5):
    q = np.radians(deg)
    # in the gripper frame the shaft axis is y; right finger turns +q about +y opens?
    Rr, tr = rot_y(+q, ar)
    Rl, tl = rot_y(-q, al)
    gap = dist(obj(Mpr, Rr, tr), obj(Mpl, Rl, tl))
    fing = dist(obj(Mfr, Rr, tr), obj(Mfl, Rl, tl))
    # clearance of the moving fingers to the static base (gears/shafts excluded by
    # design: they sit in the case bores, so only check the parts outside the case)
    rows.append({"deg": round(float(deg), 1), "pad_gap_mm": round(gap * 1000, 2),
                 "finger_finger_mm": round(fing * 1000, 2)})

# sign check: the gap must grow with q
g = [r["pad_gap_mm"] for r in rows]
assert g[-1] > g[len(g) // 3], "opening sign is inverted"

closed = next(r for r in rows if r["pad_gap_mm"] > 0)
print("pads touch at", closed["deg"], "deg")
Mor, Mol = Mfr, Mfl
open_limit = None
for r in rows:
    q = np.radians(r["deg"])
    Rr, tr = rot_y(+q, ar); Rl, tl = rot_y(-q, al)
    r["base_r_mm"] = round(dist(obj(Mor, Rr, tr), obj(Mb)) * 1000, 2)
    r["base_l_mm"] = round(dist(obj(Mol, Rl, tl), obj(Mb)) * 1000, 2)
    if open_limit is None and r["deg"] > 0 and min(r["base_r_mm"], r["base_l_mm"]) <= 0.05:   # Toyota runs fingers 0.36 mm off the case
        open_limit = r["deg"]
print("fingers reach the body at", open_limit, "deg (None = not within 60 deg)")
lim_open = (open_limit - 2.0) if open_limit else 45.0
result = {"closed_deg": closed["deg"], "open_deg": lim_open,
          "pad_gap_at_open_mm": next(r for r in rows if r["deg"] >= lim_open)["pad_gap_mm"],
          "table": rows}
json.dump(result, open(os.path.join(HERE, "finger_travel.json"), "w"), indent=1)
print({k: v for k, v in result.items() if k != "table"})
