# Parts list — US sourcing

Scope: **one YAM robot gripper + one right-hand YUBI data-collection glove**.
Target: **delivery to San Francisco 94158, or Bay Area pickup, by Friday October 9, 2026**.
Prices checked October 6, 2026 (Pacific time); USD, before tax unless stated.
Nothing in this list has been ordered. Stock and delivery estimates must be checked again at checkout.

**Sourcing is not complete under the Friday constraint.** The exact gears and stepped
shaft currently ship after Friday. Custom machining, bearings, inserts and several
small precision parts still need confirmation. A catalog link does not mean a part is
available in time. We have not established a lowest delivered price for the whole build.

Compare **whole-order cost**: required packs + shipping + rush/setup charges + tax or
import fees. Consolidate orders, but do not let one backordered item delay stocked items.
“Ships October 8” is not “arrives October 8.” MISUMI express eligibility is part-specific;
the general express-service page is not a delivery commitment.

## Already available / excluded

- Reuse the stock YAM gripper's **DM4310**; no Dynamixel, U2D2 or separate Dynamixel power supply.
- Computer, recording software and USB connections are already available.
- Reuse the **Quest 3** and its right Touch Plus controller, assuming the original controller is available.
- Wear the headset for the first iteration: **no headset mount, extrusion rig or chest mount** to buy.
- The **controller holder attached to the glove** is still required; it is a printed part.
- This is a one-glove hardware list, not a claim that Toyota's default two-hand recording configuration
  already works with one glove and a moving headset. Check the selected recording configuration,
  world-frame controller poses, calibration and synchronization before collecting training data.

Sources: [Toyota robot BOM](https://github.com/Toyota/yubi-hw/blob/main/docs/BOM/YUBI%20Gripper_DYNAMIXEL_BOM.md),
[Toyota glove BOM](https://github.com/Toyota/yubi-hw/blob/main/docs/BOM/YUBI%20Glove%20Assy_BOM.md),
[recording software](https://github.com/airoa-org/yubi-sw).

## Print versus machine

The preferred machining set is **five parts**, quantity one each. The two finger
attachments are a separately priced upgrade. No machining order should use the
print-oriented adapter STEP files without resolving their threaded features.

| Part | Process for this build | Source / release requirement |
|---|---|---|
| Toyota `GEAR SHAFT` | Machine, A2024 as Toyota specifies | [Toyota STEP](https://github.com/Toyota/yubi-hw/tree/main/STEP/gripper); preserve journal fits and coaxiality. Printing is only an assembly mock-up, not an accuracy-equivalent substitute. |
| YAM `coupler` | Prefer machined aluminum | [STEP](../cad/out/coupler.step); convert four M2 heat-set-insert pockets to properly designed metal threads. |
| YAM `motor_bracket` | Prefer machined aluminum | [STEP](../cad/out/motor_bracket.step); load-bearing motor support. |
| YAM `bracket_trimmed` | Prefer machined aluminum | [STEP](../cad/out/bracket_trimmed.step); replaces Toyota's machined `BRACKET_GRIPPER`. |
| YAM `yam_flange` | Prefer machined aluminum | [STEP](../cad/out/yam_flange.step); convert two M3 insert pockets to metal threads and measure the real wrist before release. |
| Toyota `FINGER ATTACHMENT_L/R` (2) | Optional A2024 machining upgrade | Toyota allows machined A2024 or printed PLA. Price separately; printing does not guarantee equal stiffness/precision. |
| Robot case, upper plate/camera bracket, three pad bodies, two flaps | Print as in Toyota's design | [STL/gripper](https://github.com/Toyota/yubi-hw/tree/main/STL/gripper); inspect bearing seats and assembly fit. |
| Glove upper/under plates, two geared fingers, two flaps, grip, right controller holder, PCB/cable covers | Print as in Toyota's design | [STL/glove](https://github.com/Toyota/yubi-hw/tree/main/STL/glove). Right hand uses `FINGER with Gear_t30_R` and `FINGER with Gear_t20_L`. No bought metal gears for the glove. |

The YAM adaptation is designed/simulated, **not physically validated**. Its wrist pattern
(six M3 holes on a 27 mm pitch circle and a 35 mm boss) is an assumption pending measurement.
The coupler/flange insert pockets are not suitable tap-drill holes as exported. Request
critical fits, tolerances and material approval before manufacture; 6061-T6 is a quote
candidate for new adapters, not an automatic substitute for Toyota's A2024 parts.

### Local machining candidates

| Shop | Relevant published capability | Price + Friday status |
|---|---|---|
| [finalREV, Berkeley](https://www.finalrev.com/services/millturn) | Advertises same-day Bay Area parts, single-part minimum and local pickup. [5-axis service](https://www.finalrev.com/services/5-axis-cnc) for larger/prismatic work. | **Quote required.** Millturn stock limit is 1-inch round; the gear shaft fits that diameter, the 32 mm gear does not. Confirm A2024 availability. |
| [RivCut, Union City](https://www.rivcut.com/) | Milling/turning, 2024/6061/7075 aluminum; prototypes advertised as fast as three business days; pickup by appointment. | **Quote required.** No job-specific price, capacity reservation or Friday promise obtained. |
| [twentyfour26, San Francisco](https://twentyfour26.com/) | Rapid prismatic machining in 6061-T6. | Conditional bracket backup: minimum internal radius and standard tolerances need checking against these parts. **Quote required.** |

Request one combined quote for the five preferred parts, the two optional finger
attachments separately, and modification/machining of the late bought parts below.
Require itemized setup, design revision, inspection, rush and pickup/delivery charges.
As-machined/deburred finish avoids unnecessary cosmetic finishing cost. Quotes are not
manufacturing authorization. No supplier quote request or machining order has been submitted.

## Robot motion and alignment parts

All quantities below are for the robot only.

| Qty | Required part / important geometry | Source and observed parts price | Friday status / next route |
|---|---|---|---|
| 2 | `GEAKB1.0-30-6-B-8N-QFC17-M3-LL`; module 1, 30 teeth, 6 mm face, keyed Ø8 bore, QFC17 M3 face-hole feature | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300428430/?HissuCode=GEAKB1.0-30-6-B-8N-QFC17-M3-LL), $42.51 each / **$85.02** | **Late:** displayed ship October 13. Ask for part-specific express or local modification of a compatible stock gear. Generic 30T/8 mm gears are not drop-in replacements. |
| 1 | `SSFRHQ8-20-F6-P5-T6-Q5-KC8-A12`, configured Ø8 stepped/keyed left finger shaft | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300088230/?HissuCode=SSFRHQ8-20-F6-P5-T6-Q5-A12-KC8), **$26.71** | **Late:** displayed ship October 14. Local turning/keyway quote must use the full configured drawing, not only overall diameter/length. |
| 3 | `MTA05-13ZZ DBS`, NSK Micro/ISC angular-contact bearing, nominal 5 × 13 × 5 mm | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/221000531127/?HissuCode=MTA05-13ZZ%20DBS), $23.58 each / **$70.74**; [Volition](https://www.govolition.com/product/V52-MTA05-13ZZ%20DBS) lists the same MISUMI supply | **Unconfirmed.** Volition's estimated three days to ship is not Friday delivery or independent stock. Do not replace with 695ZZ plus a shim. |
| 3 | `WSSAB10-5-1`, nominal Ø10 OD / Ø5 ID / 1 mm thickness | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110302677010/?HissuCode=WSSAB10-5-1), $23.42 each / **$70.26** | **Late:** ship October 10. Seek a stocked precision spacer or add to local machining quote. Generic M5 washers are not automatically equivalent. |
| 2 | `KEG3-8`, 3 × 3 × 8 mm, one round end and one square end | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110302681730/?HissuCode=KEG3-8), $3.90 each / **$7.80**; [Huyett 330303-008](https://www.huyett.com/330303-008) has matching nominal Form AB geometry | **Late** at MISUMI: ship October 10. Huyett is special-order with a $50 minimum, not a verified fast/cheap alternative. Ask shop to supply/finish keys. |
| 1 | Round locating pin `JPBPB2-3` | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300557320/?HissuCode=JPBPB2-3), **$7.05** | **Stock/ship candidate:** October 7–8 dispatch; shipping cost and arrival unquoted. |
| 1 | Diamond locating pin `JPDPB2-3` | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300557320/?HissuCode=JPDPB2-3), **$9.89** | **Late:** ship October 15. Ask about a stocked same-fit material variant or local modification of a round pin to the drawing. |

**Precision corrections:** the locating pins are not ordinary Ø2 × 3 mm dowels:
they have a Ø2 press-fit shank, Ø3 positioning head, 4 mm mounting length and 3 mm
positioning length. Preserve the round/diamond pairing. The original washer has ID
5.1–5.3 mm, OD 9.8–10 mm and thickness 1 ±0.05 mm. Verify any replacement's tolerance.

[NSK's catalog](https://www.nskmicro.co.jp/english/download/catalog_pdf/bearing/croxy_en.pdf)
explains the angular-contact/preload design. Radwell lists `MTA05-13ZZ DB`, a different
paired configuration, not the specified `DBS`; buying/separating those is **not an
approved substitute** without NSK confirmation. No precision-preserving printed
bearing, key or shaft substitute is selected.

**Concrete gear-blank route for a shop to quote:**
[KHK SSA1-30](https://catalog.khkgears.us/item/spur-gears/hubless-spur-gears-ssa/ssa1-30)
is **$13.45 each / $26.90 for two**, with **five on hand** displayed by KHK USA.
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
| 2 | ELP `USBFHD01M-L180` camera: one robot, one glove | [Amazon US](https://www.amazon.com/dp/B00LQ854AG), **$31.29 each used-like-new**, Amazon Resale; **$62.58 total + $0 Prime shipping** | Page showed Friday October 9 to 94158, with quantity 2 selected and only two in stock. Lowest verified camera offer; condition is used-like-new. New was $44.99 each; recheck its selected-offer delivery. |
| 1 | Seeed XIAO ESP32C6 `113991254` | [DigiKey](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/113991254/24613066), **$5.38**, 179 in stock | Combine with encoder/perfboard; delivery conditional on dispatch and chosen shipping. |
| 1 | Original AS5601 breakout, 20 × 13.5 mm, mounting holes 15 mm apart | [Switch Science #3494](https://www.switch-science.com/products/3494), ¥1,780 listed, magnet included | Exact Toyota footprint; Japan shipping and Friday arrival **not quoted**. |
| 1 instead of original | US-stock AS5601 alternative: `MIKROE-4204` Magneto 8 Click | [DigiKey](https://www.digikey.com/en/products/detail/mikroelektronika/MIKROE-4204/13157462), **$18**, two in stock | Same AS5601 IC and I²C interface, **different board/holder**. Confirm 3.3 V configuration, wiring, clearance, sensor alignment and calibration before adopting. Magnet not listed as included. |
| 1 alternate option | AS5601 `AS5601-SO_EK_AB` adapter | [DigiKey](https://www.digikey.com/en/products/detail/ams-osram-ag/AS5601-SO-EK-AB/5066883), **$19.40**, one in stock | Alternative to the $18 board, not an additional purchase. Also needs footprint/mount review. |
| 1 if US board used | Diametric encoder magnet, Radial Magnets `9042`, Ø6 × 2.5 mm, N35 | [DigiKey](https://www.digikey.com/en/products/detail/radial-magnets-inc/9042/5640338), **$0.63**, 20,539 in stock | Confirm Toyota magnet pocket and sensor airgap. Must be **diametrically**, not axially, magnetized. |
| 1 | SparkFun `PRT-08808` perfboard, 25.4 × 25.4 mm | [DigiKey](https://www.digikey.com/en/products/detail/sparkfun-electronics/08808/7387401), **$2.96**, 4,983 in stock | Exact original perfboard. |
| As needed | Pin headers / short hookup wires / solder | Check XIAO package and existing supplies; Toyota lists four header pieces | Header installation is required. Avoid ordering a new soldering kit unless missing. |
| 1 shared sheet | Grip rubber; original 1.5 mm `PX-10H15 HYPER V` | [RAPOLL solid neoprene, 12 × 12 in × 1/16 in](https://www.amazon.com/dp/B0BKQRN7S6), **$6.89 + free Prime shipping**, Thursday October 8 shown | Lowest-priced sheet checked; **material/thickness substitution** (nominal 1.5875 mm). Check grip, compliance, attachment and recalibrate jaw opening. Not equal-performance certification. |
| 1 alternative pack | Nominal 1.5 mm silicone sheet | [PATIKIL, five Ø100 mm discs](https://www.amazon.com/dp/B0G2JR4VFQ), **$9.21 + free Prime shipping**, Thursday shown in search | Alternative to neoprene, not an additional purchase. Check cutting layout and suitable silicone adhesive; grip performance is unvalidated. [Original Hyper V](https://nisshinrubber-metalcraft.com/products/hyperv%E3%82%B7%E3%83%BC%E3%83%88-px-10h-15-%E8%80%90%E6%B2%B9w270-l270-h1-5mm) remains the reference. |
| 1 band from pack | Return band, original Japanese No.16 | [MOWPOG #16 pack](https://www.amazon.com/dp/B0FCM95WH7), **$5.99 + free Prime shipping**, Thursday October 8 shown | Listing specifies 2.37 in folded length and 0.06 in width/thickness. Check return force and full travel; the size number alone is not equivalence. Reusing a suitable existing band avoids buying hundreds for one glove. |
| 0 | USB data cables/connections | Already available | Verify connector ends on the actual camera and XIAO; do not blindly order two USB-C cables. |

[DigiKey US shipping rates](https://www.digikey.com/en/help-support/delivery-information/delivery-time-and-cost):
two-day air **$13.99/order**, overnight PM **$26.99/order**. The $18 encoder + XIAO +
perfboard + magnet subtotal is **$26.97**: **$40.96 with two-day air** or **$53.96 with
overnight PM**, before tax/possible tariffs. These are rate-based estimates, not a
checkout-confirmed delivered quote. DigiKey currently warns that processing may take
an extra business day. Two-day requires Wednesday dispatch for Friday; overnight
requires Thursday dispatch. Mount adaptation remains separate work/cost.

## Screws — consolidated quantities for both builds

Counts include one robot and one right glove. Standard socket heads and low/ultra-low
heads are separate requirements. Lengths are under-head lengths. Ordinary screws use
M2 × 0.4, M2.5 × 0.45 and M3 × 0.5 threads.

| Robot | Glove | Buy/use total | Screw | Source / current status |
|---:|---:|---:|---|---|
| 4 | 4 | 8 | M2 × 6, standard socket head | [Amazon assortment candidate](https://www.amazon.com/dp/B0G8F366MV), $8.99 per kit, free Prime Thursday shown; also includes several sizes below. |
| 2 | 2 | 4 | M2.5 × 6, standard socket head | Same kit; [McMaster 91290A101](https://www.mcmaster.com/91290A101/) fallback, $11.81/50. |
| 0 | 2 | 2 | M2.5 × 8, standard socket head | Same kit; [McMaster 91290A006](https://www.mcmaster.com/91290A006/) fallback, $11.71/100. |
| 4 | 0 | 4 | M2.5 × 10, standard socket head | [VGBUY M2.5 1001-piece kit](https://www.amazon.com/dp/B0FJ1YMG3J), **$7.99 Prime price**, free Prime Thursday shown in search. Also covers M2.5 × 6/8. [McMaster 91290A007](https://www.mcmaster.com/91290A007/) fallback is $11.03/100. |
| 3 | 3 | 6 | M2.5 × 15, standard socket head | [McMaster 91290A009](https://www.mcmaster.com/91290A009/), **$4.25/10**, Thursday delivery shown; final shipping unquoted. |
| 0 | 1 | 1 | M3 × 6, standard socket head | Included in $8.99 kit. |
| 4 | 0 | 4 | M3 × 8, standard socket head | Included in $8.99 kit. |
| 6 | 0 | 6 | M3 × 10, standard socket head | [ALLWIN M3 400-piece kit](https://www.amazon.com/dp/B0F5QKDW7Y), **$4.63 Prime price**, free Prime Thursday shown in search; includes 30 screws of this length plus M3 × 6/8/12/16/20. |
| 2 | 0 | 2 | M3 × 12, standard socket head | Included in $8.99 kit. |
| 6 | 0 | 6 | M2 × 5, ultra-low head: Ø4 × 0.5 mm head | [MISUMI CBSTBR2-5](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTBR2-5), **$5.24 each / $31.44**; same steel/geometry, black nickel instead of white. October 7–8 dispatch shown. Original CBSTNR2-5 ships October 10. |
| 4 | 0 | 4 | M3 × 8, ultra-low head: Ø6 × 0.8 mm head | [MISUMI CBSTNR3-8](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTNR3-8), **$5.05 each / $20.20**, October 7–8 dispatch shown. |
| 0 | 2 | 2 | M3 × 5, ultra-low head: Ø6 × 0.8 mm head | [MISUMI CBSTNR3-5](https://us.misumi-ec.com/vona2/detail/110302280540/?HissuCode=CBSTNR3-5), **$5.05 each / $10.10**, October 7–8 dispatch shown. |
| 6 | 0 | 6 | M3 × 6, low head for rotor → coupler | [McMaster 92855A307](https://www.mcmaster.com/92855A307/), **$7.30/25**, Ø5.5 × 2 mm head, Thursday 7–9 am shown. |
| 4 | 0 | 4 | M3 × 8, low head for stator → motor bracket | [McMaster 92855A309](https://www.mcmaster.com/92855A309/), **$7.55/25**, 18-8 stainless, DIN 7984, Ø5.5 × 2 mm head, Thursday shown. [Alloy-steel 93070A064](https://www.mcmaster.com/93070A064/) is $13.62/50 if higher strength is required. |
| 2 | 0 | 2 | M2 × 8, low head for motor bracket → case back | [McMaster 92855A839](https://www.mcmaster.com/92855A839/), **$20.40/10**, Ø3.8 × 1.35 mm head, Thursday 7–9 am shown. |

McMaster dates above are displayed site estimates; the final destination/shipping
charge was not entered or quoted. MISUMI stocked rows also require a delivered quote.
The Amazon kit's stated lengths are 6/8/12/16/20 mm: it is **not a complete screw kit**
for this build. Do not buy every fallback pack as well as the kit.

One checked standard-screw combination is the $8.99 mixed kit + $7.99 M2.5 kit +
$4.63 M3 kit + $4.25 McMaster M2.5 × 15 pack: **$25.86**, including free Prime
shipping on the three Amazon kits, **plus the McMaster order's shipping and tax**.
This covers every standard screw length above; special low/ultra-low heads are extra.
Amazon search dates must be rechecked for the selected offer at checkout. Prime sale
prices and the displayed nightly delivery cutoffs may expire.

DIN 7984 and ordinary “low head” screws do **not** replace Toyota's ultra-low heads.
The new adapter counterbores and screw engagement still need checking on the machining
revision. Follow the manufacturer's reduced tightening torque for ultra-low heads.
The listed 18-8 low-head screws have 70,000 psi tensile strength; confirm required
joint preload/strength before substituting them for higher-strength alloy steel.

## Inserts for printed parts

| Robot | Glove | Total | Original specification | Sourcing status |
|---:|---:|---:|---|---|
| 4 | 0 | 4 | `SB-203030`: M2, nominal body Ø3 / knurl Ø3.3, length 3 mm | Exact US stock unresolved; generic M2 insert must match the actual printed hole and installation recommendation. |
| 5 | 5 | 10 | Toyota calls out `SB-264040`, nominal body Ø4 / knurl Ø4.3, length 4 mm | **Thread discrepancy to resolve:** assembly uses M2.5 screws; current Tokai catalog calls M2.5 `SB-254040`, while `SB-264040` is M2.6. Do not order M2.6 blindly. |
| 4 | 0 | 4 | `SB-304550`: M3, nominal body Ø4.5 / knurl Ø4.8, length 5 mm | Exact US stock unresolved. Not “M3 Ø4 × 5”; check fit before choosing another brand. |
| 0 | 2 | 2 | `SB-304540`: M3, nominal body Ø4.5 / knurl Ø4.8, length 4 mm | Exact US stock unresolved. |

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

For **machined coupler/flange**, do not buy their extra four M2 and two M3 plastic
heat-set inserts. Their metal-thread design replaces those inserts. If the adapters
are instead printed, add those six inserts, with dimensions selected for the actual CAD.

## Glove-only adjustment hardware

| Qty | Part | Source / parts price | Friday status |
|---|---|---|---|
| 4 | `JZF8-5` POM flanged bushings, nominal ID8 / OD10 / overall length5 mm | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110302640340/?HissuCode=JZF8-5), **$2.70 each / $10.80** | October 7–8 dispatch shown; delivery/shipping quote pending. |
| 1 | M3 × 6 long knurled screw, original `LRLM3-6` | [MISUMI LRLB3-6](https://us.misumi-ec.com/vona2/detail/110300245210/?HissuCode=LRLB3-6), **$6.06** | Same geometry in 303 stainless, Ø5.5 head × 10 mm high; October 7–8 dispatch. Original plated-steel LRLM3-6 is $5.78 but ships October 12. |
| 1 | `AJKTNS5-70`, M5 × 0.8, 70 mm adjustment screw | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110300599320/?HissuCode=AJKTNS5-70), **$15.14**; [black-oxide steel AJKTN5-70](https://us.misumi-ec.com/vona2/detail/110300599320/?HissuCode=AJKTN5-70), **$7.23** | **Both late:** ship October 12. Add to local-shop request. A stock bolt + knob needs tip/head/clearance review, not just a matching M5 thread. |
| 1 | `HNTT5-5` M5 pre-insertion T-slot nut | [MISUMI USA](https://us.misumi-ec.com/vona2/detail/110302246150/?HissuCode=HNTT5-5), **$0.73** | October 7–8 dispatch shown; delivered price/date pending. Exact pocket geometry, not a generic “2020” nut. |

## Order groups and shipping comparison

These are **partial order groups**, not a complete build budget or purchase instruction.
No full-build minimum delivered price can be claimed before machining and late-part
quotes are returned. Material/fit substitutions below still need the checks above.

| Order group | Checked contents | Parts / shipping / status |
|---|---|---|
| Amazon | Two used-like-new cameras, three standard screw kits, neoprene sheet and band pack | **$97.07 + $0 Prime shipping**, before tax. Add **$25.97** only if adapting prints for the two insert kits. Camera offer Friday, other listed offers Thursday at check. |
| McMaster | M2.5 × 15 pack and three low-head packs | **$39.50 + shipping + tax**, verified in an unsubmitted four-line guest basket. Site estimates Thursday. ZIP alone did not calculate shipping; final checkout/contact details are still required. |
| MISUMI stocked candidates | Six CBSTBR2-5, four CBSTNR3-8, two CBSTNR3-5, four JZF8-5, one LRLB3-6, one HNTT5-5, one JPBPB2-3 | **$86.38 + shipping + tax**. Displayed October 7–8 dispatch; choose a service with actual Friday arrival. Keep late items off this shipment. |
| DigiKey | US AS5601 board, XIAO, perfboard, diametric magnet | **$26.97 parts + $13.99 two-day = $40.96**, or **$53.96 overnight PM**, before tax/tariffs. Dispatch and board-mount validation required. |
| KHK + local machine shop | Two SSA1-30 blanks, conversion and custom machined parts | **$26.90 for blanks**; freight, engineering, machining and Friday pickup all **quote required**. Excluded from stocked-groups subtotal. |

The first four groups total **$263.91 before tax**, **plus unquoted McMaster/MISUMI
shipping**, using DigiKey two-day, and **excluding** inserts, all machining, finished
gears/shafts, bearings, precision keys/spacers, diamond pin, adjustment screw, adhesive
and any missing wiring/printing supplies. Adding both candidate insert kits gives
**$289.88 on the same incomplete basis**. Overnight DigiKey adds $13.00; selecting
the alloy-steel M3 × 8 low-head pack instead of stainless adds $6.07.

[MISUMI shipping guidance](https://us.misumi-ec.com/guide/faq/shipping.html) and
[McMaster delivery information](https://www.mcmaster.com/info/delivery).
Do not assume free MISUMI/McMaster shipping or substitute a catalog dispatch date for
arrival. Review the selected Prime offers and consolidated checkout totals before paying.

## What still prevents a complete Friday shopping list

1. Confirm a shop's **price and Friday pickup commitment** for the five machining
   parts; release revised coupler/flange drawings and verify the physical wrist.
2. Obtain a Friday route for **two finished gears and the stepped shaft**; exact catalog
   dates miss. KHK has a priced, on-hand gear blank for a shop to assess and modify.
3. Confirm **three correct angular-contact bearings**, precision washers/keys and the diamond pin.
4. Qualify candidate **insert fit/strength and rubber/band performance**, and secure the
   adjustment screw. Standard screw lengths and the T-nut now have priced sources.
5. Choose the exact encoder board or validate a US-board mount; quote its actual shipping.
6. Compare combined supplier carts, including shipping/tariffs/tax. Reconfirm all arrivals
   before ordering. Do not count partial catalog subtotals as a complete delivered budget.
