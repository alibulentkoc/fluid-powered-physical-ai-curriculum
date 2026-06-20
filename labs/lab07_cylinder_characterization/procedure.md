# Lab 07 — Characterizing the Machine's Force and Friction

**Module:** 07 — Producing the Machine's Force and Motion
**Duration:** 90 minutes
**Pressure level:** Simulation-based, with optional low-pressure hardware
**Capstone subsystem:** S4 (Actuation) + S6 (Digital twin)
**Benchmark task:** Force-Controlled Interaction

---

## Objective

Characterize the machine's real actuator: measure (or simulate) its force-vs-pressure relationship, its breakout friction, and its stick-slip behavior at low speed. Compare the real, friction-laden behavior to the ideal force model, and feed the measured parameters into the digital twin.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *produce and model a real, controllable force.*

The machine's force capacity is the foundation of Force-Controlled Interaction. But the *real* actuator has friction that sets a floor on gentle force and causes stick-slip in slow motion. This lab measures those real effects, so the machine knows the smallest force it can controllably apply and the twin predicts the real cylinder, not an ideal one.

---

## Safety

Core lab is simulation-based. The optional hardware extension uses the low-pressure rig (Lab 01 rules: ≤3.5 bar, safety glasses).

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python | 1 | |
| Module 07 code | — | `cylinder_force_model.py`, `cylinder_spec.py` |
| Optional: low-pressure cylinder + force gauge | 1 | for real force measurement |
| Optional: pressure gauge | 1 | to record applied pressure |

---

## Part 1 — Force vs. pressure

Run the force model and record the machine's force-vs-pressure relationship.

```
python cylinder_force_model.py
```

| Pressure (bar) | Extend force (kN) | Retract force (kN) |
|----------------|-------------------|--------------------|
| 25 | | |
| 50 | | |
| 100 | | |

Also record: the pressure needed for a 1.5 kN gentle grip, and what fraction of system pressure that is.

---

## Part 2 — The Actuator Selection Report and buckling

Run the spec generator and record the report.

```
python cylinder_spec.py
```

| Spec parameter | Value |
|----------------|-------|
| Bore / rod / stroke | |
| Area ratio | |
| Buckling load (kN) / SF | |
| Pressure rating (bar) | |

Then record how the buckling safety factor changes as stroke increases (300 → 1200 mm). At what stroke does the 28 mm rod become unsafe?

---

## Part 3 — Friction and stick-slip

Examine the friction model (`cylinder_friction.py` or the friction function). Record friction at several speeds and identify the Stribeck dip.

| Velocity (mm/s) | Friction (N) |
|-----------------|--------------|
| 0 (breakout) | |
| 5 | |
| 20 | |
| 50 | |
| 90 | |

Identify: the breakout force, the speed of minimum friction, and the smallest force the machine could controllably apply.

---

## Lab Report

Use the five-part structure.

### 1. Observation
What did you see? How did the real (friction-laden) behavior differ from the ideal force model, especially at low speed?

### 2. Measurement
The numbers: force vs. pressure, the buckling SF vs. stroke, the friction curve and breakout force.

### 3. Engineering Interpretation
Why is the friction highest at breakaway and in the slow range? Why does the buckling margin shrink with stroke? Connect to the lesson physics.

### 4. Machine Improvement
How does this improve the machine? You now know its real force capability, the smallest force it can controllably apply (the breakout floor), and the stroke limit for its rod. State what the machine can now do or specify that it could not before.

### 5. Digital Twin Improvement
What does the twin gain? The measured friction parameters replace the placeholder values, so the twin predicts the real cylinder's stick-slip and breakout. State how a stick-slip regime would appear in the twin's predicted-vs-measured residual (forward reference to Module 11 fault detection).

---

## Analysis questions

1. The machine's force capacity is ~20 kN but its tasks need hundreds of newtons. Why is this headroom a feature, not waste?
2. At what stroke does the 28 mm rod's buckling safety factor drop below 3? What would you change?
3. The machine is asked to apply a 30 N force, below the ~120 N breakout. What happens, and what does it imply for gentle tasks?
4. How would closed-loop control (Module 10) compensate for the stick-slip you measured?

---

## Deliverables

- [ ] Part 1 force-vs-pressure table
- [ ] Part 2 Actuator Selection Report + buckling-vs-stroke
- [ ] Part 3 friction curve + breakout force
- [ ] Five-part lab report
- [ ] Analysis answers (1–4)

---

## Machine capability check

> **What capability did the machine gain in Module 07?**

> **How did this lab advance Force-Controlled Interaction?**

> **What did this lab add to the digital twin?**

---

*Lab 07 — Version 0.1 | Pairs with Lessons 01–03. Characterizes the machine's real force and friction.*
