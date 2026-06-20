# Module 07 — Summary

*Producing the Machine's Force and Motion*

---

## The machine's journey through this module

The machine entered Module 07 able to command an actuator (Module 06) but with that actuator only roughly defined. It leaves with a complete, checked, buildable actuator — sized for force, structurally sound, modeled with its real imperfections, and matched by type to each task.

The module never studied "cylinders and motors." It solved the machine's actuation problem:

1. **Produce force** — the cylinder sized for the machine's tasks, with the headroom that enables gentle control (19.63 kN capacity, controllable down to a few bar).
2. **Specify the actuator** — the complete Actuator Selection Report: rod, stroke, mounting, pressure rating, seals, buckling checked.
3. **Model real behavior** — friction, stick-slip, breakout, and cushioning, so the twin matches the real cylinder.
4. **Choose the actuator type** — cylinder for linear tasks, motor for rotary, by task requirements.

---

## The machine's actuator (the established design)

| Parameter | Value | Source |
|-----------|-------|--------|
| Type | Double-acting cylinder | L04 (linear, position hold) |
| Bore | 50 mm | L01 (19.63 kN at 100 bar) |
| Rod | 28 mm | L02 (buckling SF 5.0; area ratio 1.46) |
| Stroke | 300 mm | L02 (work envelope) |
| Mounting | Clevis/trunnion | L02 (alignment) |
| Pressure rating | ≥ 160 bar | L02 (1.6× working) |
| Seals | Nitrile (NBR) | L02 (ISO VG 46, bench temp) |
| Friction | Stribeck (Fs≈120 N) | L03 (real behavior) |
| Rotary option | 4–6 cc/rev gear motor | L04 (when rotation needed) |

All numbers verified against the Module 07 code.

---

## Machine Capability Added

> **Before this module the machine could not:** produce a known, correctly-sized, buildable force — its actuator was undefined.
>
> **After this module the machine can:** produce sized, controllable force from a complete, structurally-sound, realistically-modeled actuator, with the right actuator type for each task.

The machine gained a **complete, real actuator** — sized muscle it can build, trust, and model.

## Benchmark Task Advanced

**Force-Controlled Interaction** advanced decisively. Before Module 07 the machine could command motion but its force capacity was undefined. After, the machine has a sized force capacity (19.63 kN) with the headroom that makes *gentle, controlled* force possible (a 1.5 kN grip needs just 7.6 bar — the task lives in the finely-controllable low range), a realistic friction model that sets the smallest controllable force (the breakout floor), and the actuator type matched to each task. **Precision Positioning** also advanced: the stick-slip friction model identifies the main obstacle to accurate slow positioning, which Module 10's control will compensate.

## Digital Twin Contribution

The twin gained the complete **actuation subsystem**:
- **Force model** — extend/retract force with back-pressure, pressure-to-force mapping
- **Structural parameters** — finalized bore, rod, stroke, area ratio (replacing Module 04 placeholders)
- **Real-behavior model** — Stribeck friction, breakout force, cushioning
- **Actuator-type logic** — cylinder-vs-motor selection and motor sizing

The twin now models the *specified, real* actuator — predicting actual force, stick-slip, and the realistic velocity profile, completing the cylinder model begun in Module 04.

## Module Artifact

The **Actuator Selection Report** — the complete, checked specification of the machine's actuator(s). Subsystem 4 of the final machine; the actuator Module 06 commands and Module 08 integrates.

---

## Lessons in this module

1. `01_producing_force.md` — the machine produces force (sizing, headroom)
2. `02_specifying_actuator.md` — the complete specification (buckling, mounting, rating)
3. `03_real_behavior.md` — friction, stick-slip, breakout, cushioning
4. `04_actuator_selection.md` — cylinder vs. motor, by task requirements

## Code (all tested)

- `code/module07/cylinder_force_model.py` — force vs. pressure, bore sizing, task pressures
- `code/module07/cylinder_spec.py` — buckling check, area ratio, Actuator Selection Report
- `code/module07/actuator_selection.py` — cylinder-vs-motor logic, motor sizing

## Lab

- `labs/lab07_cylinder_characterization/` — measuring the machine's real force and friction

---

## Self-assessment checklist

Before Module 08, confirm you can:

- [ ] Compute the machine's extend/retract force and size a bore for a required force
- [ ] Explain why large force capacity enables gentle control
- [ ] Perform an Euler buckling check and say why it matters for long strokes
- [ ] Produce a complete actuator specification (the Actuator Selection Report)
- [ ] Explain stick-slip and the breakout-force floor on gentle interaction
- [ ] Choose between a cylinder and a motor from task requirements, and size a motor
- [ ] Run all three Module 07 code files and interpret their output

---

## What comes next

The machine now has power (M05), motion control (M06), and a real actuator (M07) — all four physical subsystems exist. Module 08 — Integrating the Machine's Hydraulic Circuit — assembles them into one complete circuit: the full ISO 1219 schematic with an energy budget, the physical machine complete and ready for the sensing and intelligence of Modules 09–12.

---

*Module 07 complete. Built natively to the Physical AI pattern — machine-problem-first, requirements-first for the actuator-type decision. All numerical claims verified against tested code.*
