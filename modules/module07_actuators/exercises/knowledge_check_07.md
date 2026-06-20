# Module 07 — Knowledge Check

*Producing the Machine's Force and Motion*

Attempt all before checking the key. Target: 8 of 10.

> Keep asking: what can the machine *do* now that it could not before?

---

## Conceptual

**Q1.** What is the machine's core force relationship, and what reduces usable force below it?

**Q2.** Why is the machine's bore far larger than the minimum its tasks require?

**Q3.** Why is buckling a separate failure mode from the force rating?

**Q4.** What causes stick-slip, and why does it afflict the slow precise approach?

**Q5.** State the actuator-type selection principle in one sentence.

---

## Calculation

**Q6.** Extend and retract force for the workcell cylinder at 100 bar (50 mm bore, 28 mm rod)?

**Q7.** What pressure produces a 1.5 kN gripping force?

**Q8.** Euler buckling load for the 28 mm rod at 300 mm stroke (eff. length 400 mm, K=2.0). Safe vs. 19.63 kN?

**Q9.** Friction at 5 mm/s vs. 50 mm/s (Fs=120, Fc=70, vs=10, b=200). Which is higher?

---

## The machine

**Q10.** State the Module 07 Machine Capability Added, Benchmark Task Advanced, and Digital Twin Contribution (one sentence each).

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** $F = P \cdot A$; back-pressure (on the rod side) and friction reduce the usable force below it.

**A2.** Bore is sized by more than force — stiffness, standard sizes, future margin, and flow/speed compatibility push it larger; the headroom also enables gentle control.

**A3.** A rod rated for the force can still buckle as a column if too thin for the stroke. Buckling depends on rod diameter and effective length, not the pressure rating.

**A4.** The Stribeck dip: high static friction at rest, lower kinetic once moving. At low speed the cylinder sticks, builds pressure, slips, overshoots, sticks again — jerky motion exactly where smoothness is wanted.

**A5.** Match the actuator type to the task's motion requirements — cylinder for linear/holdable, motor for rotary/continuous.

**A6.** Extend 19.63 kN, retract 13.48 kN.

**A7.** $1500/(1963 \times 0.1) = 7.6$ bar.

**A8.** $F_{cr} = 98$ kN; safety factor 5.0 — safe.

**A9.** 5 mm/s: 109.9 N. 50 mm/s: 80 N. Friction is higher at the slow speed (Stribeck).

**A10.** Capability: a complete, real, correctly-sized actuator. Benchmark: Force-Controlled Interaction advanced — sized force with gentle-control headroom and a realistic friction floor. Twin: the full actuation subsystem (force, structural params, real friction/cushioning, actuator-type logic) added.

**Scoring:** 8–10 → ready for Module 08. 5–7 → review Lessons 01 and 03. Below 5 → rework.

</details>

---

*Knowledge Check 07 — Version 0.1*
