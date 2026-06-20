# Architect Decisions

A log of significant design choices made during curriculum development. Each entry records what was decided, why, and what alternatives were considered.

---

## AD-001 — Agriculture as Primary Demonstration Domain

**Decision:** Use agriculture as the primary validation domain for the capstone and for motivating examples throughout the curriculum.

**Rationale:**
- Agriculture is the largest user of fluid power outside heavy construction
- Agricultural robotics is an active and growing research area with open problems
- The constrained-workspace manipulation paradigm (e.g., the milking robot) is well-defined and tractable as a capstone
- Agricultural examples are intuitive and globally relevant
- Grant funding in precision agriculture and AgTech is accessible for curriculum development extensions

**Alternatives Considered:**
- Construction equipment: too large-scale for a physical lab platform
- Manufacturing: excellent domain but well-served by existing curricula
- Mining/forestry: valid but narrower audience and harder to source hardware

**Constraint:** Agriculture is the *demonstration* domain, not the *only* domain. The curriculum must not lock into crop-specific applications. The platform must read as extensible.

---

## AD-002 — Capstone as Constrained-Workspace Manipulation Cell

**Decision:** The capstone is an Intelligent Fluid-Powered Agricultural Manipulation Cell — a constrained-workspace system, not an autonomous field vehicle.

**Rationale:**
- An autonomous field vehicle is too large, too expensive, and too complex for educational deployment
- A manipulation cell can be bench-top or small-frame mounted
- The manipulation cell paradigm supports a range of end-effectors and tasks
- It mirrors the form factor of existing collaborative robot cells, which are familiar to learners
- It is achievable with modest budgets and accessible hydraulic hardware

**Alternatives Considered:**
- Full tractor-mounted implement: more authentic but impractical for most educational settings
- Pneumatic substitute: easier but loses the hydraulic context that motivates the curriculum

**Assumption:** The baseline platform uses a single hydraulic cylinder for primary actuation, with a second actuator for end-effector control. This is the minimum viable hydraulic platform.

---

## AD-003 — Module Sequence

**Decision:** The 12-module arc runs from Foundations → Components → Fluid Mechanics → Pumps → Valves → Actuators → Circuit Design → Sensing → Electro-Hydraulics → Digital Twin → Capstone.

**Rationale:**
- This follows the natural build-up of a hydraulic engineer's knowledge
- Each module adds a layer that depends on the previous ones
- The intelligence layer (sensing, electro-hydraulics, digital twin) is placed in the second half, after physical understanding is established
- The capstone is positioned last so every prior module has contributed to it

**Alternatives Considered:**
- Starting with sensing and embedding foundations earlier: considered, but learners need physical intuition before adding intelligence
- Splitting valves and motion control into two modules: possible in a future revision

**Open Question:** Whether Module 03 (Hydraulic Fluids) should come before or after Module 04 (Fluid Mechanics). Currently: Fluids before Mechanics, since fluid properties motivate the mechanics.

---

## AD-004 — No Platform Supremacy Framing

**Decision:** The curriculum explicitly avoids framing hydraulics as superior to electric actuation.

**Rationale:**
- Factually incorrect: electric systems are better in many applications
- Creates adversarial tone that reduces broad appeal
- The actual pitch is different: fluid power is important and intelligent fluid power is underserved
- Learners may come from electric robotics backgrounds and should feel welcomed

**Language Policy:**
- Preferred: "fluid power is an important actuation domain that Physical AI has largely ignored"
- Avoid: "hydraulics is more powerful than electric motors"
- Preferred: "many critical systems still depend on fluid power"
- Avoid: "electric robots can't do what hydraulics can"

---

## AD-005 — Python as Primary Simulation Language

**Decision:** Python is the primary language for simulations, digital twin development, and data analysis.

**Rationale:**
- Widest learner base
- Rich scientific computing ecosystem (NumPy, SciPy, Matplotlib, pandas)
- Compatible with Raspberry Pi embedded targets
- Open source and free

**Secondary Languages:**
- Arduino C++ for embedded microcontroller examples
- Optional: Modelica/OpenModelica for system-level simulation in advanced modules (noted as optional, not required)

---

## AD-006 — ISO 1219 as Reference Standard for Circuit Diagrams

**Decision:** Hydraulic circuit diagrams will follow ISO 1219 symbol conventions where practical.

**Rationale:**
- ISO 1219 is the international standard for hydraulic and pneumatic circuit diagrams
- Using it from the beginning teaches learners to read industry documentation
- Reduces confusion when learners encounter real equipment

**Caveat:** Some simplified symbols may be used in early modules for clarity, with a note that they are simplified. Full ISO 1219 symbols will be used by Module 08 (Circuit Design).

---

## AD-007 — Low-Pressure First Approach for Labs

**Decision:** Early lab activities will use low-pressure hydraulic or pneumatic systems (under 100 PSI / 7 bar) where possible.

**Rationale:**
- High-pressure hydraulic systems (1000–3000 PSI) are dangerous without proper training and facilities
- Low-pressure demonstrations can illustrate the key principles (Pascal's Law, flow, force multiplication)
- Pneumatic substitutes are acceptable for Modules 01–04
- Higher-pressure hydraulic work should be introduced gradually in Modules 05–08 with appropriate safety scaffolding

**Safety note:** All lab files must include explicit pressure ratings and safety warnings.

---

## AD-009 — Narrative-driven development (Directive 004)

**Decision:** The machine, not the hydraulics, is the protagonist of the curriculum. Every module must contribute a visible capability to the Smart Agricultural Workcell and answer four questions: (1) what capability did the machine gain, (2) which benchmark task improved, (3) what was added to the digital twin, (4) how does it connect to the next module.

**Implementation:**
- Created `curriculum/CURRICULUM_NARRATIVE.md` as a first-class artifact: machine mission, three benchmark tasks (Precision Positioning, Force-Controlled Interaction, Intelligent Manipulation), module-by-module machine evolution, and digital twin growth.
- Every module `summary.md` now carries a **Machine Capability Added** and **Digital Twin Contribution** section.
- Every delivered manifest header carries a mission-framing block.
- README points new students to the narrative first.

**Rationale:** Guards against curriculum drift — the risk that the course becomes "a hydraulics textbook with a capstone attached." The Physical AI curriculum succeeds because students continuously see a robot becoming more capable; this curriculum achieves the same effect with a fluid-powered intelligent machine.

**Three benchmark tasks (recurring throughout):**
1. Precision Positioning (heavy in Modules 04–08)
2. Force-Controlled Interaction (heavy in Modules 06–10)
3. Intelligent Manipulation (heavy in Modules 09–12)

---

## AD-010 — Preserve the Physical AI experience (Directive 005)

**Decision:** The student experience must mirror the Physical AI Curriculum — students continuously watch an intelligent machine become more capable. Hydraulics is a tool used to build the machine, never the subject itself. Directive 005 added a review gate enforced before Module 05.

**Implementation (gate satisfied):**
- Created three first-class `docs/` artifacts: `MACHINE_STORY.md` (the machine itself), `BENCHMARK_TASKS.md` (the three tasks with success criteria), `MODULE_ARTIFACT_MAP.md` (tangible artifact per module).
- Retrofitted ALL 17 lessons in Modules 01–04 with two mandatory sections: `## Why The Machine Needs This` (opens every lesson, before theory) and `## Machine Capability Added` (closes every lesson, concrete).
- Confirmed every module summary carries Machine Capability Added, Benchmark Task Advanced, and Digital Twin Contribution.
- Added the mandated 5-part Lab Report Format (Observation, Measurement, Engineering Interpretation, Machine Implication, Digital Twin Implication) to all four labs.
- README now opens with the machine-first doc set.

**Rationale:** Defends against the standing risk of the curriculum degrading into "a high-quality hydraulics textbook." Organize around machine capabilities (the machine needs power / motion / force / awareness / intelligence / validation), introduce hydraulic concepts only when the machine requires them.

**Per-module artifact commitment (from MODULE_ARTIFACT_MAP):**
M01 System Concept Diagram · M02 Hardware Architecture · M03 Fluid Specification · M04 Cylinder Simulation · M05 Hydraulic Power Unit Design · M06 Motion Control Architecture · M07 Actuator Selection Report · M08 Integrated Hydraulic Circuit · M09 Sensor Layer · M10 Embedded Control System · M11 Integrated Digital Twin · M12 Demonstration System.

---

## AD-011 — Physical AI experience preservation (Directive 006)

**Decision:** Technical correctness is not the success criterion; the success criterion is whether the curriculum *feels* like the Physical AI Curriculum — students watching an intelligent machine become more capable. Directive 006 set a review gate before Module 05 with the Physical AI lesson pattern (Machine Problem → Concept → Mathematical Model → Computational Model → Machine Improvement) and four narrative quality tests.

**Implementation (gate satisfied):**
- Created `docs/PHYSICAL_AI_STYLE_GUIDE.md` — mandatory reading before any lesson development; codifies the lesson pattern, four quality tests, and writing/figure/code/lab rules.
- Created `curriculum/CAPABILITY_GROWTH_MAP.md` — the machine's evolution at a glance (Module | Capability | Benchmark Task | Artifact | Twin Contribution).
- Performed and documented a narrative review (`docs/NARRATIVE_REVIEW_01-04.md`); identified 4 weak openings that led with the curriculum/concept rather than the machine's problem and rewrote them (contamination, bernoulli, simulation, what-fluid-does).
- Added explicit before/after capability statements ("Before this lesson the machine could not… / After this lesson the machine can…") to all 17 lessons.
- Added benchmark-task identification to all 17 lessons.
- Added missing digital-twin contributions to the 4 lessons that lacked them.

**Four narrative quality tests — all 17 lessons pass:** Machine Necessity, Capability Growth, Digital Twin, Machine Sketch.

**Standing principle:** When a development decision is unclear, choose the option that strengthens the machine's story.

---

## AD-012 — Module 05 built natively to Physical AI standard (Directive 007)

**Decision:** Module 05 ("Powering the Smart Agricultural Workcell," not "Hydraulic Pumps") is the first module developed entirely under the Physical AI narrative standard — the test of whether the curriculum transitions from hydraulics course to Fluid-Powered Physical AI curriculum.

**Implementation:**
- Four lessons to the directive's structure: (01) why the machine needs hydraulic power, (02) which pump — framed as a selection decision, not a catalog, (03) performance & efficiency, (04) designing the HPU (produces the artifact).
- All four lessons carry the four mandatory sections (Why The Machine Needs This, Benchmark task supported, Digital twin contribution, Machine Capability Added).
- `pump_performance_model.py` — flow, hydraulic/shaft power, efficiencies (volumetric drooping with pressure), pump curves, and the HPU design generator. Tested; all lesson numbers verified against it.
- Lab 05 (Hydraulic Power Unit Investigation) with the 5-part report (Observation → Measurement → Engineering Interpretation → Machine Improvement → Digital Twin Improvement).
- Artifact: Hydraulic Power Unit Design (Subsystem 1 of the final machine).

**Numerical reconciliation:** motor sizing standardized on the 2.2 kW frame (service-factor capability 2.53 kW ≥ 2.15 kW shaft load) consistent with Modules 01–02, after the code initially flagged a 3.0 kW result from a naive margin approach. All numbers verified against tested code.

**Architect quality check — all YES:** machine gains visible capability (generate power); Benchmark Task 1 improves (impossible → powered); twin more capable (pump/power/efficiency model); student builds a machine, not studies pumps.
