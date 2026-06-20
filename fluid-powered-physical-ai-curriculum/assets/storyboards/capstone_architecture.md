# Storyboard: Capstone Architecture

**File:** `assets/storyboards/capstone_architecture.md`  
**Figure output target:** `assets/figures/capstone_architecture.svg`  
**Status:** 🔲 Storyboard written. Figure not yet created.

---

## Purpose

Give students a complete, labeled view of the Smart Agricultural Workcell as an engineering system. This figure should be the one students return to constantly throughout the course — pinning on the wall, annotating with module numbers, and using as a navigation aid.

---

## Audience

- Students, Modules 01–12 (persistent reference)
- Instructors, contributors
- Grant applications and project proposals

---

## Educational Message

> This is the machine. By the end of the course, you will understand every part of it.

---

## Layout Concept

**Figure type:** Annotated engineering diagram — not a photograph, but a clear schematic-style illustration with callout labels

**Content:**

Left side — Hydraulic System:
- Reservoir with fluid level indicator
- Electric motor driving gear pump
- Pressure relief valve
- Filter (return line)
- Supply and return lines (color coded: red for high-pressure supply, blue for return)
- 4/3 solenoid DCV
- Flow control valve
- Primary double-acting cylinder
- Secondary actuator (small cylinder or motor)
- End effector (interchangeable — show parallel jaw gripper as default)

Right side — Intelligence System:
- Pressure transducers (callouts to cylinder ports)
- Linear position sensor (callout to cylinder rod)
- Flow sensor (callout to supply line)
- Load cell (callout to end effector)
- Camera (pointing at workspace)
- Arduino Mega (labeled: "Low-level I/O")
- Raspberry Pi 4 (labeled: "Task logic + Digital Twin interface")

Center/Background — Digital Twin:
- Laptop or screen icon showing a graph (simulated vs. measured position)
- Arrow from Raspberry Pi to the screen labeled "Sensor data"
- Arrow from screen to the workcell labeled "Commands"

**Callout labels:** Each component has a label with: component name, subsystem number (e.g., "S1: Hydraulic Power"), and the primary module that covers it (e.g., "Module 05")

---

## Format Notes

- SVG preferred, also export as high-res PNG
- Width: 1600px minimum
- Color-code by subsystem using the same palette as curriculum_roadmap.svg
- This is the single most important figure in the curriculum — allocate significant design effort here

---

## Dependencies

- `curriculum/capstone_architecture.md` — all six subsystems and component lists ✅
- Hardware specifications from Module manifests 05–09
