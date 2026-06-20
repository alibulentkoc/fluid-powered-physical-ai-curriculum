# Module 04 — Knowledge Check

*Fluid Mechanics for Intelligent Machines*

Attempt all before checking the key. Target: 8 of 10.

> This module is where the digital twin is born. Keep asking: what can the machine *predict* now?

---

## Conceptual

**Q1.** In Bernoulli's equation, if fluid speeds up through a restriction, what happens to its pressure, and why?

**Q2.** Every valve in the workcell is mathematically modeled as what single device?

**Q3.** Flow through an orifice is proportional to the square root of what?

**Q4.** Name the three components of the Stribeck friction model.

**Q5.** Why are the cylinder force balance and pressure dynamics described as "coupled"?

---

## Calculation

**Q6.** A valve ($C_d = 0.62$, $A_{max} = 4\ \text{mm}^2$, ρ = 870) is at full opening with a 30 bar drop. What flow (LPM)?

**Q7.** Using Q6's valve, what is the flow at half opening and the same pressure? At full opening and half the pressure?

**Q8.** A cylinder bore chamber (0.2 L, $B_e$ = 1.5 GPa) takes 10 LPM while the piston (50 mm bore) moves at 80 mm/s. Pressure rise rate (bar/s)?

**Q9.** The four-state cylinder ODE is `[x, v, Pb, Pr]`. Which equation governs the rate of change of `v`?

---

## Machine and twin

**Q10.** State the Module 04 **Machine Capability Added**, its **Digital Twin Contribution**, and which **benchmark task** it advances. (One sentence each.)

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** Pressure falls. By energy conservation, the kinetic energy gained as the fluid speeds up comes from pressure energy, so static pressure drops where velocity rises.

**A2.** An orifice (a variable orifice for a valve).

**A3.** The pressure drop across it.

**A4.** Static (breakaway), Coulomb (constant kinetic), and viscous (velocity-proportional) friction.

**A5.** The pressure dynamics need the piston velocity (from the force balance) and the force balance needs the pressures (from the pressure dynamics); each uses the other's output, so they must be solved together.

**A6.** $Q = 0.62\times4\times10^{-6}\times\sqrt{2\times30\times10^5/870}\times60000 = $ **12.36 LPM**.

**A7.** Half opening: **6.18 LPM** (linear in area). Half pressure (15 bar): $\sqrt{0.5} = 0.707$, so **8.74 LPM**.

**A8.** $A_b\dot{x} = \pi(0.025)^2\times0.080 = 1.571\times10^{-4}$ m³/s = 9.42 LPM. Mismatch with 10 LPM in = $9.6\times10^{-6}$ m³/s. $dP/dt = (1.5\times10^9/0.2\times10^{-3})\times9.6\times10^{-6} \approx$ **720 bar/s**.

**A9.** The force balance: $\dot{v} = (A_b P_b - A_r P_r - F_{friction} - F_{load})/m$.

**A10.** Capability: the machine can now **predict its hydraulic behavior before being built**. Twin: the valve orifice model and the coupled cylinder ODE are added — the twin's first dynamic prediction (cylinder trajectory). Benchmark task: **Precision Positioning** (predicting position over time is the foundation of positioning).

**Scoring:** 8–10 → ready for Module 05. 5–7 → review Lessons 02 and 05. Below 5 → rework the module.

</details>

---

*Knowledge Check 04 — Version 0.1*
