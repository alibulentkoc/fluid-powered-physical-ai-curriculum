# Lab 05 — Hydraulic Power Unit Investigation

**Module:** 05 — Powering the Smart Agricultural Workcell
**Duration:** 90 minutes
**Pressure level:** Simulation-based, with optional low-pressure hardware
**Capstone subsystem:** S1 (Hydraulic power) + S6 (Digital twin)
**Benchmark task:** Precision Positioning

---

## Objective

Investigate the machine's power source: measure (or simulate) its flow, estimate its efficiency, and compare theory against reality. This lab turns the HPU design from Lesson 04 into measured numbers and feeds those numbers back into the digital twin.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *generate power* — and this lab confirms how much.

The machine's HPU design predicts 10.67 LPM and 0.83 overall efficiency. But predictions must be checked against reality, because the machine's real flow and efficiency determine its real speed and the real motor load. This lab is where the machine's power source proves itself — and where the digital twin learns the machine's *actual* parameters, not just its designed ones.

---

## Safety

Core lab is simulation-based (no hazard). For the optional hardware extension, follow all low-pressure safety rules (≤3.5 bar, safety glasses, no loose lines under pressure).

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python (NumPy, Matplotlib) | 1 | |
| `pump_performance_model.py` | — | the machine's pump model |
| Optional: bench HPU with flow meter | 1 | for the hardware extension |
| Optional: pressure gauge, tachometer | 1 each | to measure operating point |

---

## Part 1 — Predict the machine's performance

Run the pump model to establish the machine's predicted power characteristics.

```
python pump_performance_model.py --plot
```

Record the predicted values and examine the performance curves.

| Predicted quantity | Value |
|--------------------|-------|
| Actual flow at 100 bar (LPM) | |
| Hydraulic power at 100 bar (kW) | |
| Overall efficiency | |
| Shaft power required (kW) | |
| Cylinder velocity at 1450 RPM (mm/s) | |

---

## Part 2 — Measure (or simulate measurement of) the real machine

If a bench HPU is available, measure flow at the outlet with a flow meter at a known pressure and speed. If not, simulate "measured" values by applying a realistic perturbation to the model (e.g., a worn pump with volumetric efficiency reduced to 0.86) and treat those as the measured machine.

| Measured quantity | Value |
|-------------------|-------|
| Motor speed (RPM) | |
| Operating pressure (bar) | |
| Measured flow (LPM) | |
| Implied volumetric efficiency (measured flow / theoretical) | |

---

## Part 3 — Theory vs. reality

Compare predicted and measured. Compute the discrepancy.

| Quantity | Predicted | Measured | Difference (%) |
|----------|-----------|----------|----------------|
| Flow (LPM) | | | |
| Volumetric efficiency | | | |
| Cylinder velocity (mm/s) | | | |

---

## Lab Report

Use the five-part structure. The last two parts are the point.

### 1. Observation
What did you see? Describe the machine's behavior — did the real (or perturbed) flow match the prediction? Was it higher or lower?

### 2. Measurement
The numbers: predicted vs. measured flow, efficiency, and the resulting cylinder velocity, with the percentage discrepancy.

### 3. Engineering Interpretation
Why is the measured flow different from the predicted? (Leakage, wear, temperature/viscosity effects on volumetric efficiency.) Connect the discrepancy to the physics from Lesson 03.

### 4. Machine Improvement
How does this improve the Smart Agricultural Workcell? You now know the machine's *real* flow and efficiency, so you can predict its *real* cylinder speed — the basis of Precision Positioning. State what the machine can now do or predict that it could not before this measurement.

### 5. Digital Twin Improvement
What does the twin gain? The measured volumetric efficiency replaces the assumed value in `pump_performance_model.py`, so the twin now predicts the machine's real flow. State how you would update the twin and what new prediction becomes trustworthy. If the measured efficiency were far below prediction, what fault would the twin's residual reveal?

---

## Analysis questions

1. Was the measured flow higher or lower than predicted? Why is lower the expected direction?
2. A 5% flow error becomes a 5% cylinder-velocity error. Why does that matter for Precision Positioning?
3. If the machine's volumetric efficiency has dropped over time, what does that tell you about the pump's condition?
4. How would you use the digital twin to detect a slowly failing pump *before* it fails completely? (Hint: track the flow residual over time.)

---

## Deliverables

- [ ] Part 1 predicted performance table
- [ ] Part 2 measured (or simulated-measured) table
- [ ] Part 3 theory-vs-reality comparison
- [ ] Five-part lab report (Observation → Measurement → Interpretation → Machine Improvement → Digital Twin Improvement)
- [ ] Analysis answers (1–4)

---

## Machine capability check

Answer in one or two sentences each:

> **What capability did the machine gain in Module 05?**

> **How did this lab advance Precision Positioning?**

> **What did this lab add to the digital twin's accuracy?**

---

*Lab 05 — Version 0.1 | Pairs with Lessons 03–04. Confirms the machine's power source and calibrates the twin's pump model.*
