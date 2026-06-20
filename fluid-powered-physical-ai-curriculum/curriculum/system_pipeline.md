# System Pipeline

**Fluid-Powered Physical AI Curriculum**  
**Document Type:** Central Curriculum Artifact  
**Status:** ✅ Version 0.1

---

## The Pipeline

Every intelligent fluid-powered machine does six things.

```
SENSE → UNDERSTAND → DECIDE → COMMAND → ACTUATE → VALIDATE
```

This pipeline is the organizing principle of the curriculum. Every module develops one or more stages of this pipeline. By Module 12, students understand and can implement all six.

---

## Stage Definitions

### 1. SENSE

*What is the machine perceiving?*

The machine reads the physical world through sensors. In a fluid-powered system, the primary sensing targets are:

| Measurement | Sensor Type | Location in Workcell |
|-------------|-------------|----------------------|
| Pressure | Piezoelectric / strain gauge transducer | Cylinder ports, system line |
| Position | Linear potentiometer, magnetostrictive | Cylinder rod |
| Flow | Turbine, gear, Coriolis | Supply line |
| Force / Load | Load cell | End effector |
| Temperature | Thermocouple, PT100 | Reservoir, return line |
| Visual | USB camera, Pi Camera | End effector, workspace |

Sensing fails for predictable reasons: sensor drift, contamination, wiring noise, sampling rate mismatch. Understanding these failure modes is part of the curriculum.

**Primary module:** 09  
**Supporting modules:** 01, 04, 10

---

### 2. UNDERSTAND

*What does the measurement mean?*

Raw sensor signals are not knowledge. Understanding requires:

- **Signal conditioning:** filtering noise, removing offsets, scaling to physical units
- **State estimation:** inferring quantities that cannot be measured directly (e.g., actuator velocity from position derivative)
- **Model comparison:** comparing measured state to expected state from the digital twin

This stage is where embedded intelligence begins. A pressure reading becomes *the system is approaching stall*. A position reading becomes *the cylinder has reached 80% of stroke*.

**Primary modules:** 09, 10, 11  
**Supporting modules:** 04, 08

---

### 3. DECIDE

*What should the machine do next?*

Decision logic ranges from simple threshold-based control to model-based predictive control. In the curriculum, students implement:

- On/off control: valve open/close based on a single threshold
- Proportional control: valve opening proportional to error
- PID control: proportional-integral-derivative feedback loop
- Sequence logic: multi-step task execution
- Safety decisions: pressure override, fault detection

**Primary module:** 10  
**Supporting modules:** 06, 08, 11

---

### 4. COMMAND

*How does the machine issue instructions to its actuators?*

Commands travel from the embedded controller to the physical system:

```
Raspberry Pi (task logic)
    ↓  USB/UART
Arduino (low-level I/O)
    ↓  PWM / analog / digital
Valve amplifier / solenoid driver
    ↓  Electrical signal
Solenoid valve / proportional valve
```

This stage includes signal generation, communication protocols (I2C, SPI, UART), and the timing constraints of embedded real-time control.

**Primary module:** 10  
**Supporting modules:** 09, 12

---

### 5. ACTUATE

*How does the machine create physical motion?*

Actuation converts the command into fluid flow, fluid flow into pressure, and pressure into force and motion. This stage covers the full hydraulic chain:

```
Pump → Valve → Cylinder / Motor → Load
```

The actuation stage is where fluid power knowledge is most concentrated. It is also where the largest energy transformations occur.

**Primary modules:** 05, 06, 07  
**Supporting modules:** 02, 03, 04, 08

---

### 6. VALIDATE

*Is the machine behaving as intended?*

Validation operates at multiple timescales:

- **Real-time:** sensor feedback confirms the cylinder reached the target position
- **Session-level:** log data is reviewed to assess performance across a task sequence
- **Design-level:** the digital twin predicts what *should* happen; comparison with measurement reveals model error or hardware faults

Validation is not an afterthought. It is what makes the system intelligent rather than merely automated.

**Primary modules:** 11, 12  
**Supporting modules:** 04, 08, 09, 10

---

## Pipeline × Module Map

| Module | Primary Stage(s) | Contribution |
|--------|-----------------|--------------|
| 01 | All (overview) | Physical intuition for the full pipeline |
| 02 | ACTUATE | Component identification across the pipeline |
| 03 | ACTUATE | Fluid properties affect transmission and sensing |
| 04 | ACTUATE, VALIDATE | Fluid mechanics models used in digital twin |
| 05 | ACTUATE | Pump: energy input to the pipeline |
| 06 | ACTUATE, COMMAND | Valves: the interface between command and motion |
| 07 | ACTUATE | Cylinders/motors: mechanical output of the pipeline |
| 08 | ACTUATE, VALIDATE | Circuit design: the physical pipeline as a whole |
| 09 | SENSE | All sensor types, signal conditioning, wiring |
| 10 | UNDERSTAND, DECIDE, COMMAND | Embedded control: the intelligence layer |
| 11 | VALIDATE | Digital twin: simulated pipeline for comparison |
| 12 | All (integration) | Full pipeline in one working system |

---

## Pipeline as Diagnostic Tool

The pipeline is also a debugging framework. When something goes wrong in the workcell, students ask:

1. **SENSE:** Am I reading the sensor correctly? Is the signal conditioned?
2. **UNDERSTAND:** Is my state estimate accurate? Is my model correct?
3. **DECIDE:** Is my control logic handling this condition?
4. **COMMAND:** Did the command reach the valve? Is the wiring correct?
5. **ACTUATE:** Is the valve opening? Is the cylinder moving?
6. **VALIDATE:** Does the digital twin predict this behavior?

This transforms troubleshooting from guesswork into systematic inquiry.

---

## Incremental Digital Twin Build

The digital twin is built stage by stage alongside the pipeline:

| Stage | Digital Twin Component Added |
|-------|------------------------------|
| SENSE | Sensor noise model, sampling rate |
| UNDERSTAND | State estimator, filter model |
| DECIDE | Control logic simulation |
| COMMAND | Command latency model |
| ACTUATE | Cylinder dynamics (pressure, force, velocity) |
| VALIDATE | Full system simulation, comparison to measured data |

Students do not encounter a complete digital twin in Module 11. They encounter a twin they have been building since Module 04.

---

*system_pipeline.md — Version 0.1*  
*This document is a living artifact. Update when module content changes the pipeline mapping.*
