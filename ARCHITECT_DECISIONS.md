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
