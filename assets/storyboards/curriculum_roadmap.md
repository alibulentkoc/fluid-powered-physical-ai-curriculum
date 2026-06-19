# Storyboard: Curriculum Roadmap

**File:** `assets/storyboards/curriculum_roadmap.md`  
**Figure output target:** `assets/figures/curriculum_roadmap.svg`  
**Status:** 🔲 Storyboard written. Figure not yet created.

---

## Purpose

Show a learner entering the curriculum exactly where they are going and how the modules connect. The roadmap should communicate *arc*, not just list. It should make the destination (the Smart Agricultural Workcell) visible from the start.

---

## Audience

- New students, first week of Module 01
- Instructors evaluating the curriculum for adoption
- Contributors considering where to add content

---

## Educational Message

> You are not taking twelve separate lessons. You are building one machine, one layer at a time.

The figure must make this feel true. Every module should visibly point toward the same endpoint.

---

## Layout Concept

**Orientation:** Left to right (time flows left to right)

**Structure:**
- Three horizontal swim lanes:
  - Top lane: **Physical System** (Hydraulic hardware)
  - Middle lane: **Intelligence Layer** (Sensing, control, software)
  - Bottom lane: **Digital Twin** (Simulation and validation)

- 12 module nodes, numbered, arranged along an arc from left to right
- Each node is labeled with module number and short title
- Nodes are color-coded by curriculum phase:
  - Modules 01–04: Gray/blue — Foundations
  - Modules 05–08: Orange — Hydraulic Engineering
  - Modules 09–10: Green — Intelligence
  - Module 11: Purple — Digital Twin
  - Module 12: Gold — Capstone

- The Smart Agricultural Workcell appears as a central icon on the right, with arrows arriving from all three swim lanes

- A secondary row beneath the modules shows the pipeline stages (SENSE / UNDERSTAND / DECIDE / COMMAND / ACTUATE / VALIDATE) and which modules cover each stage

---

## Key Visual Elements

1. Module nodes as connected circles or rounded rectangles
2. Three swim-lane horizontal bands with labeled headers
3. Color progression from foundations (cool) to integration (warm)
4. Workcell icon at the right: simplified schematic of a hydraulic arm
5. Pipeline bar at the bottom as a color-coded reference strip

---

## Format Notes

- SVG preferred (scalable, can be embedded in docs and web)
- Width: 1200–1600px recommended
- Should remain readable when printed at A3 or scaled to 50% for inline display
- Use the curriculum's color palette once defined (see `assets/style_guide.md` when created)

---

## Dependencies

- Module list must be finalized before this figure is produced (all 12 manifests now complete ✅)
- Pipeline stages from `curriculum/system_pipeline.md` ✅
- Capstone subsystem names from `curriculum/capstone_architecture.md` ✅
