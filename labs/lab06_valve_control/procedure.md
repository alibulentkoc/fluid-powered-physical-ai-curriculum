# Lab 06 — Commanding the Machine's Motion

**Module:** 06 — Controlling the Machine's Motion
**Duration:** 90 minutes
**Pressure level:** Simulation-based, with optional low-pressure / electronics hardware
**Capstone subsystem:** S3 (Motion control) + S6 (Digital twin)
**Benchmark task:** Precision Positioning

---

## Objective

Command the machine's motion electronically for the first time. Drive an extend–hold–retract sequence through the valve controller, observe the resulting motion, and explore the difference between on/off and proportional (smooth) control. This is the lab where the machine's brain first reaches its hydraulics.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *take a command and move.*

Every prior lab characterized a component. This lab is the first where the machine *acts on an instruction* — the seed of autonomy. By the end, you will have run the machine's first control sequence and seen why smooth (proportional) control matters for precise positioning.

---

## Safety

Core lab is simulation-based. The optional hardware extension involves low-voltage electronics (solenoid driver) and, if hydraulics are present, low-pressure rules from Lab 01. Always include the freewheeling diode across any real solenoid.

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python | 1 | |
| Module 06 code | — | `valve_controller.py`, `dcv_model.py`, `flow_control.py` |
| Optional: Arduino + MOSFET + solenoid valve + diode | 1 | hardware extension |
| Optional: low-pressure hydraulic rig | 1 | to see real commanded motion |

---

## Part 1 — Command the on/off sequence

Run the machine's first control logic:

```
python valve_controller.py
```

Record the commanded sequence and the resulting motion.

| Command | Solenoid state | Cylinder motion |
|---------|----------------|-----------------|
| extend | | |
| hold | | |
| retract | | |
| hold | | |

---

## Part 2 — On/off vs. proportional approach

Examine the proportional controller's smooth-approach output (`valve_controller.py`). Compare how the command changes as the cylinder nears a target, versus the on/off valve's binary behavior.

| Distance to target (mm) | On/off command | Proportional command | Proportional flow (LPM) |
|-------------------------|----------------|----------------------|-------------------------|
| 50 | full | | |
| 20 | full | | |
| 10 | full | | |
| 5 | full | | |
| 2 | full | | |

---

## Part 3 — The meter-out decision

Run `flow_control.py`. Confirm the meter-in vs. meter-out behavior for resisting and running loads, and record the meter-out flow for several approach speeds.

| Approach speed (mm/s) | Meter-out flow (LPM) | Spill over relief (LPM) |
|-----------------------|----------------------|-------------------------|
| 90 | | |
| 30 | | |
| 15 | | |

---

## Lab Report

Use the five-part structure.

### 1. Observation
What did the machine do for each command? How did the on/off and proportional approaches differ as the cylinder neared the target?

### 2. Measurement
The numbers: commanded velocities, the proportional command-vs-distance ramp, the meter-out flows and relief spill.

### 3. Engineering Interpretation
Why does the on/off valve produce abrupt motion while the proportional valve eases in? Why does slow motion spill flow over the relief? Connect to the lesson physics.

### 4. Machine Improvement
How does this improve the Smart Agricultural Workcell? The machine can now be commanded to move — state what it can do that it could not before, and how smooth control advances Precision Positioning.

### 5. Digital Twin Improvement
What does the twin gain? The controller logic now connects the command layer to the valve and cylinder models, so the twin can simulate a commanded sequence end-to-end. State how you would validate the twin's commanded motion against the real machine (forward reference to Module 09 sensors).

---

## Analysis questions

1. Why does the on/off valve overshoot a precise target, while the proportional valve can stop accurately?
2. During the slow approach, how much pump flow spills over the relief, and why is that wasteful?
3. Why must the machine meter *out* when lowering a load? What happens with meter-in?
4. How would closed-loop feedback (Module 10) improve on the open-loop smooth approach demonstrated here?

---

## Deliverables

- [ ] Part 1 command sequence table
- [ ] Part 2 on/off vs. proportional comparison
- [ ] Part 3 meter-out flow table
- [ ] Five-part lab report
- [ ] Analysis answers (1–4)

---

## Machine capability check

> **What capability did the machine gain in Module 06?**

> **How did this lab advance Precision Positioning?**

> **What did this lab add to the digital twin?**

---

## Optional hardware extension

Wire an Arduino to a MOSFET driving a low-voltage solenoid (with a freewheeling diode across the solenoid). Write the extend/hold/retract logic and trigger it from serial commands. If a low-pressure rig is available, watch the real cylinder respond to your typed commands — the machine acting on instruction, in the physical world.

---

*Lab 06 — Version 0.1 | Pairs with Lessons 01–04. The machine's first commanded motion.*
