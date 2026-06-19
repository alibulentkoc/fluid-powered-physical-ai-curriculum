# Capstone Project — Intelligent Fluid-Powered Agricultural Manipulation Cell

**Curriculum:** Fluid-Powered Physical AI  
**Module:** 12 (Capstone Integration)  
**Status:** 🟡 Overview complete. Detailed specs in development.

---

## What This Is

The Intelligent Fluid-Powered Agricultural Manipulation Cell is the physical and computational system you will build toward throughout this curriculum.

It is not a tractor. It is not a field vehicle. It is a constrained-workspace manipulation platform: a compact, bench-mountable or frame-mountable system that uses fluid power to perform precise manipulation tasks within a defined work envelope.

Think of it less like a combine harvester and more like a hydraulic collaborative robot. The physical scale is modest. The engineering challenge is real.

---

## Why Build This?

Agricultural robotics is dominated by electric actuators. But agricultural machinery — the actual equipment in the field — runs overwhelmingly on hydraulic power. Every tractor has a hydraulic system. Every large implement uses it. The hydraulic output of a standard tractor is substantial, available, and largely untapped by the robotics community.

The manipulation cell asks: *what if you designed an intelligent attachment that used the tractor's existing hydraulic system as its power source?*

This is not a hypothetical. Hydraulic attachments for tractors — grapples, lifters, pruning heads, sorting mechanisms — already exist as dumb tools. The research and educational opportunity is in making them smart: sensing, adaptive, and capable of closed-loop control.

The manipulation cell is a bench-scale prototype of that idea.

---

## System Architecture

The manipulation cell consists of five integrated subsystems:

```
┌─────────────────────────────────────────────────┐
│         INTELLIGENT MANIPULATION CELL           │
│                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │  Hydraulic│    │ Sensing &│    │ Embedded │  │
│  │  Structure│    │ Instr.   │    │ Control  │  │
│  │  (Mech.) │    │ (Elec.)  │    │ (Comp.)  │  │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘  │
│       │               │               │         │
│  ┌────▼───────────────▼───────────────▼─────┐  │
│  │            System Integration             │  │
│  └───────────────────┬───────────────────────┘  │
│                      │                           │
│              ┌───────▼───────┐                  │
│              │  Digital Twin │                  │
│              └───────────────┘                  │
└─────────────────────────────────────────────────┘
```

### Subsystem 1 — Hydraulic Structure (Modules 02–08)

The physical actuation mechanism. At minimum:

- **Primary actuator:** Single double-acting hydraulic cylinder for positioning or lifting
- **Secondary actuator:** Cylinder or motor for end-effector control (grip, rotate, or tilt)
- **Power unit:** A small hydraulic power unit (HPU) — a reservoir, pump, motor, pressure relief valve, and filter — sized for bench operation (typically 0.5–2 kW, 10–50 bar working pressure for educational settings)
- **Directional control:** Electro-hydraulic directional control valve (DCV) with solenoid actuation
- **Pressure relief:** Fixed or adjustable relief valve to protect the circuit
- **End effector:** Interchangeable. See task list below.

### Subsystem 2 — Sensing and Instrumentation (Module 09)

- **Pressure sensors:** Monitoring cylinder ports and system pressure (analog output, 0–5V or 4–20mA)
- **Position sensors:** Linear potentiometer or magnetostrictive position transducer on the primary cylinder
- **Flow sensor:** Turbine or gear-type flow sensor on the supply line
- **Camera:** USB or Pi Camera for vision-based task feedback (optional for early builds, required for full capstone)
- **Force/load cell:** On the end effector for grip force measurement

### Subsystem 3 — Embedded Control (Module 10)

- **Microcontroller:** Arduino Uno or Mega for low-level valve and sensor I/O
- **Single-board computer:** Raspberry Pi 4 for higher-level control, vision processing, and digital twin interface
- **Interface:** PWM or analog voltage outputs to proportional valve amplifiers (if proportional valves used); digital outputs to solenoid valves
- **Communication:** I2C/SPI for sensors; USB or UART between Arduino and Raspberry Pi

### Subsystem 4 — System Integration (Module 12)

The integration layer connects subsystems 1–3 into a functioning manipulation cell. This includes:
- Control loop implementation (position or force control)
- Task-level programming (automated manipulation sequences)
- HMI: a simple web or GUI interface for monitoring and manual override

### Subsystem 5 — Digital Twin (Module 11)

A software model of the physical system running in parallel:
- Simulates cylinder dynamics (pressure, position, velocity)
- Receives sensor data from the physical system
- Compares predicted and measured states
- Supports parameter identification and fault detection

Implemented in Python using SciPy for ODE integration.

---

## Manipulation Tasks

The manipulation cell supports a range of interchangeable end-effector tasks. Not all need to be implemented in a single build. The curriculum recommends implementing at least two:

| Task | End Effector | Primary Sensor |
|------|-------------|---------------|
| Grasping | Parallel jaw gripper | Force / load cell |
| Positioning | Rigid probe or platform | Position + pressure |
| Lifting | Lifting fork or platform | Load cell + position |
| Sorting | Gripper + lateral positioning | Camera + position |
| Inspection | Camera mount | Camera |
| Pruning assistance | Scissor head (low force) | Position + force |

---

## Physical Specifications (Baseline Build)

These are provisional specifications for the baseline educational build. See `ARCHITECT_DECISIONS.md` (AD-002, AD-007) for rationale.

| Parameter | Value |
|-----------|-------|
| Working pressure (max) | 100 bar (1450 PSI) |
| Primary cylinder bore | 40–63 mm |
| Primary cylinder stroke | 200–400 mm |
| Pump flow rate | 5–20 LPM |
| Motor power | 0.75–2.2 kW |
| Working envelope | ~500 mm × 500 mm |
| Fluid | Hydraulic oil ISO VG 46 |
| Controller | Arduino Mega + Raspberry Pi 4 |

*Note: A low-pressure variant (under 15 bar) using pneumatic components can substitute for most of Modules 01–06. See ARCHITECT_DECISIONS.md AD-007.*

---

## How This Builds Across the Curriculum

| Module | Contribution to the Cell |
|--------|--------------------------|
| 01 | Physical intuition: pressure, flow, force. Understand *what* the cell does |
| 02 | Identify the actual components: pump type, valve type, cylinder type |
| 03 | Select the hydraulic fluid. Understand contamination and viscosity effects |
| 04 | Model the flow: pipe losses, velocity profiles, pressure drops |
| 05 | Size and characterize the pump |
| 06 | Select and configure the directional control valves |
| 07 | Size the cylinders. Calculate force and velocity for the manipulation tasks |
| 08 | Draw and analyze the full hydraulic circuit |
| 09 | Select and wire the sensors. Configure signal conditioning |
| 10 | Write the embedded control code. Implement closed-loop position control |
| 11 | Build the digital twin in Python |
| 12 | Integrate, test, validate, and demonstrate |

---

## Deliverables for the Full Capstone

1. **Physical build log** — documented hardware assembly with photographs
2. **Hydraulic circuit diagram** — complete ISO 1219 schematic
3. **Sensor wiring diagram** — all sensors, connections, and signal conditioning
4. **Embedded control code** — Arduino and Raspberry Pi code, documented and version-controlled
5. **Digital twin notebook** — Jupyter notebook with simulation, comparison to measured data
6. **Demonstration video** — showing at least two manipulation tasks
7. **Final report** — system description, design decisions, measured performance, and reflection

---

*Capstone README — Version 0.1*  
*Full specifications, BOM, and integration guides to be developed in Modules 08–12.*
