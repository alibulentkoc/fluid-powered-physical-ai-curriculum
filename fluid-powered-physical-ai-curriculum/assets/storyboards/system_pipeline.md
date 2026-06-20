# Storyboard: System Pipeline

**File:** `assets/storyboards/system_pipeline.md`  
**Figure output target:** `assets/figures/system_pipeline.svg`  
**Status:** 🔲 Storyboard written. Figure not yet created.

---

## Purpose

Make the SENSE → UNDERSTAND → DECIDE → COMMAND → ACTUATE → VALIDATE pipeline visually memorable and physically grounded. Students should be able to point to a component in the workcell and immediately locate it on this figure.

---

## Audience

- Students entering Module 01
- Revisited in Modules 09, 10, 11 as each stage becomes primary
- Used as a reference throughout the course

---

## Educational Message

> An intelligent fluid-powered machine does six things. Every part of this curriculum develops one or more of those capabilities.

---

## Layout Concept

**Orientation:** Horizontal, left to right

**Central element:** A simplified isometric or schematic diagram of the Smart Agricultural Workcell — recognizable as a hydraulic arm with cylinder, end effector, sensors, and controller box

**Pipeline arrow:** A bold horizontal flow arrow above the workcell schematic, segmented into six colored blocks:

```
[SENSE] → [UNDERSTAND] → [DECIDE] → [COMMAND] → [ACTUATE] → [VALIDATE]
```

**Below each stage block:** A vertical "drop-down" list of the physical or software components in the workcell that belong to that stage:

- SENSE: pressure transducer, position sensor, flow sensor, load cell, camera
- UNDERSTAND: signal conditioning, state estimator, filter
- DECIDE: PID controller, state machine, safety logic
- COMMAND: Arduino, Raspberry Pi, serial protocol
- ACTUATE: solenoid valve, DCV, cylinder, motor
- VALIDATE: digital twin, residual analysis, fault detection

**Color coding:** Each stage has a distinct color. The same colors are used in the workcell diagram to tint the relevant components.

---

## Key Visual Elements

1. Six-stage pipeline bar with stage names and stage colors
2. Workcell schematic with color-tinted component regions
3. Component lists below each stage
4. A caption reading: "Every module develops one or more stages of this pipeline"
5. Optional: module number badges on each stage showing which modules develop it

---

## Format Notes

- SVG preferred
- Width: 1400px; designed for widescreen display and landscape print
- Should be usable as a poster (A2 or larger)
- Critical that the workcell schematic is recognizable — abstract but accurate

---

## Dependencies

- `curriculum/system_pipeline.md` (pipeline definitions and module map) ✅
- `curriculum/capstone_architecture.md` (component lists by subsystem) ✅
