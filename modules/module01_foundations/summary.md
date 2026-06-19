# Module 01 — Summary

*Foundations of Fluid Power and Physical AI*

---

## What you learned

Module 01 was an identity module, not a hydraulics module. You leave it understanding what Fluid-Powered Physical AI is, why it matters, and how the Smart Agricultural Workcell works as a complete system.

### The big ideas

**Fluid-Powered Physical AI is an underserved field.** Physical AI has been built almost entirely on electric actuation. Agriculture, construction, and heavy industry run on fluid power. This curriculum explores what happens when intelligence is brought into fluid-powered machines.

**The Smart Agricultural Workcell is the running system.** Every module contributes one capability to a single constrained-workspace manipulation platform — not a field vehicle, not a crop-specific tool, but an extensible research-compatible platform.

**Three equations govern every hydraulic system:**

| Equation | Form | Governs |
|----------|------|---------|
| Pascal's Law | $F = P \times A \times 0.1$ (N, bar, mm²) | Force |
| Continuity | $v = Q/A$ | Velocity |
| Hydraulic power | $P_{kW} = (p_{bar} \times Q_{LPM})/600$ | Power |

**Force multiplication is real, energy conservation is inviolable.** A larger output piston produces more force but less displacement. The two always go together.

**The workcell has six subsystems:** Hydraulic power (S1), Fluid transport (S2), Motion control (S3), Actuation (S4), Sensing and intelligence (S5), Digital twin (S6). Each maps to the SENSE → UNDERSTAND → DECIDE → COMMAND → ACTUATE → VALIDATE pipeline.

---

## The baseline workcell numbers

You should now be able to reproduce these from first principles:

| Parameter | Value |
|-----------|-------|
| System pressure | 100 bar |
| Flow rate | 10 LPM |
| Primary bore / rod | 50 / 25 mm |
| Extend force | 19.63 kN |
| Extend velocity | 84.9 mm/s |
| Hydraulic power | 1.67 kW |
| Required motor | ~2 kW |

---

## Lessons in this module

1. `01_why_this_matters.md` — the curriculum vision and the case for fluid-powered Physical AI
2. `02_physical_intuition.md` — pressure, force, flow, and energy before equations
3. `03_mathematical_foundations.md` — the three governing equations, derived and applied
4. `04_visual_explanation.md` — the six subsystems and how they interact

## Code in this module

- `code/module01/pascals_law.py` — cylinder force and velocity calculator
- `code/module01/unit_converter.py` — unit conversions and the `HydraulicSystem` class

## Lab in this module

- `labs/lab01_introduction/` — observing Pascal's Law in a low-pressure syringe circuit

---

## Self-assessment checklist

Before moving to Module 02, confirm you can:

- [ ] Explain in two sentences why fluid-powered Physical AI is worth studying
- [ ] Calculate cylinder extend force from bore and pressure
- [ ] Calculate piston velocity from flow and bore
- [ ] Calculate hydraulic power from pressure and flow
- [ ] Convert between bar/PSI, LPM/GPM, and kW/HP
- [ ] Name the six subsystems of the workcell and what each does
- [ ] Explain why retract is faster and weaker than extend
- [ ] Trace an extend command through all six subsystems
- [ ] Run both Module 01 Python scripts and modify their parameters

If you can do all nine, you are ready for Module 02.

---

## What comes next

Module 02 — Hydraulic Components and System Architecture — turns the abstract subsystems into real hardware. You will learn to identify pumps, valves, cylinders, and fittings by name and function, read ISO 1219 schematic symbols, and produce the first component map of your workcell.

The three equations from this module reappear in every subsequent one. Keep them close.

---

*Module 01 complete. This module is the reference implementation for the curriculum's tone, structure, equation density, and capstone integration. All later modules should match its standard.*
