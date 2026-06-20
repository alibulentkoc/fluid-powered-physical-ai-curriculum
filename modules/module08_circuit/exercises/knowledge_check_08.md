# Module 08 — Knowledge Check

*Integrating the Machine's Hydraulic Circuit*

Attempt all before checking the key. Target: 8 of 10.

---

## Conceptual

**Q1.** Why is a collection of correct subsystems not yet a machine?

**Q2.** What does the DCV center condition govern for the whole machine?

**Q3.** Why does the machine sequence its actuators rather than run them in parallel?

**Q4.** How does the machine hold a load safely during a power loss?

**Q5.** Why must the subsystem models be simulated *together*?

---

## Calculation

**Q6.** Pressure reaching the cylinder (100 bar pump; drops 0.54 + 1.0 + 5.0 bar)? Force available?

**Q7.** Closed-center vs. open-center idle power (115 bar relief, 5 bar drop, 10.67 LPM)?

**Q8.** Pick-and-place cycle time (position 1.66 s, grip 0.5 s, move 1.14 s, release 0.5 s, 4×0.2 s transitions)?

**Q9.** Useful work vs. hold heat per cycle (800 N, 150 mm ×2; 2.04 kW × 1.0 s hold)?

---

## The machine

**Q10.** State the Module 08 Machine Capability Added, Benchmark Task Advanced, and Digital Twin Contribution (one sentence each).

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** A machine is its subsystems *connected into one circuit* with an unbroken fluid path; separate correct parts cannot run as a whole.

**A2.** The idle energy behavior: closed-center locks the cylinder but dumps full power as heat; open-center is efficient at idle but does not lock the cylinder.

**A3.** One pump shared in parallel makes each actuator's speed depend on the other's load (unpredictable); sequencing gives full flow and known speed to one at a time.

**A4.** Spring-centered DCV closes (locks ports), pilot-operated check valves block the leak path so the trapped fluid holds the load, port reliefs cap any spike — all passive, no power needed.

**A5.** Coupled models reveal system behaviors (hold-dominated heat, startup transient, area asymmetry over a cycle) that individual models hide; integration validates the machine as a system.

**A6.** $100 - 0.54 - 1.0 - 5.0 = 93.5$ bar; force $93.5 \times 0.1 \times 1963 = 18.35$ kN.

**A7.** Closed: 2.05 kW. Open: 0.09 kW.

**A8.** $1.66 + 0.5 + 1.14 + 0.5 + 0.8 = 4.6$ s (~13 cycles/min).

**A9.** Useful $800 \times 0.15 \times 2 = 240$ J; hold heat $2040 \times 1.0 = 2040$ J.

**A10.** Capability: the machine became one complete, integrated, fail-safe system, validated end to end. Benchmark: Precision Positioning is complete as a physical capability (full actuation path validated). Twin: the integrated full-task simulation (all models coupled, full cycle, energy budget).

**Scoring:** 8–10 → ready for Module 09. 5–7 → review Lessons 01 and 04. Below 5 → rework.

</details>

---

*Knowledge Check 08 — Version 0.1*
