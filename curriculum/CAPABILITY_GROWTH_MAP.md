# Capability Growth Map

*The entire curriculum at a glance. Read top to bottom and you watch the Smart Agricultural Workcell become an intelligent machine — gaining one concrete capability per module, advancing the benchmark tasks, producing a reusable artifact, and growing its digital twin.*

> The machine is the protagonist. This table is the plot.

---

## The machine's evolution

| Module | Machine Capability | Benchmark Task Advanced | Artifact Produced | Digital Twin Contribution |
|--------|--------------------|--------------------------|-------------------|----------------------------|
| **01** | Understand itself as a complete system | All three (conceptual) | System Concept Diagram | Twin concept introduced; governing equations identified |
| **02** | Identify & select its physical components | Precision Positioning, Force-Controlled Interaction | Hardware Architecture (Component Map) | Component parameters catalogued (displacements, areas, ratings) |
| **03** | Specify & maintain its working fluid | Precision Positioning | Fluid Specification | Bulk modulus, viscosity-temperature, density, line-loss parameters |
| **04** | Predict its own hydraulic behavior | Precision Positioning | Cylinder Simulation | **Twin born:** valve model + coupled cylinder ODE |
| **05** | Generate hydraulic power | Precision Positioning | Hydraulic Power Unit Design | Pump model (flow vs. pressure & speed) |
| **06** | Direct & meter its motion | Precision Positioning, Force-Controlled Interaction | Motion Control Architecture | Valve model refined to real valve parameters |
| **07** | Produce sized, reliable force & motion | Force-Controlled Interaction | Actuator Selection Report | Cylinder parameters finalized to chosen actuator |
| **08** | Operate as one complete hydraulic circuit | Precision Positioning | Integrated Hydraulic Circuit | Component models connected into one system simulation |
| **09** | Perceive its own state | All three | Sensor Layer | Sensor models (noise, calibration); real-vs-predicted comparison begins |
| **10** | Decide & act autonomously | Force-Controlled Interaction, Autonomous Manipulation | Embedded Control System | Controller simulated in-the-loop before hardware |
| **11** | Check itself & detect faults | Autonomous Manipulation | Integrated Digital Twin | **Twin integrated:** full-system prediction + residual fault detection |
| **12** | Perform autonomous, validated manipulation | All three (demonstrated) | Demonstration System | Twin demonstrated as live monitoring & fault detection |

*Modules 01–04 are delivered; 05–12 reflect the designed arc from the manifests.*

---

## Reading the columns

**Machine Capability** — the concrete new thing the machine can do. Each is observable: you could watch the machine do it (or fail to, before the module).

**Benchmark Task Advanced** — which of the three sacred tasks got measurably closer. Precision Positioning dominates the early build (you must move before you can interact); Force-Controlled Interaction builds through the middle; Autonomous Manipulation is the payoff of the perception-and-intelligence modules.

**Artifact Produced** — the reusable thing the student builds and keeps. Artifacts chain: each is an input to the next module. (See `../docs/MODULE_ARTIFACT_MAP.md`.)

**Digital Twin Contribution** — what the software model gained. The twin is not bolted on at Module 11 — it is *born* at Module 04 and grown every module after, so that by Module 11 it is integrated, not started.

---

## The three storylines

Three threads run the length of the curriculum. Each strengthens monotonically.

### The machine becomes more physically capable
```
M01 understood → M02 componentized → M03 fluid-ready → M04 predictable →
M05 powered → M06 controllable → M07 forceful → M08 integrated
```
By Module 08 the physical machine is complete: it can generate power, direct it, and produce sized force and motion as one circuit.

### The machine becomes more intelligent
```
M09 perceives → M10 decides & acts → M11 validates itself → M12 operates autonomously
```
The intelligence layer turns a capable hydraulic machine into an intelligent one.

### The digital twin grows
```
M03 parameters → M04 first models (born) → M05–08 component models →
M09 sensor models + data → M10 control-in-loop → M11 integrated → M12 demonstrated
```
The twin is the through-line that makes the machine *self-aware* — the single feature that most distinguishes this from a conventional hydraulics course.

---

## The benchmark-task ladder

The capabilities accumulate into the three tasks:

```
Modules 04–08  ─────►  Precision Positioning
                          │  (move the tool to the target)
                          ▼
Modules 06–10  ─────►  Force-Controlled Interaction
                          │  (interact with the object safely)
                          ▼
Modules 09–12  ─────►  Autonomous Manipulation
                          (perceive, sequence, validate — on its own)
```

Autonomous Manipulation is Positioning + Force-Controlled Interaction, sequenced by a perceiving, self-validating controller. The ladder is the curriculum.

---

## At a glance: what the machine can do after each phase

| After… | The machine can… |
|--------|------------------|
| Module 04 | Predict its cylinder's motion in software (Precision Positioning, simulated) |
| Module 08 | Move with controlled, sized force as a complete hydraulic circuit (Precision Positioning + Force, physical) |
| Module 11 | Perceive, decide, act, and detect its own faults (all three tasks, validated) |
| Module 12 | Perform a full autonomous manipulation sequence while validating itself (the finished machine) |

---

*For the prose story, see `CURRICULUM_NARRATIVE.md`. For the development rules that produced this, see `../docs/PHYSICAL_AI_STYLE_GUIDE.md`.*
