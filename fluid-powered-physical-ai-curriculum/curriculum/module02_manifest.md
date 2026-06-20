# Module 02 — Hydraulic Components and System Architecture

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 02 of 12  
**Estimated Duration:** 2 weeks  
**Capstone Subsystems:** 1 (Hydraulic Power), 2 (Fluid Transport)  
**Pipeline Stages:** ACTUATE

> **Machine mission for this module:** Building the Physical Architecture of the Smart Agricultural Workcell
>
> **Machine Capability Added:** Identify and select the machine's physical components.
>
> **Benchmark task advanced:** Precision Positioning, Force-Controlled Interaction

---

## Module Purpose

Module 01 gave students a mental model. Module 02 makes it concrete.

Students move from the abstract five-element model of a hydraulic system to the actual hardware. They learn to identify real components by name and function, read schematic symbols, and trace energy flow through a physical system. By the end, they can look at a hydraulic power unit and explain what every component does and why it is there.

This module establishes the vocabulary and component knowledge that every subsequent module depends on.

**Workcell contribution:** Students produce the first component map of the Smart Agricultural Workcell — a block diagram naming the actual components that will appear in the physical build.

---

## Learning Objectives

- LO-02.1: Identify and describe the function of each major hydraulic component: pump, motor, reservoir, filter, relief valve, check valve, directional control valve, cylinder, hose, and fitting
- LO-02.2: Read and draw basic hydraulic circuit symbols following ISO 1219 conventions
- LO-02.3: Explain the difference between fixed and variable displacement pumps, and when each is appropriate
- LO-02.4: Trace energy flow from the electric motor through the pump, fluid, valves, and cylinder
- LO-02.5: Identify the six subsystems of the Smart Agricultural Workcell in a physical or schematic representation
- LO-02.6: Explain why each component category is necessary — what fails if it is removed

---

## Prerequisite Knowledge

- Module 01 complete: Pascal's Law, continuity, hydraulic power equation
- No component knowledge assumed

---

## Key Topics

### Topic 1 — Pumps: The Heart of the System
Fixed vs. variable displacement. Gear pumps, vane pumps, piston pumps. Flow-speed relationship. Volumetric efficiency. Why pump selection drives the whole system.

**Workcell connection:** The workcell baseline uses a fixed-displacement gear pump. Students calculate whether it can supply the required flow at the required pressure.

### Topic 2 — Valves: Direction, Pressure, and Flow
Three families of valves and their roles. Directional control valves (2/2, 3/2, 4/2, 4/3): notation, spool positions, spring return, solenoid actuation. Pressure control: relief, reducing, sequence, counterbalance. Flow control: throttle, needle, flow divider.

**Workcell connection:** The workcell uses a 4/3 solenoid DCV and a pressure relief valve. Students draw their workcell's valve configuration for the first time.

### Topic 3 — Cylinders and Motors
Double-acting cylinder anatomy: bore, rod, seal, port, end cap, cushion. Hydraulic motor types: gear, vane, piston. Differences in application.

**Workcell connection:** Students identify primary and secondary actuator choices for the workcell's manipulation tasks.

### Topic 4 — The Support System: Reservoir, Filter, Hoses, Fittings
Why the reservoir is more than a tank. Filter placement and rating (Beta ratio). Hose vs. pipe selection. Fitting standards (BSP, JIC, SAE). Contamination as the primary cause of hydraulic failure.

**Workcell connection:** Students specify the workcell reservoir volume and filter rating based on component requirements.

---

## Capstone Connection

**Deliverable this module:** First draft of the Smart Agricultural Workcell Component Map — a block diagram showing all six subsystems with real component names filled in for Subsystems 1 and 2.

---

## Labs

**Lab 02A — Component Identification**  
Given a physical or photographed hydraulic power unit, identify and label every component. Match to ISO 1219 symbols.

**Lab 02B — Circuit Tracing**  
Given a hydraulic schematic, trace the flow path for each valve position. Identify what happens at each actuator.

---

## Code

`code/module02/pump_flow_model.py` — Plot pump output flow vs. shaft speed for a fixed-displacement gear pump. Include volumetric efficiency curve.

---

## Assessment

- Symbol identification quiz (20 ISO 1219 symbols)
- Short answer: trace energy flow from motor shaft to cylinder rod in the workcell
- Component map submission (first draft)

---

## Connections Forward

- Module 03 specifies the fluid that fills the system just mapped
- Module 05 sizes the pump chosen here
- Module 06 configures the valves chosen here
- Module 07 sizes the cylinders chosen here

---

*Module 02 Manifest — Version 0.1*
