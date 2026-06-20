# Module 07 — Problem Set

*Producing the Machine's Force and Motion*

Work each by hand, then verify with the Module 07 code. All answers verified against the curriculum code.

> Every problem advances **Force-Controlled Interaction** — the machine learning to produce, specify, and control the force its tasks demand.

---

## Section A — Producing force

**A1.** The workcell cylinder (50 mm bore, 28 mm rod) operates at 100 bar. Compute extend and retract force.

**A2.** Why is the extend force larger than the retract force? Give the area ratio.

**A3.** A task needs 1.5 kN of gripping force. What bore pressure does the machine use? What fraction of system pressure is that?

**A4.** Why does the machine's large force capacity *help* gentle, controlled interaction?

---

## Section B — Specifying the actuator

**B1.** Name four ways a force-sized cylinder can still fail in service.

**B2.** Compute the Euler buckling load for the 28 mm rod at 300 mm stroke (effective length 400 mm, K=2.0, E=210 GPa). Compare to the 19.63 kN extend force.

**B3.** What pressure rating does the machine specify for 100 bar working pressure (1.6× design factor)?

**B4.** Why might the machine choose a clevis mount over a rigid flange?

---

## Section C — Real behavior

**C1.** Name the three components of cylinder friction and which dominates at breakaway.

**C2.** Compute the friction at 5 mm/s and 50 mm/s (Fs=120, Fc=70, vs=10 mm/s, b=200). Which is higher, and why does that matter?

**C3.** What is breakout force, and what does it set for the machine's gentlest controllable force?

**C4.** Why is the most detailed friction model not always best for the twin?

---

## Section D — Choosing the actuator type

**D1.** What can a cylinder do that a motor cannot, and vice versa?

**D2.** For each task, choose cylinder or motor: (a) primary positioning, (b) continuous spin, (c) gripping, (d) large-angle part rotation.

**D3.** Size a motor: 8 N·m torque, 6 cc/rev, 90% mechanical efficiency. What pressure? Within 100 bar?

**D4.** What flow does that motor need at 60 RPM (6 cc/rev, 92% volumetric)? Does the pump have enough?

---

## Section E — The machine

**E1.** State the machine's complete Actuator Selection Report (the primary cylinder spec).

**E2.** *Reflection:* In two sentences, what capability did the machine gain in Module 07, and how does it advance Force-Controlled Interaction?

---

## Solutions

<details>
<summary>Reveal (verified against Module 07 code)</summary>

**A1.** $A_b = \pi(25)^2 = 1963$ mm², $A_r = 1963 - \pi(14)^2 = 1348$ mm². Extend $= 100 \times 0.1 \times 1963 = 19{,}630$ N = 19.63 kN. Retract $= 100 \times 0.1 \times 1348 = 13{,}480$ N = 13.48 kN.

**A2.** The rod reduces the rod-side area, so the bore (full) area is larger. Area ratio $\phi = 1963/1348 = 1.46$. Extend force is 1.46× retract.

**A3.** $P = 1500/(1963 \times 0.1) = 7.6$ bar — 7.6% of the 100 bar system.

**A4.** Controlling a small force as a fraction of a large capacity is more precise than running a small actuator at its limit. The headroom lets the machine modulate gently in the low, finely-controllable part of its range.

**B1.** Rod buckling, wrong stroke (cannot reach / too long), mounting failure (bends rod / cracks), exceeding pressure rating, incompatible seals.

**B2.** $I = \pi(0.028)^4/64 = 3.02\times10^{-8}$ m⁴. $F_{cr} = \pi^2 \times 210\times10^9 \times 3.02\times10^{-8} / (2.0 \times 0.4)^2 = 98$ kN. Safety factor $98/19.63 = 5.0$. ✓ safe.

**B3.** $\geq 1.6 \times 100 = 160$ bar.

**B4.** A clevis allows slight angular alignment, so a misaligned load does not transfer side-load into the rod and seals (which a rigid flange would, causing wear and a bent rod).

**C1.** Static (breakout), Coulomb (constant kinetic), viscous (grows with velocity). Static dominates at breakaway.

**C2.** At 5 mm/s: $70 + 50e^{-0.25} + 200(0.005) = 70 + 38.9 + 1 = 109.9$ N. At 50 mm/s: $70 + 50e^{-25} + 200(0.050) = 70 + 0 + 10 = 80$ N. Friction is *higher* at the slow speed — the Stribeck effect — which is why slow precise motion is hardest (stick-slip).

**C3.** Breakout force is the static friction that must be overcome to start motion. It sets the smallest force the machine can controllably apply (~120 N here) — below that, stick-slip prevents smooth application.

**C4.** A more detailed model can be stiffer, harder to solve, and more sensitive to parameter errors. The twin aims for *useful* accuracy — capturing stick-slip and guiding control — not perfect fidelity.

**D1.** A cylinder gives linear force and precise position hold over a finite stroke; a motor gives continuous rotation and rotary speed control. Neither can do the other's job.

**D2.** (a) cylinder, (b) motor, (c) cylinder, (d) motor.

**D3.** $\Delta P = 2\pi \times 8 / (6\times10^{-6} \times 0.9) = 9.3\times10^6$ Pa = 93 bar. Within 100 bar. ✓

**D4.** $Q = 60 \times 6/1000/0.92 = 0.39$ LPM. The pump's 10.67 LPM is far more than enough.

**E1.** Double-acting cylinder, 50 mm bore, 28 mm rod, 300 mm stroke, clevis/trunnion mount, ≥160 bar rating, nitrile seals, area ratio 1.46, buckling SF 5.0.

**E2.** The machine gained a complete, real, correctly-sized actuator. It advances Force-Controlled Interaction by giving the machine a sized force capacity with the headroom for gentle control, plus a realistic friction model that defines the smallest force it can controllably apply.

</details>

---

*Problem Set 07 — Version 0.1*
