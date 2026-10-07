# Parts list (US sourcing)

Two builds: the **robot gripper** (this repo's modified YUBI, on the YAM) and the
**handheld** for data collection (Toyota's YUBI glove, built unmodified). The glove part
list is [further down](#handheld-yubi-glove-one-right-hand).

## Robot gripper

Everything you buy for one yubi-yam gripper. It is Toyota's
[YUBI robot-gripper BOM](https://github.com/Toyota/yubi-hw/blob/main/docs/BOM/YUBI%20Gripper_DYNAMIXEL_BOM.md)
without the Dynamixel and UR5e parts, plus the parts this design adds. Toyota's links go
to Japanese shops; the sizes below are measured from their CAD, so you can order US
equivalents.

**Fastest route:** every item with a MISUMI part number can go into one
[MISUMI USA](https://us.misumi-ec.com) cart. MISUMI USA also has
[express options](https://us.misumi-ec.com/guide/category/ecatalog/st.html), down to
same-day shipping, for eligible parts; get a quote to see which ones qualify. Order before
1 pm ET (10 am PT). The generic items also come from Amazon or McMaster-Carr, usually in
1–2 days in the Bay Area.

### Not bought

| Part | Source |
|---|---|
| DM4310 motor | out of your stock YAM gripper |
| printed parts | Toyota's `STL/gripper/` (case, upper plate, finger pads, flaps, finger attachments) and this repo's `cad/out/` (flange, trimmed bracket, motor bracket, coupler) |

### Motion parts (order first)

| Qty | Part | MISUMI P/N | Size (from CAD) | Alternative |
|---|---|---|---|---|
| 2 | spur gear | `GEAKB1.0-30-6-B-8N-QFC17-M3-LL` | module 1, 30 teeth, 6 mm face; Ø17 × 10 mm hub; Ø8 bore with 3 mm keyway and M3 set screw | a different gear would need its face width and hub checked against the case |
| 1 | left finger shaft | `SSFRHQ8-20-F6-P5-T6-Q5-KC8-A12` | Ø8 × 32 mm, stepped to Ø5 at both ends, 3 mm keyway | none |
| 1 | right finger shaft (`GEAR_SHAFT`) | machined by Toyota (A2024) | Ø20 flange + Ø8 keyed shaft, STEP in Toyota's repo | print it at 100 % infill to get going; machine it later (local shop or online CNC) |
| 3 | ball bearing | `MTA05-13ZZ DBS` | 5 mm bore, 13 mm OD, 5 mm wide | 695ZZ (5 × 13 × 4 mm) plus a 1 mm shim |
| 3 | washer | `WSSAB10-5-1` | Ø10 × Ø5 × 1 mm | any M5 thin washer with a 5.0–5.3 mm hole |
| 2 | parallel key | `KEG3-8` | 3 × 3 × 8 mm | any 3 × 3 × 8 mm key |

### Camera and pads

| Qty | Part | Where |
|---|---|---|
| 1 | ELP-USBFHD01M-L180 fisheye USB camera (the exact one Toyota uses) | [Amazon](https://www.amazon.com/dp/B00LQ854AG) |
| 1 | 1.5 mm rubber sheet for the finger pads (Toyota: NBR "HYPER V" sheet) | any 1.5 mm NBR or silicone sheet, adhesive-backed if possible |

### Screws, inserts, pins

| Qty | Fastener | MISUMI P/N | Used for |
|---|---|---|---|
| 6 | M2 × 5 ultra-low head | `CBSTNR2-5` | gear shaft → coupler (4); motor bracket → case side (2) |
| 4 | M3 × 8 ultra-low head | `CBSTNR3-8` | gears → finger attachments |
| 4 | M2 × 6 socket head | `CB2-6` | finger attachments, pads, flaps |
| 2 | M2.5 × 6 socket head | `CB2.5-6` | camera |
| 4 | M2.5 × 10 socket head | `CB2.5-10` | pads |
| 3 | M2.5 × 15 socket head | `CB2.5-15` | case → upper plate |
| 4 | M3 × 8 socket head | `CBE3-8` | case → bracket (2); bracket ears → flange (2) |
| 1 + 1 | Ø2 × 3 locating pins, round + diamond | `JPBPB2-3`, `JPDPB2-3` | bracket → upper plate |
| 4 | brass insert | `SB-304550` | Toyota's printed parts (as in their BOM) |
| 5 | brass insert | `SB-264040` | Toyota's printed parts (as in their BOM) |
| 4 | M2 brass insert | `SB-203030` | case (motor bracket screws) |
| **added by yubi-yam** | | | |
| 6 | M3 × 10 socket head | `CB3-10` | flange → YAM wrist |
| 6 | M3 × 6 low head (DIN 7984) | | coupler → DM4310 rotor |
| 4 | M3 × 8 low head (DIN 7984) | | DM4310 → motor bracket |
| 2 | M2 × 8 low head (DIN 7984) | | motor bracket → case back |
| 2 | M3 × 12 socket head | `CB3-12` | flange + bracket → upper plate |
| 4 | M2 brass insert, 3.0 mm OD × 3 mm | `SB-203030` | coupler |
| 2 | M3 heat-set insert for a Ø4.0 mm hole, 5 mm long | | flange (e.g. CNC Kitchen / Ruthex M3 standard) |

Low-head (DIN 7984) screws: McMaster-Carr "low-profile socket head screws", or MISUMI's
low-head cap screws. Toyota's ultra-low-head `CBSTNR` screws also work where the length
matches.

### Not needed from Toyota's BOM

Dynamixel XM430-W350-R, `BRACKET_DYNAMIXEL`, `BRACKET_GRIPPER` (replaced by the printed
trimmed bracket), `UR5e_FLANGE`, and the UR5e-only screws and pins (`CBE6-10`,
`XDSHC6-P4-L6-B5`), 4 of the 7 `CB2.5-15` (they held the Dynamixel), and the horn's centre
`CBSTNR2.5-6`, which is optional with the coupler.

## Handheld: YUBI glove, one right hand

Built exactly as in Toyota's
[glove assembly guide](https://github.com/Toyota/yubi-hw/tree/main/docs/AssemblyInstruction)
and [BOM](https://github.com/Toyota/yubi-hw/blob/main/docs/BOM/YUBI%20Glove%20Assy_BOM.md),
no changes. The glove's fingers have their gears printed in, so it needs no metal gears.

**Printed** (Toyota's `STL/glove/`): upper plate, under plate, `FINGER with Gear_t30_R`,
`FINGER with Gear_t20_L`, both flaps, grip, `HOLDER_Quest_R`, `COVER_PCB_R`,
`COVER_CABLE_R`.

| Qty | Part | Where | Note |
|---|---|---|---|
| 1 | Meta Quest Touch Plus controller, right | the one from your Quest 3 | buy a spare only if you want to keep using the Quest normally |
| 1 | ELP-USBFHD01M-L180 fisheye camera | [Amazon](https://www.amazon.com/dp/B00LQ854AG) | the same camera as on the robot gripper, so order 2 in total |
| 1 | Seeed XIAO ESP32C6 | Seeed, DigiKey or Amazon | runs the encoder firmware in [yubi-sw](https://github.com/airoa-org/yubi-sw/tree/main/firmware/ESP32C6_AS5601) |
| 1 | AS5601 encoder breakout, 20 × 13.5 mm, M3 holes 15 mm apart, magnet included | [Switch Science #3494](https://www.switch-science.com/products/3494) (ships from Japan) | **the one item unlikely to arrive this week**; the glove's pocket is sized for this board. Other AS5601 modules (e.g. Elecrow) need their size checked |
| 1 | perfboard, 1 × 1 inch | SparkFun 08808 (DigiKey) or any | carries the XIAO |
| 2 | USB-C cables | any | camera and XIAO to the PC |
| 1 | 1.5 mm rubber sheet | the same sheet as for the gripper | |
| 1 | small rubber band (Japanese size No. 16) | any | |

| Qty | Fastener | MISUMI P/N |
|---|---|---|
| 4 | M2 × 6 socket head | `CB2-6` |
| 2 | M2.5 × 6 socket head | `CB2.5-6` |
| 2 | M2.5 × 8 socket head | `CB2.5-8` |
| 3 | M2.5 × 15 socket head | `CB2.5-15` |
| 1 | M3 × 6 socket head | `CB3-6` |
| 2 | M3 × 5 ultra-low head | `CBSTNR3-5` |
| 1 | M3 × 6 knurled thumb screw | `LRLM3-6` |
| 1 | M5 adjusting bolt, 70 mm | `AJKTNS5-70` |
| 1 | M5 T-slot nut | `HNTT5-5` |
| 5 | brass insert | `SB-264040` |
| 2 | brass insert | `SB-304540` |
| 4 | POM bushing | `JZF8-5` |

### Tabletop rig (optional)

Toyota's rig is an aluminium-extrusion frame that holds the Quest headset above the desk
(`STL/stationary/Quest_mount.stl`), plus a RealSense overhead camera and a USB foot pedal
to start and stop recordings. For a first setup, the printed Quest mount on a tripod or a
clamp arm does the same job. Your SO-101 cameras can stand in for the RealSense, and a
foot pedal (any USB one) is a nice-to-have.

## Weekend plan

1. **Tonight:** Amazon (2 cameras, XIAO ESP32C6, rubber sheet, inserts) and McMaster
   (screws, keys, 695ZZ bearings, washers). Order the AS5601 board from Switch Science;
   until it arrives the glove works for tracking, just without the gripper opening.
2. **Tomorrow before 10 am PT:** MISUMI quote for the two gears, the left shaft and the
   glove's MISUMI-only parts (`JZF8-5` bushings, `AJKTNS5-70`, `HNTT5-5`, `LRLM3-6`),
   with express shipping where available.
3. **Meanwhile:** print everything, including Toyota's `GEAR SHAFT.stl` as a stand-in.
4. If the gears don't make it, you can still assemble and test the motor, the coupler and
   the wrist fit, and add the fingers when the gears arrive.
