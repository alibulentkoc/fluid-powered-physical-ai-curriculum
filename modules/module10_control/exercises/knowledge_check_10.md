# Module 10 — Knowledge Check

*Embedded Control — The Machine Decides and Acts*

Attempt all before checking the key. Target: 8 of 10.

---

## Conceptual

**Q1.** Why is the closed loop the machine's shift from executing commands to pursuing goals?

**Q2.** Which PID term eliminates steady-state error?

**Q3.** Why does the machine tune its PID in the digital twin before hardware?

**Q4.** Why does the safety logic have priority over the task logic?

**Q5.** What does the predicted-vs-actual comparison validate?

---

## Calculation

**Q6.** Proportional control ($K_p=0.02$) holding a load needing $u=0.06$ — steady-state error?

**Q7.** If $K_p$ is raised to 0.05 for the same hold, what is the new steady-state error?

**Q8.** The tuned controller predicts what overshoot and steady-state error?

**Q9.** Watchdog timeout 200 ms; communication lost for 300 ms. What does the machine do?

---

## The machine

**Q10.** State the Module 10 Machine Capability Added, Benchmark Task Advanced, and Digital Twin Contribution (one sentence each).

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** Open-loop, the machine executes a command and accepts whatever happens; closed-loop, it continuously acts to *achieve* a target, correcting for disturbances — pursuing a goal.

**A2.** The integral term.

**A3.** The twin models the real nonlinear behavior, so the machine can predict how a tuning behaves across conditions safely in software, before risking hardware.

**A4.** Because no task objective is worth damaging the machine or harming people; safety must be able to override any task action.

**A5.** That the twin accurately predicts the real closed-loop behavior — validating both the twin (for control design) and the controller.

**A6.** $0.06/0.02 = 3$ mm.

**A7.** $0.06/0.05 = 1.2$ mm (smaller, but higher gain risks overshoot).

**A8.** ~0.6% overshoot, ~1.2 mm steady-state error.

**A9.** The watchdog fires (300 > 200 ms); the machine (Arduino) forces a safe state independently of the Pi.

**A10.** Capability: a validated control brain (closed-loop, precise, autonomous, safe). Benchmark: Precision Positioning complete (<5% overshoot, <2 mm error, validated). Twin: became a control-design environment, predicting and validating controlled behavior.

**Scoring:** 8–10 → ready for Module 11. 5–7 → review Lessons 02 and 04. Below 5 → rework.

</details>

---

*Knowledge Check 10 — Version 0.1*
