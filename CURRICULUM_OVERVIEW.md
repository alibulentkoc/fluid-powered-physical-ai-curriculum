# Curriculum Overview

*High-level overview of the Fluid-Powered Physical AI Curriculum.*

---

## What this curriculum is

The **Fluid-Powered Physical AI Curriculum** is a modular, open-source course that takes learners from first principles in fluid mechanics to a working, validated digital twin of an intelligent electro-hydraulic robotic system.

It is built as **one coherent machine, not a list of topics**. Every module adds a capability to a single running system — the **Intelligent Fluid-Powered Agricultural Manipulation Cell** (the Smart Agricultural Workcell) — and produces an artifact the next module consumes. The machine is the story; the modules are its chapters.

By the end, a learner can understand, simulate, and reason about an intelligent fluid-powered machine end to end: power generation, motion control, force production, integration, sensing, embedded control, and a digital twin that mirrors and monitors the real system.

---

## Educational philosophy

Every topic follows a five-layer progression:

1. **Physical intuition** — a mental model before any equations
2. **Visual understanding** — diagrams and annotated figures
3. **Mathematical formulation** — governing equations with clear derivation
4. **Computational implementation** — simulate, plot, or control in code
5. **System integration** — connect the concept to the running machine

Mathematics explains the machine; it does not replace it.

---

## The twelve stages

| Module | Title | Capability added |
|--------|-------|------------------|
| 01 | Foundations of Fluid Power and Physical AI | identity & first principles |
| 02 | Hydraulic Components and System Architecture | the machine's parts |
| 03 | Hydraulic Fluids and Energy Transmission | the working medium |
| 04 | Fluid Mechanics for Intelligent Machines | the first dynamic model (digital twin born) |
| 05 | Hydraulic Pumps and Power Generation | a power source |
| 06 | Valves and Motion Control | motion control |
| 07 | Hydraulic Cylinders and Motors | force production |
| 08 | Hydraulic Circuit Design and Integration | one integrated body |
| 09 | Sensors and Instrumentation | perception |
| 10 | Electro-Hydraulic Systems and Embedded Control | a control brain |
| 11 | Digital Twins for Fluid-Powered Systems | self-awareness |
| 12 | Fluid-Powered Physical AI Capstone | a demonstrated, validated whole |

---

## Benchmark tasks

The curriculum is organized around recurring benchmark tasks the machine must perform, not abstract coverage:

- moving the manipulator to a target position
- maintaining stable hydraulic motion under load
- sensing pressure, position, and flow correctly
- coordinating electro-hydraulic control
- mirroring the machine in a digital twin
- detecting mismatch between twin and real system
- demonstrating a full capstone manipulation cycle

---

## Orientation documents

New here? Start with the machine:

- [`docs/MACHINE_STORY.md`](docs/MACHINE_STORY.md) — what the machine is and what makes it intelligent
- [`docs/BENCHMARK_TASKS.md`](docs/BENCHMARK_TASKS.md) — the tasks the machine must perform
- [`docs/MODULE_ARTIFACT_MAP.md`](docs/MODULE_ARTIFACT_MAP.md) — the artifact each module produces
- [`curriculum/CURRICULUM_NARRATIVE.md`](curriculum/CURRICULUM_NARRATIVE.md) — how the machine becomes more capable, stage by stage
- [`curriculum/CAPABILITY_GROWTH_MAP.md`](curriculum/CAPABILITY_GROWTH_MAP.md) — the capability progression across modules

Then begin with Module 01.

---

## Curriculum engineering and governance

This curriculum is designed, produced, verified, and maintained according to a defined process. The authoritative governance artifact is:

- **[`curriculum/CURRICULUM_ENGINEERING_METHODOLOGY.md`](curriculum/CURRICULUM_ENGINEERING_METHODOLOGY.md)** — the reusable methodology for designing, governing, generating, verifying, reviewing, publishing, and maintaining the curriculum. It defines the human–AI responsibility model, the repository-first principle, the educational philosophy, the module-architecture governing requirement, verification discipline, and the reporting format. It also records (§22) the specific module scale this curriculum adopted as a valid alternative implementation.

The completion record for the curriculum is:

- **[`curriculum/FINAL_COMPLETION_REPORT.md`](curriculum/FINAL_COMPLETION_REPORT.md)** — the governance milestone report documenting completion, capability progression, artifact handoffs, methodology conformance, intentional deviations, and publication readiness.

> These are governance and curriculum-engineering artifacts. They are intentionally **not** part of the primary student navigation; they document how the curriculum is built and maintained, for architects, contributors, and reviewers.

---

## Repository layout

```
fluid-powered-physical-ai-curriculum/
├── README.md
├── CURRICULUM_OVERVIEW.md              # this file
├── docs/                               # machine story, benchmark tasks, artifact map
├── curriculum/                         # manifests, narrative, methodology, completion report
├── modules/                            # lessons, summaries, exercises (per module)
├── labs/                               # hands-on lab procedures
├── code/                               # tested Python models and simulations
├── assets/                             # figures (SVG) and storyboards
└── projects/capstone/                  # the capstone demonstration
```

---

## License

MIT License. See `LICENSE`. Contributions welcome — see `CONTRIBUTING.md` and follow the production standards described in the curriculum engineering methodology.

---

*Curriculum Overview — see the Curriculum Engineering Methodology for governance and the Final Completion Report for the completion record.*
