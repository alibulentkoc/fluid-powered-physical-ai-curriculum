# Project state

Last updated: Module 01 finalized + Module 02 lessons complete

---

## Phase

**Phase 1 — Architecture: COMPLETE**
**Phase 2 — Visual Foundation: COMPLETE (figures finalized as files, visually QA'd)**
**Phase 3 — Lesson Development: Module 01 COMPLETE (reference implementation)**

Module 02 content is the next priority. Per directive, it must not begin until
Module 01 is complete and tracking files are updated — both now done.

---

## Figures — finalized and visually verified

All five figures exist as standalone, self-contained SVG files in `assets/figures/`.
Each was rendered to PNG and visually inspected. All pass the QA checklist:
text inside boxes, no label overlap, no arrow-box collisions, consistent spacing,
readable typography, understandable without external explanation.

| File | Status | QA |
|------|--------|-----|
| capstone_architecture.svg | ✅ Finalized | ✓ Visual pass |
| system_pipeline.svg | ✅ Finalized | ✓ Visual pass (filenames shortened for fit) |
| curriculum_roadmap.svg | ✅ Finalized | ✓ Visual pass (capstone subtitle trimmed) |
| module_integration_map.svg | ✅ Finalized | ✓ Visual pass |
| digital_twin_workflow.svg | ✅ Finalized | ✓ Visual pass (M11/M12 pills widened) |

Files are dark-mode compatible (embedded prefers-color-scheme media query) and
render standalone in any browser — no host-CSS dependency.

---

## Module 01 — COMPLETE (reference implementation)

| File | Status |
|------|--------|
| curriculum/module01_manifest.md | ✅ |
| modules/module01_foundations/lessons/01_why_this_matters.md | ✅ |
| modules/module01_foundations/lessons/02_physical_intuition.md | ✅ |
| modules/module01_foundations/lessons/03_mathematical_foundations.md | ✅ |
| modules/module01_foundations/lessons/04_visual_explanation.md | ✅ |
| modules/module01_foundations/summary.md | ✅ |
| modules/module01_foundations/exercises/problem_set_01.md | ✅ |
| labs/lab01_introduction/procedure.md | ✅ |
| code/module01/pascals_law.py | ✅ tested |
| code/module01/unit_converter.py | ✅ tested |

All four lessons follow the 12-part topic template. Both code files run and produce
the baseline workcell numbers (19.63 kN extend, 84.9 mm/s, 1.67 kW) consistently.

---

## Module 02 — Lessons COMPLETE

| File | Status |
|------|--------|
| curriculum/module02_manifest.md | ✅ |
| modules/module02_components/lessons/01_pumps.md | ✅ |
| modules/module02_components/lessons/02_valves.md | ✅ |
| modules/module02_components/lessons/03_cylinders_and_motors.md | ✅ |
| modules/module02_components/lessons/04_support_system.md | ✅ |
| modules/module02_components/summary.md | ✅ |
| code/module02/pump_flow_model.py | ✅ tested |

Module 02 remnants: exercises (problem set, knowledge check), Lab 02 procedure.

---

## Central artifacts and manifests

| Item | Status |
|------|--------|
| curriculum/system_pipeline.md | ✅ |
| curriculum/capstone_architecture.md | ✅ |
| All 12 module manifests | ✅ |
| All 5 storyboard specs | ✅ |
| projects/capstone/README.md | ✅ |
| 8 root governance files | ✅ |

---

## What still needs work

- Module 01: COMPLETE (all lessons, summary, problem set, knowledge check, lab procedure + equipment, both code files)
- Modules 02–12: lesson content (manifests exist; content not started)
- Coaches: tutor prompts, instructor guides, capstone rubric
- docs/: course_overview, philosophy, prerequisites, assessment_guide
- Code for Modules 02–11 (stubs identified in manifests)
- Lab procedures for Labs 02–11

---

## Next action

Module 02 remnants (exercises + Lab 02 procedure), then Module 03 lesson content.
