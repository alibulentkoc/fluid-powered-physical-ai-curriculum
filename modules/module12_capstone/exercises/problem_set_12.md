# Module 12 — Problem Set

*The Complete Autonomous Workcell — The Capstone*

Work each by hand or with the Module 12 code. All answers verified against the curriculum code.

> Every problem completes the machine as a **demonstrated, validated, documented system** — the capstone of the curriculum.

---

## Section A — Commissioning

**A1.** Why is a machine not just its subsystems tested in isolation?

**A2.** State the workcell's commissioning order and why each step depends on the prior.

**A3.** How does ordered commissioning isolate a fault?

**A4.** What milestone confirms the machine is commissioned?

---

## Section B — Integration

**B1.** Why might simulation-tuned control need refinement on hardware?

**B2.** Why is hardware tuning a *refinement* rather than a blind search?

**B3.** What two conditions define the integration milestone?

**B4.** How does the live twin differ from replay mode?

---

## Section C — Demonstration and validation

**C1.** What are the two demonstration tasks, and what does each prove?

**C2.** Name the seven capstone specifications and their targets.

**C3.** In the demonstration, what is the measured position mean error, and does it meet spec?

**C4.** What should the machine do if it misses a specification?

---

## Section D — Documentation and reflection

**D1.** Why is a working but undocumented machine not a complete deliverable?

**D2.** Name the seven documentation deliverables.

**D3.** What three questions does the critical reflection answer?

**D4.** Why is the workcell described as a *platform* rather than an endpoint?

---

## Section E — The complete machine

**E1.** State what the Demonstration System artifact comprises.

**E2.** *Reflection:* In three sentences, summarize the machine's journey from Module 01 to Module 12 — what was built, and what it became.

---

## Solutions

<details>
<summary>Reveal (verified against Module 12 code)</summary>

**A1.** A machine is its subsystems running together, commissioned and confirmed as one; integration always surprises (noise, dead-band, wiring) that isolated testing cannot reveal.

**A2.** Power → transport → motion → actuation → sensing → control+twin. Each depends on the prior: power enables everything, motion needs power, sensing observes motion, control acts on sensing — so each is confirmed on a foundation of confirmed subsystems.

**A3.** The first failing test localizes the fault to that subsystem, because all prior subsystems are already confirmed.

**A4.** All subsystems operational; basic open-loop command and sensor readback confirmed.

**B1.** Real hardware has unmodeled effects (valve dead-band, friction, sensor noise) that can make the simulated tuning overshoot or settle off-target.

**B2.** The simulation got the machine close, so only a small adjustment (guided by the real symptoms) is needed — fast and safe, not a blind search.

**B3.** The position step meets spec on hardware, and the task sequence completes without fault, repeatedly.

**B4.** The live twin steps in lockstep with the running machine, fed the real-time sensor stream, predicting and computing residuals as the machine operates (replay runs on logged data after the fact).

**C1.** Precision Positioning (proves accuracy) and Grasping and Handling (proves autonomous manipulation, including force-controlled gripping).

**C2.** Overshoot <5%, settling <3 s, SSE <2 mm, grasp success ≥4/5, placement ±10 mm, twin RMS <5 mm, fault detection ≥80%.

**C3.** Mean error ~0.3 mm — meets the <2 mm spec.

**C4.** Document why it was missed and describe how it would be addressed — honest engineering.

**D1.** Its knowledge is trapped; others cannot understand, reproduce, maintain, or extend it, so it is a one-off, not a transferable deliverable.

**D2.** Hydraulic schematic, wiring diagram, code repository, digital twin, validation report, final report, demonstration video.

**D3.** What worked and why; what would be done differently; what the platform enables.

**D4.** It is a working intelligent machine that enables further work — camera guidance, learned control, multi-actuator coordination, field deployment — not an endpoint.

**E1.** The complete Smart Agricultural Workcell: commissioned, integrated, demonstrated and validated against all seven specifications, and fully documented with critical reflection.

**E2.** Beginning with Pascal's Law (Module 01), the machine was built piece by piece — power, fluid, mechanics, pumps, valves, actuators, the integrated circuit (02–08) — then given perception (09), control (10), and a digital twin (11). In Module 12 it was commissioned, integrated, demonstrated against every specification, and documented. It became a complete, intelligent, fluid-powered machine that senses, decides, acts, and watches over itself — proven by measurement.

</details>

---

*Problem Set 12 — Version 0.1*
