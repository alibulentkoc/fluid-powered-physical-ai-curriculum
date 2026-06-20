# Curriculum Engineering Methodology

*Authoritative governance artifact for the Fluid-Powered Physical AI Curriculum.*
*Reusable for future courses in other domains.*

---

## Purpose

This document defines the reusable methodology for designing, governing, generating, verifying, reviewing, publishing, and maintaining the **Fluid-Powered Physical AI Curriculum**.

It is written so that the same process can be reused for future courses in other domains.

The curriculum is built as one coherent system: the **Intelligent Fluid-Powered Agricultural Manipulation Cell** (the Smart Agricultural Workcell). Each module adds one capability to that system, and each module produces an artifact that the next module consumes.

This is a governance and curriculum-engineering artifact, not student-facing material. It is maintained in the repository as memory (see §4) and is not part of the primary student navigation.

---

## 1. Core Principle

Most curricula fail because they become a list of topics.

This methodology treats a curriculum as **one growing machine**.

The learner should not finish with twelve separate subjects. The learner should finish with one coherent understanding of how a fluid-powered intelligent system works, from first principles through digital twin.

The machine is the story. The modules are the chapters.

---

## 2. System Story

The single running example is the **Intelligent Fluid-Powered Agricultural Manipulation Cell**.

It is:

- a fluid-powered manipulation platform
- instrumented with sensors
- controlled by embedded processors
- mirrored by a digital twin
- demonstrated in an agricultural setting

The course does not teach agriculture alone, and it does not teach fluid mechanics alone. It teaches **intelligence brought into fluid-powered machinery**.

---

## 3. Human–AI Responsibility Model

### Human Architect

Responsible for: vision, learning outcomes, scope boundaries, sequencing, standards, approval, release decisions. The human retains educational authority.

### AI Architect Assistant

Responsible for: architectural review, boundary enforcement, consistency checking, milestone evaluation, risk identification, publication planning. The AI architect does not self-authorize.

### AI Production System

Responsible for: lesson generation, notebooks, diagrams, demos, quizzes, answer keys, reports. The production AI works only inside approved boundaries and does not invent architecture.

---

## 4. Repository-First Development

The repository is the source of truth.

Authoritative files should define: project vision, current state, progress tracking, decision history, production standards, lesson template, and module manifests.

The chat is a workspace. The repository is memory.

---

## 5. Educational Philosophy

Every topic should follow this progression:

**Physical intuition → Visual understanding → Mathematical formulation → Computational implementation → System integration.**

The curriculum is not a set of isolated equations. Mathematics explains the machine. Mathematics does not replace the machine.

---

## 6. Module Architecture

Each module should:

- add one capability to the machine
- produce one concrete artifact
- hand that artifact to the next module

A module should answer: What does this module teach? What capability does it add? What does it produce? What does the next module consume?

The curriculum should remain one continuous pipeline from fluid fundamentals to the digital twin.

---

## 7. Recommended Module Shape

A module should have:

- a clear capability
- learning objectives
- lessons
- notebooks
- diagrams
- quizzes
- assessments

A common implementation pattern is:

> **8 units × 4 lessons = 32 lessons per module**, with a midpoint after Unit 4 and a capstone in Unit 8, produced in reviewed installments.

**This 8×4 pattern is a recommended implementation pattern, not a mandatory requirement.** Module size may be adjusted based on:

- audience
- curriculum scope
- delivery format
- instructional goals

**The governing requirement is not lesson count. The governing requirement is:**

> **Each module adds a capability and produces an artifact consumed by the next module.**

A curriculum that satisfies this governing requirement conforms to the methodology regardless of the module scale chosen, provided each module still has a clear capability, learning objectives, lessons, supporting computational and visual artifacts, and assessments.

See §22 for the specific module scale adopted by the Fluid-Powered Physical AI Curriculum, recorded as a valid alternative implementation.

---

## 8. Installment Workflow

Build each module in increments (Installment A, B, C, D). After each installment: stop, review, verify, approve, continue. Do not generate an entire module without checkpoints.

For modules built at a smaller scale (see §22), the installment granularity scales down accordingly: a four-lesson module may be produced and reviewed as a single installment or split as appropriate, but the stop-review-verify-approve discipline is retained.

---

## 9. Verification Strategy

Every artifact must be verifiable. Required verification includes:

- notebooks / code execute successfully
- diagrams are valid
- demos run
- quizzes render
- answer keys match quizzes
- strict site build passes

Verification is evidence, not assertion.

---

## 10. Governance and Reporting

Every milestone report begins with **EXECUTIVE SUMMARY**, then includes: Status, What Was Built, Key Educational Achievement, Architect Review Focus, Next.

This makes review fast and keeps the project state visible.

---

## 11. Scope Protection

Each module must define what belongs inside it and what does not. Useful fences for this curriculum:

- fluid mechanics ≠ control theory
- components ≠ system integration
- sensing ≠ embedded orchestration
- control ≠ digital twin
- twin ≠ machine learning
- adaptation ≠ reinforcement learning

The module boundaries must be explicit and repeated.

---

## 12. Curriculum Spine for This Course

- fluid foundations
- components and architectures
- fluid mechanics and energy transfer
- pumps and power generation
- valves and motion control
- cylinders and motors
- circuit design and integration
- sensors and instrumentation
- electro-hydraulic embedded control
- digital twins for fluid systems
- full physical AI capstone

Each module should contribute to one integrated machine.

---

## 13. Benchmark Tasks

The curriculum should be organized around a few benchmark tasks, not abstract coverage. For this course:

- moving the manipulator to a target position
- maintaining stable hydraulic motion under load
- sensing pressure, position, and flow correctly
- coordinating electro-hydraulic control
- mirroring the machine in a digital twin
- detecting mismatch between twin and real system
- demonstrating a full capstone manipulation cycle

These tasks should appear repeatedly across modules.

---

## 14. Production Phases

1. **Curriculum architecture** — define the machine, benchmark tasks, module roadmap.
2. **Repository foundation** — authoritative project files and templates.
3. **Module launch packages** — per module: manifest, structure, lesson inventory, objectives, midpoint plan, capstone concept, demo plan, notebook plan, architectural concerns.
4. **Installment production** — generate lessons and artifacts in reviewed installments.
5. **Verification** — run code, validate diagrams, check quizzes, build the site under strict mode.
6. **Publication** — release reviewed modules and maintain versioned publication states.

---

## 15. Human–AI Workflow

**Human:** defines the machine story, sets scope, approves launches, reviews milestones, decides publication timing.

**AI Architect Assistant:** checks boundaries, keeps sequence coherent, detects drift, evaluates milestone reports, helps prepare release and publication plans.

**AI Producer:** generates lesson content, notebooks, quizzes, diagrams, demos, answer keys. The AI producer should not invent architecture.

---

## 16. Release and Publication

Separate: content production, content review, release packaging, site publication, translation, maintenance.

A curriculum can be complete before it is published. Publication should happen in controlled releases, module by module or in approved batches.

---

## 17. Translation Readiness

Keep one canonical source language. All translations derive from that source. Do not maintain multiple masters.

If translation is desired, design the site and repository so that the canonical English curriculum remains stable, translated pages mirror the same structure, and module versions stay aligned across languages.

---

## 18. Reuse for Other Courses

This methodology is not specific to fluid power. To reuse it: keep the governance model, the installment workflow, the verification discipline, the repository-first approach, the reporting standard. Replace only the domain story, running example, and capstone.

The process stays the same. The subject changes.

---

## 19. Completion Criterion

A module is complete only when:

- all lessons are built
- all notebooks / code pass
- all diagrams validate
- all demos work
- all quizzes and answer keys match
- the strict site build passes
- the milestone report is approved
- the repository is updated

The full curriculum is complete only when all modules are complete and the capstone demonstrates the full machine.

---

## 20. Final Curriculum Outcome

A learner finishing the curriculum should be able to:

- understand fluid power as an intelligent actuation domain
- reason about hydraulic and electro-hydraulic systems
- instrument and control those systems
- integrate sensing, control, and embedded intelligence
- mirror and predict the system in a digital twin
- explain the full pipeline from fluid mechanics to a working intelligent manipulation cell

The end state is not a set of topics. It is one coherent machine, understood as a system.

---

## 21. Adaptation Template for New Courses

For a new course, **replace**: the machine story, the benchmark tasks, the capstone, the module content.

**Keep unchanged**: repository-first development, human–AI governance, installment production, verification discipline, publication strategy, translation readiness, review workflow.

---

## 22. Recorded Implementation — Fluid-Powered Physical AI Curriculum

This section records the specific module scale adopted by this curriculum as a **valid alternative implementation** of §7, documented so future courses can see that a non-reference scale is permitted when the governing requirement is met.

**Reference pattern (§7):** 8 units × 4 lessons = 32 lessons per module.

**Adopted implementation:** **4 lessons per module**, 12 modules, **49 lessons total** (Module 04 carries 5 lessons). Each lesson follows the twelve-part topic template (Why This Matters; Physical Intuition; Mathematical Foundations; Visual Explanation; Engineering Example; Worked Example; Interactive Demonstration; Coding Exercise; Knowledge Check; Challenge Problem; Common Mistakes; Key Takeaways).

**Rationale for the deviation:** scope and delivery format. The four-lesson module concentrates each capability into a tight, machine-centered arc (problem → concept → math → integration) appropriate for the audience and for a single-machine narrative, while keeping the curriculum manageable to produce and review. §7 explicitly permits adjusting module size for audience, scope, delivery format, and instructional goals.

**Conformance to the governing requirement:** satisfied. Each module adds exactly one capability and produces one artifact consumed by the next:

| Module | Capability added | Artifact produced → consumed by |
|--------|------------------|---------------------------------|
| 01 Foundations | identity & first principles | conceptual frame → 02 |
| 02 Components | the machine's parts | component inventory → 03 |
| 03 Fluids | the working medium | fluid/energy basis → 04 |
| 04 Fluid Mechanics | first dynamic model | the digital twin (born) → 05–11 |
| 05 Pumps | power generation | Hydraulic Power Unit → 06 |
| 06 Valves | motion control | Motion Control Architecture → 07 |
| 07 Actuators | force production | Actuator Selection Report → 08 |
| 08 Circuit | one integrated body | Integrated Hydraulic Circuit → 09 |
| 09 Sensors | perception | Sensor Layer → 10 |
| 10 Control | a control brain | Embedded Control System → 11 |
| 11 Digital Twin | self-awareness | Integrated Digital Twin → 12 |
| 12 Capstone | demonstrated whole | Demonstration System (capstone) |

**Other adopted choices, recorded for transparency:**

- **Computational artifacts** are delivered as tested Python modules (39 files, all executing) rather than Jupyter notebooks; the §9 verification intent (code executes successfully) is met by direct execution with a `--plot` path for figures.
- **Diagrams** are five standalone SVG figures (capstone architecture, system pipeline, curriculum roadmap, module integration map, digital twin workflow), coordinate-verified, plus per-figure storyboards.
- **Assessments** are delivered per module as a problem set and a knowledge check, each with verified answer keys, plus a five-part lab procedure.
- **Site build** is Material for MkDocs; the strict build passes (74 pages, exit 0), satisfying §9's strict-build requirement.

**Conclusion:** the Fluid-Powered Physical AI Curriculum is a conforming implementation of this methodology at a smaller module scale than the §7 reference pattern. The deviation is intentional, permitted, and recorded here.

---

*Curriculum Engineering Methodology — authoritative governance artifact. Not part of student navigation. See `curriculum/FINAL_COMPLETION_REPORT.md` for the completion record.*
