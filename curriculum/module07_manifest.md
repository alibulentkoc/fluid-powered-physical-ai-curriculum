# Module 07 — Hydraulic Cylinders and Motors

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 07 of 12  
**Estimated Duration:** 2 weeks  
**Capstone Subsystems:** 4 (Actuation)  
**Pipeline Stages:** ACTUATE

---

## Module Purpose

Cylinders and motors are where fluid power becomes physical motion. This module takes students from the component-level understanding of Module 02 and the dynamic equations of Module 04 to a complete actuator engineering process: sizing, modeling, and validating the actuation layer of the workcell.

By the end, students have sized both actuators in their workcell — the primary positioning cylinder and the end-effector actuator — and have the models to predict their force, speed, and efficiency.

**Workcell contribution:** Students finalize actuator specifications and complete the actuation layer of the digital twin.

---

## Learning Objectives

- LO-07.1: Calculate extend and retract force for a double-acting cylinder (Pascal's Law applied to both sides)
- LO-07.2: Calculate piston velocity and acceleration from flow rate and bore area
- LO-07.3: Analyze the differential cylinder effect (ratio of extend to retract speed)
- LO-07.4: Select a cylinder for a given load, speed, and pressure specification
- LO-07.5: Explain the role of cushioning, sealing, and rod guide in cylinder performance
- LO-07.6: Describe the operating principle and torque-speed relationship of a hydraulic motor
- LO-07.7: Compare the application domains of cylinders (linear, intermittent) vs. motors (rotary, continuous)
- LO-07.8: Write the refined cylinder dynamics model for the workcell's primary actuator

---

## Prerequisite Knowledge

- Modules 01–06 complete
- Module 04 cylinder dynamics ODE

---

## Key Topics

### Topic 1 — Double-Acting Cylinder: Complete Analysis
Full bore force vs. rod side force. Area ratio and its practical consequences. Differential connection (regenerative circuit). Stroke and work envelope. Buckling analysis for long-stroke cylinders (Euler column).

**Workcell connection:** Primary cylinder sizing: minimum bore for 500 N load at 50 bar system pressure. Stroke for 300 mm reach.

### Topic 2 — Cylinder Selection and Specification
Bore, stroke, rod diameter, mounting style, seal material. Manufacturer datasheets. Pressure rating vs. working pressure (design factor). Temperature range and fluid compatibility.

**Workcell connection:** Students produce a cylinder selection specification sheet for both actuators in the workcell.

### Topic 3 — Cylinder Performance Modeling
Friction models (Stribeck curve: static, Coulomb, viscous). Seal breakout force. Velocity-dependent effects. Cushion behavior at end of stroke. How these affect the digital twin accuracy.

**Workcell connection:** Adding friction to the Module 04 cylinder model and observing the effect on simulated step response.

### Topic 4 — Hydraulic Motors: Torque and Speed
Motor displacement, torque, and speed relationships. Volumetric and mechanical efficiency for motors (analogous to pumps but reversed). Gear motors, vane motors, and bent-axis motors.

**Workcell connection:** If the end effector uses a motor (e.g., rotary gripper): torque and speed sizing.

### Topic 5 — Cylinder vs. Motor: Application Logic
When to use a cylinder (linear, high-force, finite stroke, position hold). When to use a motor (continuous rotation, speed control, compact packaging). Hybrid applications.

**Workcell connection:** Justification of the actuator choice for each end effector task in the workcell.

---

## Capstone Connection

**Deliverable this module:** Actuator specification sheet for the Smart Agricultural Workcell. Primary cylinder and end-effector actuator, with: bore, rod, stroke, pressure rating, mount type, expected force, expected speed. Updated digital twin with friction model.

**Digital twin contribution:** Refined cylinder dynamics with Stribeck friction. Cushion model (optional extension). Motor model if applicable.

---

## Labs

**Lab 07 — Force and Velocity Measurement**  
Measure the actual extend force and velocity of a hydraulic (or pneumatic) cylinder at several pressures and flow rates. Compare to calculated values. Identify friction loss.

---

## Code

`code/module07/cylinder_sizing.py` — Interactive sizing tool: input load, pressure, required speed → output recommended bore, rod diameter, required flow.

`code/module07/friction_model.py` — Stribeck friction curve for hydraulic cylinder. Plot friction force vs. velocity. Integrate into Module 04 ODE.

---

## Assessment

- Size the primary workcell cylinder from first principles
- Explain why retract force is always less than extend force for a given pressure
- Simulation: compare cylinder step response with and without friction model

---

*Module 07 Manifest — Version 0.1*
