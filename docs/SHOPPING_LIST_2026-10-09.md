# Proposed shopping list — October 9 printed prototype

Checked **October 7, 2026, Pacific time**, for delivery to **San Francisco 94158**
by **Friday October 9**, with the M5 screw picked up at **Hayward Home Depot**.

Build scope: **one YAM robot gripper and one right-hand YUBI glove**, printed for
the weekend and upgraded with the precision parts later. Buy **two Adafruit 6357
boards and two Radial 9042 magnets** per the explicit purchasing request; the
installed requirement is one board and one magnet per glove. Other quantities
remain for one glove, and shared hardware is bought once.

The source requirements are [BOM_US.md](BOM_US.md) and
[PRINTED_PROTOTYPE.md](PRINTED_PROTOTYPE.md). This proposal records the prepared
cart contents. **Nothing has been ordered, reserved, checked out or paid.** Prices
and stock are a dated snapshot; Friday delivery is not confirmed for every vendor.

## Changes from the original list

- Use Adafruit 6357 AS5600 with `glove_upper_plate_as5600`. Remove MIKROE-4204
  because it does not fit; drop the AS5601-SO_EK_AB fallback.
- Buy two Radial 9042 diametric magnets; the Adafruit board includes no magnet.
- Add four M2×6 socket-head screws per glove for the encoder. One robot plus one
  glove now needs **12 total: 4 robot + 4 original glove + 4 encoder mount**.
- Replace the mxuteuk 888-piece mixed screw kit (`B0G8F366MV`): its diagram shows
  M2×12/16 only, with no M2×6. The $8.99 M2-only kit (`B0C6M6MJ8M`) explicitly lists
  **30 M2×6 in its packaging text**, leaving 18 spare. The diagram has mislabeled
  sizes; use the explicit packaging text for the count. The existing M2.5 and M3
  kits cover the other standard screws, so there are still three screw kits.
- Remove CBSTNR3-5 ×2; the new encoder plate uses the four M2 mount screws.
- Use three 695ZZ bearings with three printed 1 mm outer-race shims and a stock
  M5×0.8×70 socket-head screw for the prototype. Keep the original precision parts
  in the separate late shipment.

## Friday carts and pickup

Quantities below are **units/packs to buy**, with assembly quantities called out
where a pack contains surplus. Prices are the displayed guest-cart prices, before
tax and freight unless stated.

### Amazon — $160.59 parts

| Part | Buy qty | Pack / assembly use | Unit price | Line total |
|---|---:|---|---:|---:|
| [ELP USBFHD01M-L180, new](https://www.amazon.com/dp/B00LQ854AG) | 2 | One camera each for robot and glove | $44.99 | $89.98 |
| [mxuteuk M2 socket-head screw kit](https://www.amazon.com/dp/B0C6M6MJ8M) | 1 | 520 pieces; 30 M2×6, use 12 | $8.99 | $8.99 |
| [VGBUY M2.5 screw kit](https://www.amazon.com/dp/B0FJ1YMG3J) | 1 | 1001 pieces; covers M2.5×6/8/10 | $9.99 | $9.99 |
| [ALLWIN M3 screw kit](https://www.amazon.com/dp/B0F5QKDW7Y) | 1 | 400 pieces; covers M3×6/8/10/12 | $5.79 | $5.79 |
| [RAPOLL neoprene sheet](https://www.amazon.com/dp/B0BKQRN7S6) | 1 | 12×12 in, 1/16 in thick; shared sheet | $6.89 | $6.89 |
| [MOWPOG #16 return bands](https://www.amazon.com/dp/B0FCM95WH7) | 1 | 700-band pack; use one, one-time purchase | $5.99 | $5.99 |
| [KADRICK M2–M5 insert kit](https://www.amazon.com/dp/B0D5V3TZLB) | 1 | 520 pieces; printed-hole fit checks required | $15.98 | $15.98 |
| [KADRICK M2/M2.5 insert kit](https://www.amazon.com/dp/B0FD7DQS8Y) | 1 | 300 pieces; printed-hole fit checks required | $9.99 | $9.99 |
| [KABOBEARING 695ZZ, 5×13×4 mm](https://www.amazon.com/dp/B0CRP3K8ZF) | 1 | Pack of 10; use three | $6.99 | $6.99 |

All selected offers show delivery by Friday **with Prime** to 94158. The two new
cameras, replacement M2 kit and M3 kit show October 9; the other items show
October 8. Guest shipping misses Friday. Prime sign-in and offer confirmation are
still required. The cheaper used camera offer misses Friday. The bearings were the
cheapest matching pack found with delivery by Friday in the ascending-price search.

Advertised Prime prices of $7.99 for the M2.5 kit, $4.63 for M3 and $5.59 for the
bearings would reduce this cart to about **$156.03** if applied after sign-in.

### McMaster — $39.50 parts

| Part | Buy qty | Pack / assembly use | Line total |
|---|---:|---|---:|
| [91290A009 — M2.5×15 socket head](https://www.mcmaster.com/91290A009/) | 1 | Pack of 10; use six | $4.25 |
| [92855A307 — M3×6 low head](https://www.mcmaster.com/92855A307/) | 1 | Pack of 25; use six | $7.30 |
| [92855A309 — M3×8 low head](https://www.mcmaster.com/92855A309/) | 1 | Pack of 25; use four | $7.55 |
| [92855A839 — M2×8 low head](https://www.mcmaster.com/92855A839/) | 1 | Pack of 10; use two | $20.40 |

The site displays October 8 delivery. The service, freight charge and destination-specific
arrival to 94158 remain unquoted; the checkout/contact flow was not entered.

### MISUMI stocked shipment — $76.28 parts

| Part | Buy qty | Unit price | Line total |
|---|---:|---:|---:|
| [CBSTBR2-5](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTBR2-5) | 6 | $5.24 | $31.44 |
| [CBSTNR3-8](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTNR3-8) | 4 | $5.05 | $20.20 |
| [JZF8-5](https://us.misumi-ec.com/vona2/detail/110302640340/?HissuCode=JZF8-5) | 4 | $2.70 | $10.80 |
| [LRLB3-6](https://us.misumi-ec.com/vona2/detail/110300245210/?HissuCode=LRLB3-6) | 1 | $6.06 | $6.06 |
| [HNTT5-5](https://us.misumi-ec.com/vona2/detail/110302246150/?HissuCode=HNTT5-5) | 1 | $0.73 | $0.73 |
| [JPBPB2-3](https://us.misumi-ec.com/vona2/detail/110300557320/?HissuCode=JPBPB2-3) | 1 | $7.05 | $7.05 |

All six lines show stock and October 7 **dispatch**, not arrival. Shipping remains
unselected because a login is required to quote it. Choose a quoted service with
actual Friday arrival; a Thursday dispatch needs next-day air. Product pages state
a 6 p.m. Eastern same-day cutoff. Keep the late parts out of this shipment.

### DigiKey — $9.60 parts; $37.22 estimated with selected freight/tariff

| Part | Buy qty | Unit price | Line total |
|---|---:|---:|---:|
| [XIAO ESP32C6 113991254](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/113991254/24613066) | 1 | $5.38 | $5.38 |
| [Radial Magnets 9042, Ø6×2.5 mm, diametric](https://www.digikey.com/en/products/detail/radial-magnets-inc/9042/5640338) | 2 | $0.63 | $1.26 |
| [SparkFun PRT-08808 / 08808 perfboard](https://www.digikey.com/en/products/detail/sparkfun-electronics/08808/7387401) | 1 | $2.96 | $2.96 |

All three lines show Immediate availability. **FedEx Overnight P.M. Delivery is
selected at $26.99**; estimated tariffs are $0.63. Total is **$37.22 before tax**.
The site warns of an additional business day for processing; dispatch by Thursday
October 8 is necessary for Friday. No destination-specific Friday guarantee is
displayed. MIKROE-4204 and the AS5601 fallback are absent.

### Adafruit — $11.90 parts; requested two-day shipping pending

| Part | Buy qty | Unit price | Line total |
|---|---:|---:|---:|
| [6357 — AS5600 Magnetic Angle Sensor, STEMMA QT](https://www.adafruit.com/product/6357) | 2 | $5.95 | $11.90 |

In stock. [DigiKey also lists 6357](https://www.digikey.com/en/products/detail/adafruit-industries-llc/6357/26832926)
at $5.95 with 361 in stock, but does not display Friday arrival, so the boards are
in the requested Adafruit fallback cart.

**UPS 2nd Day Air is requested but not selected.** Adafruit only quotes/selects
shipping during checkout, which was not entered. Its [shipping policy](https://www.adafruit.com/shipping)
states that expedited orders placed by **11 a.m. Eastern** on weekdays usually
ship the same day; general processing is 1–2 business days. That cutoff had already
passed on October 7. Two-day requires Wednesday dispatch for Friday. If dispatch
is Thursday, two-day arrives Monday October 12 and Next Day Air would be needed
for Friday. Shipping cost and actual arrival remain unconfirmed.

Use direct VIN (3.3 V), GND, SCL and SDA wiring to the XIAO. No QT cable is needed.

### Hayward Home Depot pickup — $3.97 parts

| Part | Buy qty | Pack / assembly use | Line total |
|---|---:|---|---:|
| [Everbilt M5×0.8×70 mm socket-head cap screw](https://www.homedepot.com/p/204283625) | 1 | Pack of two; use one | $3.97 |

Model **844868**, Store SKU **540934**. Free **Hayward pickup selected**, Today;
three packs in stock at the October 7 check. Store #1017, **21787 Hesperian Blvd,
Hayward CA 94541**, **aisle 21, bay 018**. Nothing reserved or ordered. This avoids
an extra hardware-store trip in San Francisco.

## Proper-build late shipment — $285.56 parts

Prepare these separately now so available parts can arrive as early as possible.
Dates are **dispatch dates**, not delivery promises. Shipping is unselected; login
is required to quote freight. Request partial shipment and the fastest quoted air
service so undated bearings do not hold the other parts.

| Part | Buy qty | Unit price | Line total | Displayed dispatch |
|---|---:|---:|---:|---|
| [GEAKB1.0-30-6-B-8N-QFC17-M3-LL](https://us.misumi-ec.com/vona2/detail/110300428430/?HissuCode=GEAKB1.0-30-6-B-8N-QFC17-M3-LL) | 2 | $42.51 | $85.02 | October 14 |
| [SSFRHQ8-20-F6-P5-T6-Q5-A12-KC8](https://us.misumi-ec.com/vona2/detail/110300088230/?HissuCode=SSFRHQ8-20-F6-P5-T6-Q5-A12-KC8) | 1 | $26.71 | $26.71 | October 14 |
| [MTA05-13ZZ DBS](https://us.misumi-ec.com/vona2/detail/221000531127/?HissuCode=MTA05-13ZZ%20DBS) | 3 | $23.58 | $70.74 | TBD; no date |
| [WSSAB10-5-1](https://us.misumi-ec.com/vona2/detail/110302677010/?HissuCode=WSSAB10-5-1) | 3 | $23.42 | $70.26 | October 10 |
| [KEG3-8](https://us.misumi-ec.com/vona2/detail/110302681730/?HissuCode=KEG3-8) | 2 | $3.90 | $7.80 | October 10 |
| [JPDPB2-3](https://us.misumi-ec.com/vona2/detail/110300557320/?HissuCode=JPDPB2-3) | 1 | $9.89 | $9.89 | October 15 |
| [AJKTNS5-70](https://us.misumi-ec.com/vona2/detail/110300599320/?HissuCode=AJKTNS5-70) | 1 | $15.14 | $15.14 | October 12 |

The shaft catalog normalizes the `A12-KC8` feature order; this is the same configured
shaft listed as `KC8-A12` in the BOM. Several parts will not arrive early next week:
the gears/shaft dispatch October 14 and the diamond pin October 15. The five custom
machined parts remain outside these carts; the finalREV RFQ is pending, and revised
metal-thread drawings/physical wrist verification are still required before release.

## Cost and remaining delivery checks

| Group | Current amount | Basis |
|---|---:|---|
| Amazon | $160.59 | Parts; Prime deals not applied in guest cart |
| McMaster | $39.50 | Parts; freight unquoted |
| MISUMI stocked | $76.28 | Parts; freight unquoted |
| DigiKey | $37.22 | Parts + selected overnight freight + estimated tariffs |
| Adafruit | $11.90 | Parts; freight unquoted |
| Hayward Home Depot | $3.97 | Parts; free pickup selected |
| **Prototype/shared subtotal** | **$329.46** | Before tax and unquoted freight |
| MISUMI late | $285.56 | Parts; freight unquoted |
| **Both sets of carts** | **$615.02** | Before tax and unquoted freight; excludes custom machining |

Before placing orders:

1. Sign in to Amazon Prime and reconfirm the selected offers deliver by Friday.
2. Obtain MISUMI and McMaster shipping quotes with actual arrival to 94158.
3. Confirm DigiKey dispatch timing despite its processing warning.
4. Resolve Adafruit dispatch and shipping: requested two-day has no Friday promise;
   Thursday dispatch requires overnight for Friday.
5. Recheck Hayward stock before the pickup trip and request partial shipment for
   late MISUMI parts.

Printing supplies, any missing hookup wire/solder/adhesive and custom machining are
outside these totals. Check KADRICK insert fit, the substituted rubber/band and
prototype assembly before running the robot; follow the printed prototype's motor
limits. Shared hardware is reused for the proper build rather than purchased twice.
