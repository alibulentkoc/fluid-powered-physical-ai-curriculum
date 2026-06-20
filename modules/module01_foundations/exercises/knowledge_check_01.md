# Module 01 — Knowledge Check

*Foundations of Fluid Power and Physical AI*

A short formative assessment. Use it to confirm you are ready for Module 02. Attempt every question before checking the answer key at the bottom. Target: 8 of 10 correct.

---

## Conceptual (no calculation)

**Q1.** In one or two sentences, explain why Fluid-Powered Physical AI is described as an underserved field. What assumption does most current Physical AI make that this curriculum challenges?

**Q2.** State Pascal's Law in words. Then write the equation.

**Q3.** Name the five elements of any hydraulic system (the model from the Module 01 manifest), and name the six subsystems of the Smart Agricultural Workcell. How do they relate?

**Q4.** Why is the Smart Agricultural Workcell described as a *constrained-workspace manipulation platform* rather than an autonomous field vehicle? Give one reason this scale was chosen.

**Q5.** A dumb hydraulic actuator and an intelligent one differ in two subsystems. Which two, and what do they add?

---

## Calculation

**Q6.** A cylinder has a 100 mm bore. The system pressure is 200 bar. Calculate the extend force in kN.

**Q7.** A pump delivers 25 LPM into a cylinder with a 63 mm bore. Calculate the piston extend velocity in mm/s.

**Q8.** A hydraulic system operates at 160 bar and 12 LPM. Calculate the hydraulic power in kW. Then calculate the required motor power assuming 85% pump efficiency.

**Q9.** Convert each: (a) 1500 PSI to bar, (b) 8 GPM to LPM, (c) 10 HP to kW.

---

## System reasoning

**Q10.** Trace a single *retract* command through all six subsystems of the workcell. For each subsystem, write one short line describing what happens. How does the retract sequence differ from the extend sequence at the actuation stage?

---

## Answer key

<details>
<summary>Reveal answers (attempt all first)</summary>

**A1.** Most Physical AI is built on electric actuation (servos, brushless motors), but agriculture, construction, and heavy industry run overwhelmingly on fluid power. The field is underserved because almost no open educational or research material exists on bringing sensing, control, and intelligence into fluid-powered machines. The challenged assumption is that intelligent physical systems must be electrically actuated.

**A2.** Pressure is transmitted equally in all directions through a confined static fluid; pressure equals force divided by the area it acts on. Equation: $P = F/A$.

**A3.** Five elements: power source (pump), control elements (valves), actuators (cylinders/motors), fluid, conditioning elements (filter/reservoir/cooler). Six subsystems: S1 Hydraulic power, S2 Fluid transport, S3 Motion control, S4 Actuation, S5 Sensing & intelligence, S6 Digital twin. The five elements map onto subsystems S1–S4 (the physical hydraulic machine); S5 and S6 add the intelligence layer that the classic five-element model does not include.

**A4.** It is bench-scale and operates in a defined work envelope, making it affordable, safe, and achievable for education and research. An autonomous field vehicle would be too large, expensive, and complex. (Also acceptable: the constrained-workspace paradigm mirrors proven systems like the milking robot and supports interchangeable end-effectors.)

**A5.** Subsystem 5 (Sensing and intelligence) and Subsystem 6 (Digital twin). S5 adds perception and embedded decision-making; S6 adds a parallel model that validates behavior and detects faults.

**A6.** $A = \pi(50)^2 = 7854\ \text{mm}^2$. $F = 200 \times 0.1 \times 7854 = 157{,}080\ \text{N} = 157.1\ \text{kN}$.

**A7.** $A = \pi(31.5)^2 = 3117\ \text{mm}^2$. $Q = 25 \times 10^6/60 = 416{,}667\ \text{mm}^3/\text{s}$. $v = 416{,}667/3117 = 133.7\ \text{mm/s}$.

**A8.** $P_{hyd} = (160 \times 12)/600 = 3.2\ \text{kW}$. Motor power $= 3.2/0.85 = 3.76\ \text{kW}$.

**A9.** (a) $1500/14.504 = 103.4\ \text{bar}$. (b) $8 \times 3.785 = 30.3\ \text{LPM}$. (c) $10 \times 0.7457 = 7.46\ \text{kW}$.

**A10.** Sample trace:
- S6 (Digital twin): task sequencer decides "retract to 0 mm"; predicted trajectory recorded.
- S5 (Command): Raspberry Pi sends `RETRACT` to Arduino.
- S5 (Embedded): Arduino energizes solenoid B of the DCV.
- S3 (Motion control): DCV spool shifts; supply now connects to the **rod-side** port, return to the bore-side port.
- S2 (Fluid transport): pressurized oil flows to the rod-side cylinder port.
- S1 (Hydraulic power): pump maintains pressure; relief valve stays closed.
- S4 (Actuation): pressure acts on the **rod-side (annular) area** — smaller than the bore — so for the same flow the piston retracts **faster**, and for the same pressure the retract force is **lower** than extend. This is the differential cylinder effect.
- S5 (Sensing): position sensor reports decreasing extension; Arduino streams values to the Pi.
- S5 (Embedded): at 0 mm, de-energize solenoid B; DCV centers; cylinder holds.
- S6 (Validate): twin compares predicted vs. measured; small residual, no fault.

The key difference at the actuation stage: retract uses the smaller rod-side area, so retract is faster and weaker than extend.

**Scoring:** 8–10 correct → ready for Module 02. 5–7 → review Lessons 03 and 04. Below 5 → rework the full module before continuing.

</details>

---

*Knowledge Check 01 — Version 0.1*
