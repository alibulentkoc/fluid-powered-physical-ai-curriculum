# Fluid-Powered Physical AI Curriculum

Welcome. This is the student-facing site for an open curriculum in **fluid power, hydraulics, electro-hydraulic systems, sensors, embedded intelligence, agricultural robotics, and digital twins** — built around a single running machine, the **Smart Agricultural Workcell**.

Physical AI has largely been built on electrically actuated systems. Yet agriculture, construction, forestry, and heavy industry still run on fluid power. This curriculum asks a question almost no open material does: *what does it look like to bring intelligence into fluid-powered machines?* — and answers it by building one, from first principles to a validated, self-monitoring system.

Every topic is taught in five layers: **physical intuition → visual understanding → mathematical formulation → computational implementation → system integration.** You will understand not just *how* the equations work, but *why* they matter in a real machine.

## You are building one machine in twelve stages

You are not taking twelve separate modules. You are building **one machine** — the Smart Agricultural Workcell — in twelve stages. The machine is the story; the modules are its chapters. Across the curriculum it gains the ability to generate power, control motion, produce force, sense its own state, decide and act, and watch over itself with a digital twin.

- [The machine's story](MACHINE_STORY.md) — what the machine is, what it does, and what makes it intelligent
- [Benchmark tasks](BENCHMARK_TASKS.md) — the three tasks the machine must perform
- [Module → artifact map](MODULE_ARTIFACT_MAP.md) — the tangible artifact each module produces
- [Curriculum narrative](curriculum_pages/CURRICULUM_NARRATIVE.md) — how the machine becomes more capable, stage by stage

## Start here

Begin with **[Module 01 — Why this matters](modules/module01_foundations/lessons/01_why_this_matters.md)**, the orientation lesson. From there, follow the modules in order in the left sidebar — each builds directly on the machine you have so far.

## How the materials fit together

Each lesson follows a consistent twelve-part structure: Why this matters, physical intuition, mathematical foundations, a visual explanation, an engineering example, a worked example, an interactive demonstration, a coding exercise, a knowledge check, a challenge problem, common mistakes, and key takeaways. Alongside the readings you will find:

- **runnable Python** in `code/` — every model tested and ready to run,
- **hands-on labs** in `labs/` — procedures with a five-part engineering report,
- **figures** that build intuition, and
- **knowledge checks and problem sets** with worked solutions.

## The twelve stages

| Module | Title | The machine gains |
|--------|-------|-------------------|
| 01 | Foundations of Fluid Power and Physical AI | its identity and first principles |
| 02 | Hydraulic Components and System Architecture | its parts |
| 03 | Hydraulic Fluids and Energy Transmission | its working medium |
| 04 | Fluid Mechanics for Intelligent Machines | its first digital twin |
| 05 | Hydraulic Pumps and Power Generation | a power source |
| 06 | Valves and Motion Control | motion control |
| 07 | Hydraulic Cylinders and Motors | the ability to produce force |
| 08 | Hydraulic Circuit Design and Integration | one integrated body |
| 09 | Sensors and Instrumentation | perception |
| 10 | Electro-Hydraulic Systems and Embedded Control | a control brain |
| 11 | Digital Twins for Fluid-Powered Systems | self-awareness |
| 12 | Fluid-Powered Physical AI Capstone | a demonstrated, validated whole |

---

!!! note "For contributors"
    This site is the presentation layer, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) directly from the lesson sources in `modules/` and `curriculum/`. The navigation is defined in `mkdocs.yml`; pushing to `main` rebuilds and republishes the site automatically. See `ARCHITECT_DECISIONS.md` for design rationale.

*Open source under the MIT License. Improve this page on [GitHub](https://github.com/alibulentkoc/fluid-powered-physical-ai-curriculum).*
