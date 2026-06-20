# Module 12 — Knowledge Check

*The Complete Autonomous Workcell — The Capstone*

Attempt all before checking the key. Target: 8 of 10.

---

## Conceptual

**Q1.** Why is commissioning done in dependency order?

**Q2.** Why does simulation-first control make hardware integration fast and safe?

**Q3.** Why is a demonstrated machine proven by measurement, not by claims?

**Q4.** Why must the machine honestly document any missed specification?

**Q5.** Why is documentation half the engineering deliverable?

---

## Applied

**Q6.** During commissioning, sensing fails but power/transport/motion/actuation passed. Where is the fault?

**Q7.** The capstone demonstration: what is the position mean error and does it meet the <2 mm spec?

**Q8.** Grasp success is 4/5 — does this meet the spec? What does one failure (grip slip) within ±10 mm placement tell you?

**Q9.** The twin's position RMS residual during the demo is ~0.3 mm. Does it meet the <5 mm spec, and what does that confirm?

---

## The complete machine

**Q10.** State the Module 12 Machine Capability Added, Benchmark Tasks demonstrated, and Digital Twin Contribution (one sentence each).

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** So each subsystem is confirmed on a foundation of confirmed ones, keeping the machine safe during bring-up and localizing any fault to the subsystem being activated.

**A2.** The twin predicts the real behavior, so the machine arrives at hardware with gains already close — needing only a small refinement, not a risky blind search.

**A3.** Capabilities are not performance; only running the tasks and measuring against defined specs proves the machine actually works.

**A4.** Engineering integrity requires proof of shortfalls and a credible plan to address them — not quietly relaxing the spec.

**A5.** A working but undocumented machine cannot be understood, reproduced, maintained, or extended by others — documentation makes it a transferable, lasting deliverable.

**A6.** In sensing — the first failing test, with all prior subsystems confirmed, isolates the fault there.

**A7.** ~0.3 mm — yes, well under the 2 mm spec.

**A8.** Yes, 4/5 meets ≥4/5. The one failure was a grip slip (not a placement error), showing a robustness limit in gripping smooth objects — a documented weakness to address with tactile feedback.

**A9.** Yes (0.3 < 5 mm); it confirms the twin mirrors the real machine even during real autonomous tasks.

**A10.** Capability: a complete, demonstrated, validated, documented Fluid-Powered Physical AI system. Benchmarks: all three (Precision Positioning, Force-Controlled Interaction, Autonomous Manipulation) demonstrated and validated. Twin: ran in parallel during real tasks, validated (RMS ~0.3 mm) and proven as a fault detector (10/10).

**Scoring:** 8–10 → curriculum complete, mastery demonstrated. 5–7 → review Lessons 03 and 04. Below 5 → revisit the capstone.

</details>

---

*Knowledge Check 12 — Version 0.1 | The final knowledge check of the curriculum.*
