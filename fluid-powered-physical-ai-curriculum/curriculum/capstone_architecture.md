# Capstone Architecture

**Fluid-Powered Physical AI Curriculum**  
**Document Type:** Central Curriculum Artifact  
**Status:** ✅ Version 0.1

---

## The Machine

**Technical name:** Intelligent Fluid-Powered Agricultural Manipulation Cell  
**Student-facing name:** Smart Agricultural Workcell

The Smart Agricultural Workcell is a constrained-workspace manipulation platform actuated by fluid power. It operates within a defined work envelope — bench-scale or small-frame mounted — and performs manipulation tasks under embedded intelligent control.

It is not a field vehicle. It is not a crop-specific tool. It is a platform: a research-compatible, curriculum-first foundation for exploring what intelligent fluid power looks like.

---

## Six Subsystems

The workcell is divided into six subsystems. Every module in the curriculum maps to one or more of these. Together they define what the machine is, how it works, and how intelligence is embedded in it.

---

### Subsystem 1 — Hydraulic Power

*Power generation and storage*

**What it does:** Converts electrical or mechanical energy into pressurized hydraulic flow. Supplies the energy that everything else consumes.

**Physical components:**
- Electric motor (drives the pump)
- Hydraulic pump (fixed displacement gear pump for baseline build)
- Pressure relief valve (system protection)
- Accumulator (optional — pressure storage and shock absorption)
- Reservoir (fluid storage, heat rejection, air separation)

**Key parameters:**
- System pressure: up to 100 bar (educational build) / up to 250 bar (research extension)
- Flow rate: 5–20 LPM
- Motor power: 0.75–2.2 kW

**Digital twin contribution:** Pump model — flow vs. speed characteristic, volumetric efficiency

**Pipeline stages:** ACTUATE (energy source)

**Primary curriculum modules:** 05

**Supporting modules:** 02, 03, 08

---

### Subsystem 2 — Fluid Transport

*Hoses, pipes, fittings, and the reservoir*

**What it does:** Moves pressurized fluid between components. Introduces the real-world effects of viscosity, pipe friction, and pressure drop that the ideal equations ignore.

**Physical components:**
- Supply line (pump to valve)
- Return line (valve to reservoir)
- Case drain line (for motors with internal leakage)
- Hoses (flexible connections to moving components)
- Fittings (BSP, JIC, or SAE — standardized)
- Filter (return line or pressure line, typically 10–25 micron)
- Heat exchanger / cooler (for sustained operation)
- Reservoir (with level gauge, breather, clean-out plate)

**Key parameters:**
- Pipe inner diameter (affects velocity and pressure drop)
- Hose rating (burst pressure, working pressure)
- Filter rating (Beta ratio, micron rating)
- Fluid temperature range

**Digital twin contribution:** Pipe friction loss model (Darcy-Weisbach), temperature model

**Pipeline stages:** ACTUATE (transmission), VALIDATE (loss accounting)

**Primary curriculum modules:** 03, 04

**Supporting modules:** 02, 08

---

### Subsystem 3 — Motion Control

*Valves, flow control, and pressure control*

**What it does:** Governs where fluid goes, how fast it flows, and at what pressure. This is the control interface between the electrical command layer and the mechanical actuation layer.

**Physical components:**
- Directional control valve (DCV): 4/3 or 4/2, solenoid-actuated
- Pressure relief valve (system and circuit protection)
- Flow control valve (meter-in or meter-out speed control)
- Check valve (prevents reverse flow)
- Proportional valve (optional — variable flow/pressure control from analog signal)

**Key parameters:**
- Valve flow coefficient (Cv or Kv)
- Solenoid voltage and current (12VDC or 24VDC typical)
- Proportional valve hysteresis and repeatability
- Response time (ms)

**Digital twin contribution:** Valve flow model (orifice equation), switching transient model

**Pipeline stages:** COMMAND (valve receives command), ACTUATE (valve controls flow)

**Primary curriculum modules:** 06

**Supporting modules:** 08, 10

---

### Subsystem 4 — Actuation

*Cylinders and motors*

**What it does:** Converts pressurized fluid into mechanical motion and force. The primary actuator determines the workcell's reach, force, and speed envelope.

**Physical components (baseline):**
- Primary cylinder: double-acting, 40–63 mm bore, 200–400 mm stroke (positioning and lifting)
- Secondary actuator: smaller cylinder or hydraulic motor (end-effector control)
- Rod seal and end cap (leakage prevention)
- Clevis or flange mounts

**Key parameters:**
- Bore and rod diameter (determine force and area ratio)
- Stroke length (work envelope)
- Sealing system (temperature and fluid compatibility)
- Cushioning (deceleration at end of stroke)

**Digital twin contribution:** Cylinder dynamics model — force balance, friction, seal compliance

**Pipeline stages:** ACTUATE

**Primary curriculum modules:** 07

**Supporting modules:** 04, 08, 10

---

### Subsystem 5 — Sensing and Intelligence

*Sensors, embedded systems, and computer vision*

**What it does:** Perceives the state of the physical system, processes that information, and generates commands. This is where fluid power becomes *Physical AI*.

**Physical components:**

*Sensing:*
- Pressure transducer × 2 (cylinder ports, 0–100 bar, 4–20 mA output)
- Linear position sensor (cylinder rod, 0–10V or PWM)
- Flow sensor (supply line, turbine type)
- Load cell (end effector, 0–500 N)
- Thermocouple or PT100 (reservoir)
- USB camera or Raspberry Pi Camera (workspace)

*Embedded systems:*
- Arduino Mega (low-level I/O: sensor reading, valve control, PWM generation)
- Raspberry Pi 4 (high-level control: task logic, vision, digital twin interface, logging)

*Communication:*
- Arduino ↔ Raspberry Pi: USB serial (UART)
- Sensors ↔ Arduino: analog (0–5V, 4–20mA via shunt), I2C, SPI
- Raspberry Pi ↔ network: Ethernet / Wi-Fi for remote monitoring

**Digital twin contribution:** Sensor noise model, state estimator, control algorithm simulation

**Pipeline stages:** SENSE, UNDERSTAND, DECIDE, COMMAND

**Primary curriculum modules:** 09, 10

**Supporting modules:** 01, 11, 12

---

### Subsystem 6 — Digital Twin

*Simulation, validation, and monitoring*

**What it does:** Runs a real-time or near-real-time software model of the physical system. Compares predicted and measured states. Supports fault detection, parameter identification, and design iteration without touching hardware.

**Software components:**
- Cylinder dynamics ODE (SciPy `solve_ivp`)
- Valve flow model (orifice equation, lookup table)
- Pump model (speed-flow characteristic)
- Pipe friction model (Darcy-Weisbach)
- Sensor noise model (Gaussian, drift)
- State estimator (Kalman filter, optional)
- Logging and comparison dashboard (Matplotlib or Jupyter)

**Key interactions:**
- Receives: sensor data from the physical system (via Raspberry Pi log or live stream)
- Outputs: predicted states, residuals (measured − predicted), fault flags

**Digital twin contribution:** *This subsystem is the digital twin.*

**Pipeline stages:** VALIDATE

**Primary curriculum modules:** 11

**Supporting modules:** 04, 05, 06, 07, 08, 10, 12

---

## Subsystem × Module Map

| Subsystem | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 |
|-----------|----|----|----|----|----|----|----|----|----|----|----|----|
| 1: Hydraulic Power | ◇ | ● | ◇ | ◇ | ● | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ● |
| 2: Fluid Transport | ◇ | ● | ● | ● | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ● |
| 3: Motion Control | ◇ | ◇ | ◇ | ◇ | ◇ | ● | ◇ | ◇ | ◇ | ● | ◇ | ● |
| 4: Actuation | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ● | ◇ | ◇ | ◇ | ◇ | ● |
| 5: Sensing & Intel. | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ● | ● | ◇ | ● |
| 6: Digital Twin | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ◇ | ● | ● |

**Legend:** ● Primary | ◇ Supporting | (blank) Not covered

---

## Work Envelope and Task Space

The workcell operates within a roughly 500 mm × 500 mm × 400 mm envelope. Within that space, interchangeable end effectors perform manipulation tasks:

| Task | End Effector | Subsystems Active |
|------|-------------|------------------|
| Grasping | Parallel jaw gripper | 3, 4, 5 |
| Positioning | Rigid probe / platform | 3, 4, 5 |
| Lifting | Fork / platform | 1, 3, 4, 5 |
| Sorting | Gripper + lateral motion | 3, 4, 5, 6 |
| Inspection | Camera mount | 5 |
| Pruning assist | Low-force scissor head | 3, 4, 5 |

The baseline capstone implements **positioning** and **grasping** as the two required tasks. Additional tasks are extensions.

---

## Integration Sequence

The workcell does not appear fully formed. It is assembled across the curriculum:

| Module | What the Student Adds to the Workcell |
|--------|---------------------------------------|
| 01 | Mental model: what the machine is and why |
| 02 | Component map: names and functions of every part |
| 03 | Fluid selection: which hydraulic oil, why |
| 04 | First physics model: pressure drop, flow velocity |
| 05 | Pump sizing: how much flow and pressure the system needs |
| 06 | Valve selection and configuration: controlling motion |
| 07 | Cylinder sizing: force and speed for the manipulation tasks |
| 08 | Complete circuit diagram: the hydraulic system on paper |
| 09 | Sensor layer: instruments, wiring, signal conditioning |
| 10 | Control layer: Arduino + Pi code, closed-loop position control |
| 11 | Digital twin: Python simulation of the complete system |
| 12 | Integration and demonstration: everything running together |

---

*capstone_architecture.md — Version 0.1*  
*This document is the source of truth for module-to-subsystem mapping.*  
*Update when hardware or software specifications change.*
