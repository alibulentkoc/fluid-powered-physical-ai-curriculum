# Lab 10 — Tuning and Validating the Machine's Controller

**Module:** 10 — Embedded Control (the machine decides and acts)
**Duration:** 120 minutes
**Pressure level:** Simulation-based, with optional hardware confirmation
**Capstone subsystem:** S5 (control intelligence) + S6 (Digital twin)
**Benchmark task:** Precision Positioning

---

## Objective

Give the machine its brain. Tune a PID position controller in simulation to meet spec, run the autonomous task state machine with safety, and validate the closed-loop control against the digital twin — the simulation-first workflow that lets the machine act safely. This is the lab where the machine learns to decide and act.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *act on what it perceives — precisely, autonomously, and safely.*

Module 09 gave the machine perception; this lab turns that perception into action. By the end, you will have tuned a controller in simulation, run the autonomous task, and validated the control against the twin — the workflow real engineers use to develop machine control safely.

---

## Safety

Core lab is simulation-based. The optional hardware confirmation requires the low-pressure rig and all safety logic active (limits, watchdog).

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python | 1 | |
| Module 10 code | — | all four files |
| Optional: workcell rig + Arduino + Pi | 1 | hardware confirmation |

---

## Part 1 — Open-loop vs. closed-loop

Run the basics and record the difference.

```
python closed_loop_basics.py
```

| Condition | Open-loop result | Closed-loop result |
|-----------|-------------------|--------------------|
| Nominal | | |
| Cold fluid (more friction) | | |

Record the proportional steady-state error.

---

## Part 2 — Tuning the PID

Run the PID controller and record the tuning progression.

```
python pid_controller.py
```

| Tuning | Settles (mm) | Overshoot (%) | SSE (mm) |
|--------|--------------|---------------|----------|
| P only | | | |
| P+I | | | |
| P+I+D (tuned) | | | |

Confirm the tuned controller meets <5% overshoot, <2 mm error.

---

## Part 3 — The autonomous task with safety

Run the state machine and record the task progression and safety events.

```
python state_machine.py
```

| Event | Resulting state |
|-------|-----------------|
| Normal progression (6 steps) | |
| Pressure spike to 125 bar | |
| After recovery | |
| Watchdog (comm lost 300 ms) | |

---

## Part 4 — Closed-loop validation

Run the closed-loop simulation and record the predicted step response.

```
python closed_loop_simulation.py --plot
```

| Metric | Predicted |
|--------|-----------|
| Final position (mm) | |
| Overshoot (%) | |
| Steady-state error (mm) | |
| Meets spec? | |

---

## Lab Report

Use the five-part structure.

### 1. Observation
How did closed-loop differ from open-loop? How did the PID terms change the step response? How did the state machine handle the safety events?

### 2. Measurement
The numbers: open vs. closed-loop results, the tuning progression, the task/safety states, the predicted step response.

### 3. Engineering Interpretation
Why does the integral remove steady-state error? Why does the derivative damp overshoot? Why does the watchdog protect the machine even if the Pi crashes? Connect each to the lesson physics.

### 4. Machine Improvement
How does this complete the machine's brain? It can now act on perception precisely, run its task autonomously, and protect itself — state what the machine can now do that it could not when it could only perceive.

### 5. Digital Twin Improvement
The closed-loop simulation makes the twin a control-design environment. State how the predicted-vs-actual comparison validates the twin, and how a discrepancy would be used to refine it.

---

## Analysis questions

1. Why can't the machine eliminate steady-state error by raising the proportional gain?
2. Why is simulation-first control safer than tuning on hardware?
3. Why does critical safety live in the Arduino firmware, below the task logic?
4. A predicted-vs-actual discrepancy appears. How would you tell if it's a control problem or a twin problem?

---

## Deliverables

- [ ] Part 1 open vs. closed-loop
- [ ] Part 2 tuning progression
- [ ] Part 3 task + safety states
- [ ] Part 4 closed-loop validation
- [ ] Five-part lab report
- [ ] Analysis answers (1–4)

---

## Machine capability check

> **What did the machine gain in Module 10?**

> **How did this lab complete Precision Positioning as a closed-loop capability?**

> **What did the closed-loop simulation do for the digital twin?**

---

## Optional hardware confirmation

If the workcell rig is available, load the tuned PID onto the Arduino with the safety logic active, run a 200 mm step, and log the actual response. Compare to the simulation's prediction — the predicted-vs-actual validation. Confirm the safety logic by deliberately triggering a limit (carefully, at low pressure) and verifying the machine enters FAULT.

---

*Lab 10 — Version 0.1 | Pairs with Lessons 01–04. The machine learns to decide and act.*
