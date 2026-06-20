# Lab 02 — Component Identification and Circuit Tracing

**Module:** 02 — Hydraulic Components and System Architecture
**Duration:** 90 minutes (two parts)
**Pressure level:** None — this is an identification and analysis lab, no live hydraulics required
**Capstone subsystems:** S1, S2, S3, S4 (the full physical hydraulic machine)

---

## Objective

Two parts:

- **Part A — Component identification:** Given a physical hydraulic power unit (or clear photographs), identify and label every major component, and match each to its ISO 1219 symbol.
- **Part B — Circuit tracing:** Given a hydraulic schematic, trace the flow path for each valve position and determine what each actuator does.

This lab turns the named components of Module 02 into recognized hardware and readable schematics — the skills you need to produce the workcell Component Map and, eventually, the full circuit diagram in Module 08.

---

## Why this matters for the workcell

You cannot build, wire, or troubleshoot the Smart Agricultural Workcell if you cannot identify its components or read its circuit. Every later module assumes you can look at the workcell — physical or schematic — and name what you see. This lab builds that fluency before any pressure is applied.

---

## Safety

This lab involves no live hydraulics. If you are examining a real power unit:
- Confirm it is **depressurized and powered off** before touching anything.
- Do not loosen any fitting or open any valve on a charged system.
- Treat all hoses and ports as if they could contain residual pressure.

---

## Equipment

| Item | Qty | Notes |
|------|-----|-------|
| Hydraulic power unit OR labeled photographs | 1 | Bench HPU, trainer panel, or a clear photo set |
| Printed ISO 1219 symbol reference sheet | 1 | See `assets/figures/` and standard references |
| The capstone architecture figure | 1 | `assets/figures/capstone_architecture.svg` |
| A sample hydraulic schematic | 1 | Provided by instructor, or use the workcell circuit |
| Blank paper / tablet for sketching | — | For the Component Map deliverable |
| Colored pens or highlighters | set | For tracing flow paths in Part B |

If no physical unit is available, this lab runs entirely from photographs and schematics — it is designed to work either way.

---

## Part A — Component identification

### Procedure

1. Examine the power unit (or photographs). Locate and identify each of the following:
   - Electric motor
   - Pump (identify type if visible: gear, vane, piston)
   - Reservoir
   - Pressure relief valve
   - Directional control valve (note ports and positions)
   - Filter (note location: pressure line or return line)
   - Pressure gauge (if present)
   - Hoses and fittings (note the fitting standard if marked)

2. For each component, record in the table below:
   - Its name
   - Its function (one short phrase)
   - Which workcell subsystem it belongs to (S1–S4)
   - Its ISO 1219 symbol (sketch it)

### Identification table

| # | Component | Function | Subsystem | ISO 1219 symbol (sketch) |
|---|-----------|----------|-----------|--------------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |

---

## Part B — Circuit tracing

### Procedure

1. Obtain a hydraulic schematic (the workcell circuit or an instructor-provided one).
2. Identify the directional control valve and its positions.
3. For **each** spool position, trace the flow path with a colored pen:
   - From the pump (P)
   - Through the valve
   - To the actuator (A or B port)
   - And the return path back to tank (T)
4. For each position, state what the actuator does (extend, retract, hold).

### Circuit tracing table

| Valve position | P connects to | Return path | Actuator result |
|----------------|---------------|-------------|-----------------|
| Left (solenoid A) | | | |
| Center (neutral) | | | |
| Right (solenoid B) | | | |

### Analysis questions

1. In the center position, what happens to the pump's flow? (This reveals whether the circuit is open-center or closed-center.)
2. If the schematic shows a closed-center valve, where are the port relief valves, and what do they protect against?
3. Trace what happens if the relief valve setting is exceeded. Where does the fluid go?

---

## Deliverable — Workcell Component Map (Module 02 deliverable)

Using what you identified and traced, produce a **block diagram of the Smart Agricultural Workcell's Subsystems 1 and 2** with real component names and at least one specification each:

- **Subsystem 1 (Hydraulic Power):** motor (power, speed), pump (type, displacement), relief valve (setting), reservoir (volume)
- **Subsystem 2 (Fluid Transport):** supply line, return line, filter (location, Beta ratio), breather, fitting standard, fluid (placeholder — specified fully in Module 03)

This Component Map is the foundation for the detailed sizing in Modules 05–08. Keep it; you will extend it as the curriculum progresses.

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

Write 2–3 sentences:

> Having identified the components and traced the circuit, which single component do you think is most critical to get right for the workcell's precision manipulation task, and why?

## Digital twin implication

Write 2–3 sentences:

> The digital twin models the pump, valve, and cylinder. Based on this lab, which component's *real* behavior (e.g., internal leakage, valve switching, contamination sensitivity) do you expect to be hardest to capture accurately in the twin? Why?

---

## Deliverables checklist

- [ ] Completed Part A identification table (8+ components)
- [ ] Completed Part B circuit tracing table (all three positions)
- [ ] Part B analysis answers (1–3)
- [ ] Workcell Component Map block diagram
- [ ] Workcell implication paragraph
- [ ] Digital twin implication paragraph

---

*Lab 02 — Version 0.1 | Pairs with all four Module 02 lessons. Produces the Module 02 Component Map deliverable.*
