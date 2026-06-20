# Lab 11 — Running the Integrated Digital Twin

**Module:** 11 — The Integrated Digital Twin
**Duration:** 120 minutes
**Pressure level:** Simulation-based (the twin runs on logged data)
**Capstone subsystem:** S6 (Digital twin) — the culmination
**Benchmark task:** Autonomous Manipulation (self-monitoring)

---

## Objective

Run the machine's complete digital twin. Assemble and step the integrated model, run it in synchronized replay against a logged task, detect and classify an injected fault from its residual signature, fit a model parameter to measured data, and read the monitoring dashboard. This is the lab where the twin — built across the whole curriculum — becomes a whole, vigilant, observable instrument.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *run one live twin that mirrors, monitors, and refines itself.*

Every module since Module 04 contributed a piece of the twin. This lab assembles them and runs the whole twin — the machine's self-awareness made real. By the end, you will have detected a fault the sensors alone could not see, and fitted the twin to reality.

---

## Safety

Fully simulation-based — no hazard.

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python (NumPy, SciPy, Matplotlib) | 1 | |
| Module 11 code | — | all five files |

---

## Part 1 — The assembled twin

Run the integrated twin and record its behavior.

```
python workcell_twin.py
```

| Quantity | Value |
|----------|-------|
| Measured states | |
| Inferred states | |
| Position after extend (mm) | |
| Force after extend (kN) | |

---

## Part 2 — Synchronized replay

Run the twin in replay against a logged cycle.

```
python twin_replay.py
```

| Quantity | Value |
|----------|-------|
| Samples replayed | |
| Position RMS residual (mm) | |
| Relative to stroke (%) | |
| Twin verdict | |

---

## Part 3 — Fault detection

Run the fault detector and record the classifications.

```
python fault_detection.py
```

| Injected signature | Classification |
|--------------------|----------------|
| Healthy | |
| Sensor drift | |
| Seal leak | |
| Valve hysteresis | |

Record whether trend detection flagged the slow drift.

---

## Part 4 — Parameter estimation

Run the parameter fit and record the residual shrinkage.

```
python parameter_estimation.py
```

| Quantity | Value |
|----------|-------|
| Friction guess / fitted / true | |
| Healthy residual before fit (mm) | |
| Healthy residual after fit (mm) | |
| Shrinkage factor | |

---

## Part 5 — The dashboard

Run the monitoring dashboard for the healthy and faulty cases.

```
python twin_dashboard.py --plot
```

| Case | Fault flags | Status |
|------|-------------|--------|
| Healthy | | |
| With injected drift | | |

---

## Lab Report

Use the five-part structure.

### 1. Observation
How did the twin track the real machine in replay? How did each fault appear in the residuals? How did fitting change the residual?

### 2. Measurement
The numbers: replay RMS residual, fault classifications, residual shrinkage from fitting, dashboard fault flags.

### 3. Engineering Interpretation
Why does a seal leak make pressure fall below predicted? Why does fitting sharpen fault detection? Why must the twin be synchronized for residuals to mean anything? Connect each to the lesson physics.

### 4. Machine Improvement
How does this complete the machine? It now has a live twin that monitors its health and catches faults before failure — state what the machine can now do that it could not when its models were scattered.

### 5. Digital Twin Improvement
This module *is* the twin's culmination. State what the integrated twin can do (mirror, monitor, classify faults, self-refine, display) and how it will oversee the autonomous demonstration of Module 12.

---

## Analysis questions

1. Why is the same `workcell_twin.py` a simulation in one use and a digital twin in another?
2. A fault is invisible to direct sensors but visible in the residual. Explain how.
3. Why does fitting the friction parameter shrink the healthy residual by ~18×, and why does that matter?
4. How would the machine distinguish "the machine is aging (update the twin)" from "the machine is faulty (raise a flag)"?

---

## Deliverables

- [ ] Part 1 assembled twin
- [ ] Part 2 replay comparison
- [ ] Part 3 fault classifications
- [ ] Part 4 parameter fit
- [ ] Part 5 dashboard
- [ ] Five-part lab report
- [ ] Analysis answers (1–4)

---

## Machine capability check

> **What did the machine gain in Module 11?**

> **How did this lab advance Autonomous Manipulation's self-monitoring?**

> **Why is the integrated twin the culmination of the digital-twin thread?**

---

*Lab 11 — Version 0.1 | Pairs with Lessons 01–04. The twin made whole, vigilant, and observable.*
