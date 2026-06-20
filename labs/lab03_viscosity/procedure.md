# Lab 03 — Viscosity and Its Temperature Dependence

**Module:** 03 — Hydraulic Fluids and Energy Transmission
**Duration:** 60 minutes
**Pressure level:** None — this is a fluid-properties observation lab
**Capstone subsystem:** S2 (Fluid transport) — fluid selection for the workcell

---

## Objective

Observe viscosity directly and see how it changes with temperature. Compare the flow behavior of fluids of different viscosity, then warm one fluid and observe its viscosity drop. Connect the observation to the workcell's fluid selection.

This lab makes the abstract Walther curve from Lesson 02 tangible: you will *see* a fluid get thinner as it warms.

---

## Why this matters for the workcell

The workcell's fluid selection (ISO VG 46) depends on viscosity staying inside the pump's acceptable band across the operating temperature range. This lab builds physical intuition for what viscosity *is* and how strongly temperature affects it — the foundation for trusting the viscosity model that informs the workcell Fluid Specification.

---

## Safety

- Use **food-grade** fluids (water, cooking oils) or clearly labeled non-hazardous fluids only.
- Do **not** heat any fluid above 60°C without dedicated heating equipment and supervision.
- Never heat fluid in a sealed container.
- Wipe up oil spills immediately to prevent slip hazards.
- Wear safety glasses.

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Two fluids of clearly different viscosity | 2 | e.g., water and vegetable oil; or two cooking oils |
| Identical clear tubes or graduated cylinders | 2 | For the timed-flow comparison |
| Small steel ball or bead | 2 | One per tube, for the falling-ball method |
| Stopwatch or phone timer | 1 | |
| Thermometer (0–80°C) | 1 | Food/lab thermometer |
| Warm water bath OR controlled warm area | 1 | To gently warm one fluid sample |
| Ruler | 1 | To mark fall distance |
| Recording sheet | 1 | Table below |

---

## Part 1 — Compare two viscosities (falling-ball method)

The falling-ball viscometer is the simplest viscosity demonstration: a denser ball falls slower through a more viscous fluid.

### Procedure

1. Fill two identical clear tubes with the two different fluids to the same height.
2. Mark a start line and a finish line on each tube (same distance apart).
3. Drop an identical ball into each fluid and time its fall between the lines.
4. Record the fall time for each. The slower fall indicates higher viscosity.
5. Repeat three times per fluid and average.

### Data

| Fluid | Trial 1 (s) | Trial 2 (s) | Trial 3 (s) | Average (s) | Relative viscosity |
|-------|------------|------------|------------|-------------|--------------------|
| Fluid A (___) | | | | | |
| Fluid B (___) | | | | | |

The fluid with the longer average fall time is more viscous.

---

## Part 2 — Viscosity vs. temperature

### Procedure

1. Take the more viscous fluid (e.g., the cooking oil).
2. Measure and record its temperature.
3. Drop the ball and time the fall (as in Part 1). Record.
4. Gently warm the fluid to about 40–50°C (warm water bath; do not exceed 60°C). Measure the new temperature.
5. Drop the ball again and time the fall. Record.
6. Compare the two fall times.

### Data

| Condition | Temperature (°C) | Fall time (s) |
|-----------|------------------|---------------|
| Cool | | |
| Warm | | |

---

## Analysis

1. Which fluid in Part 1 was more viscous? How did the fall time tell you?
2. In Part 2, did the fall time get shorter or longer when warmed? What does this confirm about the viscosity-temperature relationship?
3. The Walther equation (Lesson 02) predicts viscosity falls as temperature rises. Does your observation agree, at least qualitatively?
4. Estimate: if warming the fluid roughly halved the fall time, by roughly what factor did its viscosity change? (Fall time is inversely related to viscosity for a slow-falling ball.)

---

## Workcell implication

Write 2–3 sentences:

> The workcell uses ISO VG 46 oil and operates around 40–60°C. Based on what you observed about temperature and viscosity, explain why the workcell's fluid selection had to consider the *whole* operating temperature range, not just a single temperature.

## Digital twin implication

Write 2–3 sentences:

> The digital twin models the fluid's viscosity to predict flow and pressure-drop behavior. Based on this lab, why must the twin's viscosity value depend on the fluid's current temperature rather than being a fixed constant? What would go wrong if it used a single fixed viscosity?

---

## Deliverables

- [ ] Part 1 data table (two fluids, three trials each)
- [ ] Part 2 data table (cool vs. warm)
- [ ] Analysis answers (1–4)
- [ ] Workcell implication paragraph
- [ ] Digital twin implication paragraph

---

## Extension (optional)

Run `code/module03/viscosity_model.py` and compare its predicted viscosity-temperature curve for a real hydraulic oil with the qualitative trend you observed. The lab shows the *direction* and *rough magnitude* of the effect; the model gives the precise curve.

---

*Lab 03 — Version 0.1 | Pairs with Lesson 02 (viscosity).*
