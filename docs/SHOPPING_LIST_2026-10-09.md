# Proposed shopping list — October 9 printed prototype

Checked **October 7, 2026, Pacific time**, for delivery to **San Francisco 94158**
by **Friday October 9**, with the M5 screw picked up at **Hayward Home Depot**.

Build scope: **two YAM robot grippers and two YUBI gloves, one left and one right**,
printed for the weekend and upgraded with the precision parts later. Per-unit
hardware is doubled; shared packs are bought once. Each glove gets one XIAO,
perfboard, Adafruit 6357 board and Radial 9042 magnet. The left glove uses Toyota's
left-hand printed parts and the same purchased hardware as the right glove.

The source requirements are [BOM_US.md](BOM_US.md) and
[PRINTED_PROTOTYPE.md](PRINTED_PROTOTYPE.md). This proposal records the prepared
cart contents. **Nothing has been ordered, reserved, checked out or paid.** Prices
and stock are a dated snapshot; Friday delivery is not confirmed for every vendor.

## Changes from the original list

- Use Adafruit 6357 AS5600 with `glove_upper_plate_as5600`. Remove MIKROE-4204
  because it does not fit; drop the AS5601-SO_EK_AB fallback.
- Buy two Radial 9042 diametric magnets; the Adafruit board includes no magnet.
- Add four M2×6 socket-head screws per glove for the encoder. Two robots and two
  gloves need **24 total: 8 robot + 8 original glove + 8 encoder mount**.
- Replace the mxuteuk 888-piece mixed screw kit (`B0G8F366MV`): its diagram shows
  M2×12/16 only, with no M2×6. The $8.99 M2-only kit (`B0C6M6MJ8M`) explicitly lists
  **30 M2×6 in its packaging text**, leaving 6 spare. The diagram has mislabeled
  sizes; use the explicit packaging text for the count. The existing M2.5 and M3
  kits cover the other standard screws, so there are still three screw kits.
- Remove CBSTNR3-5 ×4; the new encoder plate uses the four M2 mount screws.
- Use six 695ZZ bearings with six printed 1 mm outer-race shims and two stock
  M5×0.8×70 socket-head screws for the prototypes. Keep the original precision parts
  in the separate late shipment.

## Friday carts and pickup

Quantities below are **units/packs to buy**, with assembly quantities called out
where a pack contains surplus. Prices are the displayed guest-cart prices, before
tax and freight unless stated.

### Amazon — $250.57 parts

| Part | Buy qty | Pack / assembly use | Unit price | Line total |
|---|---:|---|---:|---:|
| [ELP USBFHD01M-L180, new](https://www.amazon.com/dp/B00LQ854AG) | 4 | one camera for each of two robots and two gloves | $44.99 | $179.96 |
| [mxuteuk M2 socket-head screw kit](https://www.amazon.com/dp/B0C6M6MJ8M) | 1 | 520-piece kit; 30 M2×6, use 24, leaving 6 spare | $8.99 | $8.99 |
| [VGBUY M2.5 screw kit](https://www.amazon.com/dp/B0FJ1YMG3J) | 1 | M2.5×6: 50 available/8 needed; ×8: 40/4; ×10: 40/8 | $9.99 | $9.99 |
| [ALLWIN M3 screw kit](https://www.amazon.com/dp/B0F5QKDW7Y) | 1 | M3×6/8/10/12: 30 each; need 2/8/12/4 | $5.79 | $5.79 |
| [RAPOLL neoprene sheet](https://www.amazon.com/dp/B0BKQRN7S6) | 1 | 12×12-inch shared sheet for eight pad pieces across two robots and two gloves | $6.89 | $6.89 |
| [MOWPOG #16 return bands](https://www.amazon.com/dp/B0FCM95WH7) | 1 | 700-band pack; use two bands | $5.99 | $5.99 |
| [KADRICK M2–M5 insert kit](https://www.amazon.com/dp/B0D5V3TZLB) | 1 | M2×3: 60/16; M3×4: 50/4; M3×5: 50/12; includes printed adapter inserts | $15.98 | $15.98 |
| [KADRICK M2/M2.5 insert kit](https://www.amazon.com/dp/B0FD7DQS8Y) | 1 | M2.5×4: 60/20 needed | $9.99 | $9.99 |
| [KABOBEARING 695ZZ, 5×13×4 mm](https://www.amazon.com/dp/B0CRP3K8ZF) | 1 | 10 bearings; use six for two printed grippers | $6.99 | $6.99 |

All selected offers show delivery by Friday **with Prime** to 94158. The four new
cameras (quantity four checked), replacement M2 kit and M3 kit show October 9;
the other items show October 8. Guest shipping misses Friday. Prime sign-in and offer confirmation are
still required. The cheaper used camera offer misses Friday. The bearings were the
cheapest matching pack found with delivery by Friday in the ascending-price search.

Advertised Prime prices of $7.99 for the M2.5 kit, $4.63 for M3 and $5.59 for the
bearings would reduce this cart to about **$246.01** if applied after sign-in.

### McMaster — $43.75 parts

| Part | Buy qty | Pack / assembly use | Line total |
|---|---:|---|---:|
| [91290A009 — M2.5×15 socket head](https://www.mcmaster.com/91290A009/) | 2 | two ten-packs, 20 screws available; use 12 | $8.50 |
| [92855A307 — M3×6 low head](https://www.mcmaster.com/92855A307/) | 1 | one pack, 25 screws available; use 12 | $7.30 |
| [92855A309 — M3×8 low head](https://www.mcmaster.com/92855A309/) | 1 | one pack, 25 screws available; use 8 | $7.55 |
| [92855A839 — M2×8 low head](https://www.mcmaster.com/92855A839/) | 1 | one pack, 10 screws available; use 4 | $20.40 |

The site displays October 8 delivery. The service, freight charge and destination-specific
arrival to 94158 remain unquoted; the checkout/contact flow was not entered.

### MISUMI stocked shipment — $152.56 parts

| Part | Buy qty | Unit price | Line total |
|---|---:|---:|---:|
| [CBSTBR2-5](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTBR2-5) | 12 | $5.24 | $62.88 |
| [CBSTNR3-8](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTNR3-8) | 8 | $5.05 | $40.40 |
| [JZF8-5](https://us.misumi-ec.com/vona2/detail/110302640340/?HissuCode=JZF8-5) | 8 | $2.70 | $21.60 |
| [LRLB3-6](https://us.misumi-ec.com/vona2/detail/110300245210/?HissuCode=LRLB3-6) | 2 | $6.06 | $12.12 |
| [HNTT5-5](https://us.misumi-ec.com/vona2/detail/110302246150/?HissuCode=HNTT5-5) | 2 | $0.73 | $1.46 |
| [JPBPB2-3](https://us.misumi-ec.com/vona2/detail/110300557320/?HissuCode=JPBPB2-3) | 2 | $7.05 | $14.10 |

All six lines show stock and October 7 **dispatch**, not arrival. Shipping remains
unselected because a login is required to quote it. Choose a quoted service with
actual Friday arrival; a Thursday dispatch needs next-day air. Product pages state
a 6 p.m. Eastern same-day cutoff. Keep the late parts out of this shipment.

### DigiKey — $29.84 parts; $57.77 estimated with selected freight/tariff

| Part | Buy qty | Unit price | Line total |
|---|---:|---:|---:|
| [XIAO ESP32C6 113991254](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/113991254/24613066) | 2 | $5.38 | $10.76 |
| [Radial Magnets 9042, Ø6×2.5 mm, diametric](https://www.digikey.com/en/products/detail/radial-magnets-inc/9042/5640338) | 2 | $0.63 | $1.26 |
| [SparkFun PRT-08808 / 08808 perfboard](https://www.digikey.com/en/products/detail/sparkfun-electronics/08808/7387401) | 2 | $2.96 | $5.92 |
| [6357 — AS5600 Magnetic Angle Sensor, STEMMA QT](https://www.digikey.com/en/products/detail/adafruit-industries-llc/6357/26832926) | 2 | $5.95 | $11.90 |

All four lines show Immediate availability. **FedEx Overnight P.M. Delivery is
selected at $26.99**; estimated tariffs are $0.94. Total is **$57.77 before tax**.
The site warns of an additional business day for processing; dispatch by Thursday
October 8 is necessary for Friday. No destination-specific Friday guarantee is
displayed. The two Adafruit 6357 boards (1528-6357-ND) are in this overnight cart;
the separate Adafruit cart was emptied. MIKROE-4204 and the AS5601 fallback are absent.
Use direct VIN (3.3 V), GND, SCL and SDA wiring to the XIAO; no QT cable is needed.

### Hayward Home Depot pickup — $3.97 parts

| Part | Buy qty | Pack / assembly use | Line total |
|---|---:|---|---:|
| [Everbilt M5×0.8×70 mm socket-head cap screw](https://www.homedepot.com/p/204283625) | 1 | two M5×0.8×70 socket-head screws; use both, one per glove | $3.97 |

Model **844868**, Store SKU **540934**. Free **Hayward pickup selected**, Today;
three packs in stock at the October 7 check. Store #1017, **21787 Hesperian Blvd,
Hayward CA 94541**, **aisle 21, bay 018**. Janos is going to Hayward today;
this one two-pack covers both gloves. Nothing reserved or ordered.

## Proper-build late shipment — $571.12 parts

Prepare these separately now so available parts can arrive as early as possible.
Dates are **dispatch dates**, not delivery promises. Shipping is unselected; login
is required to quote freight. Request partial shipment and the fastest quoted air
service so undated bearings do not hold the other parts.

| Part | Buy qty | Unit price | Line total | Displayed dispatch |
|---|---:|---:|---:|---|
| [GEAKB1.0-30-6-B-8N-QFC17-M3-LL](https://us.misumi-ec.com/vona2/detail/110300428430/?HissuCode=GEAKB1.0-30-6-B-8N-QFC17-M3-LL) | 4 | $42.51 | $170.04 | October 14 |
| [SSFRHQ8-20-F6-P5-T6-Q5-A12-KC8](https://us.misumi-ec.com/vona2/detail/110300088230/?HissuCode=SSFRHQ8-20-F6-P5-T6-Q5-A12-KC8) | 2 | $26.71 | $53.42 | October 14 |
| [MTA05-13ZZ DBS](https://us.misumi-ec.com/vona2/detail/221000531127/?HissuCode=MTA05-13ZZ%20DBS) | 6 | $23.58 | $141.48 | TBD; no date |
| [WSSAB10-5-1](https://us.misumi-ec.com/vona2/detail/110302677010/?HissuCode=WSSAB10-5-1) | 6 | $23.42 | $140.52 | October 10 |
| [KEG3-8](https://us.misumi-ec.com/vona2/detail/110302681730/?HissuCode=KEG3-8) | 4 | $3.90 | $15.60 | October 10 |
| [JPDPB2-3](https://us.misumi-ec.com/vona2/detail/110300557320/?HissuCode=JPDPB2-3) | 2 | $9.89 | $19.78 | October 15 |
| [AJKTNS5-70](https://us.misumi-ec.com/vona2/detail/110300599320/?HissuCode=AJKTNS5-70) | 2 | $15.14 | $30.28 | October 12 |

The shaft catalog normalizes the `A12-KC8` feature order; this is the same configured
shaft listed as `KC8-A12` in the BOM. Several parts will not arrive early next week:
the gears/shafts dispatch October 14 and the diamond pins October 15. The five custom
machined part types now need two each (ten parts total) and remain outside these
carts; the original one-set finalREV RFQ is pending. A revised two-set quote, metal-thread
drawings and physical wrist verification are still required before release; no new
supplier message or machining order has been sent.

## Shared-pack count check

Counts include both robots and both gloves, plus the extra inserts for the printed
couplers/flanges. Pack counts were checked against product text/size diagrams.

| Required size / item | Needed | Available in selected shared packs | Result |
|---|---:|---:|---|
| M2×6 socket head | 24 | 30 | 6 spare |
| M2.5×6 / ×8 / ×10 socket head | 8 / 4 / 8 | 50 / 40 / 40 | One VGBUY kit covers all three |
| M2.5×15 socket head | 12 | 20 (two McMaster ten-packs) | 8 spare |
| M3×6 / ×8 / ×10 / ×12 standard socket head | 2 / 8 / 12 / 4 | 30 each | One ALLWIN kit covers all four |
| M3×6 low head / M3×8 low head / M2×8 low head | 12 / 8 / 4 | 25 / 25 / 10 | One of each McMaster low-head pack |
| M2×3 inserts | 16 | 60 in the M2–M5 kit | Includes 8 extra for two printed couplers |
| M2.5×4 inserts | 20 | 60 in the M2/M2.5 kit | One kit |
| M3×5 inserts | 12 | 50 in the M2–M5 kit | Includes 4 extra for two printed flanges |
| M3×4 inserts | 4 | 50 in the M2–M5 kit | One kit |
| 695ZZ bearings | 6 | 10 | 4 spare; print 6 shims |
| M5×0.8×70 socket-head screws | 2 | 2 | One Hayward two-pack |
| #16 return bands | 2 | 700 | One pack |
| Neoprene pad pieces | 8 | One 12×12 in (304.8×304.8 mm) sheet | Shared cutting layout covers both sets |

The rubber meshes are about 83 mm long and 20/30 mm wide; there is ample sheet
area for the eight pad pieces with cutting allowance. Match Toyota's pad outlines
when cutting. Insert quantities cover the printed build; metal threads replace the
adapter inserts in the machined upgrade. Fit/strength checks remain as in the BOM.

## Cost and remaining delivery checks

| Group | Current amount | Basis |
|---|---:|---|
| Amazon | $250.57 | Parts; Prime deals not applied in guest cart |
| McMaster | $43.75 | Parts; freight unquoted |
| MISUMI stocked | $152.56 | Parts; freight unquoted |
| DigiKey | $57.77 | Parts + selected overnight freight + estimated tariffs |
| Hayward Home Depot | $3.97 | Parts; free pickup selected |
| **Prototype/shared subtotal** | **$508.62** | Before tax and unquoted freight |
| MISUMI late | $571.12 | Parts; freight unquoted |
| **Prototype + proper-build carts** | **$1,079.74** | Before tax and unquoted freight; excludes custom machining |

Before placing orders:

1. Sign in to Amazon Prime and reconfirm the selected offers deliver by Friday.
2. Obtain MISUMI and McMaster shipping quotes with actual arrival to 94158.
3. Confirm DigiKey dispatch timing despite its processing warning.
4. Recheck Hayward stock before the pickup trip and request partial shipment for
   late MISUMI parts.

Printing supplies, any missing hookup wire/solder/adhesive and custom machining are
outside these totals. Check KADRICK insert fit, the substituted rubber/band and
prototype assembly before running the robot; follow the printed prototype's motor
limits. Shared hardware is reused for the proper build rather than purchased twice.
