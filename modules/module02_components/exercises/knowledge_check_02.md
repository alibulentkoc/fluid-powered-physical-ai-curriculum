# Module 02 — Knowledge Check

*Hydraulic Components and System Architecture*

A short formative assessment. Attempt every question before checking the key. Target: 8 of 10 correct.

---

## Conceptual

**Q1.** Does a pump create flow or pressure? What determines the quantity it does *not* directly create?

**Q2.** Name the three families of valves and the single job each performs.

**Q3.** What does each character mean in "4/3 closed-center solenoid DCV"?

**Q4.** Why is the retract force of a double-acting cylinder always less than its extend force at the same pressure?

**Q5.** What is the single most common cause of hydraulic system failure, and which subsystem is the primary defense against it?

---

## Calculation

**Q6.** A 9 cc/rev gear pump runs at 1450 RPM with 91% volumetric efficiency. What is the actual flow in LPM?

**Q7.** A flow control valve has $C_d = 0.65$, area 2.5 mm², pressure drop 36 bar, fluid density 870 kg/m³. Calculate the flow in LPM.

**Q8.** A hydraulic motor has 12 cc/rev displacement at a 100 bar pressure drop and 90% mechanical efficiency. Calculate the output torque in N·m.

**Q9.** A filter is rated $\beta_{10} = 200$. Calculate its capture efficiency at 10 μm.

---

## System reasoning

**Q10.** You are choosing between an open-center and a closed-center DCV for the workcell. The workcell must grip an object and hold it precisely while a second actuator performs a task. Which DCV do you choose, what does it require for protection, and what is the tradeoff you accept?

---

## Answer key

<details>
<summary>Reveal answers (attempt all first)</summary>

**A1.** A pump creates flow. Pressure is determined by the resistance the flow meets — the load on the actuators and the relief valve setting. The pump does not create pressure on its own.

**A2.** Directional control (where the fluid goes), pressure control (how much pressure can build before relieving), flow control (how fast the fluid flows, and therefore how fast the actuator moves).

**A3.** "4" = four ports (P, T, A, B). "3" = three spool positions. "Closed-center" = in the neutral position all ports are blocked, locking the cylinder. "Solenoid" = electrically actuated by solenoids. "DCV" = directional control valve.

**A4.** The rod occupies part of the cross-sectional area on the rod side, so the effective (annular) area is smaller than the full bore area. Force = pressure × area, so the smaller rod-side area gives a smaller force at the same pressure.

**A5.** Contamination (dirt, water, wear particles in the fluid). The support system — primarily the filter, plus a sealed reservoir and good fittings/breather — is the main defense.

**A6.** $Q_a = 9 \times 1450 / 1000 \times 0.91 = 11.87$ LPM.

**A7.** $A = 2.5\times10^{-6}$ m², $\Delta P = 36\times10^5$ Pa. $\sqrt{2\times36\times10^5/870} = \sqrt{8276} = 90.97$ m/s. $Q = 0.65 \times 2.5\times10^{-6} \times 90.97 = 1.478\times10^{-4}$ m³/s $= 8.87$ LPM.

**A8.** $T = (12\times10^{-6} \times 100\times10^5)/(2\pi) \times 0.9 = (120/6.283)\times0.9 = 17.2$ N·m.

**A9.** $(1 - 1/200)\times100 = 99.5\%$.

**A10.** Choose the **closed-center** DCV — its neutral position blocks all ports and hydraulically locks the cylinder, holding the gripped object precisely without continuous pump effort. It requires **port relief valves** to protect against pressure spikes when an external load pushes on the locked cylinder. The tradeoff accepted: slightly higher heat generation at idle (the pump cannot circulate freely back to tank in neutral) and the added complexity/cost of the port reliefs, in exchange for reliable load holding.

**Scoring:** 8–10 → ready for Module 03. 5–7 → review Lessons 01 and 02. Below 5 → rework the module.

</details>

---

*Knowledge Check 02 — Version 0.1*
