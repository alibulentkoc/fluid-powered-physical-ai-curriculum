# Orifice flow and the valve model
## Module 04 · Lesson 02

*Every valve in the workcell is, mathematically, an orifice. This lesson builds the orifice flow model — the first component of the digital twin.*

---

## Why The Machine Needs This

The machine's digital twin must predict how much fluid each valve passes, because that flow sets how fast the cylinder moves. Every valve in the workcell is, mathematically, an orifice. The machine needs its first predictive model — the valve.

---

## 1. Why this matters

This is a milestone lesson. The orifice equation is the mathematical model of every valve in the workcell — the directional control valve, the flow control valve, the relief valve. And it is the **first piece of the digital twin** you will write.

From here, the curriculum builds the twin component by component. The valve model you write in this lesson becomes the input boundary condition for the cylinder simulation in Lesson 05, which becomes the core of the integrated twin in Module 11. Everything downstream depends on getting this right.

---

## 2. Physical intuition

An orifice is just a restriction — a hole the fluid must squeeze through. A valve is an *adjustable* orifice: opening or closing it changes the effective hole size.

The physics: fluid forced through a small opening must accelerate (Bernoulli, Lesson 01). The pressure drop across the opening drives the flow. A bigger pressure drop pushes more flow through; a bigger opening lets more through at the same pressure drop.

The non-obvious part — and the one that matters most for control — is that flow depends on the *square root* of the pressure drop, not the pressure drop itself. Double the pressure drop and you do not double the flow; you multiply it by √2 ≈ 1.41. This square-root relationship is the single most important fact about valve behavior, and it makes hydraulic control genuinely harder than it first appears (Module 10 deals with the consequences).

There is also a loss: real orifices do not pass as much flow as ideal theory predicts, because the fluid stream contracts and there is turbulence. The **discharge coefficient** $C_d$ (typically 0.6–0.7) captures this real-world shortfall.

---

## 3. Mathematical foundations

### The orifice equation

$$Q = C_d \cdot A \cdot \sqrt{\frac{2\,\Delta P}{\rho}}$$

- $Q$ = flow rate (m³/s)
- $C_d$ = discharge coefficient (~0.62 for a sharp-edged orifice)
- $A$ = orifice opening area (m²)
- $\Delta P$ = pressure drop across the orifice (Pa)
- $\rho$ = fluid density (kg/m³)

This is derived directly from Bernoulli (the velocity through the opening is $\sqrt{2\Delta P/\rho}$) multiplied by the area and the discharge coefficient that corrects for real losses.

### The valve as a variable orifice

For a valve, the opening area $A$ is a function of the command signal $u$ (0 = closed, 1 = fully open):

$$A(u) = A_{max} \cdot u$$

So the valve flow model is:

$$Q(u, \Delta P) = C_d \cdot A_{max} \cdot u \cdot \sqrt{\frac{2\,\Delta P}{\rho}}$$

This single equation is the workcell's valve model. Given a command and a pressure drop, it returns the flow. It is the first function in the digital twin.

### Cavitation limit

If the pressure drop is large enough that the local pressure falls below the fluid's vapor pressure, the fluid vaporizes — **cavitation**. The collapsing vapor bubbles erode components and make the flow model break down. Real valve models cap the usable pressure drop below the cavitation threshold.

> **Workcell relevance:** This is the model you implement as `valve_flow()` in `code/module04/orifice_flow.py`. It becomes the boundary condition feeding the cylinder simulation in Lesson 05 and the integrated twin in Module 11.

---

## 4. Visual explanation

> See figure: `assets/figures/digital_twin_workflow.svg` (the valve orifice model block)

The digital twin workflow figure shows where this model lives: on the twin side, the "Valve orifice model" block sits between the pump model and the cylinder ODE. It takes the command (from the control side) and the pressure drop (from the system state) and outputs the flow into the cylinder.

A flow-vs-pressure-drop plot is the signature visual: a square-root curve, rising steeply at first then flattening. Several curves, one per valve opening, fan out — wider openings give higher curves. This family of curves *is* the valve model, visualized.

---

## 5. Engineering example

**Why proportional valves need careful control**

A simple on/off solenoid valve is either fully open or fully closed — the command $u$ is 0 or 1. A proportional valve can take any opening in between, giving smooth speed control.

But the square-root pressure relationship means the flow does not respond linearly to either the command or the pressure. As the cylinder moves and the load changes, the pressure drop across the valve changes, so the same command produces different flows at different times. A controller that assumes linear behavior will mistune.

This is why Module 10 spends real effort on control: the valve model from this lesson is nonlinear, and good control must account for it. The workcell's baseline uses an on/off DCV (simpler), with a proportional valve as a documented upgrade path — and the orifice model is what makes the upgrade analyzable.

---

## 6. Worked example

**Problem:** The workcell's flow control valve has $C_d = 0.62$, a maximum opening area of 4 mm², and operates with hydraulic oil (ρ = 870 kg/m³).

(a) At full opening (u = 1) with a 30 bar drop, what flow does it pass (LPM)?
(b) At half opening (u = 0.5) with the same 30 bar drop?
(c) At full opening but only 15 bar drop (half the pressure)?

**Solution:**

*(a)* Full opening, 30 bar:
$$Q = 0.62 \times (4\times10^{-6}) \times \sqrt{\frac{2 \times 30\times10^5}{870}}$$
$$\sqrt{\frac{6\times10^6}{870}} = \sqrt{6897} = 83.0\ \text{m/s}$$
$$Q = 0.62 \times 4\times10^{-6} \times 83.0 = 2.06\times10^{-4}\ \text{m}^3/\text{s} = 12.3\ \text{LPM}$$

*(b)* Half opening: area halves, so flow halves → **6.2 LPM**. (Flow is linear in opening area.)

*(c)* Half the pressure drop: flow scales with √(15/30) = √0.5 = 0.707 → $12.3 \times 0.707 = 8.7\ \text{LPM}$. (Flow is *not* halved — only reduced by ~29%, because of the square-root relationship.)

The contrast between (b) and (c) is the lesson: halving the *opening* halves the flow, but halving the *pressure* only reduces it by ~29%. This asymmetry is the heart of valve control difficulty.

---

## 7. Interactive demonstration

```python
import math

def valve_flow_lpm(u, dp_bar, cd=0.62, area_max_mm2=4.0, rho=870):
    """Orifice valve model. u in [0,1], returns flow in LPM."""
    area = area_max_mm2 * 1e-6 * u
    dp = dp_bar * 1e5
    q = cd * area * math.sqrt(2 * dp / rho)
    return q * 60000

print("Effect of opening (at 30 bar):")
for u in [0.25, 0.5, 0.75, 1.0]:
    print(f"  u={u:.2f}: {valve_flow_lpm(u, 30):.2f} LPM")

print("\nEffect of pressure (at full opening):")
for dp in [7.5, 15, 30, 60]:
    print(f"  dP={dp:4.1f} bar: {valve_flow_lpm(1.0, dp):.2f} LPM")
```

Run it. Opening scales flow linearly; pressure scales it by a square root. Internalizing this difference is the goal of the lesson.

---

## 8. Coding exercise

Write `code/module04/orifice_flow.py` — the first digital twin component. It should:

1. Implement `valve_flow(u, dp, cd, area_max, rho)` returning flow in SI units
2. Provide an LPM convenience wrapper
3. Plot flow vs. pressure drop for several valve openings (u = 0.25, 0.5, 0.75, 1.0)
4. Plot flow vs. command at a fixed pressure drop (showing linearity in opening)
5. Include a docstring noting this is the valve model used by the cylinder simulation in Lesson 05

This file is imported by later digital twin code. Write it cleanly — it is reused.

---

## 9. Knowledge check

1. Write the orifice equation and define each symbol.
2. Flow depends on the square root of what quantity?
3. If you double a valve's opening area at constant pressure drop, what happens to the flow? If you double the pressure drop at constant opening?
4. What does the discharge coefficient $C_d$ account for?
5. What is cavitation, and why does it limit the usable pressure drop across a valve?

---

## 10. Challenge problem

The workcell's DCV (modeled as an orifice) feeds the primary cylinder. During an extend stroke, the pressure drop across the valve changes as the load varies: it starts at 40 bar (cylinder accelerating) and settles to 20 bar (steady motion).

**a)** With $C_d = 0.62$, $A_{max} = 8\ \text{mm}^2$, full opening, calculate the flow at 40 bar and at 20 bar.

**b)** The cylinder has a 50 mm bore. Convert both flows to piston velocities (mm/s). (Recall continuity from Module 01.)

**c)** The cylinder therefore moves faster when accelerating (higher ΔP) than at steady state? Explain whether this matches physical intuition, and what it implies for predicting the cylinder's motion.

**d)** Why does this changing pressure drop make open-loop position control (just timing the valve) unreliable, motivating the closed-loop control of Module 10?

---

## 11. Common mistakes

**Assuming flow is proportional to pressure drop.** It is proportional to the *square root* of pressure drop. This is the most common and most consequential error in valve modeling.

**Forgetting the discharge coefficient.** Ideal orifice theory overpredicts flow. The real flow is lower by the factor $C_d$ (~0.62). Omitting it gives flows ~40% too high.

**Treating the valve opening and the pressure drop as independent of the system.** In a real system, as the cylinder moves, the load and therefore the pressure drop change — so the flow changes even at constant command. The valve model must be solved together with the cylinder dynamics (Lesson 05).

**Ignoring cavitation.** Pushing too large a pressure drop across a valve causes cavitation, which damages components and breaks the flow model. Real models cap ΔP.

---

## 12. Key takeaways

- Every valve is mathematically an orifice; the orifice equation $Q = C_d A \sqrt{2\Delta P/\rho}$ is the workcell's valve model.
- Flow is linear in opening area but proportional to the square root of pressure drop — a crucial asymmetry for control.
- The discharge coefficient $C_d$ (~0.62) corrects ideal theory for real-world losses.
- This valve model is the first digital twin component, written as `orifice_flow.py`, and reused throughout the curriculum.
- The valve and cylinder dynamics must be solved together because the pressure drop depends on the system state.

---


## Machine Capability Added

The machine has its **first digital-twin component**. The valve model (`orifice_flow.py`) predicts flow from command and pressure drop — the input that drives the cylinder simulation, and the first piece of the workcell that exists in software.

---

*Lesson 02 — Version 0.1 | Next: Lesson 03 — Cylinder dynamics: the force balance*
