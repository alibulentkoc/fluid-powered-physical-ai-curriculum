# Module 03 — Hydraulic Fluids and Energy Transmission

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 03 of 12  
**Estimated Duration:** 1.5 weeks  
**Capstone Subsystems:** 2 (Fluid Transport)  
**Pipeline Stages:** ACTUATE (transmission), VALIDATE (fluid condition monitoring)

---

## Module Purpose

The fluid is not background. The fluid *is* the power transmission medium. Its properties determine how efficiently energy moves through the system, how long components last, and how the system behaves at temperature extremes.

In an intelligent system, fluid condition is also a sensing target. Contamination, temperature, and viscosity all affect system performance in ways a digital twin must account for.

This module is shorter than most. Its purpose is precise: give students the fluid property knowledge they need to make informed selections and to model transmission behavior.

**Workcell contribution:** Students make and document the fluid specification for their Smart Agricultural Workcell — fluid type, viscosity grade, operating temperature range, and contamination target.

---

## Learning Objectives

- LO-03.1: Explain the four primary functions of hydraulic fluid: power transmission, lubrication, sealing, and heat transfer
- LO-03.2: Define viscosity and viscosity index, and explain their significance for system performance
- LO-03.3: Describe how temperature affects fluid viscosity and system behavior
- LO-03.4: Explain ISO cleanliness codes and why contamination is the primary cause of hydraulic failure
- LO-03.5: Compare fluid types: mineral oil, synthetic, biodegradable (HE, HETG, HEES) — appropriate selection for agricultural environments
- LO-03.6: Calculate energy loss due to viscous friction (basic pipe flow)
- LO-03.7: Describe how a digital twin must account for fluid temperature and viscosity change over time

---

## Prerequisite Knowledge

- Modules 01, 02 complete
- Basic physics: temperature, density

---

## Key Topics

### Topic 1 — What Hydraulic Fluid Actually Does
Four functions. Power transmission (incompressibility). Lubrication (pump and motor internals). Sealing (viscosity fills clearances). Heat removal (fluid circulates heat to reservoir/cooler).

**Workcell connection:** The workcell runs indoors in an educational setting. How does this affect fluid selection compared to an outdoor agricultural machine?

### Topic 2 — Viscosity and the Viscosity-Temperature Relationship
Dynamic vs. kinematic viscosity. ISO VG grades (22, 32, 46, 68, 100). Viscosity Index. The Walther equation. Why cold start is dangerous and hot running causes leakage.

**Workcell connection:** Students model the viscosity of their selected fluid from 10°C to 80°C and identify the acceptable operating window.

### Topic 3 — Contamination, Filtration, and ISO Cleanliness
ISO 4406 cleanliness code. Where contamination enters. Filter rating (Beta ratio, absolute micron rating). Component sensitivity to contamination. Why most hydraulic failures are contamination-related.

**Workcell connection:** Students specify the filter for the workcell based on the most sensitive component (likely the directional control valve).

### Topic 4 — Energy Losses in Fluid Transmission
Viscous pipe friction (Darcy-Weisbach). Reynolds number. Laminar vs. turbulent flow. Fitting losses. Why transmission efficiency depends on fluid and pipe sizing.

**Workcell connection:** First estimate of pressure drop between the pump and the primary cylinder in the workcell.

---

## Capstone Connection

**Deliverable this module:** Fluid Specification Document for the Smart Agricultural Workcell. One page covering: fluid type, ISO VG grade, operating temperature range, ISO cleanliness target, filter specification, and rationale for each choice.

**Digital twin contribution:** Viscosity-temperature model (`viscosity(T)` function) added to the twin. First pipe friction loss calculation.

---

## Labs

**Lab 03 — Viscosity Observation**  
Compare the flow behavior of two fluids of different viscosity (e.g., water and cooking oil, or two hydraulic oils of different VG grades) through the same tube at the same temperature. Observe and record flow rate and character. Introduce the viscometer concept.

*Safety note: Use food-grade or clearly non-hazardous fluids for this demonstration. No heating above 60°C without dedicated equipment.*

---

## Code

`code/module03/viscosity_model.py` — Plot viscosity vs. temperature for ISO VG 46 hydraulic oil using the Walther equation. Overlay the acceptable viscosity window for a typical gear pump.

`code/module03/pipe_friction.py` — Calculate pressure drop in a pipe given flow rate, diameter, length, and fluid viscosity. Plot pressure drop vs. flow rate.

---

## Assessment

- Short calculation: viscosity at 40°C and 80°C, pressure drop for workcell supply line
- Fluid specification document
- Reflection: how would fluid selection change if the workcell were deployed outdoors in a Nordic winter?

---

*Module 03 Manifest — Version 0.1*
