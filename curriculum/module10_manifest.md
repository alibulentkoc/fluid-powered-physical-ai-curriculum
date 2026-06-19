# Module 10 — Electro-Hydraulic Systems and Embedded Control

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 10 of 12  
**Estimated Duration:** 3 weeks  
**Capstone Subsystems:** 3 (Motion Control), 5 (Sensing and Intelligence)  
**Pipeline Stages:** UNDERSTAND, DECIDE, COMMAND

---

## Module Purpose

This is the intelligence module.

Students have a fully instrumented hydraulic system. They have sensor data. Now they must close the loop: use sensor measurements to make decisions and issue commands that drive the system toward a desired state.

This module covers the full embedded control stack: from the physics of feedback control, through PID implementation on Arduino, to task-level sequencing on the Raspberry Pi. It is the most software-intensive module in the curriculum and the one where fluid power and Physical AI most directly meet.

**Workcell contribution:** Working closed-loop position control of the primary workcell cylinder. A complete task sequence (approach → grip → lift → return) running autonomously on the embedded system.

---

## Learning Objectives

- LO-10.1: Explain the difference between open-loop and closed-loop control, and why closed-loop is necessary for precision hydraulic positioning
- LO-10.2: Derive and implement a proportional-integral-derivative (PID) controller for cylinder position
- LO-10.3: Tune a PID controller using the Ziegler-Nichols method and systematic trial-and-error
- LO-10.4: Implement position control on Arduino using sensor feedback and valve command output
- LO-10.5: Design and implement a multi-step task sequence on Raspberry Pi (state machine architecture)
- LO-10.6: Implement safety logic: pressure limit, position limit, watchdog timer
- LO-10.7: Describe the challenges specific to hydraulic control: nonlinearity, friction, dead-band, and compressibility
- LO-10.8: Connect the control algorithm to the digital twin — simulate the closed-loop system before running on hardware

---

## Prerequisite Knowledge

- Modules 01–09 complete
- Module 09: sensors wired and data logging working
- Python: intermediate (functions, loops, file I/O)
- Arduino: comfortable with `analogRead()`, `analogWrite()`, `Serial`

---

## Key Topics

### Topic 1 — Why Hydraulic Control is Hard
Nonlinearity of the orifice equation. Friction and dead-band in the valve. Compressibility-induced lag. Load-dependent velocity. How these differ from controlling a DC motor and why they matter for PID tuning.

**Workcell connection:** Demonstrate open-loop positioning of the workcell cylinder. Show the inconsistency that motivates closed-loop control.

### Topic 2 — Feedback Control Fundamentals
Error, proportional response, integral windup, derivative kick. Block diagram of a closed-loop system. Transfer function concept (intuitive, not rigorous). Why proportional alone is usually insufficient.

**Workcell connection:** Draw the control block diagram for the workcell position loop.

### Topic 3 — PID Implementation on Arduino
Discrete-time PID. Anti-windup. Derivative filtering. Output clamping (valve command saturation). Sample rate considerations. Code structure: read sensor → compute error → compute PID → write output → wait.

**Workcell connection:** `position_control.ino` — PID position controller for the primary workcell cylinder.

### Topic 4 — PID Tuning
Ziegler-Nichols open-loop method. Trial-and-error with logged data. Understanding overshoot, steady-state error, and oscillation as symptoms of tuning problems. The role of the digital twin in predicting tuning behavior before hardware testing.

**Workcell connection:** Tune the PID for a 200 mm step response in the workcell. Target: < 5% overshoot, < 2 mm steady-state error.

### Topic 5 — Task Sequencing on Raspberry Pi
State machine architecture. States: IDLE, APPROACH, GRIP, LIFT, HOLD, RETURN, FAULT. Transitions and guards. Communication between Raspberry Pi (task logic) and Arduino (low-level control). Serial command protocol design.

**Workcell connection:** Implement the full workcell task sequence as a Python state machine on the Raspberry Pi.

### Topic 6 — Safety Logic
Pressure limit: override valve command if system pressure exceeds threshold. Position limit: hard stop before physical end of stroke. Watchdog timer: if communication is lost, return to safe state. Why safety is not an afterthought in fluid-powered machines.

**Workcell connection:** Safety checks integrated into the workcell Arduino firmware.

### Topic 7 — Simulating the Closed-Loop System
Adding the PID controller to the Module 08 integrated simulation. Simulating the full closed-loop response. Using the simulation to predict PID parameters before hardware tuning. Identifying simulation-hardware discrepancies.

**Workcell connection:** Simulate the workcell position step response with the digital twin before first hardware run. Record the prediction and compare to actual.

---

## Capstone Connection

**Major deliverable this module:** Working electro-hydraulic control system for the Smart Agricultural Workcell.

- `position_control.ino` — Arduino PID position controller
- `task_sequencer.py` — Raspberry Pi state machine for task execution
- `safety_monitor.py` — Pressure and position limit monitoring
- Tuning log: recorded step responses, PID parameters, performance metrics
- Closed-loop simulation in the digital twin

**Digital twin contribution:** PID controller simulation. Closed-loop system model with valve, cylinder, friction, and control algorithm. Simulation-hardware comparison for the step response.

---

## Labs

**Lab 10A — Open-Loop Positioning**  
Command the cylinder to three positions using timed open-loop valve commands. Measure actual position reached. Quantify the error and inconsistency that motivates closed-loop control.

**Lab 10B — PID Position Control**  
Implement the PID controller. Command a 150 mm step. Log the response. Tune Kp, Ki, Kd systematically. Plot and annotate the best response.

**Lab 10C — Full Task Sequence**  
Run the complete workcell task sequence (approach → grip → lift → return). Log all sensor channels. Verify task completion criteria are met for each step.

---

## Code

`code/module10/position_control/position_control.ino` — Full Arduino PID position controller with safety limits and serial command interface.

`code/module10/task_sequencer.py` — Raspberry Pi state machine. Sends commands to Arduino, monitors responses, logs data.

`code/module10/closed_loop_sim.ipynb` — Closed-loop simulation: digital twin with PID controller in the loop.

`code/module10/pid_tuning_analysis.ipynb` — Analyze tuning logs: plot step responses, calculate performance metrics.

---

## Assessment

- Derive the discrete-time PID equation from the continuous form
- Explain what integral windup is and how to prevent it
- Lab report: tuning log, annotated step response plots, achieved performance vs. target
- Written reflection: what limitations of the hydraulic system most affected your ability to achieve the tuning targets?

---

## Connections Forward

Module 10 delivers a working intelligent fluid-powered system. Module 11 builds the full digital twin that models, monitors, and validates it. Module 12 integrates everything for demonstration and final assessment.

---

*Module 10 Manifest — Version 0.1*
