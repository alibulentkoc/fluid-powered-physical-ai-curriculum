# Module 03 — Problem Set

*Hydraulic Fluids and Energy Transmission*

Work each by hand, then verify with the Module 03 code files. Solutions at the bottom — all numerical answers verified against the curriculum code.

---

## Section A — Fluid functions and bulk modulus

**A1.** Name the four jobs hydraulic fluid does simultaneously, with one sentence each.

**A2.** A cylinder holds 0.3 L of oil on its bore side. The bulk modulus is 1.8 GPa. How much does the oil compress (mL) when pressure rises to 120 bar?

**A3.** If entrained air drops the effective bulk modulus to 0.5 GPa, recalculate A2. By what factor does the compression increase?

**A4.** Explain why a system with entrained air feels "spongy" and responds slowly.

---

## Section B — Viscosity

**B1.** What does "ISO VG 32" tell you precisely?

**B2.** An ISO VG 32 oil is 32 cSt at 40°C and 5.4 cSt at 100°C. Using the Walther model (or `viscosity_model.py`), estimate its viscosity at 50°C.

**B3.** A gear pump needs viscosity between 13 and 80 cSt. For ISO VG 46 (46 cSt @40°C, 6.8 @100°C), at roughly what temperature does the oil drop *below* the thick limit of 80 cSt (i.e., become thin enough to pump comfortably)?

**B4.** Why does a higher Viscosity Index give a wider usable temperature window?

---

## Section C — Contamination

**C1.** What does the ISO 4406 code 18/16/13 represent? Is it cleaner or dirtier than 17/15/12?

**C2.** A filter is rated $\beta_{10} = 150$. Calculate its efficiency at 10 μm and the number of >10 μm particles passed if 1,000,000 enter.

**C3.** The workcell's solenoid DCV requires ISO 18/16/13. A proportional valve requiring 17/15/12 is added. What is the new system target, and why?

**C4.** Why is "particles passed" a more meaningful measure than "efficiency percentage" when comparing filters?

---

## Section D — Energy losses

**D1.** Define the Reynolds number and state the approximate laminar threshold.

**D2.** A 14 LPM flow of ISO VG 46 oil (46 cSt, 870 kg/m³) passes through a 10 mm ID line, 2.5 m long. Calculate velocity, Reynolds number, and pressure drop.

**D3.** Why does halving a pipe's diameter increase the pressure drop by far more than a factor of two?

**D4.** Why are suction lines sized for lower velocity than pressure lines?

---

## Section E — System reasoning (workcell)

**E1.** Assemble the workcell Fluid Specification: state the fluid type, ISO VG grade, cleanliness target, filter Beta minimum, and supply-line diameter, with a one-line rationale for each.

**E2.** A reflection question: the workcell is moved from an indoor lab (stable 45°C) to an unheated barn (5°C winter mornings). Which two fluid properties become problematic, and what would you change?

---

## Solutions

<details>
<summary>Reveal (verified against curriculum code)</summary>

**A1.** Power transmission (incompressible fluid carries pressure to the actuator); lubrication (films protect pump, valve, and cylinder surfaces); sealing (viscosity fills clearances to limit leakage); heat removal (fluid carries heat to the reservoir/cooler).

**A2.** $\Delta V = V \cdot \Delta P / B = (0.3\times10^{-3} \times 120\times10^5)/(1.8\times10^9) = 2.0\times10^{-6}\ \text{m}^3 = 2.0$ mL.

**A3.** With B = 0.5 GPa: $\Delta V = (0.3\times10^{-3} \times 120\times10^5)/(0.5\times10^9) = 7.2$ mL. Increase factor = 1.8/0.5 = 3.6×.

**A4.** Air compresses far more easily than oil, lowering the effective bulk modulus. The piston moves to compress the air before full pressure builds on the load, so the system absorbs input as compression instead of motion — sluggish, springy response.

**B1.** ISO VG 32 = a fluid with kinematic viscosity of 32 cSt at 40°C.

**B2.** ≈ 21.5 cSt at 50°C (Walther model).

**B3.** ISO VG 46 reaches ~80 cSt at about 28°C (84 cSt at 28°C, 79.5 cSt at 29°C). So above roughly 28–29°C it is within the pumpable band on the thick side.

**B4.** A higher VI means viscosity changes less with temperature — a flatter viscosity-temperature curve. The flatter curve stays within the pump's acceptable band over a wider temperature range, widening the usable window.

**C1.** 18/16/13 = particle-count codes for particles >4, >6, and >14 μm per mL (codes 18, 16, 13 respectively). It is *dirtier* than 17/15/12 (higher numbers = more particles).

**C2.** Efficiency $= (1 - 1/150)\times100 = 99.33\%$. Particles passed $= 1{,}000{,}000/150 = 6{,}667$.

**C3.** New target 17/15/12 — the proportional valve is more sensitive than the solenoid DCV, and the most sensitive component sets the system target.

**C4.** Two filters can both read "99-point-something percent" yet pass very different absolute particle counts (e.g., β=100 passes 10,000; β=1000 passes 1,000 of a million). It is the absolute count of damaging particles reaching components that determines wear, so particles-passed is the meaningful comparison.

**D1.** $Re = vD/\nu$, dimensionless. Laminar below ~2300; turbulent above ~4000.

**D2.** $v = 2.97$ m/s, $Re = 646$ (laminar), $\Delta P = 0.951$ bar. (Verify with `pipe_friction.py`.)

**D3.** Loss scales with velocity squared, and for fixed flow, velocity scales with $1/D^2$ (smaller area → faster fluid). Combined with the $L/D$ term, halving the diameter raises the loss by roughly an order of magnitude, not a factor of two.

**D4.** Low suction velocity (≤1.2 m/s) prevents the pump inlet from being starved, which would cause cavitation — vapor bubbles that collapse and erode the pump. Pressure lines tolerate higher velocity because they are not at risk of inlet cavitation.

**E1.** Fluid type: mineral-based oil (indoor, no spill/biodegradability need). ISO VG 46 (mid-band viscosity across the 40–60°C range). Cleanliness target 18/16/13 (set by the solenoid DCV). Filter $\beta_{10} \geq 100$ (achieves/holds the target). Supply line 10 mm (≈0.54 bar loss, 2.1 m/s velocity — within limits).

**E2.** Viscosity (at 5°C the VG 46 oil is far above the 80 cSt thick limit — ~262 cSt — risking cold-start cavitation) and pour point / cold-flow behavior. Changes: switch to a lower VG grade or a high-VI / multigrade fluid to keep cold viscosity pumpable, and consider a reservoir heater or warm-up cycle. Document the tradeoff (cost, availability).

</details>

---

*Problem Set 03 — Version 0.1*
