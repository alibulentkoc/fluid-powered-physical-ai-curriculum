# Module 08 — Hydraulic Circuit Design and Integration

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 08 of 12  
**Estimated Duration:** 2 weeks  
**Capstone Subsystems:** 1, 2, 3, 4 (full hydraulic system integration)  
**Pipeline Stages:** ACTUATE, VALIDATE

---

## Module Purpose

Modules 02–07 developed knowledge of individual components. Module 08 puts the system together.

Students draw, analyze, and simulate a complete hydraulic circuit for the Smart Agricultural Workcell. They learn to think about circuit design as a systems engineering problem: energy budgets, sequencing, protection, and the interaction between components that no individual component analysis reveals.

This is the module where students produce the **complete hydraulic schematic of their workcell** — the master document that drives hardware procurement and assembly.

**Workcell contribution:** Complete hydraulic circuit schematic, system energy analysis, and integrated simulation of the full hydraulic system (pump + transport + valve + cylinder).

---

## Learning Objectives

- LO-08.1: Draw a complete hydraulic circuit diagram for a two-actuator system using ISO 1219 symbols
- LO-08.2: Analyze a circuit for series, parallel, and independent actuator operation
- LO-08.3: Calculate system pressure and flow demand under worst-case operating conditions
- LO-08.4: Identify and explain the function of every protection element in the circuit (relief, check, counterbalance)
- LO-08.5: Perform a system energy balance: pump input power vs. useful work vs. heat generated
- LO-08.6: Explain the causes and consequences of hydraulic shock and describe circuit design strategies to minimize it
- LO-08.7: Simulate the complete workcell hydraulic circuit (pump → transport → valve → cylinder) in Python
- LO-08.8: Identify the signals that the sensing and control layer (Modules 09–10) must monitor to protect and control this circuit

---

## Prerequisite Knowledge

- Modules 01–07 complete
- Module 04: cylinder ODE simulation

---

## Key Topics

### Topic 1 — Circuit Design Principles
Open vs. closed-center circuits. Open vs. closed-loop circuits (hydrostatic transmission). Load-sensing circuits. Why the center condition of the DCV determines system energy consumption at rest.

**Workcell connection:** The workcell uses an open-center or closed-center circuit — students justify their choice.

### Topic 2 — Multi-Actuator Circuits
Series vs. parallel actuator connections. Pressure intensification in series circuits. Flow sharing in parallel. Priority valves. Sequencing valves vs. programmed sequencing.

**Workcell connection:** The workcell's two actuators (primary cylinder + end-effector actuator) operate in sequence, not simultaneously. Students design the sequencing logic.

### Topic 3 — Circuit Protection
Relief valve placement (system and port relief). Check valves to prevent reverse flow and cylinder drift. Counterbalance valves for over-running loads. Thermal relief. Filter placement.

**Workcell connection:** What happens if the workcell DCV loses power while the cylinder is extended under load? Design the circuit to handle this safely.

### Topic 4 — Energy Analysis and Heat Generation
System efficiency from pump shaft to cylinder rod. Heat rejected to the fluid. Required reservoir volume and cooler sizing. Why efficiency matters in continuous-duty applications.

**Workcell connection:** Energy budget for the workcell at continuous duty (e.g., 10 cycles/minute). Required reservoir volume and whether a cooler is needed.

### Topic 5 — Integrated System Simulation
Combining the pump model (Module 05), valve model (Module 06), and cylinder model (Module 07) into a single simulation. System startup transient. Response to a complete task cycle.

**Workcell connection:** Simulate a full positioning task cycle: startup → extend → hold → retract → stop. Plot pressure, flow, position, and force vs. time.

---

## Capstone Connection

**Major deliverable this module:** Complete Hydraulic Circuit Schematic for the Smart Agricultural Workcell — full ISO 1219 schematic with component identification numbers, port labels, pressure ratings, and a component list.

**Digital twin contribution:** Full integrated simulation: `code/module08/workcell_circuit_sim.ipynb` — the most complete version of the digital twin to date. This notebook becomes the foundation that Module 11 will refine.

---

## Labs

**Lab 08 — Circuit Build and Trace**  
Build or configure a two-actuator circuit (bench hydraulic trainer or low-pressure equivalent). Operate both actuators in sequence. Measure pressure at key points. Compare to predicted values.

---

## Code

`code/module08/workcell_circuit_sim.ipynb` — Full integrated simulation of the workcell hydraulic circuit through a complete task cycle.

`code/module08/energy_analysis.py` — System energy balance: calculate pump input power, useful work, and heat generated for a specified duty cycle.

---

## Assessment

- Draw the complete workcell circuit from memory (open-book for reference symbols only)
- Energy analysis calculation: is a cooler required for the specified duty cycle?
- Simulation: predict the system pressure during a hold phase with a closed-center DCV

---

## Connections Forward

Module 08 closes the hydraulic system engineering arc (Modules 02–08). Beginning with Module 09, the curriculum shifts focus to the intelligence layer: sensing, embedded control, and digital twin development. Students enter Module 09 with a fully designed hydraulic system whose behavior they can predict and simulate.

---

*Module 08 Manifest — Version 0.1*
