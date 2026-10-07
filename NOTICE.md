# Notices

**YUBI gripper.** The design is copyright 2026 Toyota Motor Corporation, licensed
under CERN-OHL-W-2.0: https://github.com/Toyota/yubi-hw. It was published with AIRoA
as YUBI (Ohkawa, Arima et al., CoRL 2026, arXiv:2606.10244). This repository's parts
are modified from it:

- `bracket_trimmed` is Toyota's `BRACKET_GRIPPER`, cut back.
- `motor_bracket` reuses the case-side tab of Toyota's `BRACKET_DYNAMIXEL`.
- `coupler` reproduces the Dynamixel horn interface on Toyota's `GEAR_SHAFT`.

Meshes under `sim/assets/` and `sdk/overlay/` are generated from Toyota's STEP files.

Modifications copyright 2026 Janos Meny, released under CERN-OHL-W-2.0.

**i2RT SDK.** Copyright I2RT Robotics, MIT licence: https://github.com/i2rt-robotics/i2rt.
`sdk/i2rt-yubi_4310.patch` and the config in `sdk/overlay/` follow the SDK's existing
gripper files.

**DM4310 dimensions.** Checked against Damiao's DM-J4310 model as published in OpenArm
v1.1 (Enactic, CERN-OHL-S-2.0). It was used for measurements only; no geometry from it
is included here. `cad/out/dm4310_envelope_reference.step` is a plain cylinder drawn
from those dimensions.
