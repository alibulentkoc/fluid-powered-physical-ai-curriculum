# Module 11 — Digital Twins for Fluid-Powered Systems

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 11 of 12  
**Estimated Duration:** 2.5 weeks  
**Capstone Subsystems:** 6 (Digital Twin)  
**Pipeline Stages:** VALIDATE

> **Machine mission:** The Integrated Digital Twin
>
> **Machine Capability Added:** Run one live twin that mirrors, monitors, and refines itself.
>
> **Benchmark task advanced:** Autonomous Manipulation (self-monitoring)
>
> **Artifact:** Integrated Digital Twin

---

## Module Purpose

The digital twin is not new to students at this point. They have been building it since Module 04.

What Module 11 does is integrate, formalize, and validate. Students assemble the component models developed across the curriculum into a single, coherent software system that runs alongside the physical workcell, ingests real sensor data, and produces actionable insight: *is the system behaving as expected, and if not, where is the discrepancy?*

This module also introduces the ideas that elevate a simulation to a true digital twin: real-time data synchronization, parameter estimation, fault detection, and predictive monitoring.

**Workcell contribution:** A complete, validated digital twin of the Smart Agricultural Workcell. The twin receives sensor data from the physical system, runs a parallel simulation, and reports residuals and fault flags.

---

## Learning Objectives

- LO-11.1: Define a digital twin and distinguish it from a simulation (data synchronization, bidirectional coupling, validation)
- LO-11.2: Integrate previously developed component models (pump, valve, pipe, cylinder, sensor) into a unified system model
- LO-11.3: Synchronize the digital twin with live sensor data from the workcell
- LO-11.4: Calculate and plot residuals (measured − predicted) for each sensor channel
- LO-11.5: Use residual analysis to identify model errors and hardware faults
- LO-11.6: Implement basic parameter estimation: fit cylinder friction coefficient to measured data
- LO-11.7: Design a fault detection rule set based on residual thresholds
- LO-11.8: Build a monitoring dashboard that displays live data and twin predictions simultaneously

---

## Prerequisite Knowledge

- Modules 01–10 complete
- Module 04: cylinder ODE simulation
- Module 08: integrated circuit simulation
- Module 09: sensor data logging
- Module 10: PID controller simulation
- Python: SciPy, Matplotlib, pandas (intermediate)

---

## Key Topics

### Topic 1 — What Makes a Digital Twin
Simulation vs. digital twin: the synchronization criterion. Asset model, state estimator, and data connection. The twin lifecycle: calibration → operation → validation → update.

**Workcell connection:** Mapping the workcell components to the twin's asset model. Identifying which states are directly measured (pressure, position) and which must be inferred (friction coefficient, valve dead-band).

### Topic 2 — System Integration: Assembling the Twin
Connecting pump → pipe → valve → cylinder into a single ODE system. Shared state vector. Handling the coupling between subsystems. Time-stepping strategy for the integrated model.

**Workcell connection:** Combining Modules 04–07 simulation notebooks into `workcell_twin.py` — a single runnable model of the entire workcell.

### Topic 3 — Data Synchronization
Reading logged CSV data into the twin. Aligning time axes. Resampling mismatched sample rates. Running the twin in replay mode: step through time, feed measured inputs, compare predicted outputs.

**Workcell connection:** Feed Module 09–10 sensor logs into the twin. Plot measured vs. predicted position, pressure, and force on the same axes.

### Topic 4 — Residual Analysis and Fault Detection
Residual definition: ε = y_measured − y_predicted. Healthy vs. faulty residual patterns. Threshold-based fault detection. Examples: cylinder seal leak (pressure residual rises), sensor drift (position residual grows slowly), valve hysteresis (asymmetric response residual).

**Workcell connection:** Implement a fault detection system that raises flags when residuals exceed thresholds. Test with a simulated fault (e.g., add a known offset to one sensor).

### Topic 5 — Parameter Estimation
Why model parameters are never perfectly known. Fitting friction coefficient to measured step response. Simple least-squares fitting using SciPy `curve_fit`. Iterative model refinement.

**Workcell connection:** Improve the cylinder friction model by fitting it to the measured step response from Module 10.

### Topic 6 — Monitoring Dashboard
Real-time vs. replay mode. Matplotlib animation or simple web dashboard (Flask/Dash). Key displays: position tracking, pressure, residuals, fault flags. What an operator would look at.

**Workcell connection:** `twin_dashboard.ipynb` — a monitoring dashboard for the workcell. Can run in replay mode on logged data or live if the system is running.

---

## Capstone Connection

**Major deliverable this module:** Complete validated digital twin of the Smart Agricultural Workcell.

Components:
- `code/module11/workcell_twin.py` — integrated system model
- `code/module11/data_sync.py` — sensor log ingestion and time alignment
- `code/module11/fault_detection.py` — residual calculation and threshold rules
- `code/module11/parameter_estimation.ipynb` — friction fitting notebook
- `code/module11/twin_dashboard.ipynb` — monitoring dashboard

Validation report: plot of measured vs. predicted for all sensor channels across a full task cycle, residual analysis, identified model-hardware discrepancies and their explanations.

---

## Labs

**Lab 11 — Twin Validation**  
Run a complete task cycle on the physical workcell. Log all sensor data. Feed the log into the digital twin. Produce measured-vs-predicted plots. Write a validation report: where does the twin agree with the hardware, and where does it diverge? Propose at least one model improvement.

---

## Code

`code/module11/workcell_twin.py` — Full workcell digital twin. Runnable standalone.

`code/module11/twin_dashboard.ipynb` — Live or replay monitoring dashboard.

`code/module11/fault_injection_test.py` — Test script: inject synthetic faults into sensor data, verify fault detection raises correct flags.

---

## Assessment

- Explain in writing: what distinguishes a digital twin from a physics simulation?
- Implement a residual-based fault detection rule for a cylinder seal leak
- Validation report: measured vs. predicted for a full workcell task cycle, with annotated discrepancy analysis

---

*Module 11 Manifest — Version 0.1*
