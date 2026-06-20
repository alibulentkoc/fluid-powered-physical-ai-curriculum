# Storyboard: Module Integration Map

**File:** `assets/storyboards/module_integration_map.md`  
**Figure output target:** `assets/figures/module_integration_map.svg`  
**Status:** 🔲 Storyboard written. Figure not yet created.

---

## Purpose

Show how the knowledge and artifacts from each module flow into subsequent modules and into the capstone. Make visible the dependencies that cannot be seen by looking at the module list alone.

---

## Audience

- Instructors planning pacing and sequencing
- Students who want to understand why module order matters
- Contributors adding new content (need to understand upstream dependencies)

---

## Educational Message

> You cannot build the control system before you understand the valves. You cannot validate the digital twin before you have real sensor data. The order matters — and here is why.

---

## Layout Concept

**Figure type:** Directed acyclic graph (DAG) — module nodes with dependency arrows

**Nodes:** 12 module nodes + the capstone

**Arrows represent:**
- Conceptual dependency (must understand X before Y)
- Artifact dependency (uses output of module X in module Y)

**Key dependency chains to highlight:**

Chain 1 — Physics to Twin:
Module 01 → Module 04 → Module 08 → Module 11

Chain 2 — Hardware to Control:
Module 02 → Module 06 → Module 10

Chain 3 — Sensing to Validation:
Module 09 → Module 10 → Module 11 → Module 12

**Artifact labels on arrows:** Each arrow should note the specific artifact that flows: e.g., "cylinder ODE model" (04→08), "sensor data log" (09→11), "PID parameters" (10→12)

---

## Format Notes

- SVG preferred
- Width: 1200px
- Use consistent module colors from curriculum_roadmap.svg
- Arrows should be clearly directional (arrowheads)
- Artifact labels should be small but readable

---

## Dependencies

- All module manifests complete ✅

---
---

# Storyboard: Digital Twin Workflow

**File:** `assets/storyboards/digital_twin_workflow.md`  
**Figure output target:** `assets/figures/digital_twin_workflow.svg`  
**Status:** 🔲 Storyboard written. Figure not yet created.

---

## Purpose

Explain how the digital twin works as a running system — not just what it is, but what data flows into it, what it produces, and how a student interacts with it. This figure should make the abstract concept of a digital twin concrete and actionable.

---

## Audience

- Students entering Module 11
- Researchers and practitioners unfamiliar with digital twins in fluid power
- Reviewers of grant proposals or research papers based on this curriculum

---

## Educational Message

> The digital twin is not a finished product you receive. It is a living model you build and maintain alongside the physical system.

---

## Layout Concept

**Figure type:** Data flow diagram — two columns (physical system | digital twin) with data flows between them

**Left column — Physical System:**
```
[Pump + Motor]
      ↓ (pressurized flow)
[Valves]
      ↓ (flow command)
[Cylinder]
      ↓ (motion)
[End Effector]
      
[Sensors: pressure, position, flow, force]
      ↓ (sensor signals)
[Arduino + Raspberry Pi]
      ↓ (logged data / live stream)
```

**Right column — Digital Twin:**
```
[Pump Model]
      ↓
[Valve Model]
      ↓
[Cylinder ODE]
      ↓
[Sensor Noise Model]
      ↓
[State Estimator]
      ↓
[Residual Calculator]  ←── receives measured data from left column
      ↓
[Fault Detector]
      ↓
[Dashboard / Report]
```

**Data flow arrows between columns:**
- Physical → Twin: "Measured sensor data (CSV or live serial)"
- Twin → Physical: "Predicted states (overlaid on dashboard)"
- Twin → Physical: "Fault flags (alert to operator)"

**Incremental build annotation:**
A timeline bar at the bottom showing which module contributed each twin component:
```
[Cylinder ODE: M04] [Valve model: M06] [Pump model: M07] [Sensor noise: M09] [Controller: M10] [Integration: M11]
```

---

## Format Notes

- SVG preferred
- Width: 1400px; two-column layout
- Use consistent color coding: physical system in orange/warm tones, digital twin in blue/cool tones
- The incremental build timeline at bottom is unique to this figure and highly important — it makes visible that the twin is built progressively

---

## Dependencies

- `curriculum/system_pipeline.md` — VALIDATE stage definition ✅
- `curriculum/capstone_architecture.md` — Subsystem 6 ✅
- Module 11 manifest ✅
