# Module 05 — Knowledge Check

*Powering the Smart Agricultural Workcell*

Attempt all before checking the key. Target: 8 of 10.

> Keep asking: what can the machine *do* now that it could not before?

---

## Conceptual

**Q1.** Why can the machine not operate at all before Module 05?

**Q2.** Does a pump create flow or pressure? What creates the other?

**Q3.** Why must the machine's pump be positive-displacement?

**Q4.** State the pump-selection principle in one sentence (it is not "pick the best pump").

**Q5.** Why must the machine's motor be sized larger than the hydraulic power it delivers?

---

## Calculation

**Q6.** The machine's pump is 8 cc/rev at 1450 RPM, 0.92 volumetric efficiency. Actual flow?

**Q7.** At 10.67 LPM and 100 bar, what hydraulic power does the machine deliver?

**Q8.** With overall efficiency 0.83, what shaft power must the motor supply for Q7?

**Q9.** Size the machine's reservoir (4× rule) and relief valve (1.15×) at 10.67 LPM / 100 bar.

---

## The machine

**Q10.** State the Module 05 Machine Capability Added, Benchmark Task Advanced, and Digital Twin Contribution (one sentence each).

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** It has no source of hydraulic power — nothing makes its fluid flow, so no motion, force, or task is possible.

**A2.** A pump creates flow. Pressure is created by the resistance the flow meets (the load and the relief setting).

**A3.** Only positive-displacement pumps trap and force discrete fluid volumes, building the high pressures (100 bar+) hydraulics require; centrifugal pumps cannot.

**A4.** The machine picks the pump whose strengths match its mission, not the most capable pump available.

**A5.** Because losses (leakage and friction) mean the motor must supply more than the hydraulic power delivered; shaft power = hydraulic power / overall efficiency.

**A6.** $8 \times 1450/1000 \times 0.92 = 10.67$ LPM.

**A7.** $100 \times 10.67/600 = 1.78$ kW.

**A8.** $1.78/0.83 = 2.15$ kW.

**A9.** Reservoir $= 4 \times 10.67 = 43$ L → standard 40 L. Relief $= 100 \times 1.15 = 115$ bar.

**A10.** Capability: the machine can now generate hydraulic power from a complete HPU. Benchmark: Precision Positioning advanced from impossible to powered — the machine has flow and can compute the cylinder velocity it produces. Twin: a full pump-and-power model (flow, efficiency, power, curves) was added, predicting the machine's real performance.

**Scoring:** 8–10 → ready for Module 06. 5–7 → review Lessons 03 and 04. Below 5 → rework the module.

</details>

---

*Knowledge Check 05 — Version 0.1*
