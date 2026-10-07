# Parts list — US sourcing

Scope: **two YAM robot grippers + two YUBI data-collection gloves, one left and one right**.
Target: **delivery to San Francisco 94158, or Bay Area pickup, by Friday October 9, 2026**.
Prices initially checked October 6, 2026 (Pacific time); selected cart contents and
prices updated October 7. USD, before tax unless stated. The purchase quantities
cover two robots and both gloves: **four cameras, two XIAOs, two perfboards, two
Adafruit 6357 boards and two Radial 9042 magnets**. Shared packs are bought once.
Nothing in this list has been ordered. Stock and delivery estimates must be checked again at checkout.

See the [proposed October 9 shopping list](SHOPPING_LIST_2026-10-09.md) for the prepared
carts and the [printed prototype](PRINTED_PROTOTYPE.md) for the weekend substitutions.
The prototype uses printed drive parts/adapters, six 695ZZ bearings with six printed
shims, and two stock M5 socket-head screws from one Hayward two-pack. Keep the late
precision parts in a separate proper-build shipment.

**Proper-build sourcing is not complete under the Friday constraint.** The exact
gears and stepped shaft currently ship after Friday. Custom machining, bearings, inserts and several
small precision parts still need confirmation. A catalog link does not mean a part is
available in time. We have not established a lowest delivered price for the whole build.

Compare **whole-order cost**: required packs + shipping + rush/setup charges + tax or
import fees. Consolidate orders, but do not let one backordered item delay stocked items.
“Ships October 8” is not “arrives October 8.” MISUMI express eligibility is part-specific;
the general express-service page is not a delivery commitment.

## Already available / excluded

- Reuse the two stock YAM grippers' **DM4310 motors**; no Dynamixel, U2D2 or separate Dynamixel power supply.
- Computer, recording software and USB connections are already available.
- Reuse the **Quest 3** and both Touch Plus controllers, assuming both original controllers are available.
- Wear the headset for the first iteration: **no headset mount, extrusion rig or chest mount** to buy.
- The **controller holders attached to the gloves** are still required; print one left and one right.
- This two-glove hardware list does not establish that recording with a moving headset is validated. Check the selected recording configuration,
  world-frame controller poses, calibration and synchronization before collecting training data.

Sources: [Toyota robot BOM](https://github.com/Toyota/yubi-hw/blob/main/docs/BOM/YUBI%20Gripper_DYNAMIXEL_BOM.md),
[Toyota glove BOM](https://github.com/Toyota/yubi-hw/blob/main/docs/BOM/YUBI%20Glove%20Assy_BOM.md),
[recording software](https://github.com/airoa-org/yubi-sw).

## Print versus machine

The preferred machining set is **five part types, quantity two each (ten parts)**.
The four finger attachments (one L/R pair per robot) are a separately priced upgrade. No machining order should use the
print-oriented adapter STEP files without resolving their threaded features.

| Part | Process for this build | Source / release requirement |
|---|---|---|
| Toyota `GEAR SHAFT` | Machine, A2024 as Toyota specifies | [Toyota STEP](https://github.com/Toyota/yubi-hw/tree/main/STEP/gripper); preserve journal fits and coaxiality. Printing is only an assembly mock-up, not an accuracy-equivalent substitute. |
| YAM `coupler` | Prefer machined aluminum | [STEP](../cad/out/coupler.step); convert four M2 heat-set-insert pockets to properly designed metal threads. |
| YAM `motor_bracket` | Prefer machined aluminum | [STEP](../cad/out/motor_bracket.step); load-bearing motor support. |
| YAM `bracket_trimmed` | Prefer machined aluminum | [STEP](../cad/out/bracket_trimmed.step); replaces Toyota's machined `BRACKET_GRIPPER`. |
| YAM `yam_flange` | Prefer machined aluminum | [STEP](../cad/out/yam_flange.step); convert two M3 insert pockets to metal threads and measure the real wrist before release. |
| Toyota `FINGER ATTACHMENT_L/R` (4 total) | Optional A2024 machining upgrade | Toyota allows machined A2024 or printed PLA. Price separately; printing does not guarantee equal stiffness/precision. |
| Robot case, upper plate/camera bracket, three pad bodies, two flaps | Print as in Toyota's design | [STL/gripper](https://github.com/Toyota/yubi-hw/tree/main/STL/gripper); inspect bearing seats and assembly fit. |
| Glove upper/under plates, two geared fingers, two flaps, grip, hand-specific controller holders, PCB/cable covers | Print; use the adapted AS5600 upper plate | [Printed prototype](PRINTED_PROTOTYPE.md) for `glove_upper_plate_as5600`; other parts from [STL/glove](https://github.com/Toyota/yubi-hw/tree/main/STL/glove). Right hand uses `FINGER with Gear_t30_R` / `FINGER with Gear_t20_L`; left hand uses `FINGER with Gear_t30_L` / `FINGER with Gear_t20_R` and `_L` controller holder/covers. Both use the same AS5600 plate and purchased hardware. No bought metal gears for the gloves. |

The YAM adaptation is designed/simulated, **not physically validated**. Its wrist pattern
(six M3 holes on a 27 mm pitch circle and a 35 mm boss) is an assumption pending measurement.
The coupler/flange insert pockets are not suitable tap-drill holes as exported. Request
critical fits, tolerances and material approval before manufacture; 6061-T6 is a quote
candidate for new adapters, not an automatic substitute for Toyota's A2024 parts.

### Local machining candidates

| Shop | Relevant published capability | Price + Friday status |
|---|---|---|
| [finalREV, Berkeley](https://www.finalrev.com/services/millturn) | Advertises same-day Bay Area parts, single-part minimum and local pickup. [5-axis service](https://www.finalrev.com/services/5-axis-cnc) for larger/prismatic work. | **RFQ sent October 6; response pending.** Millturn stock limit is 1-inch round; the gear shaft fits that diameter, the 32 mm gear does not. Confirm A2024 availability. |
| [RivCut, Union City](https://www.rivcut.com/) | Milling/turning, 2024/6061/7075 aluminum; prototypes advertised as fast as three business days; pickup by appointment. | **Quote required.** No job-specific price, capacity reservation or Friday promise obtained. |
| [twentyfour26, San Francisco](https://twentyfour26.com/) | Rapid prismatic machining in 6061-T6. | Conditional bracket backup: minimum internal radius and standard tolerances need checking against these parts. **Quote required.** |

Request a revised combined quote for two of each preferred part type (ten parts),
with the four optional finger attachments separately, and modification/machining of the late bought parts below.
Require itemized setup, design revision, inspection, rush and pickup/delivery charges.
As-machined/deburred finish avoids unnecessary cosmetic finishing cost. Quotes are not
manufacturing authorization. **finalREV RFQ sent October 6, 2026** with the five-part
base set, two optional finger attachments, source CAD and catalog-part modification
requests. Requested itemized pricing, total pickup/delivery costs and committed Friday
October 9 availability. **Awaiting response; price and Friday capacity are unconfirmed.**
The October 6 RFQ covered one set; the doubled quantities have not been sent to the
shop. A revised two-set quote is required. Other supplier RFQs have not been sent.
No machining order has been placed.

## Robot motion and alignment parts

All quantities below are totals for **two robots**, excluding the gloves.

| Qty | Required part / important geometry | Source and observed parts price | Friday status / next route |
|---|---|---|---|
| 4 | `GEAKB1.0-30-6-B-8N-QFC17-M3-LL`; module 1, 30 teeth, 6 mm face, keyed Ø8 bore, QFC17 M3 face-hole feature | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300428430/?HissuCode=GEAKB1.0-30-6-B-8N-QFC17-M3-LL), $42.51 each / **$170.04** | **Late:** October 7 cart showed ship October 14. Ask for part-specific express or local modification of a compatible stock gear. Generic 30T/8 mm gears are not drop-in replacements. |
| 2 | `SSFRHQ8-20-F6-P5-T6-Q5-KC8-A12`, configured Ø8 stepped/keyed left finger shaft | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300088230/?HissuCode=SSFRHQ8-20-F6-P5-T6-Q5-A12-KC8), **$26.71 each / $53.42** | **Late:** displayed ship October 14. Local turning/keyway quote must use the full configured drawing, not only overall diameter/length. |
| 6 | `MTA05-13ZZ DBS`, NSK Micro/ISC angular-contact bearing, nominal 5 × 13 × 5 mm | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/221000531127/?HissuCode=MTA05-13ZZ%20DBS), $23.58 each / **$141.48**; [Volition](https://www.govolition.com/product/V52-MTA05-13ZZ%20DBS) lists the same MISUMI supply | **Unconfirmed:** October 7 cart has no ship date. Volition's estimated three days to ship is not Friday delivery or independent stock. Preserve these bearings for the proper build; 695ZZ plus a printed shim is only the documented prototype stand-in. |
| 6 | `WSSAB10-5-1`, nominal Ø10 OD / Ø5 ID / 1 mm thickness | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110302677010/?HissuCode=WSSAB10-5-1), $23.42 each / **$140.52** | **Late:** ship October 10. Seek a stocked precision spacer or add to local machining quote. Generic M5 washers are not automatically equivalent. |
| 4 | `KEG3-8`, 3 × 3 × 8 mm, one round end and one square end | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110302681730/?HissuCode=KEG3-8), $3.90 each / **$15.60**; [Huyett 330303-008](https://www.huyett.com/330303-008) has matching nominal Form AB geometry | **Late** at MISUMI: ship October 10. Huyett is special-order with a $50 minimum, not a verified fast/cheap alternative. Ask shop to supply/finish keys. |
| 2 | Round locating pin `JPBPB2-3` | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300557320/?HissuCode=JPBPB2-3), **$7.05 each / $14.10** | **Stock/ship candidate:** October 7–8 dispatch; shipping cost and arrival unquoted. |
| 2 | Diamond locating pin `JPDPB2-3` | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300557320/?HissuCode=JPDPB2-3), **$9.89 each / $19.78** | **Late:** ship October 15. Ask about a stocked same-fit material variant or local modification of a round pin to the drawing. |

**Precision corrections:** the locating pins are not ordinary Ø2 × 3 mm dowels:
they have a Ø2 press-fit shank, Ø3 positioning head, 4 mm mounting length and 3 mm
positioning length. Preserve the round/diamond pairing. The original washer has ID
5.1–5.3 mm, OD 9.8–10 mm and thickness 1 ±0.05 mm. Verify any replacement's tolerance.

**Cheaper spacer candidate:** [KB3D SS-5101-50 DIN 988 shim rings](https://kb-3d.com/store/inserts-fasteners-adhesives/288-5x10x1mm-shim-ring-washer-pack-of-50-din988-1634423113147.html)
are **$3.79 per pack of 50**, with **two packs in stock** in the retailer listing.
Nominal dimensions are 5 × 10 × 1 mm; stainless steel replaces the original aluminum.
Confirm actual ID/OD/thickness tolerances, shaft/fillet clearance and flat seating
before using them as WSSAB replacements. They are a credible low-cost precision-shim
candidate, not an ordinary M5 washer. Shipping from Ohio must be expedited and quoted;
the retailer publishes a 2 pm Eastern same-day cutoff, not a Friday-arrival guarantee.

[NSK's catalog](https://www.nskmicro.co.jp/english/download/catalog_pdf/bearing/croxy_en.pdf)
explains the angular-contact/preload design. Radwell lists `MTA05-13ZZ DB`, a different
paired configuration, not the specified `DBS`; buying/separating those is **not an
approved substitute** without NSK confirmation. No precision-preserving printed
bearing, key or shaft substitute is selected.

**Concrete gear-blank route for a shop to quote:**
[KHK SSA1-30](https://catalog.khkgears.us/item/spur-gears/hubless-spur-gears-ssa/ssa1-30)
is **$13.45 each / $53.80 for four**, with **five on hand** at the original KHK USA check.
It is unhardened S45C steel, module 1, 30 teeth, 20° pressure angle, Ø8 plain bore,
Ø32 outside diameter, **10 mm face width** and JIS N8 quality. It needs a shop's
geometry review, width reduction to 6 mm, keyway and the configured face features;
tooth accuracy/backlash must also meet the application. It is **a machining blank,
not a drop-in replacement**. Overnight freight and machining/pickup remain unquoted.
Grainger lists this blank for $19.99 but showed October 22 delivery, so its offer
does not meet the deadline. Do not order blanks until a shop accepts the conversion.

## Cameras, glove electronics and shared consumables

| Qty to buy | Part | Source / observed price | Delivery / compatibility |
|---|---|---|---|
| 4 | ELP `USBFHD01M-L180` camera: one per robot/glove | [Amazon US](https://www.amazon.com/dp/B00LQ854AG), **$44.99 each new / $179.96 total** | October 7 check with quantity 4 showed Friday October 9 to 94158 with Prime. The cheaper used-like-new offer now misses Friday. Guest shipping misses Friday; sign-in and selected-offer confirmation required. |
| 2 | Seeed XIAO ESP32C6 `113991254` | [DigiKey](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/113991254/24613066), **$5.38 each / $10.76** | Immediate availability in the prepared cart; combine with perfboard/magnets. Delivery conditional on dispatch and chosen shipping. |
| 2 | Adafruit `6357` AS5600 breakout | [DigiKey 1528-6357-ND](https://www.digikey.com/en/products/detail/adafruit-industries-llc/6357/26832926), **$5.95 each / $11.90 total** | Immediate availability in the overnight DigiKey cart, one board per glove. Use `glove_upper_plate_as5600` and four extra M2×6 screws per glove. Separate Adafruit cart emptied. Actual Friday arrival remains unconfirmed. |
| 2 | Diametric encoder magnet, Radial Magnets `9042`, Ø6 × 2.5 mm, N35 | [DigiKey](https://www.digikey.com/en/products/detail/radial-magnets-inc/9042/5640338), **$0.63 each / $1.26 total** | Immediate availability in the prepared cart. Board ships without a magnet. Use the documented 2 mm sensor gap. Must be **diametrically**, not axially, magnetized. |
| 2 | SparkFun `PRT-08808` perfboard, 25.4 × 25.4 mm | [DigiKey](https://www.digikey.com/en/products/detail/sparkfun-electronics/08808/7387401), **$2.96 each / $5.92** | Exact original perfboard; Immediate availability in the prepared cart. |
| As needed | Pin headers / short hookup wires / solder | Check XIAO package and existing supplies; Toyota lists four header pieces per glove (eight total) | Header installation is required. Avoid ordering a new soldering kit unless missing. |
| 1 shared sheet | Grip rubber; original 1.5 mm `PX-10H15 HYPER V` | [RAPOLL solid neoprene, 12 × 12 in × 1/16 in](https://www.amazon.com/dp/B0BKQRN7S6), **$6.89 + free Prime shipping**, Thursday October 8 shown | Lowest-priced sheet checked; **material/thickness substitution** (nominal 1.5875 mm). Check grip, compliance, attachment and recalibrate jaw opening. Not equal-performance certification. |
| 1 alternative pack | Nominal 1.5 mm silicone sheet | [PATIKIL, five Ø100 mm discs](https://www.amazon.com/dp/B0G2JR4VFQ), **$9.21 + free Prime shipping**, Thursday shown in search | Alternative to neoprene, not an additional purchase. Check cutting layout and suitable silicone adhesive; grip performance is unvalidated. [Original Hyper V](https://nisshinrubber-metalcraft.com/products/hyperv%E3%82%B7%E3%83%BC%E3%83%88-px-10h-15-%E8%80%90%E6%B2%B9w270-l270-h1-5mm) remains the reference. |
| 2 bands from one pack | Return band, original Japanese No.16 | [MOWPOG #16 pack](https://www.amazon.com/dp/B0FCM95WH7), **$5.99 + free Prime shipping**, Thursday October 8 shown | Listing specifies 2.37 in folded length and 0.06 in width/thickness. Check return force and full travel; the size number alone is not equivalence. Reusing a suitable existing band avoids buying hundreds for two gloves. |
| 0 | USB data cables/connections | Already available | Verify connector ends on the actual camera and XIAO; do not blindly order two USB-C cables. |

[DigiKey US shipping rates](https://www.digikey.com/en/help-support/delivery-information/delivery-time-and-cost):
two-day air **$13.99/order**, overnight PM **$26.99/order**. The prepared cart contains
two each of XIAO, perfboard, Adafruit 6357 and Radial 9042, **$29.84 parts**, with
**FedEx Overnight P.M. selected**. Estimated tariff is **$0.94**, for **$57.77 before tax**.
Friday arrival to 94158 is not displayed. DigiKey warns that processing may take an
extra business day: overnight requires dispatch by Thursday October 8. `MIKROE-4204`
does not fit the glove and is removed; the `AS5601-SO_EK_AB` fallback is dropped too.
The separate Adafruit cart was emptied; both 6357 boards ship with the DigiKey order.
Solder VIN (3.3 V), GND, SCL and SDA directly to each XIAO; no QT cable is needed.

## Screws — consolidated quantities for both builds

Counts include **two robots and two gloves (one left, one right)**. Standard socket heads and low/ultra-low
heads are separate requirements. Lengths are under-head lengths. Ordinary screws use
M2 × 0.4, M2.5 × 0.45 and M3 × 0.5 threads.

| Two robots | Two gloves | Assembly total | Screw | Source / current status |
|---:|---:|---:|---|---|
| 8 | 16 | 24 | M2 × 6, standard socket head | [mxuteuk M2-only 520-piece kit](https://www.amazon.com/dp/B0C6M6MJ8M), **$8.99**, explicitly lists **30 M2×6**; Friday with Prime shown. Glove count includes four extra AS5600 mount screws per glove. Original mixed kit removed: it contains M2×12/16, no M2×6. |
| 4 | 4 | 8 | M2.5 × 6, standard socket head | Included in the VGBUY M2.5 kit below; [McMaster 91290A101](https://www.mcmaster.com/91290A101/) fallback, $11.81/50. |
| 0 | 4 | 4 | M2.5 × 8, standard socket head | Included in the VGBUY M2.5 kit below; [McMaster 91290A006](https://www.mcmaster.com/91290A006/) fallback, $11.71/100. |
| 8 | 0 | 8 | M2.5 × 10, standard socket head | [VGBUY M2.5 1001-piece kit](https://www.amazon.com/dp/B0FJ1YMG3J), **$9.99 guest cart**, advertised Prime deal $7.99; October 8 with Prime shown. Also covers M2.5 × 6/8. [McMaster 91290A007](https://www.mcmaster.com/91290A007/) fallback is $11.03/100. |
| 6 | 6 | 12 | M2.5 × 15, standard socket head | [McMaster 91290A009](https://www.mcmaster.com/91290A009/), **two $4.25 ten-packs / $8.50**, 20 available for 12 needed, Thursday delivery shown; final shipping unquoted. |
| 0 | 2 | 2 | M3 × 6, standard socket head | Included in the ALLWIN M3 kit below. |
| 8 | 0 | 8 | M3 × 8, standard socket head | Included in the ALLWIN M3 kit below. |
| 12 | 0 | 12 | M3 × 10, standard socket head | [ALLWIN M3 400-piece kit](https://www.amazon.com/dp/B0F5QKDW7Y), **$5.79 guest cart**, advertised Prime deal $4.63; October 9 with Prime shown. Includes 30 screws of this length plus M3 × 6/8/12/16/20. |
| 4 | 0 | 4 | M3 × 12, standard socket head | Included in the ALLWIN M3 kit above. |
| 12 | 0 | 12 | M2 × 5, ultra-low head: Ø4 × 0.5 mm head | [MISUMI CBSTBR2-5](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTBR2-5), **$5.24 each / $62.88**; same steel/geometry, black nickel instead of white. October 7–8 dispatch shown. Original CBSTNR2-5 ships October 10. |
| 8 | 0 | 8 | M3 × 8, ultra-low head: Ø6 × 0.8 mm head | [MISUMI CBSTNR3-8](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTNR3-8), **$5.05 each / $40.40**, October 7–8 dispatch shown. |
| 12 | 0 | 12 | M3 × 6, low head for rotor → coupler | [McMaster 92855A307](https://www.mcmaster.com/92855A307/), **$7.30/25**, Ø5.5 × 2 mm head, Thursday 7–9 am shown. |
| 8 | 0 | 8 | M3 × 8, low head for stator → motor bracket | [McMaster 92855A309](https://www.mcmaster.com/92855A309/), **$7.55/25**, 18-8 stainless, DIN 7984, Ø5.5 × 2 mm head, Thursday shown. [Alloy-steel 93070A064](https://www.mcmaster.com/93070A064/) is $13.62/50 if higher strength is required. |
| 4 | 0 | 4 | M2 × 8, low head for motor bracket → case back | [McMaster 92855A839](https://www.mcmaster.com/92855A839/), **$20.40/10**, Ø3.8 × 1.35 mm head, Thursday 7–9 am shown. |

McMaster dates above are displayed site estimates; the final destination/shipping
charge was not entered or quoted. MISUMI stocked rows also require a delivered quote.
The original [888-piece mixed kit](https://www.amazon.com/dp/B0G8F366MV) has only
M2×12/16 in its size diagram and cannot cover M2×6. The replacement M2-only kit's
packaging text explicitly lists 30 M2×6, leaving **6 spare** after the required 24.
Its size diagram has mislabeled entries, so the count is taken from the packaging
text. The two CBSTNR3-5 mount screws per glove are no longer required by the AS5600
plate. Do not buy every fallback pack as well as the selected kits.

The prepared standard-screw combination is the **$8.99 M2 kit + $9.99 M2.5 kit +
$5.79 M3 kit + two $4.25 McMaster M2.5 × 15 packs = $33.27** before freight/tax.
Advertised Prime deals of $7.99 for M2.5 and $4.63 for M3 would reduce it to **$30.11**
if applied after sign-in. All three Amazon kits show delivery by Friday with Prime,
**plus the McMaster order's shipping and tax**.
This covers every standard screw length above; special low/ultra-low heads are extra.
Amazon search dates must be rechecked for the selected offer at checkout. Prime sale
prices and the displayed nightly delivery cutoffs may expire.

DIN 7984 and ordinary “low head” screws do **not** replace Toyota's ultra-low heads.
The new adapter counterbores and screw engagement still need checking on the machining
revision. Follow the manufacturer's reduced tightening torque for ultra-low heads.
The listed 18-8 low-head screws have 70,000 psi tensile strength; confirm required
joint preload/strength before substituting them for higher-strength alloy steel.


## Printed-prototype stand-ins

These are temporary purchases for the [printed prototype](PRINTED_PROTOTYPE.md),
not precision-equivalent replacements for the proper-build parts.

| Buy qty | Stand-in | Source / price | Fulfillment / use |
|---|---|---|---|
| 1 pack of 10; use 6 | 695ZZ deep-groove bearings, 5 × 13 × 4 mm | [KABOBEARING](https://www.amazon.com/dp/B0CRP3K8ZF), **$6.99** guest cart; advertised Prime deal $5.59 | October 8 with Prime shown. Cheapest matching Friday-capable pack found in the ascending-price search. Print six `bearing_shim_1mm` parts under the outer races. |
| 1 pack of 2; use both | M5 × 0.8 × 70 mm socket-head cap screw | [Home Depot Everbilt 844868, SKU 540934](https://www.homedepot.com/p/204283625), **$3.97** | **Hayward pickup selected**, free, Today; three packs in stock October 7. Store #1017, 21787 Hesperian Blvd, Hayward CA 94541; aisle 21, bay 018. Janos is going today; this one pack covers both gloves. Nothing reserved or ordered. |

## Inserts for printed parts

| Two robots | Two gloves | Base total | Original specification | Sourcing status |
|---:|---:|---:|---|---|
| 8 | 0 | 8 | `SB-203030`: M2, nominal body Ø3 / knurl Ø3.3, length 3 mm | Exact US stock unresolved; generic M2 insert must match the actual printed hole and installation recommendation. |
| 10 | 10 | 20 | Toyota calls out `SB-264040`, nominal body Ø4 / knurl Ø4.3, length 4 mm | **Thread discrepancy to resolve:** assembly uses M2.5 screws; current Tokai catalog calls M2.5 `SB-254040`, while `SB-264040` is M2.6. Do not order M2.6 blindly. |
| 8 | 0 | 8 | `SB-304550`: M3, nominal body Ø4.5 / knurl Ø4.8, length 5 mm | Exact US stock unresolved. Not “M3 Ø4 × 5”; check fit before choosing another brand. |
| 0 | 4 | 4 | `SB-304540`: M3, nominal body Ø4.5 / knurl Ø4.8, length 4 mm | Exact US stock unresolved. |

[Tokai dimensions](https://tokai-mmc.co.jp/insert/seihin_sb.html) and
[catalog](https://www.tokai-mmc.co.jp/insert/catalog/SB.pdf).
A different insert is acceptable only after adapting/checking the printed hole, pullout
resistance and surrounding wall; “any heat-set kit works” was incorrect.

**Fast US candidates, requiring printed-hole adaptation/fit validation:**

- [KADRICK 520-piece kit](https://www.amazon.com/dp/B0D5V3TZLB), **$15.98**, includes
  M2 × 3 mm long (listed OD 3 mm), M3 × 4 mm and M3 × 5 mm (listed OD 4.5 mm).
- [KADRICK M2/M2.5 300-piece kit](https://www.amazon.com/dp/B0FD7DQS8Y), **$9.99**,
  includes M2.5 × 4 mm long, listed OD 3.5 mm, thread pitch 0.45 mm.
- Both product pages showed **free Prime delivery Thursday October 8** to 94158.
  Together **$25.97 delivered before tax** at the checked offers. These are not the
  original Tokai insert shapes/diameters. Preserve hole centers, select pilot holes
  for these inserts, and check wall thickness, installation, screw engagement and
  pullout/torque resistance before using them in load-bearing printed parts. Do not
  install a loose insert into the original larger hole and call it equivalent.

This closes the supply search for candidate inserts, **not their fit/strength
qualification**. Exact Tokai US stock remains unresolved. A cheaper $9.99 Dianrui
assortment was rejected as a complete kit because it lacks the needed M2 × 3 and
M3 × 5 lengths; the $9.99 KADRICK M3-only kit showed October 12 delivery.

For **machined couplers/flanges**, metal threads replace the adapter inserts.
For two printed sets, add **eight M2×3 and four M3×5 inserts** to the base counts.
The selected single kits cover **16 M2×3 / 60 available**, **20 M2.5×4 / 60**,
**12 M3×5 / 50**, and **4 M3×4 / 50**. These counts include the printed adapters;
keep the existing printed-hole fit/strength checks.

## Glove-only adjustment hardware

| Qty for two gloves | Part | Source / parts price | Friday status |
|---|---|---|---|
| 8 | `JZF8-5` POM flanged bushings, nominal ID8 / OD10 / overall length5 mm | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110302640340/?HissuCode=JZF8-5), **$2.70 each / $21.60** | October 7–8 dispatch shown; delivery/shipping quote pending. |
| 2 | M3 × 6 long knurled screw, original `LRLM3-6` | [MISUMI LRLB3-6](https://us.misumi-ec.com/vona2/detail/110300245210/?HissuCode=LRLB3-6), **$6.06 each / $12.12** | Same geometry in 303 stainless, Ø5.5 head × 10 mm high; October 7–8 dispatch. Original plated-steel LRLM3-6 is $5.78 but ships October 12. |
| 2 | `AJKTNS5-70`, M5 × 0.8, 70 mm adjustment screw | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300599320/?HissuCode=AJKTNS5-70), **$15.14 each / $30.28**; [black-oxide steel AJKTN5-70](https://us.misumi-ec.com/vona2/detail/110300599320/?HissuCode=AJKTN5-70), **$7.23** | **Both late:** ship October 12. Add to local-shop request. A stock bolt + knob needs tip/head/clearance review, not just a matching M5 thread. |
| 2 | `HNTT5-5` M5 pre-insertion T-slot nut | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110302246150/?HissuCode=HNTT5-5), **$0.73 each / $1.46** | October 7–8 dispatch shown; delivered price/date pending. Exact pocket geometry, not a generic “2020” nut. |

## Order groups and shipping comparison

The [proposed shopping list](SHOPPING_LIST_2026-10-09.md) records the six prepared
carts, purchase quantities and shared-pack count audit. These remain **partial
order groups**, not a complete build budget: tax, unquoted freight and custom
machining are excluded. Nothing has been ordered. Material/fit substitutions still
need the checks above.

| Order group | Checked contents | Parts / shipping / status |
|---|---|---|
| Amazon | Four new cameras; one each M2/M2.5/M3 screw kit, neoprene sheet, #16 band pack, both KADRICK kits and ten-pack of 695ZZ bearings | **$250.57 parts**. Quantity four cameras still shows Friday with Prime; guest shipping misses. Advertised Prime deals would reduce parts to about $246.01 if applied after sign-in. |
| McMaster | Two M2.5×15 ten-packs; one each of the three low-head packs | **$43.75 + shipping + tax** in the unsubmitted cart. Site estimates Thursday; destination-specific freight/arrival remain unquoted. Shared low-head packs cover 12/25 M3×6, 8/25 M3×8 and 4/10 M2×8. |
| MISUMI stocked | CBSTBR2-5 ×12, CBSTNR3-8 ×8, JZF8-5 ×8, LRLB3-6 ×2, HNTT5-5 ×2, JPBPB2-3 ×2 | **$152.56 + shipping + tax**. October 7 dispatch displayed; shipping unselected/login required. Quote actual Friday arrival. CBSTNR3-5 removed. Keep late items separate. |
| DigiKey | Two each XIAO, perfboard, Adafruit 6357 and Radial 9042 magnet | **$29.84 parts + $26.99 selected overnight PM + $0.94 estimated tariffs = $57.77 before tax**. All Immediate; processing warning/actual Friday arrival still need confirmation. Separate Adafruit cart emptied. |
| Home Depot, Hayward | One two-pack of Everbilt M5×0.8×70 socket-head screws | **$3.97 + tax**. Free Hayward pickup selected, Today; Janos is going today. Use both screws. Aisle 21, bay 018. Nothing reserved. |
| MISUMI late / proper build | Four gears, two stepped shafts, six MTA05-13ZZ DBS, six spacers, four keys, two diamond pins, two AJKTNS5-70 | **$571.12 + shipping + tax** in the separate cart. Freight unselected/login required. Gears/shafts dispatch October 14, pins October 15, bearings undated. Request partial shipment. |

The five prototype/shared groups total **$508.62**, including selected DigiKey freight
and estimated tariffs, before sales tax and unquoted McMaster/MISUMI freight. The
late cart adds **$571.12**, making **$1,079.74** on the same incomplete basis.
Custom machining (ten preferred parts), adhesive and any missing wiring/printing
supplies are excluded. The KHK gear-blank conversion remains a separately quoted
alternative, not an additional purchase in these carts. Selecting the alloy-steel
M3×8 low-head pack instead of stainless adds $6.07; one pack still covers both robots.

[MISUMI shipping guidance](https://us.misumi-ec.com/guide/faq/shipping.html) and
[McMaster delivery information](https://www.mcmaster.com/info/delivery).
Do not assume free MISUMI/McMaster shipping or substitute a catalog dispatch date for
arrival. Review the selected Prime offers and consolidated checkout totals before paying.

## Delivery checks before ordering

For the printed prototype, confirm Amazon Prime offers, quoted MISUMI/McMaster
arrival to 94158 and DigiKey dispatch despite the processing warning. All glove
electronics are consolidated on DigiKey overnight. Recheck Hayward pickup stock.
The full checklist is in the [proposed shopping list](SHOPPING_LIST_2026-10-09.md).

## What still prevents a complete proper build by Friday

1. Confirm a shop's **price and Friday pickup commitment** for the five machining
   part types (two each); release revised coupler/flange drawings and verify both physical wrists.
2. Obtain a Friday route for **four finished gears and two stepped shafts**; exact catalog
   dates miss. KHK has a priced, on-hand gear blank for a shop to assess and modify.
3. Confirm **six correct angular-contact bearings**, precision washers/keys and both diamond pins.
4. Qualify candidate **insert fit/strength and rubber/band performance**, and secure the
   adjustment screws. Standard screw lengths and the T-nuts now have priced sources.
5. Validate the selected AS5600 board/plate in both physical gloves and confirm its shipping.
6. Compare combined supplier carts, including shipping/tariffs/tax. Reconfirm all arrivals
   before ordering. Do not count partial catalog subtotals as a complete delivered budget.
