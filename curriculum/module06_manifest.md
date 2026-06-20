# Module 06 — Valves and Motion Control

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 06 of 12  
**Estimated Duration:** 2 weeks  
**Capstone Subsystems:** 3 (Motion Control)  
**Pipeline Stages:** COMMAND (valve receives signal), ACTUATE (valve controls flow)

> **Machine mission:** Controlling the Machine's Motion
>
> **Machine Capability Added:** Direct, protect, throttle, and command its motion.
>
> **Benchmark task advanced:** Precision Positioning (+ begins Force-Controlled Interaction)
>
> **Artifact:** Motion Control Architecture

---

## Module Purpose

Valves are the interface between intelligence and motion. Every command the embedded controller issues — *extend the cylinder, hold position, retract* — becomes a valve state. Understanding valves is understanding how the machine translates decisions into physical action.

This module covers valves from three angles: physical operation, mathematical modeling, and control signal interface. By the end, students can select a valve, model its flow behavior, and write the code to command it from an Arduino.

**Workcell contribution:** Students configure the valve circuit for the workcell and write their first valve command code.

---

## Learning Objectives

- LO-06.1: Explain the operating principle of directional, pressure, and flow control valves
- LO-06.2: Read and draw 4/3 and 4/2 directional control valve symbols (all spool positions)
- LO-06.3: Apply the orifice equation to model flow through a valve at a given opening
- LO-06.4: Describe how a solenoid valve converts an electrical signal to a spool position
- LO-06.5: Explain proportional valves and how they enable variable flow control from an analog signal
- LO-06.6: Write Arduino code to command a solenoid DCV (digital output) and a proportional valve (PWM output)
- LO-06.7: Describe meter-in vs. meter-out speed control and explain when each is preferred
- LO-06.8: Add the valve model to the digital twin simulation

---

## Prerequisite Knowledge

- Modules 01–05 complete
- Module 04: orifice flow equation
- Basic Arduino (digital output, PWM)

---

## Key Topics

### Topic 1 — Directional Control Valves in Depth
4/3 DCV: four ports, three positions. Spool center configurations (open center, closed center, tandem, float). Spring return vs. detent. Solenoid actuation: 12VDC and 24VDC. Response time.

**Workcell connection:** The workcell uses a 4/3 DCV with spring-centered closed center. Why closed center? Holding position without pump load.

### Topic 2 — Pressure Control Valves
Relief valve (system protection), pressure reducing valve (downstream limit), counterbalance valve (load holding), sequence valve (multi-actuator sequencing). Setting and adjustment.

**Workcell connection:** Where each type appears in the workcell circuit and why.

### Topic 3 — Flow Control and Speed Regulation
Throttle valve, needle valve, flow divider. Meter-in vs. meter-out. Temperature compensation (pressure-compensated flow control). Why meter-out is preferred for resisting loads.

**Workcell connection:** End effector speed control. Sizing the flow control for the required approach and grip speed.

### Topic 4 — Proportional Valves: Variable Control
How proportional valves differ from on/off valves. Spool position vs. current (I-Q curve). Hysteresis. Amplifier cards vs. direct Arduino PWM. The role of proportional valves in closed-loop position control.

**Workcell connection:** Upgrade path from on/off DCV to proportional valve — what capability is gained and at what cost.

### Topic 5 — Commanding Valves from Embedded Systems
Digital output for solenoid valves (relay or MOSFET driver). PWM output for proportional valves (frequency, duty cycle to current). Freewheeling diode for solenoid protection. Arduino code for each.

**Workcell connection:** First embedded control code for the workcell: extend, hold, retract sequence via serial command.

---

## Capstone Connection

**Deliverable this module:** Valve configuration document for the workcell (type, port connections, center condition, solenoid voltage) + working Arduino sketch: `valve_sequence.ino` demonstrating extend–hold–retract operation on command.

**Digital twin contribution:** Valve model integrated into cylinder simulation — `valve_opening(command, time)` replaces the ideal step input used in Modules 04–05.

---

## Labs

**Lab 06A — Valve Identification and Configuration**  
Identify valve types in a physical hydraulic panel or schematic. Trace the flow path for each valve state.

**Lab 06B — Arduino Valve Command**  
Wire a solenoid valve to an Arduino through a MOSFET driver. Write code to extend and retract a cylinder (or pneumatic equivalent) on serial command. Observe and record response.

---

## Code

`code/module06/valve_model.py` — Orifice-based valve model. Inputs: command signal (0–1), pressure drop. Output: flow rate. Plots Q vs. ΔP for several openings.

`code/module06/valve_sequence/valve_sequence.ino` — Arduino sketch: serial command interface for extend/hold/retract sequence.

---

## Assessment

- Draw the workcell 4/3 DCV in all three positions with correct ISO 1219 symbols
- Explain in writing: why does a closed-center DCV hold load without continuous pump flow?
- Simulation: compare step valve vs. proportional ramp opening on cylinder velocity profile

---

*Module 06 Manifest — Version 0.1*
