# Lab 04 — Cylinder Step Response and the First Twin Validation

**Module:** 04 — Fluid Mechanics for Intelligent Machines
**Duration:** 90 minutes
**Pressure level:** Simulation-based (no live hydraulics required); optional low-pressure hardware extension
**Capstone subsystems:** S4 (Actuation) + S6 (Digital twin)
**Benchmark task:** Precision Positioning

---

## Objective

Run the workcell cylinder simulation, observe its step response (extend-then-hold), and perform the curriculum's first **digital twin validation**: compare the simulation's prediction against an independent hand calculation. This is the moment the twin earns trust.

You will also explore how the twin's predictions change when parameters change — bulk modulus, valve size, load — building intuition for what the model captures.

---

## Why this matters for the machine

> **What can the machine do now that it could not before?** It can *predict its own motion.*

In Module 04 the machine gained a software shadow — a digital twin that simulates the cylinder responding to a valve command. But a prediction is only useful if it is trustworthy. This lab establishes that trust by validating the simulation against independent analysis, exactly as you would validate a real twin against real sensor data (which arrives in Module 09). Precision Positioning — moving the end-effector to a target — depends entirely on the machine being able to predict where the cylinder will go.

---

## Safety

The core lab is simulation-based and carries no physical hazard. If you attempt the optional hardware extension, follow all Lab 01 low-pressure safety rules (≤3.5 bar, safety glasses, no pointing a charged syringe at anyone).

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Computer with Python, NumPy, SciPy, Matplotlib | 1 | |
| The Module 04 code files | — | `orifice_flow.py`, `cylinder_dynamics.py`, `cylinder_simulation.py` |
| Calculator or spreadsheet | 1 | For the hand-calculation validation |

---

## Part 1 — Run the step response

### Procedure

1. Run the simulation:
   ```
   python cylinder_simulation.py --plot
   ```
2. Examine the printed trajectory table and the saved plot (`cylinder_simulation.png`).
3. Record the steady extend velocity, the final position at the end of the extend phase, and confirm the cylinder holds position after the valve closes.

### Data

| Quantity | Value from simulation |
|----------|----------------------|
| Steady extend velocity (mm/s) | |
| Position at t = 1.0 s (mm) | |
| Position after hold (mm) | |
| Does it hold when valve closes? (Y/N) | |

---

## Part 2 — Validate against hand calculation

This is the twin validation. Predict the steady velocity *independently*, then compare.

### Procedure

1. From the orifice model, the valve passes a flow $Q$ at the steady-state pressure drop. At steady velocity, all that flow goes into moving the piston: $Q = A_{bore} \cdot v$.
2. Using `orifice_flow.py` (or the orifice equation by hand), compute the flow at the steady-state bore pressure drop the simulation reports.
3. Divide by the bore area to get the predicted steady velocity.
4. Compare to the simulation's steady velocity from Part 1.

### Data

| Quantity | Value |
|----------|-------|
| Steady bore pressure drop (bar) | |
| Valve flow at that drop (LPM) | |
| Bore area (mm²) | |
| Predicted velocity = Q / A (mm/s) | |
| Simulation velocity (mm/s) | |
| Agreement (% difference) | |

If the two agree within a few percent, the twin is validated for this case.

---

## Part 3 — Explore parameter sensitivity

Change one parameter at a time in `cylinder_simulation.py` (or via `CylinderParams`) and observe the effect.

### Procedure

Run the simulation three more times, each with one change:

1. **Lower bulk modulus** (e.g., $B_e$ = 0.5 GPa, simulating entrained air). What happens to the pressure build-up and response?
2. **Larger external load** (e.g., double `load_N`). What happens to the steady velocity and the pressures?
3. **Smaller valve** (reduce `valve_area_max_m2`). What happens to the steady velocity?

### Data

| Change | Effect on velocity | Effect on pressure/response |
|--------|--------------------|-----------------------------|
| Lower bulk modulus | | |
| Larger load | | |
| Smaller valve | | |

---

## Analysis

1. Did the simulation's steady velocity match your hand calculation (Part 2)? Within what percentage? What does agreement tell you about the twin?
2. In Part 3, which parameter most strongly affected the steady velocity? Does this match the orifice/continuity reasoning?
3. The real cylinder has not been built yet, but the twin already predicts its motion. Why is validating against a hand calculation a meaningful first step, even before real sensor data exists?
4. The simulation uses a robust (quasi-static or stiff-solver) formulation. Why might the most physically detailed model not always be the best teaching or engineering model?

---

## Machine capability check

Answer in one or two sentences each:

> **What capability did the machine gain in Module 04?**

> **Which benchmark task did this lab advance, and how?**

> **What did this lab add to the digital twin's credibility?**

---

## Digital twin implication

Write 2–3 sentences:

> In Module 09 you will add real sensors and compare their readings to this same simulation. Based on this lab, what would it mean if the real cylinder's measured velocity disagreed sharply with the twin's prediction? What might that residual reveal?

---

## Deliverables

- [ ] Part 1 step-response data
- [ ] Part 2 validation table with % agreement
- [ ] Part 3 sensitivity table
- [ ] Analysis answers (1–4)
- [ ] Machine capability check (three answers)
- [ ] Digital twin implication paragraph

---

## Optional hardware extension

If a low-pressure syringe rig (Lab 01) is available, command a manual "step" (push the input piston suddenly) and observe the output piston's response. Note qualitatively how the real response differs from the ideal simulation — compliance, friction, and air all show up as departures from the predicted curve. This previews the real-vs-twin comparison of Module 09.

---

*Lab 04 — Version 0.1 | Pairs with Lesson 05 (simulation). The curriculum's first digital twin validation.*
