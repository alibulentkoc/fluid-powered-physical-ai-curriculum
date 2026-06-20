# Module 05 — Problem Set

*Powering the Smart Agricultural Workcell*

Work each by hand, then verify with `code/module05/pump_performance_model.py`. All answers verified against the curriculum code.

> Every problem advances the machine toward **Precision Positioning** — the machine cannot position anything until it can generate and account for its own power.

---

## Section A — The machine's flow

**A1.** The machine's pump is 8 cc/rev at 1450 RPM, volumetric efficiency 0.92. What actual flow does the machine get?

**A2.** What pump displacement would the machine need for 8 LPM actual at 1450 RPM and 0.92 efficiency?

**A3.** The machine's cylinder has a 50 mm bore. At 10.67 LPM actual, what is the extend velocity?

**A4.** The machine must slow to a 30 mm/s approach. What motor speed achieves it (8 cc/rev, 0.92, 50 mm bore)?

---

## Section B — Pump selection

**B1.** Why must the machine use a positive-displacement pump rather than a centrifugal one?

**B2.** State, in one sentence each, why the gear pump beats the vane and piston pumps *for the workcell's mission*.

**B3.** What two numerical checks confirm a chosen pump meets the machine's requirements?

**B4.** A new mission demands 180 bar, smooth variable flow, generous budget, high cleanliness. Does the gear pump still win? What does?

---

## Section C — Efficiency and power

**C1.** Distinguish volumetric efficiency from mechanical efficiency. What does each account for?

**C2.** The machine delivers 10.67 LPM at 80 bar. What hydraulic power is that?

**C3.** With overall efficiency 0.83, what shaft power does the machine's motor supply at 100 bar / 10.67 LPM?

**C4.** At 120 bar the machine's volumetric efficiency drops to 0.91 and overall to 0.82. What shaft power is required, and is a 2.2 kW motor (2.53 kW with service factor) still adequate?

---

## Section D — The power unit

**D1.** Size the machine's reservoir using the 4× rule at 10.67 LPM.

**D2.** What relief valve setting does the machine use at 100 bar operating pressure (1.15×)?

**D3.** Name the components of the machine's HPU and one job of each.

**D4.** Why must the HPU be the first physical subsystem the machine gets?

---

## Section E — The machine

**E1.** State the machine's complete HPU design (pump, motor, flow, pressure, reservoir, relief).

**E2.** *Reflection:* In two sentences, what capability did the machine gain in Module 05, and why is it the prerequisite for every other capability?

---

## Solutions

<details>
<summary>Reveal (verified against pump_performance_model.py)</summary>

**A1.** $Q_a = 8 \times 1450 / 1000 \times 0.92 = 10.67$ LPM.

**A2.** $Q_t = 8/0.92 = 8.70$ LPM theoretical needed; $D = 8.70 \times 1000 / 1450 = 6.0$ cc/rev.

**A3.** $A = \pi(25)^2 = 1963$ mm². $Q_a = 10.67$ LPM $= 177{,}867$ mm³/s. $v = 177{,}867/1963 = 90.6$ mm/s.

**A4.** Required flow $= 30 \times 1963 = 58{,}890$ mm³/s $= 3.53$ LPM actual $= 3.84$ LPM theoretical. $n = 3.84 \times 1000 / 8 = 480$ RPM.

**B1.** Only positive-displacement pumps trap and force discrete volumes of fluid, building the high pressures (100 bar+) hydraulics require. Centrifugal pumps move volume at low pressure and cannot build hydraulic pressure.

**B2.** Gear vs. vane: the workcell does not need the vane's quietness or variable displacement, and the gear pump is more robust and cheaper. Gear vs. piston: the piston pump's high-pressure, high-efficiency, variable-flow strengths are wasted on a 100 bar fixed-flow bench machine, while its cost and contamination-sensitivity hurt the mission.

**B3.** (1) Pressure rating ≥ operating pressure × (1 + margin); (2) actual flow ≥ required flow.

**B4.** No — the gear pump no longer wins. The piston pump becomes attractive, driven by the variable-flow and high-pressure (180 bar) requirements, now that budget and cleanliness no longer rule it out.

**C1.** Volumetric efficiency accounts for flow lost to internal leakage (slippage past the gears). Mechanical efficiency accounts for torque lost to friction (bearings, gears, seals).

**C2.** $P_{hyd} = 80 \times 10.67 / 600 = 1.42$ kW.

**C3.** $P_{hyd} = 100 \times 10.67/600 = 1.78$ kW. $P_{shaft} = 1.78/0.83 = 2.15$ kW.

**C4.** At 120 bar: $Q_a$ ≈ 10.67 × (0.91/0.92) ≈ 10.55 LPM; $P_{hyd} = 120 \times 10.55/600 = 2.11$ kW; $P_{shaft} = 2.11/0.82 = 2.57$ kW. The 2.2 kW motor's service-factor capability (2.53 kW) is marginal — essentially at its limit. For sustained 120 bar duty the machine should step up to a 3 kW motor; for brief excursions the 2.2 kW frame is borderline acceptable. (The code reports 2.58 kW shaft at 120 bar.)

**D1.** $V = 4 \times 10.67 = 43$ L; rounded to a standard **40 L** tank (within the 32–53 L range).

**D2.** $115$ bar ($100 \times 1.15$).

**D3.** Motor (shaft power), pump (flow), coupling (join motor to pump), reservoir (store/de-aerate/cool fluid), relief valve (pressure safety), filter/breather (cleanliness, tank breathing).

**D4.** Nothing else in the machine can be tested or operated without a source of power; the HPU is the foundation every other subsystem plugs into, and its flow/pressure/cleanliness set hard limits on the machine's speed, force, and reliability.

**E1.** Gear pump 8 cc/rev; 2.2 kW motor at 1450 RPM; 10.67 LPM actual; 100 bar operating; 40 L reservoir; 115 bar relief.

**E2.** The machine gained its power source — the ability to generate controlled, pressurized flow. It is the prerequisite for everything because no motion, force, or task is possible until the machine can make its fluid flow.

</details>

---

*Problem Set 05 — Version 0.1*
