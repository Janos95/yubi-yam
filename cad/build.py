"""Build the yubi-yam parts from Toyota's YUBI gripper CAD.

Run from the repo root (needs the third_party/yubi-hw submodule):

    python3 cad/build.py

What it does
  1. Loads Toyota's robot-side YUBI gripper assembly (Dynamixel version) with
     every part placed in assembly coordinates.
  2. Builds the four parts that turn it into a YAM gripper driven by a DM4310:
       coupler          replaces the Dynamixel horn (DM4310 rotor -> YUBI gear shaft)
       motor_bracket    holds the DM4310 behind the case, using the case's M2 inserts
       bracket_trimmed  Toyota's BRACKET_GRIPPER, cut back to clear the larger motor
       yam_flange       YAM wrist output -> bracket (replaces Toyota's UR5e flange)
  3. Checks every new part against every kept Toyota part and the motor for
     interference, and fails loudly if anything overlaps.
  4. Writes STEP + STL for the new parts to cad/out/, and the rigid-body meshes
     the MuJoCo model needs (in the i2RT gripper frame, metres) to sim/assets/.

All coordinates below are Toyota assembly coordinates in millimetres unless a
name says otherwise. The yubi-yam gripper frame is defined in GRIPPER_FRAME.
"""
from __future__ import annotations

import json
import math
import os
import re
import sys
from dataclasses import dataclass, asdict

import cadquery as cq
import numpy as np
import trimesh
from OCP.BRep import BRep_Tool
from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCP.BRepGProp import BRepGProp
from OCP.BRepMesh import BRepMesh_IncrementalMesh
from OCP.GProp import GProp_GProps
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TCollection import TCollection_ExtendedString
from OCP.TDF import TDF_ChildIterator, TDF_Label
from OCP.TDataStd import TDataStd_Name
from OCP.TDocStd import TDocStd_Document
from OCP.TopAbs import TopAbs_FACE, TopAbs_REVERSED
from OCP.TopExp import TopExp_Explorer
from OCP.TopLoc import TopLoc_Location
from OCP.TopoDS import TopoDS
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.gp import gp_Trsf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOYOTA_ASSY = os.path.join(ROOT, "third_party/yubi-hw/STEP/gripper/YUBI Gripper Assy_Dynamixel_ver2.STEP")
OUT = os.path.join(ROOT, "cad/out")
SIM_ASSETS = os.path.join(ROOT, "sim/assets")


# --------------------------------------------------------------------------------------
# Parameters
# --------------------------------------------------------------------------------------
@dataclass
class WristInterface:
    """YAM joint-6 output, where a gripper bolts on.

    Not published by i2RT. The default assumes the gripper bolts straight onto a
    DM4310 rotor (the YAM's last link is 57 mm wide, the 4310's diameter): 6x M3 on a
    27 mm circle around a 35 mm boss. Verify on the arm and change here if it differs.
    """
    bolt_circle_d: float = 27.0
    bolt_count: int = 6
    bolt_clearance_d: float = 3.4      # M3
    head_counterbore_d: float = 6.0    # M3 socket head
    pilot_d: float = 35.3              # recess that centres on the 35 mm rotor boss
    pilot_depth: float = 0.8
    phase_deg: float = 0.0             # rotation of the bolt pattern about the wrist axis


@dataclass
class Params:
    wrist: WristInterface
    # DM4310 (Damiao DM-J4310-2EC), dimensions checked against Damiao's model as
    # published in OpenArm v1.1: body 57 x 45 mm, rotor boss 35 x 1 mm, rotor
    # 6x M3 on PCD 27, stator front ring 6x M3 on PCD 50, back 4x M3 on PCD 38.
    motor_d: float = 57.0
    motor_body_len: float = 45.0
    motor_boss_d: float = 35.0
    motor_boss_len: float = 1.0
    motor_rotor_pcd: float = 27.0
    motor_stator_pcd: float = 50.0
    motor_clock_deg: float = 0.0       # stator holes at 0, 60, ... deg in the XZ plane
    # Locating pins, measured on the YAM's gripper motor (label RD-J10D, DM4310 size):
    # rotor: 2x Ø4 pins standing 4.2 proud, 120 deg apart on PCD 23.1 (24 over both
    # pins), each midway between two rotor screw holes; the third midway hole is empty.
    rotor_pin_d: float = 4.0
    rotor_pin_pcd: float = 23.1
    rotor_pin_len: float = 4.2
    # stator ring: 2x Ø3 pins standing 5.5 proud, opposite each other on PCD 50,
    # each 15 deg (6.5 mm) from a screw hole. Which side of the hole is not known for
    # sure, so the bracket clears both sides.
    stator_pin_d: float = 3.0
    stator_pin_len: float = 5.5
    stator_pin_offset_deg: float = 15.0
    # The thick right finger pad (PAD_t30_R) reaches 3 mm behind the case, at 82-107 deg
    # around the shaft and >= 26.6 mm out. The bracket gets a relief over the arc the pad
    # sweeps, and the stator screws inside that arc are left out (4 of 6 used).
    pad_relief_deg: tuple = (40.0, 150.0)
    pad_relief_r: float = 25.0          # pad's closest point is 26.6 mm out
    pad_relief_y: float = 835.0         # pad reaches back to y = 836.5
    # Driven gear shaft (Toyota GEAR_SHAFT), axis along +Y
    shaft_x: float = 839.07
    shaft_z: float = 1270.57
    shaft_face_y: float = 840.5        # end face that the Dynamixel horn bolted to
    shaft_horn_pcd: float = 16.0       # 4x M2 through the shaft flange into the horn
    shaft_pilot_d: float = 8.0         # recess in the shaft end, 3 mm deep
    shaft_pilot_depth: float = 3.0
    case_back_y: float = 839.5         # back face of Toyota CASE
    case_hole_d: float = 22.0          # hole in the case back the horn used to enter
    # Layout choices
    bracket_plate_t: float = 6.0       # motor bracket plate thickness (Y)
    flange_under_motor_y: float = 833.6  # flange plate runs back under the motor bracket foot
    flange_plate_t: float = 8.0
    flange_hub_d: float = 44.0
    flange_hub_h: float = 10.0         # hub below the plate; keeps the wide plate off the wrist
    flange_plate_ymax: float = 873.0   # full width of Toyota's bracket
    trim_y: float = 839.6              # BRACKET_GRIPPER is cut away below this Y
    wrist_axis_x: float = 854.07       # centre of the two finger shafts
    wrist_axis_y: float = 856.5        # mid-plane of the finger attachments


P = Params(wrist=WristInterface())

# Derived positions
STATOR_FACE_Y = P.case_back_y - P.bracket_plate_t            # motor front ring sits on the bracket
ROTOR_FACE_Y = STATOR_FACE_Y + P.motor_boss_len               # coupler bolts here
FLANGE_TOP_Z = 1242.5735                                      # underside of BRACKET_GRIPPER (measured)
FLANGE_PLATE_BOT_Z = FLANGE_TOP_Z - P.flange_plate_t
WRIST_FACE_Z = FLANGE_PLATE_BOT_Z - P.flange_hub_h            # mates the YAM wrist output

# i2RT gripper frame: origin on the wrist output face, z along the wrist axis pointing
# away from the fingers (fingers at -z, as in i2RT's linear_4310 model), metres.
GRIPPER_FRAME_ORIGIN = np.array([P.wrist_axis_x, P.wrist_axis_y, WRIST_FACE_Z])
GRIPPER_FRAME_R = np.diag([1.0, -1.0, -1.0])


# --------------------------------------------------------------------------------------
# Toyota CAD
# --------------------------------------------------------------------------------------
def load_toyota_parts(path: str) -> dict[str, list]:
    """Leaf parts of a STEP assembly, placed in assembly coordinates, keyed by name."""
    if not os.path.exists(path):
        sys.exit(f"Toyota CAD not found at {path}\nRun: git submodule update --init third_party/yubi-hw")
    doc = TDocStd_Document(TCollection_ExtendedString("doc"))
    r = STEPCAFControl_Reader(); r.SetNameMode(True)
    if r.ReadFile(path) != 1:
        sys.exit(f"Could not read {path}")
    r.Transfer(doc)
    st = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())

    def name(l):
        n = TDataStd_Name()
        return n.Get().ToExtString() if l.FindAttribute(TDataStd_Name.GetID_s(), n) else "?"

    out: dict[str, list] = {}

    def walk(lbl, trsf, nm):
        ref = TDF_Label()
        if st.IsReference_s(lbl) and st.GetReferredShape_s(lbl, ref):
            walk(ref, trsf.Multiplied(st.GetLocation_s(lbl).Transformation()), name(ref)); return
        if st.IsAssembly_s(lbl):
            it = TDF_ChildIterator(lbl, False)
            while it.More():
                c = it.Value()
                if st.IsComponent_s(c):
                    walk(c, trsf, nm)
                it.Next()
            return
        placed = BRepBuilderAPI_Transform(st.GetShape_s(lbl), trsf, True).Shape()
        out.setdefault(nm.replace(" ", "_"), []).append(cq.Shape.cast(placed))

    it = TDF_ChildIterator(st.Label(), False)
    while it.More():
        l = it.Value()
        if st.IsFree_s(l) and st.IsShape_s(l):
            walk(l, gp_Trsf(), name(l))
        it.Next()
    return out


def one(parts, name):
    s = parts[name]
    assert len(s) == 1, (name, len(s))
    return s[0]


# --------------------------------------------------------------------------------------
# Geometry helpers
# --------------------------------------------------------------------------------------
def cyl_y(d, y0, y1, x, z):
    """Solid cylinder along +Y from y0 to y1 centred on (x, z)."""
    return cq.Solid.makeCylinder(d / 2, y1 - y0, cq.Vector(x, y0, z), cq.Vector(0, 1, 0))


def cyl_z(d, z0, z1, x, y):
    return cq.Solid.makeCylinder(d / 2, z1 - z0, cq.Vector(x, y, z0), cq.Vector(0, 0, 1))


def cyl_x(d, x0, x1, y, z):
    return cq.Solid.makeCylinder(d / 2, x1 - x0, cq.Vector(x0, y, z), cq.Vector(1, 0, 0))


def box(x0, x1, y0, y1, z0, z1):
    return cq.Solid.makeBox(x1 - x0, y1 - y0, z1 - z0, cq.Vector(x0, y0, z0))


def polar(cx, cz, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cz + r * math.sin(a)


def volume(shape) -> float:
    g = GProp_GProps(); BRepGProp.VolumeProperties_s(shape.wrapped, g)
    return g.Mass()


def common_volume(a, b) -> float:
    op = BRepAlgoAPI_Common(a.wrapped, b.wrapped)
    op.Build()
    if not op.IsDone():
        return float("nan")
    return volume(cq.Shape.cast(op.Shape()))


# --------------------------------------------------------------------------------------
# New parts
# --------------------------------------------------------------------------------------
def stator_pin_angles():
    """Both candidate positions of the two stator-ring pins (15 deg either side of the
    holes at 0 and 180 deg); the bracket clears all four, the motor sits in either way."""
    o = P.stator_pin_offset_deg
    return [P.motor_clock_deg + b + s * o for b in (0, 180) for s in (-1, 1)]


def rotor_pin_angles():
    """Midway between rotor screws (which sit at 30 + 60k): the coupler gets a pocket at
    three of these, 120 deg apart, so the rotor's two pins fit in any of three clockings."""
    return [0.0, 120.0, 240.0]


def make_motor(with_pins=True):
    """DM4310 envelope, output facing +Y onto the driven shaft (reference only).
    Includes the measured locating pins (stator pins at every candidate position)."""
    x, z = P.shaft_x, P.shaft_z
    body = cyl_y(P.motor_d, STATOR_FACE_Y - P.motor_body_len, STATOR_FACE_Y, x, z)
    boss = cyl_y(P.motor_boss_d, STATOR_FACE_Y, ROTOR_FACE_Y, x, z)
    m = body.fuse(boss)
    if with_pins:
        for a in stator_pin_angles():
            px, pz = polar(x, z, P.motor_stator_pcd / 2, a)
            m = m.fuse(cyl_y(P.stator_pin_d, STATOR_FACE_Y, STATOR_FACE_Y + P.stator_pin_len, px, pz))
        for a in rotor_pin_angles()[:2]:
            px, pz = polar(x, z, P.rotor_pin_pcd / 2, a)
            m = m.fuse(cyl_y(P.rotor_pin_d, ROTOR_FACE_Y, ROTOR_FACE_Y + P.rotor_pin_len, px, pz))
    return m.clean()


def make_coupler():
    """DM4310 rotor (6x M3, PCD 27) -> YUBI gear shaft (4x M2 inserts, PCD 16, 8 mm pilot).

    Reproduces the Dynamixel horn interface on the shaft side, so Toyota's GEAR_SHAFT
    and its screws are used unchanged.
    """
    disk_d, neck_d = 35.0, 20.6
    disk_end = P.case_back_y - 0.5                     # 0.5 mm clear of the case back
    x, z = P.shaft_x, P.shaft_z
    c = cyl_y(disk_d, ROTOR_FACE_Y, disk_end, x, z)
    c = c.fuse(cyl_y(neck_d, disk_end, P.shaft_face_y, x, z))
    c = c.fuse(cyl_y(P.shaft_pilot_d - 0.1, P.shaft_face_y, P.shaft_face_y + P.shaft_pilot_depth - 0.2, x, z))
    # rotor screws: M3 through, heads counterbored into the shaft-side face of the disk
    for k in range(6):
        hx, hz = polar(x, z, P.motor_rotor_pcd / 2, 30 + 60 * k)
        c = c.cut(cyl_y(3.4, ROTOR_FACE_Y - 1, disk_end + 1, hx, hz))
        c = c.cut(cyl_y(6.0, disk_end - 2.2, disk_end + 1, hx, hz))
    # shaft screws: M2 heat-set inserts (Toyota's SB-203030, 3.0 OD x 3 mm) at PCD 16
    for k in range(4):
        hx, hz = polar(x, z, P.shaft_horn_pcd / 2, 90 * k)
        c = c.cut(cyl_y(3.1, P.shaft_face_y - 3.3, P.shaft_face_y + 1, hx, hz))
        c = c.cut(cyl_y(1.8, P.shaft_face_y - 5.5, P.shaft_face_y, hx, hz))
    # pockets for the rotor's Ø4 locating pins (3 positions, pins use 2); 0.2 clearance
    for a in rotor_pin_angles():
        hx, hz = polar(x, z, P.rotor_pin_pcd / 2, a)
        c = c.cut(cyl_y(P.rotor_pin_d + 0.2, ROTOR_FACE_Y - 1, ROTOR_FACE_Y + P.rotor_pin_len + 0.6, hx, hz))
    # centre M2.5 (optional, as on the horn): self-tapping pilot
    c = c.cut(cyl_y(2.1, P.shaft_face_y - 4.0, P.shaft_face_y + P.shaft_pilot_depth, x, z))
    return c.clean()


def sector_y(r_in, r_out, a0, a1, y0, y1, cx, cz, steps=24):
    """Annular sector prism along +Y (angles in deg, measured in the XZ plane)."""
    outer = [polar(cx, cz, r_out, a0 + (a1 - a0) * i / steps) for i in range(steps + 1)]
    inner = [polar(cx, cz, r_in, a1 - (a1 - a0) * i / steps) for i in range(steps + 1)]
    pts = [cq.Vector(px, y0, pz) for px, pz in outer + inner]
    face = cq.Face.makeFromWires(cq.Wire.makePolygon(pts, close=True))
    return cq.Solid.extrudeLinear(face, cq.Vector(0, y1 - y0, 0))


def stator_holes():
    """Stator screw angles actually used (those outside the pad relief)."""
    a0, a1 = P.pad_relief_deg
    return [a for a in (P.motor_clock_deg + 60 * k for k in range(6)) if not (a0 - 8 <= a % 360 <= a1 + 8)]


def make_motor_bracket(toyota):
    """Plate behind the case: holds the DM4310 by its front ring, bolts to the case.

    The case-side features (side tab with 2x M2 into the case's side inserts) are
    taken directly from Toyota's BRACKET_DYNAMIXEL, so they match the case exactly.
    """
    y0, y1 = STATOR_FACE_Y, P.case_back_y
    x, z = P.shaft_x, P.shaft_z
    plate = cyl_y(61.0, y0, y1, x, z)
    plate = plate.fuse(box(x, 888.0, y0, y1, 1251.0, 1283.0))           # arm to the back inserts
    plate = plate.fuse(box(820.57, x, y0, y1, 1252.0, 1283.0))          # web to the side tab
    # flat foot resting on the wrist flange: a second load path for the motor's
    # weight (325 g vs the Dynamixel's 82 g) besides the four M2 screws into the case
    plate = plate.cut(box(700, 1000, y0 - 1, y1 + 1, 0, FLANGE_TOP_Z))
    # Toyota's side tab: everything of BRACKET_DYNAMIXEL in front of the plate
    dyn = one(toyota, "BRACKET_DYNAMIXEL")
    tab = dyn.intersect(box(815, 830, y1, 860, 1240, 1300))
    plate = plate.fuse(tab)
    # bore for the rotor boss and coupler
    plate = plate.cut(cyl_y(38.0, y0 - 1, y1 + 1, x, z))
    # relief for the swept finger pad
    a0, a1 = P.pad_relief_deg
    plate = plate.cut(sector_y(P.pad_relief_r, 45.0, a0, a1, P.pad_relief_y, y1 + 1, x, z))
    # M3 into the stator ring (outside the relief), heads counterbored on the case side
    for ang in stator_holes():
        hx, hz = polar(x, z, P.motor_stator_pcd / 2, ang)
        plate = plate.cut(cyl_y(3.4, y0 - 1, y1 + 1, hx, hz))
        plate = plate.cut(cyl_y(6.0, y1 - 2.0, y1 + 1, hx, hz))   # DIN 7984 head (2.0) flush;
        # M3x8 then engages 4.0 of the ring's ~4.8 deep threads
    # slots for the stator ring's Ø3 locating pins (5.5 proud), both candidate sides
    for ang in stator_pin_angles():
        r = P.motor_stator_pcd / 2
        w = P.stator_pin_d / 2 + 0.4
        plate = plate.cut(sector_y(r - w, r + w, ang - 3.5, ang + 3.5, y0 - 1, y1 + 1, x, z))
        for e in (ang - 3.5, ang + 3.5):
            ex, ez = polar(x, z, r, e)
            plate = plate.cut(cyl_y(2 * w, y0 - 1, y1 + 1, ex, ez))
    # 2x M2 into the case back inserts (Toyota positions), heads on the motor side
    for zz in (1257.57, 1275.57):
        plate = plate.cut(cyl_y(2.4, y0 - 1, y1 + 1, 883.07, zz))
        plate = plate.cut(cyl_y(4.2, y0 - 1, y0 + 1.6, 883.07, zz))
    return plate.clean()


def make_bracket_trimmed(toyota):
    """Toyota BRACKET_GRIPPER with the part under the motor removed."""
    b = one(toyota, "BRACKET_GRIPPER")
    return b.cut(box(700, 1000, 700, P.trim_y, 1000, 1400)).clean()


def make_yam_flange():
    """Plate under the trimmed bracket + hub that bolts to the YAM wrist output."""
    w = P.wrist
    cx, cy = P.wrist_axis_x, P.wrist_axis_y
    f = box(812.1, 896.1, P.trim_y, P.flange_plate_ymax, FLANGE_PLATE_BOT_Z, FLANGE_TOP_Z)
    # shelf under the motor bracket foot (motor body itself starts at y = 833.5)
    f = f.fuse(box(822.0, 856.0, P.flange_under_motor_y, P.trim_y, FLANGE_PLATE_BOT_Z, FLANGE_TOP_Z))
    f = f.fuse(cyl_z(P.flange_hub_d, WRIST_FACE_Z, FLANGE_TOP_Z, cx, cy))
    # wrist bolts: through, heads counterbored from the top (fit before the bracket)
    for k in range(w.bolt_count):
        a = math.radians(w.phase_deg + 360.0 * k / w.bolt_count)
        hx, hy = cx + w.bolt_circle_d / 2 * math.cos(a), cy + w.bolt_circle_d / 2 * math.sin(a)
        f = f.cut(cyl_z(w.bolt_clearance_d, WRIST_FACE_Z - 1, FLANGE_TOP_Z + 1, hx, hy))
        f = f.cut(cyl_z(w.head_counterbore_d, WRIST_FACE_Z + 6.0, FLANGE_TOP_Z + 1, hx, hy))
    f = f.cut(cyl_z(w.pilot_d, WRIST_FACE_Z - 1, WRIST_FACE_Z + w.pilot_depth, cx, cy))
    # Gripper -> flange, 4x M3:
    #  * 2x from the top through the bracket into M3 heat-set inserts (Toyota's bracket
    #    screws to the UR flange at these points; the other four fall in the trimmed area)
    for (ix, iy) in ((817.07, 849.5), (891.07, 849.5)):
        f = f.cut(cyl_z(4.0, FLANGE_TOP_Z - 5.5, FLANGE_TOP_Z + 1, ix, iy))
        f = f.cut(cyl_z(2.5, FLANGE_TOP_Z - 7.0, FLANGE_TOP_Z, ix, iy))
    #  * 2x from below through flange + bracket into the upper plate's inserts, at
    #    Toyota's upper-plate screw positions (M3x12 instead of Toyota's M3x8)
    for (ix, iy) in ((825.32, 869.0), (882.82, 869.0)):
        f = f.cut(cyl_z(3.4, FLANGE_PLATE_BOT_Z - 1, FLANGE_TOP_Z + 1, ix, iy))
        f = f.cut(cyl_z(6.0, FLANGE_PLATE_BOT_Z - 1, FLANGE_PLATE_BOT_Z + 4.0, ix, iy))
    return f.clean()


# --------------------------------------------------------------------------------------
# Meshing / export
# --------------------------------------------------------------------------------------
def to_trimesh(shape, tol=0.05) -> trimesh.Trimesh:
    s = shape.wrapped
    BRepMesh_IncrementalMesh(s, tol, False, 0.3, True)
    V, F, off = [], [], 0
    e = TopExp_Explorer(s, TopAbs_FACE)
    while e.More():
        f = TopoDS.Face(e.Current()); loc = TopLoc_Location(); t = BRep_Tool.Triangulation_s(f, loc)
        if t is not None:
            tr = loc.Transformation()
            for i in range(1, t.NbNodes() + 1):
                p = t.Node(i).Transformed(tr); V.append((p.X(), p.Y(), p.Z()))
            rev = f.Orientation() == TopAbs_REVERSED
            for i in range(1, t.NbTriangles() + 1):
                a, b, c = t.Triangle(i).Get()
                F.append((off + a - 1, off + c - 1, off + b - 1) if rev else (off + a - 1, off + b - 1, off + c - 1))
            off += t.NbNodes()
        e.Next()
    m = trimesh.Trimesh(np.array(V), np.array(F))
    m.merge_vertices()
    return m


def to_gripper_frame(m: trimesh.Trimesh) -> trimesh.Trimesh:
    m = m.copy()
    m.vertices = ((m.vertices - GRIPPER_FRAME_ORIGIN) @ GRIPPER_FRAME_R.T) / 1000.0
    return m


def to_gripper_point(p) -> list[float]:
    return (((np.asarray(p, float) - GRIPPER_FRAME_ORIGIN) @ GRIPPER_FRAME_R.T) / 1000.0).round(6).tolist()


SCREWS = re.compile(r"^(CB|CBE|CBSTNR|JP|SB-|XDSHC)")


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(SIM_ASSETS, exist_ok=True)
    print("loading Toyota assembly ...")
    toyota = load_toyota_parts(TOYOTA_ASSY)

    print("building parts ...")
    new = {
        "coupler": make_coupler(),
        "motor_bracket": make_motor_bracket(toyota),
        "bracket_trimmed": make_bracket_trimmed(toyota),
        "yam_flange": make_yam_flange(),
    }
    motor = make_motor()

    # ---- interference check -------------------------------------------------------
    removed = {"DYNAMIXEL_XM430-W350-R", "BRACKET_DYNAMIXEL", "BRACKET_GRIPPER", "UR5e_FLANGE"}
    missing = removed - set(toyota)
    assert not missing, f"Toyota part names changed: {missing}"
    kept = {}
    for nm, shapes in toyota.items():
        if nm in removed or SCREWS.match(nm):
            continue
        for i, s in enumerate(shapes):
            kept[f"{nm}#{i}"] = s
    bodies = dict(new); bodies["DM4310"] = motor
    # pairs that touch by design (mating faces) are fine; only volume overlap counts
    report, bad = [], []
    names = list(bodies) + list(kept)
    allshapes = {**bodies, **kept}
    for i, a in enumerate(list(bodies)):
        for b in names[i + 1:]:
            if a == b:
                continue
            bb_a, bb_b = allshapes[a].BoundingBox(), allshapes[b].BoundingBox()
            if (bb_a.xmax < bb_b.xmin or bb_b.xmax < bb_a.xmin or bb_a.ymax < bb_b.ymin or
                    bb_b.ymax < bb_a.ymin or bb_a.zmax < bb_b.zmin or bb_b.zmax < bb_a.zmin):
                continue
            v = common_volume(allshapes[a], allshapes[b])
            if v > 0.5:      # mm^3
                bad.append((a, b, round(v, 2)))
            report.append((a, b, round(v, 3)))
    for a, b, v in bad:
        print(f"  INTERFERENCE {a} x {b}: {v} mm^3")

    # ---- exports --------------------------------------------------------------------
    summary = {"params": asdict(P), "derived": {
        "stator_face_y": STATOR_FACE_Y, "rotor_face_y": ROTOR_FACE_Y,
        "wrist_face_z": WRIST_FACE_Z, "gripper_frame_origin_mm": GRIPPER_FRAME_ORIGIN.tolist()},
        "parts": {}, "interference": bad}
    for nm, s in new.items():
        cq.exporters.export(cq.Workplane().add(s), os.path.join(OUT, f"{nm}.step"))
        m = to_trimesh(s)
        m.export(os.path.join(OUT, f"{nm}.stl"))
        bb = s.BoundingBox()
        summary["parts"][nm] = {"volume_cm3": round(volume(s) / 1000, 2),
                                "pla_g_100pct": round(volume(s) / 1000 * 1.24, 1),
                                "size_mm": [round(bb.xlen, 1), round(bb.ylen, 1), round(bb.zlen, 1)]}

    # motor envelope, for reference and fit checks in other CAD tools
    cq.exporters.export(cq.Workplane().add(motor), os.path.join(OUT, "dm4310_envelope_reference.step"))

    # mass estimates per rigid group, from part volumes (g/cm^3; prints at ~60 % fill)
    PRINT = 1.24 * 0.6
    density = [(r"^GEAKB|^SSFRHQ|^KEG|^MTA05", 7.85), (r"^GEAR_SHAFT|^WSSAB", 2.8),
               (r"^RUBBER", 1.2), (r".*", PRINT)]
    fixed_g = {"USB_CAMERA_ELP-USBFHD01M-L180": 20.0}

    def mass_g(names, extra_new=()):
        g = 0.0
        for nm in names:
            for s_ in toyota[nm]:
                if nm in fixed_g:
                    g += fixed_g[nm]; continue
                rho = next(d for pat, d in density if re.match(pat, nm))
                g += volume(s_) / 1000 * rho
        g += sum(volume(new[n]) / 1000 * PRINT for n in extra_new)
        return g

    summary["mass_kg"] = {
        "base": round((mass_g(["CASE", "UPPER_PLATE_CAMERA_BKT", "USB_CAMERA_ELP-USBFHD01M-L180",
                               "MTA05-13ZZ_DBS", "WSSAB10-5-1"],
                              ["motor_bracket", "bracket_trimmed", "yam_flange"]) + 325.0 + 15.0) / 1000, 4),
        "finger_r": round((mass_g(["FINGER_ATTACHMENT_R", "PAD_t30_R", "RUBBER_SHEET_t30_R", "FLAP_R",
                                   "GEAR_SHAFT", "KEG3-8"], ["coupler"]) +
                           volume(sorted(toyota["GEAKB1.0-30-6-B-8N-QFC17-M3-LL"], key=lambda s: s.Center().x)[0]) / 1000 * 7.85
                           - volume(sorted(toyota["KEG3-8"], key=lambda s: s.Center().x)[1]) / 1000 * 7.85) / 1000, 4),
        "finger_l": round((mass_g(["FINGER_ATTACHMENT_L", "PAD_t20", "RUBBER_SHEET_t20", "FLAP_L",
                                   "SSFRHQ8-20-F6-P5-T6-Q5-KC8-A12"]) +
                           volume(sorted(toyota["GEAKB1.0-30-6-B-8N-QFC17-M3-LL"], key=lambda s: s.Center().x)[1]) / 1000 * 7.85 +
                           volume(sorted(toyota["KEG3-8"], key=lambda s: s.Center().x)[1]) / 1000 * 7.85) / 1000, 4),
        "note": "DM4310 325 g, camera 20 g, screws ~15 g; printed parts at 60 % fill PLA",
    }

    # rigid groups for the sim, in the gripper frame
    def grp(names_exact=(), extra=()):
        ms = []
        for nm in names_exact:
            if nm not in toyota:
                sys.exit(f"Toyota part {nm!r} not found; have: {sorted(toyota)}")
            for s in toyota[nm]:
                ms.append(to_trimesh(s, 0.1))
        ms += [to_trimesh(s, 0.1) for s in extra]
        return to_gripper_frame(trimesh.util.concatenate(ms))

    gears = sorted(toyota["GEAKB1.0-30-6-B-8N-QFC17-M3-LL"], key=lambda s: s.Center().x)
    keys = sorted(toyota["KEG3-8"], key=lambda s: s.Center().x)
    groups = {
        "base": grp(["CASE", "UPPER_PLATE_CAMERA_BKT", "USB_CAMERA_ELP-USBFHD01M-L180",
                     "MTA05-13ZZ_DBS", "WSSAB10-5-1"],
                    [new["motor_bracket"], new["bracket_trimmed"], new["yam_flange"], motor]),
        "finger_r": grp(["FINGER_ATTACHMENT_R", "PAD_t30_R", "RUBBER_SHEET_t30_R", "FLAP_R", "GEAR_SHAFT"],
                        [gears[0], keys[0], new["coupler"]]),
        "finger_l": grp(["FINGER_ATTACHMENT_L", "PAD_t20", "RUBBER_SHEET_t20", "FLAP_L",
                         "SSFRHQ8-20-F6-P5-T6-Q5-KC8-A12"], [gears[1], keys[1]]),
        # collision-check versions: finger bodies without gear/shaft, body without bearings
        "finger_r_body": grp(["FINGER_ATTACHMENT_R", "PAD_t30_R", "RUBBER_SHEET_t30_R", "FLAP_R"]),
        "finger_l_body": grp(["FINGER_ATTACHMENT_L", "PAD_t20", "RUBBER_SHEET_t20", "FLAP_L"]),
        "base_body": grp(["CASE", "UPPER_PLATE_CAMERA_BKT", "USB_CAMERA_ELP-USBFHD01M-L180"],
                         [new["motor_bracket"], new["bracket_trimmed"], new["yam_flange"], motor]),
        "context": grp(["CASE", "UPPER_PLATE_CAMERA_BKT", "USB_CAMERA_ELP-USBFHD01M-L180"]),
        "pad_r": grp(["RUBBER_SHEET_t30_R"]),
        "pad_l": grp(["RUBBER_SHEET_t20"]),
    }
    for nm, m in groups.items():
        m.export(os.path.join(SIM_ASSETS, f"{nm}.stl"))

    # finger axes and contact geometry for the sim
    summary["sim"] = {
        "axis_r": to_gripper_point([P.shaft_x, 850.0, P.shaft_z]),
        "axis_l": to_gripper_point([P.shaft_x + 30.0, 850.0, P.shaft_z]),
        "axis_dir": [0.0, 1.0, 0.0],   # +Y Toyota == -Y gripper frame; sign handled in the model
        "pad_tip_z": to_gripper_point([0, 0, 1375.6])[2],
        "camera": to_gripper_point(toyota[[k for k in toyota if k.startswith("USB")][0]][0].Center().toTuple()),
    }
    with open(os.path.join(OUT, "build_summary.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    print(json.dumps({k: summary[k] for k in ("parts", "interference")}, indent=1))
    if bad:
        sys.exit("interference found")


if __name__ == "__main__":
    main()
