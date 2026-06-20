# Module 10 — Summary

*Embedded Control — The Machine Decides and Acts*

---

## The machine's journey through this module

The machine entered Module 10 able to perceive (Module 09) but unable to act on what it perceived — it sensed errors but could not correct them. It leaves with a complete, validated Embedded Control System: it closes the loop, positions precisely, runs its whole task autonomously, protects itself, and validates its control in simulation before acting. This is the module where the machine gains a brain.

1. **Act on perception** — the closed loop connects sensing to action; proportional control corrects toward a target.
2. **Control precisely** — the PID controller eliminates steady-state error and damps overshoot, meeting <5% overshoot, <2 mm error.
3. **Run its task safely** — the state machine sequences the autonomous task; independent safety logic forces a safe state on any danger.
4. **Validate before acting** — the closed-loop simulation predicts and validates control in the twin before hardware.

---

## The machine's control system (the established design)

| Element | Specification |
|---------|--------------|
| Control loop | Closed-loop position feedback |
| Controller | PID, $K_p=0.02$, $K_i=0.002$, $K_d=0.04$, anti-windup, derivative filtering |
| Performance | 0.6% overshoot, ~1.2 mm steady-state error (meets <5%, <2 mm) |
| Task logic | State machine: IDLE → APPROACH → GRIP → LIFT → MOVE → RELEASE → FAULT |
| Safety | Pressure limit (118 bar), position limit (295 mm), watchdog (200 ms) — priority override |
| Architecture | Pi (task) ↔ Arduino (PID + safety firmware) |
| Validation | Simulation-first: predicted then confirmed against hardware |

All numbers verified against the Module 10 code.

---

## Machine Capability Added

> **Before this module the machine could not:** act on what it perceived — it sensed but could not correct, decide, or protect itself autonomously.
>
> **After this module the machine can:** close the loop, position to spec, run its full task autonomously with safety, and validate its control in simulation before acting.

The machine gained a **validated control brain** — perception turned into precise, autonomous, safe action.

## Benchmark Task Advanced

**Precision Positioning** is now complete as a closed-loop capability: the PID controller achieves <5% overshoot and <2 mm steady-state error, validated in simulation and confirmed against hardware — accurate, repeatable positioning, the benchmark fully met. **Force-Controlled Interaction** gained closed-loop force regulation (the same PID structure regulates grip force). **Autonomous Manipulation** advanced decisively: the state machine executes the full pick-and-place task autonomously from sensor feedback, with safety override — the machine running its own task.

## Digital Twin Contribution

The twin became a **control-design environment**:
- **Closed-loop structure** — feedback from sensed position to valve command
- **PID controller** — the tuning environment predicting step response for any gains
- **State machine + safety** — simulating the complete autonomous task and its safety responses
- **Closed-loop validation** — predicted-vs-actual comparison validating the twin for control design

The twin can now predict and validate the machine's *controlled* behavior — the capability that makes a digital twin genuinely useful for engineering. The machine designs its control simulation-first, the payoff of the physics-based twin built across the whole curriculum.

## Module Artifact

The **Embedded Control System** — the closed-loop PID controller, the autonomous task state machine, the safety logic, and the simulation-validated control design. The machine's brain.

---

## Lessons in this module

1. `01_acting_on_perception.md` — the machine acts on perception (the closed loop)
2. `02_pid_controller.md` — a precise controller (PID and tuning)
3. `03_state_machine_safety.md` — task logic and safety (the state machine)
4. `04_closing_loop_simulation.md` — validating control before acting (simulation-first)

## Code (all tested)

- `code/module10/closed_loop_basics.py` — open-loop vs. proportional closed-loop
- `code/module10/pid_controller.py` — the PID controller, tuned to spec
- `code/module10/state_machine.py` — autonomous task logic + safety override
- `code/module10/closed_loop_simulation.py` — PID + machine model, validated step response

## Lab

- `labs/lab10_closed_loop/` — tuning and validating the machine's position controller

---

## Self-assessment checklist

Before Module 11, confirm you can:

- [ ] Explain why open-loop positioning is inconsistent and how feedback corrects it
- [ ] Explain what each PID term does and why hydraulics are hard to control
- [ ] Tune a PID to meet an overshoot/error spec, with anti-windup
- [ ] Describe the task state machine and its sensor-driven transitions
- [ ] Explain the safety logic and why it lives below the task logic
- [ ] Explain simulation-first control and the predicted-vs-actual validation
- [ ] Run all four Module 10 code files

---

## What comes next

The machine now perceives, decides, and acts — but its digital twin, though built and validated piece by piece, is not yet a single integrated system running alongside the machine. Module 11 — The Integrated Digital Twin — brings all the twin's models together into one live counterpart that runs in parallel with the machine, monitors it continuously via residuals, detects faults, and enables predictive maintenance. The control system of this module runs the machine; the integrated twin of Module 11 watches over it.

---

*Module 10 complete. The machine decides and acts. Built natively to the Physical AI pattern. All numerical claims verified against tested code.*
