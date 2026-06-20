# Module 04 — Problem Set

*Fluid Mechanics for Intelligent Machines*

Work each by hand, then verify with the Module 04 code files. All numerical answers are verified against the curriculum code.

> Keep the machine in view: every problem here is a step toward predicting and controlling the workcell's motion — the foundation of **Precision Positioning**.

---

## Section A — Bernoulli and energy

**A1.** Name the three forms of energy in Bernoulli's equation.

**A2.** Hydraulic oil (ρ = 870 kg/m³) flows at 2.0 m/s in a 10 mm line, then accelerates into a 5 mm restriction. Find the velocity in the restriction and the ideal (frictionless) pressure drop.

**A3.** Why must a friction head-loss term be added to Bernoulli for real hydraulic lines?

---

## Section B — Orifice / valve model (the first twin component)

**B1.** Write the orifice equation and state what flow is proportional to (regarding pressure drop).

**B2.** A valve has $C_d = 0.62$, $A_{max} = 3\ \text{mm}^2$, ρ = 870. At full opening with a 25 bar drop, what flow (LPM)?

**B3.** Using B2's valve, what flow at half opening, same 25 bar? At full opening but 6.25 bar (quarter of the pressure)?

**B4.** Explain why halving the valve opening halves the flow, but quartering the pressure drop only halves the flow.

---

## Section C — Cylinder force balance

**C1.** Write Newton's second law for a hydraulic cylinder and name each term.

**C2.** A cylinder (63 mm bore, 36 mm rod) is extending. $P_b$ = 90 bar, $P_r$ = 8 bar, mass = 4 kg, v = 40 mm/s, Coulomb friction = 70 N, viscous coeff = 250 N·s/m, external load = 150 N. Calculate the instantaneous acceleration.

**C3.** Name the three components of the Stribeck friction model and state which dominates at very low velocity.

**C4.** What is stick-slip, and why does it threaten Precision Positioning?

---

## Section D — Pressure dynamics

**D1.** Why does pressure build at a finite rate rather than instantly?

**D2.** A bore chamber (0.25 L) has effective bulk modulus 1.5 GPa. 12 LPM flows in while the piston (50 mm bore) moves at 70 mm/s. Calculate the pressure rise rate (bar/s).

**D3.** Why is the effective bulk modulus lower than the pure-oil value?

**D4.** Why must the force balance and pressure dynamics be solved together?

---

## Section E — Simulation and the machine

**E1.** The four-state cylinder ODE is `[x, v, Pb, Pr]`. State what each represents and which equation governs its rate of change.

**E2.** Run `cylinder_simulation.py`. At what steady velocity does the cylinder extend, and how does this compare to the curriculum's baseline of ~85 mm/s? Why is matching the hand calculation important for a digital twin?

**E3.** *Machine reflection:* In one or two sentences, state what new capability the machine gained in Module 04, and which benchmark task it advances.

---

## Solutions

<details>
<summary>Reveal (verified against curriculum code)</summary>

**A1.** Pressure energy, kinetic energy (½ρv²), potential/elevation energy (ρgh).

**A2.** $v_2 = v_1 (D_1/D_2)^2 = 2.0 \times (10/5)^2 = 8.0$ m/s. $\Delta P = \frac12\rho(v_2^2 - v_1^2) = \frac12(870)(64 - 4) = 26{,}100$ Pa = **0.26 bar**.

**A3.** Bernoulli assumes frictionless flow. Real lines lose pressure to viscous friction (Darcy-Weisbach), so a head-loss term $h_{loss}$ must be added to balance the energy equation in practice.

**B1.** $Q = C_d A \sqrt{2\Delta P/\rho}$. Flow is proportional to the **square root** of the pressure drop.

**B2.** $Q = 0.62 \times 3\times10^{-6} \times \sqrt{2\times25\times10^5/870} \times 60000 = $ **8.46 LPM**.

**B3.** Half opening: **4.23 LPM** (linear in area). Quarter pressure (6.25 bar): $\sqrt{6.25/25} = 0.5$, so **4.23 LPM** as well.

**B4.** Flow is linear in opening area (halving area halves flow) but proportional to the *square root* of pressure drop (quartering pressure multiplies flow by √¼ = ½). The square-root relationship is the source of the asymmetry — and the core difficulty of valve control.

**C1.** $m\ddot{x} = A_b P_b - A_r P_r - F_{friction} - F_{load}$: inertia = driving force − back-pressure force − friction − external load.

**C2.** $A_b = \pi(0.0315)^2 = 3.117\times10^{-3}$ m², $A_r = A_b - \pi(0.018)^2 = 2.099\times10^{-3}$ m². Drive = $3.117\times10^{-3}\times90\times10^5 = 28{,}055$ N. Back = $2.099\times10^{-3}\times8\times10^5 = 1{,}679$ N. Friction = $70 + 250(0.04) = 80$ N. Net = $28{,}055 - 1{,}679 - 80 - 150 = 26{,}146$ N. $a = 26{,}146/4 = $ **6{,}536 m/s²** (large — the cylinder is far from balance and will accelerate hard until pressures equilibrate).

**C3.** Static (breakaway) friction, Coulomb (constant kinetic) friction, viscous (velocity-proportional) friction. Static/Stribeck dominates at very low velocity.

**C4.** Stick-slip is jerky alternating sticking and slipping motion at low speed, caused by the high static friction that must be overcome to start moving. It threatens Precision Positioning because the slow, fine approach to a target happens exactly in the low-velocity regime where stick-slip occurs.

**D1.** Because the fluid is slightly compressible (finite bulk modulus). Incoming fluid partly compresses before it can build pressure, so pressure rises over a finite time.

**D2.** $A_b = \pi(0.025)^2 = 1.963\times10^{-3}$ m². $A_b\dot{x} = 1.963\times10^{-3}\times0.070 = 1.374\times10^{-4}$ m³/s. $Q_{in} = 12/60000 = 2.0\times10^{-4}$ m³/s. Mismatch = $6.26\times10^{-5}$ m³/s. $dP/dt = (1.5\times10^9/0.25\times10^{-3})\times6.26\times10^{-5} = 3.75\times10^{8}$ Pa/s = **3{,}753 bar/s**.

**D3.** Hose compliance (lines stretch under pressure) and any entrained air both make the system softer, lowering the effective bulk modulus below the pure-oil value.

**D4.** The pressure dynamics need the piston velocity (from the force balance), and the force balance needs the pressures (from the pressure dynamics). Each depends on the other's output, so they must be integrated simultaneously as one coupled system.

**E1.** `x` = position (governed by $\dot{x}=v$); `v` = velocity (force balance, $\dot{v}=F_{net}/m$); `Pb` = bore pressure (pressure dynamics); `Pr` = rod pressure (pressure dynamics).

**E2.** The cylinder extends at roughly **82 mm/s** steady, close to the ~85 mm/s baseline established in Modules 01–03. Matching the hand calculation matters because a digital twin is only trustworthy if its predictions agree with independent analysis — agreement is the first validation that the model is correct.

**E3.** The machine gained the ability to **predict its hydraulic behavior before being built** — the digital twin's first dynamic model. It advances **Precision Positioning**, since predicting cylinder position over time is the foundation of moving an end-effector to a target.

</details>

---

*Problem Set 04 — Version 0.1*
