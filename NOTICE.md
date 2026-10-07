# Notices

**YUBI gripper.** The design is copyright 2026 Toyota Motor Corporation, licensed
under CERN-OHL-W-2.0: https://github.com/Toyota/yubi-hw. It was published with AIRoA
as YUBI (Ohkawa, Arima et al., CoRL 2026, arXiv:2606.10244). This repository's parts
are modified from it:

- `bracket_trimmed` is Toyota's `BRACKET_GRIPPER`, cut back.
- `motor_bracket` reuses the case-side tab of Toyota's `BRACKET_DYNAMIXEL`.
- `coupler` reproduces the Dynamixel horn interface on Toyota's `GEAR_SHAFT`.
- `cad/out/printed/drive_R_printed` / `drive_L_printed` merge Toyota's `GEAR_SHAFT`
  and the catalogue gear, shaft, key and washers of Toyota's assembly into single printable parts.
- `cad/out/printed/glove_upper_plate_as5600` is Toyota's glove `UPPER PLATE_CAMERA BKT`
  with new mounting bosses for an Adafruit AS5600 board.

Meshes under `sim/assets/` and `sdk/overlay/` are generated from Toyota's STEP files.

Modifications copyright 2026 Janos Meny, released under CERN-OHL-W-2.0.

**i2RT SDK.** Copyright I2RT Robotics, MIT licence: https://github.com/i2rt-robotics/i2rt.
`sdk/i2rt-yubi_4310.patch` and the config in `sdk/overlay/` follow the SDK's existing
gripper files.

**DM4310 dimensions.** Checked against Damiao's DM-J4310 model as published in OpenArm
v1.1 (Enactic, CERN-OHL-S-2.0). It was used for measurements only; no geometry from it
is included here. `cad/out/dm4310_envelope_reference.step` is a plain cylinder drawn
from those dimensions.

**Adafruit AS5600 board model.** `cad/vendor/adafruit_6357_as5600.step` is from
https://github.com/adafruit/Adafruit_CAD_Parts, copyright Adafruit Industries, MIT
licence (`cad/vendor/LICENSE-adafruit-cad-parts`). Used for the glove fit check only.
