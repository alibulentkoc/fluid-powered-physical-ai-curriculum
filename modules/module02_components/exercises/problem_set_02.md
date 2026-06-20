# Module 02 — Problem Set

*Hydraulic Components and System Architecture*

Work each by hand, then verify with `code/module02/pump_flow_model.py` where relevant. Solutions are at the bottom — attempt before checking.

---

## Section A — Pumps

**A1.** A gear pump has a displacement of 11 cc/rev and runs at 1450 RPM. Calculate the theoretical flow in LPM.

**A2.** The same pump has a volumetric efficiency of 0.90. What is the actual delivered flow?

**A3.** A workcell needs 14 LPM actual flow at 1800 RPM with 92% volumetric efficiency. What pump displacement (cc/rev) is required?

**A4.** A pump delivers 12 LPM at 150 bar with an overall efficiency of 0.84. What motor power (kW) is required to drive it?

**A5.** Explain in one or two sentences why doubling a fixed-displacement pump's shaft speed doubles its flow, but tilting a variable-displacement pump's swashplate changes flow at constant speed.

---

## Section B — Valves

**B1.** Decode the valve designation "4/3 closed-center solenoid DCV, spring-centered." State the number of ports, number of positions, what the center position does, how it is actuated, and how it returns to center.

**B2.** A flow control valve has $C_d = 0.65$, an opening area of 3 mm², and a pressure drop of 40 bar. Fluid density is 870 kg/m³. Calculate the flow in LPM.

**B3.** Using the orifice equation, by what factor does flow change if the pressure drop across a valve increases from 20 bar to 80 bar (area unchanged)?

**B4.** Label the four ports of a 4/3 DCV and describe what each connects to in the workcell.

**B5.** Why does the workcell's closed-center DCV require port relief valves, when an open-center design would not?

---

## Section C — Cylinders and motors

**C1.** A cylinder has a 63 mm bore and a 36 mm rod, operating at 120 bar. Calculate the extend force and the retract force, both in kN.

**C2.** What is the extend-to-retract force ratio for the cylinder in C1?

**C3.** A hydraulic motor has 10 cc/rev displacement, operates at a 90 bar pressure drop, with 90% mechanical efficiency. Calculate the output torque in N·m.

**C4.** The same motor receives 9 LPM with 92% volumetric efficiency. Calculate its output speed in RPM.

**C5.** A task requires continuous rotation at constant torque. Cylinder or motor? Explain in one sentence.

---

## Section D — Support system

**D1.** A filter is rated $\beta_{10} = 75$. Calculate its capture efficiency at 10 μm.

**D2.** A workcell pump delivers 12 LPM. Using the rule of thumb k = 4 minutes, recommend a continuous-duty reservoir volume.

**D3.** Why must the suction line be sized larger than the pressure line?

**D4.** Two filters are available: $\beta_{10} = 100$ and $\beta_{10} = 1000$. The difference in efficiency is small in percentage terms. Why might the higher-Beta filter still be the better choice for protecting a sensitive DCV over a long service life?

---

## Section E — System reasoning (workcell)

**E1.** The workcell uses an 8 cc/rev gear pump at 1450 RPM (92% vol. eff.). It must drive a 50 mm bore cylinder. What is the maximum extend velocity (mm/s) achievable with this pump's full actual flow?

**E2.** You are producing the Module 02 Component Map. List the components you would name for Subsystem 1 (Hydraulic Power) and Subsystem 2 (Fluid Transport), with at least one specification for each.

---

## Solutions

<details>
<summary>Reveal (try first!)</summary>

**A1.** $Q_t = 11 \times 1450 / 1000 = 15.95$ LPM

**A2.** $Q_a = 15.95 \times 0.90 = 14.36$ LPM

**A3.** Theoretical needed $= 14/0.92 = 15.22$ LPM. $D = 15.22 \times 1000 / 1800 = 8.46$ cc/rev. Round up to a 9 or 10 cc/rev standard size.

**A4.** Hydraulic power $= (150 \times 12)/600 = 3.0$ kW. Motor $= 3.0/0.84 = 3.57$ kW → 4 kW standard motor.

**A5.** For a fixed-displacement pump, flow = displacement × speed, so flow is proportional to speed (displacement is constant). A variable-displacement pump changes the swept volume per revolution by tilting its swashplate, so it can vary flow while the shaft speed (set by the driving motor) stays fixed.

**B1.** 4 ports (P, T, A, B); 3 positions; the center position blocks all ports (closed center), hydraulically locking the cylinder; actuated by solenoids (one per side); returns to center by springs when both solenoids are de-energized.

**B2.** $A = 3\times10^{-6}$ m², $\Delta P = 40\times10^5$ Pa. $\sqrt{2 \times 40\times10^5 / 870} = \sqrt{9195} = 95.9$ m/s. $Q = 0.65 \times 3\times10^{-6} \times 95.9 = 1.87\times10^{-4}$ m³/s $= 11.2$ LPM.

**B3.** Flow ∝ √ΔP. Ratio $= \sqrt{80/20} = \sqrt{4} = 2$. Flow doubles. (Note: a 4× pressure increase gives only a 2× flow increase.)

**B4.** P = pressure, from the pump. T = tank, return to reservoir. A = to one cylinder port (e.g., bore side). B = to the other cylinder port (e.g., rod side). Shifting the spool connects P→A and B→T (extend) or P→B and A→T (retract).

**B5.** A closed-center valve traps fluid in the cylinder when centered, hydraulically locking it. An external load pushing on the locked rod can spike the trapped pressure far above the system relief setting; port relief valves cap that spike and protect the cylinder and seals. An open-center valve connects P→T when centered, so the cylinder is not locked and cannot trap a damaging spike the same way.

**C1.** Bore area $= \pi(31.5)^2 = 3117$ mm². Extend $= 120 \times 0.1 \times 3117 = 37{,}404$ N $= 37.4$ kN. Rod-side area $= 3117 - \pi(18)^2 = 3117 - 1018 = 2099$ mm². Retract $= 120 \times 0.1 \times 2099 = 25{,}188$ N $= 25.2$ kN.

**C2.** $37.4 / 25.2 = 1.48$.

**C3.** $T = (10\times10^{-6} \times 90\times10^5)/(2\pi) \times 0.9 = (90/6.283)\times0.9 = 12.9$ N·m.

**C4.** $n = Q \cdot \eta_v / D_m = (9 \text{ LPM} \times 0.92)/(10 \text{ cc/rev})$. Convert: $9$ LPM $= 9000$ cc/min. $n = 9000 \times 0.92 / 10 = 828$ RPM.

**C5.** Motor — it provides continuous rotation at sustained torque, which a finite-stroke cylinder cannot.

**D1.** $(1 - 1/75)\times100 = 98.67\%$.

**D2.** $V = 4 \times 12 = 48$ L.

**D3.** To keep suction velocity low (typically below ~1.2 m/s) so the pump inlet is not starved; high suction velocity causes cavitation, which erodes the pump.

**D4.** The percentage efficiency difference is small, but the higher-Beta filter removes a far larger fraction of the *largest, most damaging* particles. Over long service, the cumulative number of damaging particles passed by the $\beta=100$ filter is ten times that of the $\beta=1000$ filter, which matters for a precision DCV with micron-scale clearances.

**E1.** Actual flow $= 8 \times 1450 / 1000 \times 0.92 = 10.67$ LPM $= 177{,}867$ mm³/s. Bore area $= \pi(25)^2 = 1963$ mm². $v = 177{,}867 / 1963 = 90.6$ mm/s.

**E2.** Sample Component Map:
- Subsystem 1 (Hydraulic Power): electric motor (2.2 kW, 1450 RPM); gear pump (8 cc/rev, fixed displacement); pressure relief valve (set ~110–120 bar); reservoir (12–20 L for intermittent bench duty).
- Subsystem 2 (Fluid Transport): supply line (rated >150 bar hose); return line; return-line filter ($\beta_{10} \geq 100$) with clogging indicator; breather; fittings standardized to BSP (or regional norm); ISO VG 46 hydraulic oil (specified fully in Module 03).

</details>

---

*Problem Set 02 — Version 0.1*
