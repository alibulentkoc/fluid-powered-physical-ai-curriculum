# Module 12 — Fluid-Powered Physical AI Capstone

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 12 of 12  
**Estimated Duration:** 3–4 weeks  
**Capstone Subsystems:** All six  
**Pipeline Stages:** All six (SENSE → UNDERSTAND → DECIDE → COMMAND → ACTUATE → VALIDATE)

> **Machine mission:** The Complete Autonomous Workcell (Capstone)
>
> **Machine Capability Added:** Operate as one demonstrated, validated, documented intelligent system.
>
> **Benchmark tasks:** All three demonstrated and validated
>
> **Artifact:** Demonstration System (curriculum completion)

---

## Module Purpose

Module 12 is not a new module. It is the culmination of everything that came before.

Students have designed a hydraulic system, selected components, built a sensor layer, written embedded control code, and developed a digital twin. Module 12 brings all of that together into one working, demonstrated, documented platform: the Smart Agricultural Workcell operating as an intelligent fluid-powered machine.

The goal is not a perfect system. The goal is a *real* system — one that works, one that students understand completely, and one that students can describe, defend, and extend.

**Workcell contribution:** The workcell, complete and demonstrated. All six subsystems integrated. Two manipulation tasks performed autonomously. Digital twin running in parallel and validated.

---

## Learning Objectives

- LO-12.1: Integrate all six workcell subsystems into a functioning system
- LO-12.2: Commission and validate the workcell against defined performance specifications
- LO-12.3: Demonstrate at least two autonomous manipulation tasks
- LO-12.4: Run the digital twin in parallel with the physical system during a demonstration
- LO-12.5: Produce professional-level documentation: circuit schematic, wiring diagram, code repository, validation report, and final report
- LO-12.6: Reflect critically on system performance, design decisions, and what would be done differently
- LO-12.7: Identify at least one research or extension direction that the platform enables

---

## Prerequisite Knowledge

- Modules 01–11 complete
- All workcell subsystems functional at the subsystem level (tested individually in Modules 05–11)

---

## Module Structure

Module 12 is structured as a project sprint, not a series of topic lessons. The learning happens through integration, debugging, and demonstration.

### Phase 1 — System Assembly (Week 1)

**Activities:**
- Assemble the physical workcell: hydraulic circuit, sensor wiring, embedded electronics
- Commission subsystems in order: hydraulic power → fluid transport → motion control → actuation → sensing → control
- Run the checklist: does each subsystem function correctly in isolation?

**Milestone:** All subsystems operational. Basic open-loop valve command and sensor readback confirmed.

---

### Phase 2 — Closed-Loop Integration (Week 2)

**Activities:**
- Activate position control loop
- Tune PID for positioning task
- Activate end-effector control (grip force or position)
- Test task sequence: approach → grip → lift → return
- Connect digital twin to live sensor stream

**Milestone:** Position step response meets specification (< 5% overshoot, < 2 mm steady-state error). Task sequence completes without fault.

---

### Phase 3 — Demonstration Tasks (Week 3)

**Task 1: Precision Positioning**  
Command the primary cylinder to five positions within the work envelope. Measure actual vs. commanded position. Calculate mean absolute error and maximum error. Digital twin prediction overlaid.

**Task 2: Grasping and Handling**  
Pick up a test object (defined mass and geometry). Transport it within the work envelope. Release it at a target location. Success criteria: object not damaged, placement within ±10 mm of target.

**Extension tasks (optional):**
- Camera-guided approach
- Force-limited grip
- Fault detection during operation

---

### Phase 4 — Documentation and Presentation (Week 4)

**Deliverables:**

| Deliverable | Description |
|-------------|-------------|
| Final hydraulic schematic | Complete ISO 1219 circuit diagram with component list |
| Wiring diagram | All sensors, controllers, and power connections |
| Code repository | All Arduino sketches and Python scripts, documented and version-controlled |
| Digital twin notebook | Full twin with validation against demonstration data |
| Validation report | Measured performance vs. specifications, residual analysis, fault detection test |
| Final report | 10–15 pages: system description, design decisions, results, critical reflection, future directions |
| Demonstration video | 5–10 minutes: system overview, both tasks performed, digital twin display |

---

## Capstone Performance Specifications

| Metric | Target |
|--------|--------|
| Position step response — overshoot | < 5% |
| Position step response — settling time | < 3 s |
| Position steady-state error | < 2 mm |
| Grasping task success rate | ≥ 4/5 attempts |
| Placement accuracy | ± 10 mm |
| Digital twin prediction error (position) | < 5 mm RMS over full task cycle |
| Fault detection — true positive rate | ≥ 80% for injected test faults |

Students who do not meet a target must document why and describe how they would address it.

---

## Integration Checklist

Before demonstration:

**Hydraulic System**
- [ ] System pressure tested to working pressure without leak
- [ ] Relief valve set and verified
- [ ] Both actuators cycle through full stroke without fault
- [ ] Filter condition checked

**Sensing**
- [ ] All sensors calibrated with calibration records
- [ ] Data logging verified: all channels recording at ≥ 10 Hz
- [ ] Signal conditioning noise level acceptable

**Embedded Control**
- [ ] Arduino firmware: all safety limits active
- [ ] PID parameters logged and reproducible
- [ ] Task sequence tested 5 times without fault
- [ ] Watchdog timer verified

**Digital Twin**
- [ ] Twin validated against at least one historical run
- [ ] Fault detection rules tested with synthetic faults
- [ ] Dashboard displays live (or replay) data correctly

---

## Assessment

Modules 01–11 each contribute individual assessments. Module 12 is assessed holistically:

| Component | Weight |
|-----------|--------|
| System integration and commissioning (observed) | 20% |
| Demonstration: Task 1 (positioning) | 20% |
| Demonstration: Task 2 (grasping) | 20% |
| Digital twin and validation report | 20% |
| Final report | 20% |

Rubric details in `coaches/capstone_rubric.md` (to be developed).

---

## What Comes After

The Smart Agricultural Workcell is a platform. Module 12 is not the end — it is the beginning of what can be built on this foundation:

- End-effector library expansion
- Machine learning for task classification or anomaly detection
- Multi-workcell coordination
- Full tractor-mounted implementation
- Research publication on intelligent electro-hydraulic control

The curriculum is open-source. The platform is documented. The invitation to extend it is explicit.

---

*Module 12 Manifest — Version 0.1*
