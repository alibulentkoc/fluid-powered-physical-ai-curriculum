# Module 11 — Knowledge Check

*The Integrated Digital Twin*

Attempt all before checking the key. Target: 8 of 10.

---

## Conceptual

**Q1.** What makes a model a digital twin rather than a simulation?

**Q2.** Why must the twin infer some states rather than measure them?

**Q3.** What is a fault's "residual signature," and why does it enable classification?

**Q4.** Why does fitting parameters sharpen fault detection?

**Q5.** Why must the twin's vigilance be shown on a dashboard?

---

## Applied

**Q6.** A log at 200 Hz, twin at 100 Hz — what must happen before comparison?

**Q7.** The pressure residual ramps steadily negative; position and force are normal. What fault?

**Q8.** Healthy residual is 3 mm; a fault adds 1.5 mm. After fitting, healthy residual drops to 0.6 mm. Is the fault now detectable? Why?

**Q9.** Replaying a logged cycle gives a position RMS residual of 0.2% of stroke. Twin verdict?

---

## The machine

**Q10.** State the Module 11 Machine Capability Added, Benchmark Task Advanced, and Digital Twin Contribution (one sentence each).

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** Synchronization with a specific real machine — fed its real inputs, continuously compared to its real outputs.

**A2.** Some states (friction, dead-band, leakage) have no sensor; the twin estimates them from measured states and the model.

**A3.** The characteristic pattern its residual makes (steady ramp, linear drift, asymmetry); the pattern names the fault, enabling diagnosis not just alarm.

**A4.** It shrinks the healthy residual toward noise, so small faults stand above it instead of hiding beneath a parameter-error residual.

**A5.** Residuals and flags in code help no operator; a dashboard surfaces the twin's vigilance so a human can read the machine's health at a glance.

**A6.** Resample onto a common time grid (and align the clocks) so the points correspond.

**A7.** A cylinder seal leak (pressure falls below predicted; position/force normal rules out mechanical/sensor faults).

**A8.** Yes — the 1.5 mm fault was hidden beneath the 3 mm healthy residual but stands clearly above the 0.6 mm fitted residual.

**A9.** Synchronized — a faithful mirror (residual far below the typical threshold).

**A10.** Capability: a complete integrated digital twin (mirrors, monitors, self-refines, displays). Benchmark: Autonomous Manipulation gains its self-monitoring foundation. Twin: the culmination — assembled, synchronized, vigilant, observable.

**Scoring:** 8–10 → ready for Module 12. 5–7 → review Lessons 03 and 04. Below 5 → rework.

</details>

---

*Knowledge Check 11 — Version 0.1*
