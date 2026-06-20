# Lab 01 — Observing Pressure and Force in a Simple Hydraulic System

**Module:** 01 — Foundations of Fluid Power and Physical AI
**Duration:** 90 minutes
**Pressure level:** Low (under 50 PSI / 3.5 bar) — pneumatic or water-filled syringe substitute acceptable
**Capstone subsystem:** S4 (Actuation) — first physical contact with force multiplication

---

## Objective

Observe Pascal's Law directly. Build a two-cylinder hydraulic circuit, apply a known input force, measure the output force, and compare the result to the theoretical force ratio predicted by $F_{out}/F_{in} = A_{out}/A_{in}$.

This lab is the physical anchor for Lessons 02 and 03. You calculated force multiplication on paper. Here you feel it.

---

## Why this matters for the workcell

The Smart Agricultural Workcell's primary cylinder converts system pressure into the force that positions the manipulation arm. The end-effector cylinder converts pressure into grip force. Everything the workcell does mechanically begins with the principle you observe in this lab: pressure acting on an area produces force, and the area ratio sets the force ratio.

Before you can size the workcell cylinders (Module 07), you must trust this relationship from direct experience.

---

## Safety

⚠️ **Read before starting.**

- This lab uses **low-pressure** sealed syringes filled with water or food-grade mineral oil. Do not exceed 3.5 bar (50 PSI).
- Do not use compressed air above 3 bar without proper pneumatic fittings rated for it.
- Wear safety glasses. A syringe seal can fail and spray fluid.
- Do not point a pressurized syringe at anyone.
- If using oil, keep paper towels on hand and avoid slip hazards.
- Dispose of fluids per your facility's guidelines.

---

## Equipment

See `equipment.md` for the full list. Core items:

- 1 small syringe (input): 10 mm bore — record exact value
- 1 large syringe (output): 30 mm bore — record exact value
- Flexible tubing to connect them (silicone, 4–6 mm ID)
- Water or food-grade mineral oil
- A set of known masses (e.g., 100 g, 200 g, 500 g) or a small force gauge
- A ruler or calipers (to measure piston displacement)
- A digital kitchen scale (to measure output force via mass, if no force gauge)
- Clamp stand or fixture to hold syringes vertical

---

## Procedure

### Part 1 — Build the circuit

1. Fill both syringes and the connecting tube completely with fluid. **Eliminate all air bubbles** — trapped air compresses and ruins the measurement (this is itself an important lesson: hydraulic fluid must be incompressible).
2. Connect the two syringes with the tube. Secure both vertically in the clamp stand, pistons up.
3. Confirm that pushing one piston down raises the other.

### Part 2 — Measure the area ratio

4. Measure and record the exact bore diameter of each syringe (inside diameter of the barrel).
5. Calculate each piston area: $A = \pi (d/2)^2$.
6. Calculate the theoretical force ratio: $A_{out}/A_{in}$.

### Part 3 — Measure force multiplication

7. Place a known mass on the **input** (small) piston. Record the input force: $F_{in} = m \cdot g$.
8. Measure the **output** force needed to balance it. Two methods:
   - **Force gauge:** push down on the large piston until the small piston just lifts; read the gauge.
   - **Scale method:** rest the large piston on a kitchen scale; read the force (mass × g) the system exerts on the scale.
9. Record $F_{out}$.
10. Repeat for at least three different input masses.

### Part 4 — Measure displacement (energy conservation)

11. Mark the starting position of both pistons.
12. Push the input piston down a measured distance $d_{in}$ (e.g., 30 mm).
13. Measure how far the output piston rises: $d_{out}$.
14. Record both.

### Part 5 — Vary the area ratio (optional extension)

15. If a third syringe of different bore is available, swap it in and repeat Parts 2–4.

---

## Data sheet

| Trial | Input mass (g) | $F_{in}$ (N) | $F_{out}$ measured (N) | $F_{out}$ theoretical (N) | % error |
|-------|---------------|-------------|----------------------|--------------------------|---------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

| Displacement | $d_{in}$ (mm) | $d_{out}$ (mm) | $d_{in}/d_{out}$ | $A_{out}/A_{in}$ |
|--------------|--------------|---------------|-----------------|------------------|
| | | | | |

Theoretical force ratio $A_{out}/A_{in}$ = __________

---

## Analysis

Answer in your lab report:

1. How close was your measured force ratio to the theoretical ratio? What is the percent error?
2. List at least three sources of error. (Hint: friction in the syringe seals, trapped air, measurement precision.)
3. Did the displacement ratio $d_{in}/d_{out}$ match the area ratio $A_{out}/A_{in}$? What does this confirm about energy conservation?
4. Calculate the input work ($F_{in} \times d_{in}$) and the output work ($F_{out} \times d_{out}$) for one trial. Are they equal? Should they be? Where did any lost energy go?

---

## Lab Report Format

Every lab report for this curriculum follows the same five-part structure. It forces you to connect what you observed to the machine you are building.

1. **Observation** — What happened? Describe what you saw, qualitatively.
2. **Measurement** — What were the numbers? Record your data and any calculations.
3. **Engineering Interpretation** — What do the numbers mean physically? Explain the result using the lesson's concepts.
4. **Machine Implication** — What does this mean for the Smart Agricultural Workcell? Which capability or benchmark task does it affect, and how?
5. **Digital Twin Implication** — What does this mean for the digital twin? What should the twin predict, or what fault would this reveal as a residual?

The last two parts are the most important. A lab that stops at interpretation is a physics exercise; a lab that reaches the machine and the twin is part of building an intelligent machine.

---

## Workcell implication

Write 2–3 sentences answering:

> The workcell's gripper cylinder has a 25 mm bore at 80 bar. Based on what you observed in this lab, what is the relationship between the gripper's bore size and the force it applies to a workpiece? Why does the workcell need a way to *limit* grip force rather than just maximize it?

## Digital twin implication

Write 2–3 sentences answering:

> In this lab, you observed that trapped air ruins the force measurement. A digital twin of a hydraulic cylinder assumes the fluid is incompressible. What would happen to the twin's predictions if the real system had air trapped in it? How might the residual (predicted − measured) reveal this fault?

---

## Deliverables

- Completed data sheet
- Analysis answers (1–4)
- Workcell implication paragraph
- Digital twin implication paragraph
- One photograph of your assembled circuit

---

*Lab 01 — Version 0.1 | Pairs with Lessons 02 and 03*
