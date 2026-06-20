# Lab 08 — Running the Machine's Full Task Cycle

**Module:** 08 — Integrating the Machine's Hydraulic Circuit
**Duration:** 120 minutes
**Pressure level:** Simulation-based (the integrated machine)
**Capstone subsystem:** All physical subsystems (S1–S4) + S6 (Digital twin)
**Benchmark task:** Precision Positioning

---

## Objective

Run the machine's complete task cycle in the integrated simulation — startup → extend → hold → retract → stop — combining the pump, valve, and cylinder models into one system. Read the four-panel behavior plot, account for the machine's energy, and confirm the integrated machine works as a whole. This is the lab where the physical machine runs end to end for the first time.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *run a complete task as one integrated system.*

Every prior module built or characterized a piece. This lab runs them all together. By the end, you will have validated that the machine's subsystems work as a coupled whole, and you will have the integrated simulation that the digital twin (Modules 10–11) builds on.

---

## Safety

Fully simulation-based — no hazard.

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python (NumPy, Matplotlib) | 1 | |
| Module 08 code | — | `integrated_simulation.py`, `circuit_model.py`, `task_sequencer.py`, `circuit_protection.py` |

---

## Part 1 — The integrated circuit

Run the circuit model and record the integrated machine's key figures.

```
python circuit_model.py
```

| Quantity | Value |
|----------|-------|
| Pressure reaching cylinder (bar) | |
| Force available (kN) | |
| Idle power, closed-center (kW) | |
| Idle power, open-center (kW) | |

---

## Part 2 — The full task cycle

Run the integrated simulation with plotting.

```
python integrated_simulation.py --plot
```

Examine the four-panel plot (position, pressure, flow, force vs. time) and record:

| Cycle feature | Value |
|---------------|-------|
| Total cycle time (s) | |
| Extend velocity (mm/s) | |
| Retract velocity (mm/s) | |
| Hold pressure (bar) | |
| Peak force (kN) | |

Sketch or describe each of the four signals across the five phases (startup, extend, hold, retract, stop).

---

## Part 3 — The energy budget

From the simulation and the energy model, account for the machine's per-cycle energy.

| Energy term | Value (J) | % of cycle |
|-------------|-----------|------------|
| Useful work | | |
| Hold heat | | |
| Motion heat | | |
| **Total** | | |

Then compute the average heat load at 13 cycles/minute, and judge whether the 40 L reservoir suffices.

---

## Lab Report

Use the five-part structure.

### 1. Observation
What did the integrated machine do across the full cycle? How did the four signals behave through the five phases?

### 2. Measurement
The numbers: cycle time, velocities, pressures, forces, and the energy budget.

### 3. Engineering Interpretation
Why does the pressure jump during the hold? Why is the retract faster than the extend? Why does the hold dominate the energy budget? Connect each to the subsystem physics (Modules 05–07).

### 4. Machine Improvement
How does this complete the machine? The integrated simulation validates that all subsystems work together — state what the machine can now do (run a full task as one system) that it could not when the subsystems were separate.

### 5. Digital Twin Improvement
The integrated simulation *is* the digital twin executing a full task. State how it will be used in Modules 10–11 (closed-loop control, fault detection), and how comparing its prediction to a real machine would reveal faults.

---

## Analysis questions

1. The useful work is ~7% of the per-cycle energy. Where does the rest go, and which phase dominates?
2. Why does the integrated simulation reveal behaviors that the individual subsystem models could not?
3. At continuous high duty (18 cycles/min, 1.5 s holds), would the machine need a cooler? Estimate the heat load.
4. How would the digital twin use this integrated simulation to detect a developing fault (e.g., a worn pump or a sticking valve)?

---

## Deliverables

- [ ] Part 1 integrated circuit figures
- [ ] Part 2 full-cycle features + signal sketches
- [ ] Part 3 energy budget
- [ ] Five-part lab report
- [ ] Analysis answers (1–4)

---

## Machine capability check

> **What did the machine become in Module 08?**

> **How did this lab complete Precision Positioning as a physical capability?**

> **What is the integrated simulation's role in the digital twin going forward?**

---

*Lab 08 — Version 0.1 | Pairs with Lessons 01–04. The physical machine, run end to end.*
