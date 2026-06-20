# Lab 12 — The Complete Capstone Demonstration

**Module:** 12 — The Complete Autonomous Workcell (CAPSTONE)
**Duration:** Project sprint (the culminating lab)
**Pressure level:** Full system — simulation-validated, hardware-demonstrated
**Capstone subsystems:** All six
**Benchmark tasks:** All three

---

## Objective

Demonstrate and validate the complete Smart Agricultural Workcell. Commission the machine in order, close every loop, perform both autonomous benchmark tasks with the digital twin running in parallel, and validate the measured performance against all seven capstone specifications. This is the culminating lab of the entire curriculum — the machine proven, as a complete Fluid-Powered Physical AI system.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *operate as one complete, demonstrated, validated, intelligent system.*

Every module built a piece. This lab runs the whole machine and proves it works — by measurement, against defined specifications. By the end, you will have demonstrated an autonomous fluid-powered machine that senses, decides, acts, and watches over itself.

---

## Safety

Simulation-validated throughout; hardware demonstration (if available) requires all safety logic active (limits, watchdog) and the full integration checklist confirmed.

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python (NumPy, SciPy, Matplotlib) | 1 | |
| Module 12 code | — | all three files |
| Modules 10–11 code | — | imported by the demonstration |
| Optional: complete workcell rig | 1 | full hardware demonstration |

---

## Part 1 — Commissioning

Run the commissioning procedure for a working machine and a faulty one.

```
python commissioning.py
```

| Case | Result |
|------|--------|
| Fully working machine | |
| Machine with sensing fault | |

Confirm the fault is isolated to the correct subsystem.

---

## Part 2 — Integration

Run the integration milestone check.

```
python integration.py
```

| Metric | Value | Spec | Pass? |
|--------|-------|------|-------|
| Position overshoot | | <5% | |
| Steady-state error | | <2 mm | |
| Settling time | | <3 s | |
| Task sequence | | 5/5 | |
| Twin tracks live | | <5 mm | |
| **Integration milestone** | | | |

---

## Part 3 — The complete demonstration

Run the full capstone demonstration.

```
python capstone_demonstration.py --plot
```

### Task 1 — Precision Positioning

| Target (mm) | Measured (mm) | Error (mm) |
|-------------|---------------|------------|
| 50 | | |
| 120 | | |
| 200 | | |
| 90 | | |
| 270 | | |

Mean absolute error: ______  Max error: ______

### Task 2 — Grasping and Handling

| Attempt | Placed (mm) | Error (mm) | Result |
|---------|-------------|------------|--------|
| 1–5 | | | |

Success rate: ______ / 5

### Validation scorecard

| Specification | Target | Measured | Pass? |
|---------------|--------|----------|-------|
| Position overshoot | <5% | | |
| Position settling | <3 s | | |
| Position SSE | <2 mm | | |
| Grasp success | ≥4/5 | | |
| Placement | ±10 mm | | |
| Twin RMS | <5 mm | | |
| Fault detection | ≥80% | | |

**Capstone result:** ______

---

## Lab Report

This is the curriculum's final report — the full deliverable. Use the five-part structure, expanded.

### 1. Observation
Describe the complete machine performing both tasks. How did the twin track it? How did each subsystem contribute to the whole?

### 2. Measurement
The complete results: commissioning, integration milestone, both tasks, twin validation, fault detection, and the seven-spec scorecard.

### 3. Engineering Interpretation
Why did the machine meet (or miss) each spec? Connect the performance to the physics and design decisions across the whole curriculum — the velocity servo, the twin, the safety logic.

### 4. Machine Improvement
This is the complete machine. State what it can now do as one system that no subsystem could do alone, and reflect: what worked, what you would do differently.

### 5. Digital Twin Improvement
The twin ran in parallel during real tasks, validated and detecting faults. State the twin's final role and one extension the platform enables that the twin would support.

---

## Final deliverable (the capstone)

Beyond the lab report, assemble the complete deliverable:

- [ ] Hydraulic schematic (ISO 1219, component list)
- [ ] Wiring diagram (all sensors, controllers, power)
- [ ] Code repository (all modules, documented)
- [ ] Digital twin (validated against demonstration data)
- [ ] Validation report (seven specs, measured results)
- [ ] Final report (system, decisions, results, reflection, future directions)
- [ ] Demonstration (the machine performing both tasks, twin displayed)

---

## Analysis questions

1. Why is commissioning in dependency order safer and faster than turning everything on at once?
2. The simulation-tuned control transferred to (simulated) hardware with minor refinement. Why is this the payoff of the whole twin investment?
3. The capstone met all seven specs. Which spec was the machine's tightest margin, and why?
4. Identify one extension the platform enables, and explain how the digital twin would let you develop it safely.

---

## Machine capability check (the final one)

> **What did the machine become in Module 12?**

> **Which benchmark tasks did it demonstrate and validate?**

> **What did the digital twin's parallel run prove?**

> **What does the completed platform enable next?**

---

## The curriculum, complete

This lab completes the Fluid-Powered Physical AI curriculum. The Smart Agricultural Workcell — built from Pascal's Law to an autonomous, self-monitoring machine — is demonstrated, validated, and documented. From first principles to a working intelligent machine: the journey is finished.

---

*Lab 12 — Version 0.1 | Pairs with Lessons 01–04. The complete machine, demonstrated. THE FINAL LAB OF THE CURRICULUM.*
