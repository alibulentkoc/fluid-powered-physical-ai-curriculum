# Module 05 — Hydraulic Pumps and Power Generation

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 05 of 12  
**Estimated Duration:** 1.5 weeks  
**Capstone Subsystems:** 1 (Hydraulic Power)  
**Pipeline Stages:** ACTUATE (energy source)

> **Machine mission:** Powering the Smart Agricultural Workcell
>
> **Machine Capability Added:** Generate hydraulic power.
>
> **Benchmark task advanced:** Precision Positioning
>
> **Artifact:** Hydraulic Power Unit Design

---

## Module Purpose

The pump is where the system begins. It converts rotational mechanical energy into pressurized flow. Everything else in the workcell is downstream of this conversion.

Students leave this module able to select, size, and model a pump for the workcell, and to account for the pump's real behavior — including volumetric and mechanical efficiency — in the digital twin.

**Workcell contribution:** Students finalize the pump specification for the Smart Agricultural Workcell and add the pump model to the digital twin.

---

## Learning Objectives

- LO-05.1: Explain the operating principle of gear, vane, and piston pumps
- LO-05.2: Define displacement, flow rate, volumetric efficiency, and overall efficiency
- LO-05.3: Calculate theoretical pump flow from displacement and shaft speed
- LO-05.4: Correct theoretical flow for volumetric efficiency to get actual flow
- LO-05.5: Calculate pump input power from flow, pressure, and efficiency
- LO-05.6: Size a pump for the workcell based on actuator flow and pressure requirements
- LO-05.7: Model pump flow and efficiency in Python and add this model to the digital twin

---

## Prerequisite Knowledge

- Modules 01–04 complete

---

## Key Topics

### Topic 1 — Pump Operating Principles
Positive displacement vs. dynamic (centrifugal). Why hydraulic systems use positive displacement. Gear pump geometry and operation. Introduction to vane and piston types.

### Topic 2 — Flow Rate, Displacement, and Speed
Theoretical flow: Q_t = D × n (displacement × speed). Actual flow: Q_a = Q_t × η_v. Leakage as the primary source of volumetric loss.

### Topic 3 — Efficiency and Input Power
Volumetric efficiency (η_v). Mechanical efficiency (η_m). Overall efficiency (η = η_v × η_m). Input power: P_in = (p × Q_a) / η. Why pump efficiency matters for system energy consumption.

### Topic 4 — Pump Selection and Sizing
Matching pump displacement to actuator requirements. Pressure-flow characteristic curves. Speed limits (cavitation at high speed, inadequate flow at low speed). Noise and pulsation.

**Workcell connection:** Students size the gear pump for the workcell: required flow (from Module 07 cylinder sizing, previewed here), maximum system pressure, shaft speed from the motor.

### Topic 5 — Pump Model for the Digital Twin
Flow-speed-pressure characteristic as a look-up model. Volumetric efficiency as a function of pressure. Adding the pump model to the simulation from Module 04.

---

## Capstone Connection

**Deliverable this module:** Pump specification sheet for the Smart Agricultural Workcell. Includes: pump type, displacement (cc/rev), rated speed (RPM), rated pressure (bar), volumetric efficiency curve, motor power requirement.

**Digital twin contribution:** `pump_model(speed_rpm, pressure_bar) → flow_lpm` — replaces the fixed flow assumption used in Module 04 simulation.

---

## Labs

**Lab 05 — Pump Characterization**  
If hardware is available: measure pump output flow at several shaft speeds and pressures. Plot the Q-P characteristic. Calculate volumetric efficiency. Compare to manufacturer datasheet.

If hardware is not available: use the Python model to simulate the characteristic curve. Vary leakage coefficient and observe the effect.

---

## Code

`code/module05/pump_model.py` — Gear pump flow model. Inputs: displacement, speed, pressure. Outputs: theoretical flow, actual flow, volumetric efficiency. Plots Q vs. speed at several pressures.

---

## Assessment

- Calculation: size a pump for stated workcell requirements
- Explain why pump volumetric efficiency decreases at high pressure
- Add pump model to Module 04 cylinder simulation and plot system pressure vs. time during startup

---

*Module 05 Manifest — Version 0.1*
