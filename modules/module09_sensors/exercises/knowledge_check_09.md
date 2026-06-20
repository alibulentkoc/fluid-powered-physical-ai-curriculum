# Module 09 — Knowledge Check

*Sensing — The Machine Perceives*

Attempt all before checking the key. Target: 8 of 10.

---

## Conceptual

**Q1.** Why is sensing the foundation of the machine's intelligence?

**Q2.** How does the machine compute force without a force sensor on the cylinder?

**Q3.** What is the fundamental tradeoff every filter makes?

**Q4.** What is a residual, and why does it need the digital twin?

**Q5.** Why is the logged comparison the digital twin's "moment of truth"?

---

## Calculation

**Q6.** Bore transducer 13.5 mA, rod 4.2 mA (range 0–160 bar). Pressures and cylinder force?

**Q7.** A moving average of N=4 at 10 ms: noise factor and lag?

**Q8.** Turbine meter K=0.5, reads 18.0 Hz. Flow and leakage residual (vs 10.67)?

**Q9.** Position RMS residual 0.87 mm over 150 mm. Twin verdict?

---

## The machine

**Q10.** State the Module 09 Machine Capability Added, Benchmark Task Advanced, and Digital Twin Contribution (one sentence each).

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** The machine cannot decide, control, or self-monitor without first perceiving its state; sensing (the SENSE stage) supplies the feedback all intelligence acts on.

**A2.** From differential pressure: $F = P_{bore}A_{bore} - P_{rod}A_{rod}$ — the two pressures and the areas give the force directly.

**A3.** Noise reduction vs. lag: more smoothing means cleaner signal but more lag (slower/unstable control); less means responsive but noisy.

**A4.** The difference between measured and expected (twin-predicted) value; it needs the twin to supply the expectation that makes a measurement meaningful.

**A5.** It is the first time the twin's predictions are checked against real sensor data, validating it as a faithful model (or revealing where to refine it).

**A6.** Bore 95 bar, rod 2.0 bar; force $= (95 \times 1963 - 2.0 \times 1348) \times 0.1 = 18.38$ kN.

**A7.** Noise $\times 1/\sqrt{4} = 0.5$; lag $= (4-1)/2 \times 10 = 15$ ms.

**A8.** $Q = 0.5 \times 18.0 = 9.0$ LPM; residual $= 10.67 - 9.0 = 1.67$ LPM (15.6%).

**A9.** 0.6% of stroke — excellent; the twin is a faithful mirror and the machine is healthy.

**A10.** Capability: perception (sense state, clean, diagnose, log, connect to twin). Benchmark: Autonomous Manipulation began — the machine can perceive its state. Twin: connected to reality via sensor data (residual + logged comparison), validated and refinable.

**Scoring:** 8–10 → ready for Module 10. 5–7 → review Lessons 03 and 04. Below 5 → rework.

</details>

---

*Knowledge Check 09 — Version 0.1*
