# Module 02 — Summary

*Hydraulic Components and System Architecture*

---

## What you learned

Module 01 gave you a mental model and the governing equations. Module 02 made it concrete hardware. You can now identify every major hydraulic component by name and function, read the basics of ISO 1219 schematic symbols, and explain why each component exists in the Smart Agricultural Workcell.

### The big ideas

**Pumps create flow, not pressure.** A positive-displacement pump moves a fixed volume per revolution. Pressure arises only when that flow meets resistance. The workcell uses an 8 cc/rev fixed-displacement gear pump at 1450 RPM, delivering ~10.7 LPM actual.

**Three valve families do three jobs.** Directional (where the fluid goes), pressure (how hard the system can push), flow (how fast the actuator moves). The workcell uses a 4/3 closed-center solenoid DCV with a pressure relief valve and a flow control valve.

**Cylinders give linear motion; motors give rotation.** A double-acting cylinder pushes and pulls under power, with the differential effect making retract weaker and faster than extend. The workcell's primary actuator is a cylinder; its end effector may use either.

**The support system prevents most failures.** Reservoir, filter, hoses, and fittings keep the fluid clean, cool, and contained. Contamination is the number-one cause of hydraulic failure, and the filter must be matched to the most sensitive component (the workcell's DCV).

---

## Key relationships introduced

| Relationship | Equation | Used for |
|--------------|----------|----------|
| Theoretical pump flow | $Q_t = D \cdot n$ | Pump sizing |
| Actual pump flow | $Q_a = Q_t \cdot \eta_v$ | Real flow delivery |
| Orifice / valve flow | $Q = C_d A \sqrt{2\Delta P/\rho}$ | Valve and flow control |
| Motor torque | $T = D_m \Delta p / 2\pi \cdot \eta_m$ | Rotary actuator sizing |
| Filter efficiency | $(1 - 1/\beta_x)$ | Filter selection |

---

## Lessons in this module

1. `01_pumps.md` — pumps as the heart of the system; the workcell's gear pump
2. `02_valves.md` — the three valve families and ISO 1219 notation
3. `03_cylinders_and_motors.md` — actuator anatomy and the cylinder-vs-motor choice
4. `04_support_system.md` — reservoir, filter, hoses, fittings, and contamination control

## Code in this module

- `code/module02/pump_flow_model.py` — gear pump flow vs. speed, with the workcell operating point (tested)

## Lab in this module

- `labs/lab02_component_identification/` — identify and label real components and ISO 1219 symbols

---

## Module 02 deliverable

The **Component Map** of the Smart Agricultural Workcell: a block diagram naming the actual components for Subsystems 1 and 2 — pump type and displacement, valve types, cylinder dimensions, reservoir volume, filter Beta ratio, and fitting standard.

---

## Self-assessment checklist

Before moving to Module 03, confirm you can:

- [ ] Explain why a pump creates flow rather than pressure
- [ ] Size a gear pump's displacement for a required flow and speed
- [ ] Name the three valve families and what each controls
- [ ] Decode "4/3 closed-center solenoid DCV" completely
- [ ] Describe the anatomy of a double-acting cylinder
- [ ] Decide between a cylinder and a motor for a given task
- [ ] Explain the Beta ratio and match a filter to a component
- [ ] State why suction lines are larger than pressure lines
- [ ] Run `pump_flow_model.py` and interpret the flow-vs-speed result

---

## Machine Capability Added

> **Identify and select the physical components the machine is made of.**

The machine's six subsystems now have real, named hardware. You can look at a workcell — physical or schematic — and identify every component and explain why it is there. The deliverable, the Component Map, is the machine drawn with its actual parts.

**Benchmark task advanced:** Precision Positioning and Force-Controlled Interaction both become physically concrete — you now know which components produce the motion and the force each task needs.

## Digital Twin Contribution

The twin gains its first **parameters**: pump displacement, cylinder bore and rod areas, valve type and port configuration, filter rating. These are the raw numbers the twin's models will use once they are written in Module 04.

**New prediction enabled:** none yet (the models that use these parameters arrive in Module 04).
**Connects to next module:** Module 03 specifies the fluid that fills these components and gives the twin its physical fluid parameters.

---

## What comes next

Module 03 — Hydraulic Fluids and Energy Transmission — specifies the fluid that fills the system you just mapped. You will learn how viscosity, temperature, and contamination affect performance, and you will make the fluid specification for the workcell.

The components in this module reappear with full sizing detail in Modules 05–08: the pump in Module 05, the valves in Module 06, the cylinders in Module 07, and the complete circuit in Module 08.

---

*Module 02 complete. Built to the Module 01 reference standard: 12-part lessons, worked examples grounded in the workcell, tested code, explicit capstone connection.*
