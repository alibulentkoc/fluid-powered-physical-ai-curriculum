# Fluid-Powered Physical AI Curriculum

**An open curriculum in Fluid Power, Hydraulics, Electro-Hydraulic Systems, Sensors, Embedded Intelligence, Agricultural Robotics, and Digital Twins.**

---

## What This Is

Physical AI has largely been built on electrically actuated systems. Most open curricula in robotics, embedded intelligence, and machine learning assume servo motors, stepper drives, or brushless DC actuators. That assumption excludes a significant portion of the real world.

Agriculture, construction, forestry, and heavy industry still depend overwhelmingly on fluid power. Hydraulic systems move the vast majority of the world's working machinery. And yet almost no open educational material exists that asks: *what does it look like to bring intelligence into these systems?*

This curriculum answers that question.

**Fluid-Powered Physical AI** is a modular, open-source curriculum that takes learners from first principles in fluid mechanics to a working digital twin of an intelligent electro-hydraulic robotic system. The thread connecting every module is a single running platform:

> **The Intelligent Fluid-Powered Agricultural Manipulation Cell**

This is not a crop-specific machine. It is a constrained-workspace manipulation platform actuated by fluid power, instrumented with real sensors, controlled by embedded processors, and mirrored by a software digital twin. Agriculture is the demonstration domain. The platform is general enough to support research, education, and extension into adjacent fields.

---

## Who This Is For

- Engineering students with some background in mechanics or electronics who want to understand fluid-powered systems
- Practitioners in agricultural, industrial, or construction equipment who want to add sensing and embedded control
- Researchers exploring intelligent actuation beyond electric motors
- Educators building fluid power or mechatronics courses
- Makers and hobbyists curious about hydraulic robotics

---

## What You Will Build

By the end of this curriculum, you will understand, simulate, and physically prototype key elements of an intelligent electro-hydraulic manipulation system. The capstone integrates:

- A hydraulic positioning structure (cylinder or motor driven)
- Interchangeable end effectors for manipulation tasks
- Pressure, position, and flow sensing
- Embedded control using Arduino and Raspberry Pi
- Vision-based feedback where applicable
- A digital twin implemented in Python and/or simulation software

---

## Course Structure

| Module | Title | Status |
|--------|-------|--------|
| 01 | Foundations of Fluid Power and Physical AI | 🟡 In Progress |
| 02 | Hydraulic Components and System Architecture | 🔲 Planned |
| 03 | Hydraulic Fluids and Energy Transmission | 🔲 Planned |
| 04 | Fluid Mechanics for Intelligent Machines | 🔲 Planned |
| 05 | Hydraulic Pumps and Power Generation | 🔲 Planned |
| 06 | Valves and Motion Control | 🔲 Planned |
| 07 | Hydraulic Cylinders and Motors | 🔲 Planned |
| 08 | Hydraulic Circuit Design and Integration | 🔲 Planned |
| 09 | Sensors and Instrumentation | 🔲 Planned |
| 10 | Electro-Hydraulic Systems and Embedded Control | 🔲 Planned |
| 11 | Digital Twins for Fluid-Powered Systems | 🔲 Planned |
| 12 | Fluid-Powered Physical AI Capstone | 🔲 Planned |

---

## Repository Layout

```
fluid-powered-physical-ai-curriculum/
├── README.md                  # This file
├── CONTRIBUTING.md            # How to contribute
├── LICENSE                    # MIT License
├── TODO.md                    # Active task list
├── PROJECT_BOOTSTRAP.md       # How to get started
├── PROJECT_STATE.md           # Current state snapshot
├── master_progress.md         # Detailed progress tracker
├── ARCHITECT_DECISIONS.md     # Key design decisions and rationale
│
├── docs/                      # Course overview, philosophy, roadmap
├── curriculum/                # Module manifests and learning objectives
├── modules/                   # Teaching content, lesson files
├── labs/                      # Hands-on lab procedures and data sheets
├── assets/                    # Figures, diagrams, images
│   ├── figures/
│   └── diagrams/
├── code/                      # Code examples, simulations, stubs
├── coaches/                   # AI tutor prompts, instructor notes
└── projects/
    └── capstone/              # Capstone project: the Manipulation Cell
```

---

## Educational Philosophy

Each topic follows a five-stage progression:

1. **Physical intuition** — build a mental model before any equations
2. **Visual understanding** — diagrams, schematics, and annotated figures
3. **Mathematical formulation** — governing equations with clear derivation
4. **Computational implementation** — simulate, plot, or control in code
5. **System integration** — connect the concept to the running capstone platform

---

## Getting Started

See [`PROJECT_BOOTSTRAP.md`](PROJECT_BOOTSTRAP.md) for environment setup and first steps.

Start with [`curriculum/module01_manifest.md`](curriculum/module01_manifest.md) for the Module 1 learning plan.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions of lessons, labs, diagrams, and code are welcome. Please follow the module design standard described there.

---

## License

MIT License. See [`LICENSE`](LICENSE).

---

## Acknowledgments

This curriculum is inspired in spirit and structure by the Physical AI Curriculum project. It is independently developed and focused on the largely underserved domain of fluid-powered intelligent systems.
