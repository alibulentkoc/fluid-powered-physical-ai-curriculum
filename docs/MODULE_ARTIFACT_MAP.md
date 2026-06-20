# Module Artifact Map

*Every module produces one visible, reusable artifact. Students should see, at a glance, that they are continuously building a system — each module leaves something concrete behind that the next module builds on.*

This table is the proof that the curriculum is a build sequence, not a reading list.

---

## The artifacts

| Module | Artifact | What it is | Status |
|--------|----------|-----------|--------|
| 01 | **System Concept Diagram** | The whole machine drawn and labeled — six subsystems, the pipeline, the capstone | ✅ Delivered |
| 02 | **Hardware Architecture** | The Component Map: every subsystem with its real, named components | ✅ Delivered |
| 03 | **Fluid Specification** | The one-page fluid spec — grade, cleanliness, filter, line sizing, all justified | ✅ Delivered |
| 04 | **Cylinder Simulation** | Working code that predicts the cylinder's motion — the digital twin's first model | ✅ Delivered |
| 05 | **Hydraulic Power Unit Design** | The sized, characterized power source (motor + pump + relief + reservoir) | ◻ Planned |
| 06 | **Motion Control Architecture** | The valve configuration that directs and meters the machine's motion | ◻ Planned |
| 07 | **Actuator Selection Report** | The sized, justified primary cylinder and end-effector actuator | ◻ Planned |
| 08 | **Integrated Hydraulic Circuit** | The complete ISO 1219 circuit with an energy budget | ◻ Planned |
| 09 | **Sensor Layer** | The machine's senses — pressure, position, flow, force — specified and wired | ◻ Planned |
| 10 | **Embedded Control System** | The brain — PID control and the task state machine | ◻ Planned |
| 11 | **Integrated Digital Twin** | The full software twin, predicting the whole machine and detecting faults | ◻ Planned |
| 12 | **Demonstration System** | The complete machine performing all three benchmark tasks autonomously | ◻ Planned |

---

## How the artifacts chain together

Each artifact is an input to the next. This is what makes the curriculum a build, not a survey:

```
System Concept Diagram (M01)
   │  defines the subsystems to populate
   ▼
Hardware Architecture (M02)
   │  names the components to fill with fluid
   ▼
Fluid Specification (M03)
   │  gives the physical parameters the model needs
   ▼
Cylinder Simulation (M04)  ◄── digital twin is born here
   │  the prediction the power source must feed
   ▼
Hydraulic Power Unit Design (M05)
   │  the power the motion control directs
   ▼
Motion Control Architecture (M06)
   │  the control the actuator obeys
   ▼
Actuator Selection Report (M07)
   │  the actuator the circuit integrates
   ▼
Integrated Hydraulic Circuit (M08)  ◄── physical machine complete
   │  the machine the sensors observe
   ▼
Sensor Layer (M09)
   │  the perception the controller uses
   ▼
Embedded Control System (M10)
   │  the behavior the twin validates
   ▼
Integrated Digital Twin (M11)  ◄── intelligent machine complete
   │  the system the demonstration proves
   ▼
Demonstration System (M12)  ◄── the finished machine
```

---

## Artifact + capability + task, per module

The fuller picture — each module's artifact, the capability it adds, the benchmark task it advances, and its twin contribution — for the delivered modules:

| Module | Artifact | Machine capability added | Benchmark task advanced | Digital twin contribution |
|--------|----------|--------------------------|-------------------------|---------------------------|
| 01 | System Concept Diagram | Understand the system | All three (conceptual) | The twin concept is introduced |
| 02 | Hardware Architecture | Identify & select components | Positioning, Force | Component parameters catalogued |
| 03 | Fluid Specification | Specify & maintain the fluid | Positioning | Bulk modulus, viscosity, density, line loss |
| 04 | Cylinder Simulation | Predict hydraulic behavior | Positioning | Valve model + cylinder ODE — **twin born** |

(Modules 05–12 follow the same pattern; see `CURRICULUM_NARRATIVE.md` for the planned arc.)

---

## The rule

> If a module does not produce a visible, reusable artifact, it is not finished.

An artifact is something a student can point to and say "the machine has this now." A list of facts learned is not an artifact. A spec, a diagram, a working simulation, a wired sensor layer — those are artifacts. They accumulate into the machine.

---

*For the narrative of how the machine evolves, see `../curriculum/CURRICULUM_NARRATIVE.md`. For the tasks the artifacts serve, see `BENCHMARK_TASKS.md`.*
