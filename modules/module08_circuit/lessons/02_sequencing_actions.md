# The machine sequences its actions
## Module 08 · Lesson 02

*A real task is not one motion — it is a sequence: position, then grip, then move, then release. This lesson gives the machine the ability to coordinate its two actuators in the right order, the first step from single motions toward a complete task.*

---

## Why The Machine Needs This

The machine has a primary cylinder for positioning and an end-effector actuator for gripping (Module 07). But a manipulation task needs them to work *in coordination*: the machine must position the end-effector, *then* grip, *then* move, *then* release — in a definite order, never gripping before it has arrived or moving before it has gripped. Two actuators sharing one pump cannot simply both run at once and hope for the best; the machine must sequence them.

The machine needs the logic and the circuit to coordinate its actuators in sequence. This is the bridge from "the machine can make a motion" to "the machine can perform a task" — the foundation of Autonomous Manipulation.

**Benchmark task supported:** Autonomous Manipulation (a task is a coordinated sequence of motions, and sequencing is the first step toward executing one) and Precision Positioning (correct sequencing ensures the machine positions before it acts).

---

## 1. The machine's problem

Consider the simplest real task: pick up a workpiece. It is not one motion — it is at least four, in a strict order:

1. **Position** the end-effector over the workpiece (primary cylinder extends)
2. **Grip** the workpiece (end-effector actuator closes)
3. **Move** the workpiece to its destination (primary cylinder retracts)
4. **Release** (end-effector actuator opens)

Get the order wrong and the task fails catastrophically: grip before positioning and the machine clamps empty air; move before gripping and it carries nothing; release before arriving and it drops the workpiece. The order is not optional — it is the task.

There is also a resource problem. Both actuators draw flow from the same pump (10.67 LPM). If both moved at once, they would share the flow, each moving slower and at unpredictable speeds depending on their relative loads. For a bench machine with one pump, running the actuators *in sequence* — one at a time — gives each the full, predictable flow, and enforces the correct order for free.

The machine's problem: coordinate its two actuators so they act in the correct sequence, one at a time, reliably.

---

## 2. The concept: sequencing, two ways

The machine can enforce a sequence by two distinct means — one hydraulic, one programmed — and the choice matters.

**Hydraulic sequencing (sequence valves).** A sequence valve holds off a second actuator until the first reaches a set pressure. When the first cylinder completes its stroke and pressure rises (it has bottomed out or met its load), the sequence valve opens and routes flow to the second actuator. The order is enforced *by the hydraulics themselves*, with no controller. This is robust and simple, but rigid — the sequence is fixed by the plumbing, and "pressure reached" is a crude proxy for "task step complete."

**Programmed sequencing (the controller).** The machine's controller (introduced in Module 06) commands each actuator in turn, using sensor feedback (Module 09) to know when each step is truly complete before starting the next. *Position* until the position sensor confirms arrival, *then* grip until the force sensor confirms the grip, *then* move. This is flexible — the sequence is software, easily changed — and precise, because it waits for the *actual* completion of each step, not a pressure proxy.

**The workcell uses programmed sequencing.** Because the machine is becoming intelligent — it will have sensors and a controller (Modules 09–10) — software sequencing is the natural choice. It is flexible (new tasks are new code, not new plumbing) and it integrates with the closed-loop control and state machine to come. The sequence valve is the simpler, dumber alternative the machine does *not* need, because it is building a brain. This is a case where the machine's intelligence makes a hydraulic component unnecessary.

For now, with the actuators running one at a time, the single pump comfortably drives whichever actuator is active at full flow.

---

## 3. Mathematical model

**Single-pump, sequential operation.** Because only one actuator moves at a time, each gets the full pump flow:
$$Q_{active} = Q_{pump} = 10.67\ \text{LPM}$$
and its speed is the full-flow speed from Module 05 — predictable, because it does not share flow.

**Why not parallel?** If both actuators ran in parallel, they would share flow based on their relative resistances. The flow to each:
$$Q_1 + Q_2 = Q_{pump}, \quad \frac{Q_1}{Q_2} \approx \sqrt{\frac{\Delta P_2}{\Delta P_1}}$$
(each path an orifice, flow splitting by the inverse square-root of resistance). This makes each actuator's speed depend on the *other's* load — unpredictable and hard to control. Sequencing avoids this entirely: one actuator, full flow, known speed.

**Sequence timing.** The total task time is the sum of the step times (plus brief transitions), since steps run in sequence:
$$t_{task} = t_{position} + t_{grip} + t_{move} + t_{release} + t_{transitions}$$
For the workcell, a positioning stroke of ~150 mm at ~90 mm/s takes ~1.7 s; the full pick-and-place cycle is the sum of such steps — the basis for the cycle-time and throughput analysis of Lesson 04.

---

## 4. Visual explanation

> See figure: `assets/figures/system_pipeline.svg` (the DECIDE → COMMAND → ACTUATE sequence)

Picture the task as a timeline, one actuator active in each segment: the primary cylinder extends (position), then the end-effector closes (grip), then the primary cylinder retracts (move), then the end-effector opens (release). At any instant, exactly one bar is active, drawing the full pump flow. A state diagram captures the logic: each state commands one actuator and waits for its completion signal before transitioning to the next. This state-machine view is exactly how the machine's controller (Module 10) will sequence the task — the figure previews the machine's decision logic.

---

## 5. Engineering example

**Why intelligent machines prefer programmed sequencing**

Older hydraulic machines relied heavily on sequence valves and mechanical interlocks to enforce order — clever plumbing that needed no electronics. But every change to the task meant re-plumbing. Modern intelligent machines sequence in software: the controller commands each step and uses sensors to confirm completion, so a new task is just new code.

The Smart Agricultural Workcell, built to be intelligent, takes the software path. This is a recurring theme of the curriculum: as the machine gains a brain and senses, it can replace hydraulic cleverness (sequence valves, mechanical interlocks) with flexible, sensor-driven software logic. The hydraulics get *simpler* as the intelligence grows. The machine sequences its pick-and-place not with a sequence valve but with a state machine that knows, from its sensors, exactly when each step is done — the subject of Module 10.

---

## 6. Worked example

**The machine's pick-and-place sequence.** Define the full coordinated sequence for a pick-and-place task, with the completion condition for each step.

| Step | Actuator | Action | Completion condition | Time (approx) |
|------|----------|--------|---------------------|---------------|
| 1. Position | Primary cylinder | extend to target | position sensor = target | ~1.7 s (150 mm @ 90 mm/s) |
| 2. Grip | End-effector | close jaws | force sensor = grip force | ~0.5 s |
| 3. Move | Primary cylinder | retract to destination | position sensor = destination | ~1.1 s (150 mm @ 132 mm/s) |
| 4. Release | End-effector | open jaws | jaw open confirmed | ~0.5 s |

*Total cycle time:* ≈ 1.7 + 0.5 + 1.1 + 0.5 + transitions ≈ **4–5 s per cycle**, giving ~12–15 cycles/minute.

Each step runs one actuator at full pump flow, waits for its sensor-confirmed completion, then transitions. The machine performs a coordinated task — not a single motion — for the first time. This sequence *is* the skeleton of the state machine the controller will execute in Module 10, and the cycle time feeds the throughput analysis in Lesson 04.

---

## 7. Interactive demonstration

```python
def task_sequence():
    """The machine's pick-and-place sequence with completion conditions."""
    steps = [
        ("position", "primary cylinder", "extend", "position == target", 1.7),
        ("grip",     "end-effector",     "close",  "force == grip_force", 0.5),
        ("move",     "primary cylinder", "retract","position == dest",    1.1),
        ("release",  "end-effector",     "open",   "jaw open confirmed",  0.5),
    ]
    t = 0.0
    for name, actuator, action, done_when, dur in steps:
        print(f"  [{t:4.1f}s] {name:9s}: {actuator:16s} {action:8s} "
              f"until {done_when}")
        t += dur + 0.2   # + transition
    print(f"  Total cycle: {t:.1f} s  ({60/t:.0f} cycles/min)")

task_sequence()
```

Run it. One actuator per step, each waiting for its completion condition — the machine coordinating a real task.

---

## 8. Coding exercise

Create `code/module08/task_sequencer.py` that:

1. Defines the pick-and-place sequence as an ordered list of steps with completion conditions
2. Simulates the sequence, tracking which actuator is active and the elapsed time
3. Enforces that only one actuator runs at a time (full pump flow to the active one)
4. Computes the total cycle time and throughput (cycles/minute)

This is the skeleton of the machine's task logic, realized as the state machine in Module 10.

---

## 9. Knowledge check

1. Why is a real manipulation task not a single motion?
2. What goes wrong if the machine performs the pick-and-place steps in the wrong order?
3. Why does the machine run its actuators in sequence rather than in parallel?
4. Compare hydraulic sequencing (sequence valves) with programmed sequencing. Which does the workcell use, and why?
5. How does the machine's growing intelligence let it simplify its hydraulics?

---

## 10. Challenge problem

The machine is given a faster duty target: 20 cycles per minute for the pick-and-place task.

**a)** What is the maximum cycle time allowed for 20 cycles/minute?

**b)** The current cycle is ~4.5 s (≈13/min). Where could the machine save time — which steps, and how? (Consider speeds and transitions.)

**c)** If the machine sped up the positioning stroke by running the pump faster (Module 05), what other subsystems are affected (flow, valve, heat)?

**d)** Could running two actuators in parallel help? What would the machine lose in speed predictability, and why does sequencing remain preferable?

---

## 11. Common mistakes

**Allowing steps out of order.** The sequence *is* the task. Gripping before positioning or releasing before arriving fails catastrophically. The machine must enforce the order.

**Running both actuators in parallel on one pump.** Shared flow makes each actuator's speed depend on the other's load — unpredictable and hard to control. Sequence them: one at a time, full flow, known speed.

**Using "pressure reached" as a completion signal when precision matters.** A sequence valve fires on pressure, a crude proxy for "step done." Sensor-confirmed completion (programmed sequencing) is precise and flexible.

**Adding sequence valves to an intelligent machine.** If the machine has a controller and sensors, software sequencing is more flexible and precise. Do not add hydraulic complexity the intelligence makes unnecessary.

---

## 12. Key takeaways

- A real task is a *coordinated sequence* of motions (position → grip → move → release), not a single motion.
- The order is the task; wrong order fails catastrophically. The machine must enforce it.
- With one pump, the machine sequences its actuators (one at a time, full flow, predictable speed) rather than running them in parallel (shared flow, unpredictable).
- Sequencing can be hydraulic (sequence valves) or programmed (controller + sensors); the workcell uses programmed sequencing for flexibility and precision.
- The pick-and-place sequence is the skeleton of the state machine the controller executes in Module 10; its cycle time (~4–5 s) feeds the throughput analysis.

---

## Machine Capability Added

> **Before this lesson the machine could not:** coordinate its actuators — it could make single motions but not perform a multi-step task in the correct order.
>
> **After this lesson the machine can:** sequence its two actuators through a coordinated task (position → grip → move → release), one at a time at full flow, each step confirmed before the next.

The machine now has **coordinated, sequenced action** — the bridge from single motions to a complete task. You can define the machine's pick-and-place as an ordered sequence with completion conditions, the skeleton of the autonomous task logic to come. This is the first real step toward Autonomous Manipulation.

**Digital twin contribution:** the task-sequence model is added to the twin — the ordered steps, their completion conditions, and the single-actuator-at-a-time flow allocation. The twin can now simulate a coordinated task sequence and predict its cycle time, not just individual motions.

---

*Lesson 02 — Version 0.1 | Next: Lesson 03 — How the machine fails safely (circuit protection)*
