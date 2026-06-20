# Lab 09 — Perceiving and Logging a Task Cycle

**Module:** 09 — Sensing (the machine perceives)
**Duration:** 120 minutes
**Pressure level:** Simulation-based, with optional sensor hardware
**Capstone subsystem:** S5 (Sensing) + S6 (Digital twin)
**Benchmark task:** Autonomous Manipulation

---

## Objective

Give the machine its senses. Read and convert sensor signals, filter the noise, detect a hidden fault from a flow residual, and log a complete task cycle to compare against the digital twin. This is the lab where the physical machine first connects to its digital model.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *perceive its own state and check itself against its twin.*

Every prior module built the physical machine. This lab gives it perception — and, crucially, connects that perception to the digital twin. By the end, you will have validated the twin against logged sensor data, the foundation of all the machine's self-monitoring.

---

## Safety

Core lab is simulation-based. The optional hardware extension uses low-voltage sensors (no hydraulic pressure required for the electronics).

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python | 1 | |
| Module 09 code | — | all four files |
| Optional: pressure transducer, pot, load cell, Arduino | 1 set | hardware extension |

---

## Part 1 — Reading the senses

Run the sensor models and record the machine's perceptions.

```
python sensor_models.py
```

| Sensor reading | Value |
|----------------|-------|
| 13.5 mA bore pressure | |
| Cylinder force (93.5 bore, 3 rod) | |
| 0 mA signal | |
| Load cell grip (raw 1150, tared at 1050) | |

---

## Part 2 — Cleaning the senses

Run the filter models. Record the noise-vs-lag tradeoff.

```
python signal_filters.py
```

| Filter | Noise factor | Lag (ms) |
|--------|--------------|----------|
| MA(4) | | |
| MA(9) | | |
| MA(25) | | |

Record the noise reduction achieved by MA(4) and exp(0.4) on the held-still signal.

---

## Part 3 — Detecting the invisible

Run the flow-sensing diagnosis. Record the pump-health trend.

```
python flow_sensing.py
```

| Week | Flow (LPM) | Leak (LPM) | Status |
|------|-----------|------------|--------|
| 1 | | | |
| 4 | | | |
| 8 | | | |
| 12 | | | |

Record the predicted weeks-to-failure.

---

## Part 4 — Logging and the twin

Run the data logger and record the twin comparison.

```
python data_logger.py
```

| Quantity | Value |
|----------|-------|
| Samples logged | |
| Position RMS residual (mm) | |
| Relative to range (%) | |
| Twin verdict | |

---

## Lab Report

Use the five-part structure.

### 1. Observation
What did the machine perceive across the task cycle? How did the raw and filtered signals differ? How did the flow residual reveal the hidden pump wear?

### 2. Measurement
The numbers: sensor conversions, filter noise/lag, the leakage trend, the twin residual.

### 3. Engineering Interpretation
Why does the 4–20 mA signal detect a broken wire for free? Why does heavier filtering add lag? Why does the flow residual reveal what no single sensor sees? Connect each to the lesson physics.

### 4. Machine Improvement
How does this improve the machine? It can now perceive its state, diagnose hidden faults, and check itself against its twin — state what the machine can now do that it could not when blind.

### 5. Digital Twin Improvement
The logged comparison connects the physical machine to the twin. State what the twin gained (validation against reality, the residual mechanism) and how a departing residual would be used (fault detection or model refinement).

---

## Analysis questions

1. The machine senses force two ways (differential pressure and load cell). Why is this redundancy valuable?
2. Why can't the machine simply filter as heavily as possible to remove all noise?
3. The flow residual grew slowly over weeks. How does this enable predictive (not reactive) maintenance?
4. A large twin residual could mean a machine fault *or* a twin error. How would you distinguish them?

---

## Deliverables

- [ ] Part 1 sensor readings
- [ ] Part 2 filter tradeoff table
- [ ] Part 3 pump-health trend
- [ ] Part 4 twin comparison
- [ ] Five-part lab report
- [ ] Analysis answers (1–4)

---

## Machine capability check

> **What did the machine gain in Module 09?**

> **How did this lab advance Autonomous Manipulation?**

> **What did the logged comparison do for the digital twin?**

---

## Optional hardware extension

Wire a pressure transducer (or potentiometer as a stand-in), a position pot, and a load cell to an Arduino. Read them, apply an exponential filter, and stream over serial to a Python logger that writes CSV. If a low-pressure rig is available, log a real motion and compare to the twin's prediction — the physical machine and its digital model meeting in real data.

---

*Lab 09 — Version 0.1 | Pairs with Lessons 01–04. The machine perceives and checks its twin.*
