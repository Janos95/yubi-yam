"""Parts for the fully printed prototype (weekend build) — robot gripper and glove.

Run from the repo root after cad/build.py:

    python3 cad/printed.py

Robot gripper
  The proper build uses MISUMI gears, a stepped shaft, keys, precision washers and NSK
  bearings that ship late. For a printed prototype each finger's rotating group is
  merged into ONE printable part, in exactly the place and shape of the bought parts:
      drive_R_printed = Toyota GEAR_SHAFT + gear + key + washer
      drive_L_printed = MISUMI stepped shaft + gear + key + both washers
  The NSK MTA05-13ZZ DBS bearings (5 x 13 x 5) are replaced by 695ZZ (5 x 13 x 4) plus
  a printed 1 mm shim ring in each bearing seat. The yubi-yam coupler, motor bracket,
  trimmed bracket and wrist flange are printed from cad/out/*.stl unchanged (they
  were designed around heat-set inserts).

Glove
  Toyota's encoder board (Switch Science AS5601, Japan) is replaced by the US-stocked
  Adafruit 6357 AS5600 breakout. AS5600 and AS5601 share the I2C address (0x36) and
  every register yubi-sw's firmware reads (0x0B status, 0x0C raw angle, 0x1A AGC,
  0x1B magnitude), so the firmware is unchanged. The board is larger, so the glove's
  upper plate gets new mounting bosses: the AS5600 sits exactly where the AS5601 did,
  chip centred on the finger magnet with the same 2 mm air gap. One plate fits both
  hands (Toyota uses the same upper plate for left and right).

Outputs: cad/out/printed/*.stl / *.step and printed_summary.json. Fails loudly if a new
part interferes with anything it sits next to.
"""
from __future__ import annotations

import json
import os
import sys

import cadquery as cq
import trimesh
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCP.BRepClass3d import BRepClass3d
from OCP.gp import gp_Trsf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B  # noqa: E402

ROOT = B.ROOT
OUT = os.path.join(ROOT, "cad/out/printed")
GLOVE_R = os.path.join(ROOT, "third_party/yubi-hw/STEP/glove/YUBI Glove Assy_ver2_R.STEP")
GLOVE_L = os.path.join(ROOT, "third_party/yubi-hw/STEP/glove/YUBI Glove Assy_ver2_L.STEP")
ADAFRUIT_AS5600 = os.path.join(ROOT, "cad/vendor/adafruit_6357_as5600.step")
PLATE = "UPPER_PLATE_CAMERA_BKT_12bit_AS5601_v2_INSERT_TYPE"

TOL = 0.5  # mm^3 of overlap tolerated (numerical noise on touching faces)


# --------------------------------------------------------------------------------------
# Robot gripper
# --------------------------------------------------------------------------------------
def pick(parts, name, pred):
    s = [p for p in parts[name] if pred(p.Center())]
    assert len(s) >= 1, name
    return s


def fuse_all(shapes):
    out = shapes[0]
    for s in shapes[1:]:
        out = out.fuse(s)
    return out.clean()


def outer_only(shape):
    """Drop internal void shells (hairline gaps between a bore and its shaft become
    voids when the parts are merged; a print should be solid there)."""
    solids = shape.Solids()
    assert len(solids) == 1, f"expected one solid, got {len(solids)}"
    shell = BRepClass3d.OuterShell_s(solids[0].wrapped)
    return cq.Solid.makeSolid(cq.Shell(shell)).fix()


def make_drives(toyota):
    right = lambda c: c.x < B.P.wrist_axis_x      # noqa: E731
    left = lambda c: c.x > B.P.wrist_axis_x       # noqa: E731
    gear = "GEAKB1.0-30-6-B-8N-QFC17-M3-LL"
    drive_r = fuse_all([B.one(toyota, "GEAR_SHAFT")] + pick(toyota, gear, right)
                       + pick(toyota, "KEG3-8", right) + pick(toyota, "WSSAB10-5-1", right))
    drive_l = fuse_all([B.one(toyota, "SSFRHQ8-20-F6-P5-T6-Q5-KC8-A12")] + pick(toyota, gear, left)
                       + pick(toyota, "KEG3-8", left) + pick(toyota, "WSSAB10-5-1", left))
    return outer_only(drive_r), outer_only(drive_l)


def make_shim():
    """1 mm ring that fills the 695ZZ (4 mm) in a 5 mm bearing seat; touches only the outer race."""
    return cq.Solid.makeCylinder(6.4, 1.0).cut(cq.Solid.makeCylinder(4.9, 1.0))


# --------------------------------------------------------------------------------------
# Glove
# --------------------------------------------------------------------------------------
MAGNET_X, MAGNET_Z = -11.6905, 1020.0       # finger magnet axis (glove assembly coords)
CHIP_FACE_Y = 26.92                          # AS5601 chip face; magnet top is at 24.92
SLAB_TOP_Y = 21.92                           # top of the plate's main slab
BOARD_L, BOARD_W, PCB_T = 25.4, 17.78, 1.57  # Adafruit 6357
CHIP_H = 1.5                                 # SOIC-8 body height above the PCB
BOARD_HOLES = [(2.5, 2.5), (2.5, 15.2), (22.9, 2.5), (22.9, 15.2)]   # board coords, mm
PCB_FACE_Y = CHIP_FACE_Y + CHIP_H            # component-side face of the PCB (= old PCB plane)
BOSS_D, PILOT_D, PILOT_DEPTH = 4.2, 1.7, 5.5  # M2 x 6 self-tapping into PLA/PETG


def board_trsf():
    """Adafruit board coords (x along length, y across, z up from the PCB back) ->
    glove coords: length along z, components facing the magnet (-y), chip on the axis."""
    t = gp_Trsf()
    # x_g = -(by - W/2) + MAGNET_X ; y_g = PCB_FACE_Y + PCB_T - bz ; z_g = (bx - L/2) + MAGNET_Z
    t.SetValues(0, -1, 0, MAGNET_X + BOARD_W / 2,
                0, 0, -1, PCB_FACE_Y + PCB_T,
                1, 0, 0, MAGNET_Z - BOARD_L / 2)
    return t


def board_point(bx, by):
    return MAGNET_X - (by - BOARD_W / 2), MAGNET_Z + (bx - BOARD_L / 2)


def load_board():
    parts = B.load_toyota_parts(ADAFRUIT_AS5600)
    t = board_trsf()
    placed = {}
    for nm, ss in parts.items():
        placed[nm] = [cq.Shape.cast(BRepBuilderAPI_Transform(s.wrapped, t, True).Shape()) for s in ss]
    return placed


def make_glove_plate(plate, board):
    # 1. remove Toyota's two AS5601 bosses (they sit under the bigger board)
    p = plate.cut(B.box(-14.5, -7.3, SLAB_TOP_Y + 0.08, 32.0, 1009.0, 1031.0))
    # 2. clearance (0.4 mm) around the board and every component on it
    for nm, ss in board.items():
        for s in ss:
            bb = s.BoundingBox()
            p = p.cut(B.box(bb.xmin - 0.4, bb.xmax + 0.4, bb.ymin - 0.4, 32.0, bb.zmin - 0.4, bb.zmax + 0.4))
    # 3. four new bosses up to the PCB's component face, with self-tapping M2 pilots
    for bx, by in BOARD_HOLES:
        x, z = board_point(bx, by)
        p = p.fuse(B.cyl_y(BOSS_D, SLAB_TOP_Y - 0.5, PCB_FACE_Y, x, z))
        p = p.cut(B.cyl_y(PILOT_D, PCB_FACE_Y - PILOT_DEPTH, PCB_FACE_Y + 0.1, x, z))
    return p.clean()


# --------------------------------------------------------------------------------------
def solid_ok(s):
    """Toyota's left-glove FINGER t30_L solid is stored inside-out (negative volume),
    which makes boolean checks report it overlapping everything. Flip such solids."""
    return cq.Shape.cast(s.wrapped.Reversed()) if B.volume(s) < 0 else s


def check(new, neighbours, label, failures, skip=(), baseline=None):
    """Fail on overlap with any neighbour. With `baseline` (the Toyota part being
    replaced), only overlap beyond what the original part already had counts, e.g.
    screws modelled at nominal size inside their tapped holes."""
    for nm, ss in neighbours.items():
        if nm in skip:
            continue
        for s in ss:
            a, b = new.BoundingBox(), s.BoundingBox()
            if (a.xmax < b.xmin or b.xmax < a.xmin or a.ymax < b.ymin or b.ymax < a.ymin
                    or a.zmax < b.zmin or b.zmax < a.zmin):
                continue                  # cannot touch (also sidesteps broken solids)
            s = solid_ok(s)
            v = B.common_volume(new, s)
            if baseline is not None and v > TOL:
                v -= B.common_volume(baseline, s)
            if v > TOL:
                failures.append(f"{label} x {nm}: {v:.2f} mm^3")


def export(shape, name):
    cq.exporters.export(cq.Workplane().add(shape), os.path.join(OUT, name + ".step"))
    stl = os.path.join(OUT, name + ".stl")
    cq.exporters.export(cq.Workplane().add(shape), stl, tolerance=0.01, angularTolerance=0.1)
    m = trimesh.load(stl)                 # weld seams so slicers see a closed mesh
    m.merge_vertices(digits_vertex=2)   # 0.01 mm: also welds sliver seams on the gear teeth
    m.update_faces(m.nondegenerate_faces()); m.update_faces(m.unique_faces())
    m.remove_unreferenced_vertices(); trimesh.repair.fill_holes(m); trimesh.repair.fix_normals(m)
    m.export(stl)
    return bool(m.is_watertight)


def main():
    os.makedirs(OUT, exist_ok=True)
    failures, summary = [], {}

    # robot
    toyota = B.load_toyota_parts(B.TOYOTA_ASSY)
    drive_r, drive_l = make_drives(toyota)
    merged = {"GEAR_SHAFT", "SSFRHQ8-20-F6-P5-T6-Q5-KC8-A12", "GEAKB1.0-30-6-B-8N-QFC17-M3-LL",
              "KEG3-8", "WSSAB10-5-1",
              # parts the YAM build removes
              "DYNAMIXEL_XM430-W350-R", "BRACKET_DYNAMIXEL", "BRACKET_GRIPPER", "UR5e_FLANGE",
              # screws/bearings that sit in or on the drive parts by design
              "CBSTNR3-8", "CBSTNR2-5", "CBSTNR2.5-6", "MTA05-13ZZ_DBS"}
    check(drive_r, toyota, "drive_R", failures, skip=merged)
    check(drive_l, toyota, "drive_L", failures, skip=merged)
    check(drive_r, {"drive_L": [drive_l], "coupler": [B.make_coupler()]}, "drive_R", failures)
    for nm, s in [("drive_R_printed", drive_r), ("drive_L_printed", drive_l), ("bearing_shim_1mm", make_shim())]:
        wt = export(s, nm)
        summary[nm] = {"volume_mm3": round(B.volume(s), 1), "stl_watertight": wt}

    # glove (left and right use the same upper plate in the same place; check both)
    board = load_board()
    chip = [s for s in board["SOIC8_150MIL"]][0].Center()
    assert abs(chip.x - MAGNET_X) < 0.05 and abs(chip.z - MAGNET_Z) < 0.05, chip
    plate_new = None
    for path in (GLOVE_R, GLOVE_L):
        glove = B.load_toyota_parts(path)
        plate = B.one(glove, PLATE)
        plate_new = make_glove_plate(plate, board)
        skip = {PLATE, "AS5601", "CBSTNR3-5"}           # replaced / no longer used
        side = "R" if path == GLOVE_R else "L"
        for nm, ss in board.items():
            for s in ss:
                check(s, glove, f"glove_{side} board.{nm}", failures, skip=skip)
                check(s, {"plate_new": [plate_new]}, f"glove_{side} board.{nm}", failures)
        check(plate_new, glove, f"glove_{side} plate_new", failures, skip=skip, baseline=plate)
        magnet_top = B.one(glove, "MAGNET_D6_AS5601").BoundingBox().ymax
        chip_face = min(s.BoundingBox().ymin for s in board["SOIC8_150MIL"])
        summary[f"glove_{side}_air_gap_mm"] = round(chip_face - magnet_top, 2)
        lowest = min(s.BoundingBox().ymin for ss in board.values() for s in ss)
        finger_top = max(s.BoundingBox().ymax for k, ss in glove.items() if k.startswith("FINGER") for s in ss)
        summary[f"glove_{side}_board_to_finger_mm"] = round(lowest - finger_top, 2)
    wt = export(plate_new, "glove_upper_plate_as5600")
    board_all = fuse_all([s for ss in board.values() for s in ss])
    export(board_all, "adafruit_as5600_reference")
    summary["glove_upper_plate_as5600"] = {"volume_mm3": round(B.volume(plate_new), 1), "stl_watertight": wt}
    summary["failures"] = failures
    json.dump(summary, open(os.path.join(OUT, "printed_summary.json"), "w"), indent=1)
    print(json.dumps(summary, indent=1))
    if failures:
        sys.exit("INTERFERENCE:\n  " + "\n  ".join(failures))


if __name__ == "__main__":
    main()
