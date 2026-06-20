# Curriculum Narrative
## The Story of the Smart Agricultural Workcell

*This is the spine of the curriculum. Read it first. It explains what you are building, why, and how the machine becomes more capable with every module.*

> You are not taking twelve modules. You are building one machine in twelve stages.

---

## The machine

You are building the **Smart Agricultural Workcell** — formally, the Intelligent Fluid-Powered Agricultural Manipulation Cell. It is a bench-scale, fluid-powered manipulation system that senses its surroundings, decides what to do, acts through hydraulic actuators, and continuously checks itself against a digital twin.

It is not a tractor, not a field robot, not a crop-specific tool. It is a constrained-workspace manipulation platform — small enough to build and study, complete enough to demonstrate every principle of intelligent fluid power.

---

## The mission

Most "Physical AI" is built on electric motors. But the machines that feed and build the world — in agriculture, construction, mining, and heavy industry — run on fluid power. Almost no open educational material exists for bringing modern sensing, control, and intelligence into fluid-powered systems.

The Smart Agricultural Workcell exists to close that gap. It is the vehicle through which you learn to make a hydraulic machine *intelligent*.

---

## The three benchmark tasks

Everything the machine does reduces to three recurring tasks. Every module advances at least one of them. They are the workcell's equivalent of a harvesting robot's "pick the fruit" mission.

### Task 1 — Precision Positioning
Move a tool or end-effector to a target location accurately.
*Positioning, alignment, controlled approach.*
Developed most heavily in Modules 04–08.

### Task 2 — Force-Controlled Interaction
Apply a controlled force to an object without damaging it.
*Gripping, pressing, compliant contact.*
Developed most heavily in Modules 06–10.

### Task 3 — Intelligent Manipulation
Detect an object and execute a full autonomous manipulation sequence.
*Pick-and-place, inspection, sorting, handling.*
Developed most heavily in Modules 09–12.

After Module 12, the machine performs all three, autonomously, while validating itself.

---

## The six subsystems

The machine is organized into six subsystems. Each module develops one or more of them.

| Subsystem | What it is | Built in |
|-----------|-----------|----------|
| S1 — Hydraulic power | Motor, pump, relief, reservoir | Module 05 |
| S2 — Fluid transport | Hoses, pipes, filter, return line | Modules 03–04 |
| S3 — Motion control | Directional, flow, pressure valves | Module 06 |
| S4 — Actuation | Primary cylinder, end-effector actuator | Module 07 |
| S5 — Sensing & intelligence | Sensors, Arduino, Raspberry Pi | Modules 09–10 |
| S6 — Digital twin | Software model running alongside the machine | Modules 04–11 |

---

## Module-by-module: how the machine evolves

Each entry answers the only question that matters: **what can the machine do now that it could not do before?**

### Module 01 — Foundations
**Machine capability added:** *Understand the system.*
The machine exists as a complete concept. You can name its six subsystems, trace a command through all of them, and compute its core numbers (≈19.6 kN force, ≈85 mm/s, ≈1.67 kW). Nothing physical yet — but the whole machine is in view.
**Benchmark task advanced:** all three, at the conceptual level.
**Digital twin:** the idea of the twin is introduced; no model yet.
**Whiteboard after this module:** the whole workcell, labeled.

### Module 02 — Physical Architecture
**Machine capability added:** *Identify and select the physical components the machine is made of.*
Every subsystem now has real, named hardware: an 8 cc/rev gear pump, a 4/3 closed-center valve, a 50 mm cylinder, a return-line filter. You produce the machine's Component Map.
**Benchmark task advanced:** Precision Positioning and Force-Controlled Interaction both become physically concrete — you now know which parts produce motion and force.
**Digital twin:** component parameters (displacements, areas, ratings) are catalogued — the raw numbers the twin will use.
**Whiteboard after this module:** the workcell with its real components named on each subsystem.

### Module 03 — Working Fluid
**Machine capability added:** *Specify and maintain the fluid that carries the machine's power.*
The machine can now be correctly filled: ISO VG 46 oil, 18/16/13 cleanliness, a β₁₀≥100 filter, 10 mm supply lines. The Fluid Specification is the deliverable.
**Benchmark task advanced:** Precision Positioning — clean, correct-viscosity, air-free fluid is what makes precise, repeatable motion possible.
**Digital twin:** the first physical parameters the twin needs — bulk modulus, viscosity, density, line losses — are quantified and verified against code.
**Whiteboard after this module:** the machine, filled, with its fluid properties annotated on the lines.

### Module 04 — Predicting Behavior
**Machine capability added:** *Predict how the machine's hydraulics will behave before building them.*
The first true digital-twin components exist as tested code: the valve orifice model and the coupled cylinder ODE. The machine now has a software shadow that simulates its cylinder extending and holding.
**Benchmark task advanced:** Precision Positioning — you can now predict the cylinder's position and velocity over time, the foundation of positioning.
**Digital twin:** **born here.** `orifice_flow.py` (valve model) and `cylinder_dynamics.py` (force balance + pressure dynamics) produce the first prediction: cylinder motion in response to a valve command.
**Whiteboard after this module:** a position-vs-time curve of the cylinder, predicted by the twin.

### Module 05 — Generating Power *(planned)*
**Machine capability added:** *Generate hydraulic power.*
Subsystem 1 is sized and modeled — pump curves, efficiency, motor selection. The machine has a real power source.
**Benchmark task advanced:** Precision Positioning (the power to move).
**Digital twin:** a pump model is added — predicts available flow vs. pressure and speed.

### Module 06 — Controlling Motion *(planned)*
**Machine capability added:** *Direct and regulate motion.*
Subsystem 3 in detail. The machine can start, stop, reverse, and meter its motion.
**Benchmark task advanced:** Precision Positioning and Force-Controlled Interaction.
**Digital twin:** the valve model from Module 04 is refined and parameterized to the real valves.

### Module 07 — Producing Force and Motion *(planned)*
**Machine capability added:** *Produce sized, reliable linear force and motion.*
Subsystem 4 fully specified — bore, rod, stroke, buckling, cushioning.
**Benchmark task advanced:** Force-Controlled Interaction.
**Digital twin:** cylinder parameters finalized; the cylinder ODE is tuned to the chosen actuator.

### Module 08 — Integrating the Circuit *(planned)*
**Machine capability added:** *Operate as one complete hydraulic circuit.*
All four physical subsystems combine into a single schematic with an energy budget.
**Benchmark task advanced:** Precision Positioning (full actuation path validated).
**Digital twin:** the component models connect into one system simulation.

### Module 09 — Sensing *(planned)*
**Machine capability added:** *Perceive its own state.*
Subsystem 5 begins. The machine measures pressure, position, flow, and force.
**Benchmark task advanced:** all three — perception underlies everything intelligent.
**Digital twin:** sensor models (noise, calibration) added; real sensor data can now be compared to predictions.

### Module 10 — Deciding and Acting *(planned)*
**Machine capability added:** *Decide and act autonomously.*
PID control and a task state machine close the loop. The machine acts on its own.
**Benchmark task advanced:** Force-Controlled Interaction and Intelligent Manipulation.
**Digital twin:** the controller runs in simulation (control-in-the-loop) before touching hardware.

### Module 11 — Self-Validation *(planned)*
**Machine capability added:** *Check itself and detect faults.*
The twin components from Modules 04–10 integrate. Residual analysis compares prediction to measurement in real time.
**Benchmark task advanced:** Intelligent Manipulation (reliable, self-aware operation).
**Digital twin:** **fully integrated.** Predicts the whole system; flags faults from residuals.

### Module 12 — The Complete Machine *(planned)*
**Machine capability added:** *Perform autonomous, validated manipulation.*
All six subsystems work together. The machine executes the three benchmark tasks autonomously while the twin validates every action.
**Benchmark task advanced:** all three, demonstrated end-to-end.
**Digital twin:** demonstrated as a live fault-detection and monitoring system.

---

## The digital twin's growth

The twin is not bolted on at the end. It is grown, module by module, so that by Module 11 it is *integrated*, not *started*:

```
M03  parameters       bulk modulus, viscosity, density, line loss
M04  first models     valve orifice model + cylinder ODE  ← twin is born
M05  pump model       flow vs. pressure and speed
M06  valve refined    real valve parameters
M07  cylinder tuned   real actuator parameters
M08  system sim       components connected
M09  sensor models    noise + calibration; data comparison begins
M10  control-in-loop  controller simulated before hardware
M11  integrated twin  full-system prediction + residual fault detection
M12  demonstrated     live monitoring and fault detection
```

Every module's **Digital Twin Contribution** section states exactly what it adds.

---

## The final demonstration (Module 12)

After Module 12, the Smart Agricultural Workcell:

- **Senses** its pressure, position, flow, and force
- **Understands** that state through filtering and estimation
- **Decides** what to do via a task state machine
- **Commands** its valves through embedded control
- **Actuates** its cylinder to position and to apply controlled force
- **Validates** every action against a digital twin that was built across the entire course

It performs all three benchmark tasks — precision positioning, force-controlled interaction, and an intelligent pick-and-place manipulation sequence — autonomously, and it detects a deliberately induced fault through the twin's residuals.

That is the story. The machine is the protagonist. Each module is a chapter in which it becomes more capable.

---

*This document is maintained as the curriculum's narrative spine. Modules marked "(planned)" describe the designed arc from the manifests; Modules 01–04 are delivered and their entries reflect built content.*
