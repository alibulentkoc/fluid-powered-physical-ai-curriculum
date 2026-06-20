# Module 01 — Problem Set

*Foundations of Fluid Power and Physical AI*

Work these by hand first, then verify with `code/module01/unit_converter.py`. Solutions are at the bottom — attempt each problem before looking.

---

## Section A — Pascal's Law (force)

**A1.** A hydraulic cylinder has a bore diameter of 50 mm. A pressure of 150 bar is applied. Calculate the output (extend) force in kN.

**A2.** A cylinder must lift a 5000 N load with a 40 mm bore. What minimum pressure (bar) is required?

**A3.** A cylinder has a 63 mm bore and a 35 mm rod. At 120 bar, calculate both the extend force and the retract force in kN. Why are they different?

**A4.** Two pistons share a fluid. Piston A is 20 mm diameter; Piston B is 70 mm diameter. A 100 N force on A produces what force on B?

---

## Section B — Continuity (velocity)

**B1.** A pump delivers 20 LPM into a cylinder with a 60 mm bore. Calculate the piston velocity in mm/s.

**B2.** A workcell cylinder (50 mm bore) must extend at 100 mm/s. What flow rate (LPM) is required?

**B3.** A cylinder has a 40 mm bore and a 22 mm rod. At 12 LPM, calculate the extend velocity and the retract velocity. Which is faster, and by what ratio?

---

## Section C — Hydraulic power

**C1.** A hydraulic system operates at 200 bar and 30 LPM. Calculate the hydraulic power in kW.

**C2.** A system must deliver 3 kW of hydraulic power at 180 bar. What flow rate (LPM) is needed?

**C3.** A pump delivers 2.5 kW of hydraulic power. If the pump is 82% efficient overall, what motor power (kW) is required?

---

## Section D — Unit conversion

**D1.** Convert 2000 PSI to bar.

**D2.** Convert 10 GPM to LPM.

**D3.** Convert 15 HP to kW.

**D4.** A datasheet lists a pump as "8 cc/rev at 1450 RPM". What is the theoretical flow in LPM? (Hint: flow = displacement × speed.)

---

## Section E — System reasoning (workcell)

**E1.** You are designing an automated gripper for the workcell. The gripper cylinder has a 25 mm bore. The available system pressure is 80 bar. What is the maximum grip force the cylinder can produce?

**E2.** The workcell's tractor power source delivers 40 LPM at up to 175 bar. The workcell needs 10 LPM at 100 bar. What fraction of the available hydraulic power does the workcell consume?

**E3.** A reflection question (no single right answer): The workcell currently runs indoors at 100 bar. If it were redesigned to mount on a tractor and operate outdoors in a cold climate, name three things you would re-examine and explain why.

---

## Solutions

<details>
<summary>Click to reveal (try first!)</summary>

**A1.** $A = \pi(25)^2 = 1963\ \text{mm}^2$. $F = 150 \times 0.1 \times 1963 = 29{,}452\ \text{N} = 29.45\ \text{kN}$

**A2.** $A = \pi(20)^2 = 1257\ \text{mm}^2$. $P = F/(A \times 0.1) = 5000/(1257 \times 0.1) = 39.8\ \text{bar}$

**A3.** Bore area $= \pi(31.5)^2 = 3117\ \text{mm}^2$ → extend $= 120 \times 0.1 \times 3117 = 37.4\ \text{kN}$. Rod-side area $= 3117 - \pi(17.5)^2 = 3117 - 962 = 2155\ \text{mm}^2$ → retract $= 120 \times 0.1 \times 2155 = 25.9\ \text{kN}$. Different because the rod occupies area on the retract side, reducing the effective piston area.

**A4.** $A_A = \pi(10)^2 = 314\ \text{mm}^2$, $A_B = \pi(35)^2 = 3848\ \text{mm}^2$. $F_B = 100 \times (3848/314) = 1225\ \text{N}$

**B1.** $A = \pi(30)^2 = 2827\ \text{mm}^2$. $Q = 20 \times 10^6/60 = 333{,}333\ \text{mm}^3/\text{s}$. $v = 333{,}333/2827 = 117.9\ \text{mm/s}$

**B2.** $A = \pi(25)^2 = 1963\ \text{mm}^2$. $Q = A \times v = 1963 \times 100 = 196{,}300\ \text{mm}^3/\text{s} = 11.8\ \text{LPM}$

**B3.** Bore area $= \pi(20)^2 = 1257\ \text{mm}^2$, rod-side $= 1257 - \pi(11)^2 = 1257 - 380 = 877\ \text{mm}^2$. $Q = 12 \times 10^6/60 = 200{,}000\ \text{mm}^3/\text{s}$. Extend $v = 200{,}000/1257 = 159\ \text{mm/s}$. Retract $v = 200{,}000/877 = 228\ \text{mm/s}$. Retract is faster by ratio $1257/877 = 1.43$.

**C1.** $P = (200 \times 30)/600 = 10\ \text{kW}$

**C2.** $Q = (P \times 600)/p = (3 \times 600)/180 = 10\ \text{LPM}$

**C3.** $P_{motor} = 2.5/0.82 = 3.05\ \text{kW}$

**D1.** $2000/14.504 = 137.9\ \text{bar}$

**D2.** $10 \times 3.785 = 37.85\ \text{LPM}$

**D3.** $15 \times 0.7457 = 11.19\ \text{kW}$

**D4.** $8\ \text{cc/rev} \times 1450\ \text{rev/min} = 11{,}600\ \text{cc/min} = 11.6\ \text{LPM}$ (theoretical; actual is lower by volumetric efficiency — see Module 05)

**E1.** $A = \pi(12.5)^2 = 491\ \text{mm}^2$. $F = 80 \times 0.1 \times 491 = 3927\ \text{N} \approx 3.9\ \text{kN}$. (Note: for gripping delicate objects this is far more than needed — grip force is controlled by limiting pressure or using force feedback, covered in Modules 09–10.)

**E2.** Available power $= (175 \times 40)/600 = 11.67\ \text{kW}$. Workcell power $= (100 \times 10)/600 = 1.67\ \text{kW}$. Fraction $= 1.67/11.67 = 14.3\%$. The workcell uses a small fraction — confirming tractor-compatibility.

**E3.** Sample answer: (1) Fluid viscosity — cold weather thickens oil, affecting pump cavitation and pressure drop; a different ISO VG grade or a viscosity-index improver may be needed (Module 03). (2) Filtration and contamination — outdoor operation introduces dust and water; filter rating and reservoir sealing must be reconsidered (Module 03). (3) Sensor and electronics environmental rating — outdoor temperature swings, moisture, and vibration require ruggedized sensors and enclosures (Module 09).

</details>

---

*Problem Set 01 — Version 0.1*
