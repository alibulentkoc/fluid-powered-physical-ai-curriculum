# Choosing the machine's actuator type
## Module 07 · Lesson 04

*The machine has a cylinder for its main motion — but its end-effector might need rotation, not linear push. This lesson is the engineering decision: for each task the machine performs, does it need a cylinder or a motor? Requirements first, then the choice.*

---

## Why The Machine Needs This

The machine's primary actuator is a cylinder — correct for linear positioning and force. But the workcell's end-effector tasks are varied: some need linear motion (press, lift), some need rotation (turn a gripper, rotate a part for inspection), some need continuous spinning. A cylinder cannot rotate continuously; a motor cannot hold a precise linear position. The machine must *choose the right actuator type for each task*, or it picks an actuator that physically cannot do the job.

This lesson gives the machine the decision logic: given a task's requirements, does it need a cylinder (linear, finite stroke, position hold) or a hydraulic motor (continuous rotation, speed control)? Like the pump selection in Module 05, this is requirements-first engineering — the task defines the need, and the actuator type follows.

**Benchmark task supported:** Force-Controlled Interaction and Autonomous Manipulation (the right actuator type for each end-effector task is what lets the machine grip, turn, and manipulate objects correctly).

---

## 1. The machine's requirements

Before choosing any actuator, the machine states what each task needs. The decision is judged against these requirements — the actuator type follows from the task, not from habit.

The workcell's actuator tasks and their requirements:

| Task | Motion needed | Force/torque | Position hold? | Range |
|------|--------------|--------------|----------------|-------|
| Primary positioning | linear | high force | yes (hold target) | finite (300 mm stroke) |
| Gripping | linear (jaw close) | controlled force | yes (hold grip) | small finite |
| Part rotation (inspect) | rotary | low torque | sometimes | continuous or large angle |
| Conveyor/spin (if present) | rotary | low torque | no | continuous |

Notice the split: positioning and gripping need *linear, finite, holdable* motion; rotation and spinning need *rotary, continuous* motion. These are fundamentally different requirements, and they point to different actuators. The machine's problem: match each task to the actuator type its requirements demand.

---

## 2. Evaluating the options

Two actuator types are candidates. The machine evaluates each against the task requirements — not as a catalog, but as options to accept or reject per task.

**Option A — Hydraulic cylinder** (linear actuator; pressure on a piston produces linear force)
- *Pros:* high linear force, precise position hold (closed-center lock, Module 06), finite controlled stroke, simple, the natural choice for pushing/pressing/lifting/gripping.
- *Cons:* cannot rotate continuously; limited to its stroke length.
- *Against the requirements:* ideal for primary positioning and gripping — linear, high-force, holdable, finite range. ✓

**Option B — Hydraulic motor** (rotary actuator; flow through it produces continuous rotation and torque)
- *Pros:* continuous rotation, good speed control, compact for rotary tasks, steady torque.
- *Cons:* does not naturally hold a precise *linear* position; holding a static rotary position needs a brake or counterbalance; lower precision for point-to-point positioning than a cylinder.
- *Against the requirements:* ideal for continuous rotation (spinning, conveyor) and large-angle part rotation; wrong for linear positioning or gripping. ✓ for rotary tasks only.

### The decision matrix

Scoring each actuator against the task requirements (✓ suited, ✗ unsuited):

| Task requirement | Cylinder | Motor |
|------------------|:--------:|:-----:|
| Linear positioning | ✓ | ✗ |
| High linear force | ✓ | ✗ |
| Precise position hold | ✓ | ✗ (needs brake) |
| Controlled gripping force | ✓ | ✗ |
| Continuous rotation | ✗ | ✓ |
| Rotary speed control | ✗ | ✓ |
| Large-angle part rotation | partial | ✓ |

The matrix shows there is no single "best" actuator — the right choice depends entirely on the task's requirements. For *this machine's core tasks* (positioning, gripping), the **cylinder** wins decisively. For any *rotary* end-effector task, the **motor** wins.

### The selected actuators

The machine chooses by task:

- **Primary positioning + gripping → cylinder.** These are linear, high-force, position-hold tasks — exactly the cylinder's strengths. The workcell's primary actuator and gripper are cylinders.
- **Rotary end-effector tasks (if used) → motor.** A rotary gripper, part-turning, or conveyor uses a hydraulic motor, sized for torque and speed (next section).

The machine does not force one actuator type onto every task. It matches the actuator to what each task's requirements demand — the essence of the engineering decision. Most of the workcell's defined tasks are linear, so the cylinder dominates; a rotary motor is the documented option for rotation when a task needs it.

---

## 3. Confirming the choice (motor sizing, when used)

When the machine *does* need a motor for a rotary task, it sizes the motor analogously to the pump (Module 05, run in reverse — a motor is a pump driven backward by flow).

**Motor torque** from pressure drop and displacement:
$$T = \frac{\Delta P \cdot D_m}{2\pi} \cdot \eta_m$$

**Motor speed** from flow and displacement:
$$n = \frac{Q \cdot \eta_v}{D_m}$$

*Example — a rotary gripper motor.* Suppose a rotary task needs 5 N·m of torque. With a 4 cc/rev gear motor at 90% mechanical efficiency:
$$\Delta P = \frac{2\pi T}{D_m \cdot \eta_m} = \frac{2\pi \times 5}{4\times10^{-6} \times 0.9} = 8.7\times10^{6}\ \text{Pa} = 87\ \text{bar}$$

The motor needs 87 bar to produce 5 N·m — within the machine's 100 bar capability. At, say, 2 LPM the speed would be $n = (2/60000)/(4\times10^{-6}) \times 0.9 \approx 7.5\ \text{rev/s} = 450\ \text{RPM}$. The motor sizing confirms the rotary task is feasible within the machine's power envelope.

For the baseline workcell with linear tasks, no motor is needed — but the machine has the logic to add and size one when a rotary task arises.

---

## 4. Visual explanation

![Capstone Architecture](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/capstone_architecture.svg)

*Figure: capstone architecture — see full diagram above.* (Subsystem 4 — actuation options)

Picture the decision as a fork driven by the task. A task arrives with requirements: is the motion linear or rotary? Does it need finite controlled travel with position hold, or continuous rotation? Linear-and-holdable flows down the cylinder branch; rotary-and-continuous flows down the motor branch. The figure shows the machine's actuators as a small toolkit — a cylinder for linear tasks, a motor for rotary ones — with each task routed to the actuator its requirements demand. The machine is not "a cylinder machine" or "a motor machine"; it is a machine that picks the right actuator per task.

---

## 5. Engineering example

**Why real machines mix actuator types**

An excavator uses cylinders for its boom, arm, and bucket (linear, high-force, position-hold tasks) but a hydraulic motor for its swing (continuous rotation of the cab) and its track drives (continuous travel). No engineer would use a cylinder to rotate the cab — it cannot rotate continuously — or a motor to extend the bucket — it cannot hold a precise linear position under load. The machine mixes actuator types because its tasks have mixed requirements.

The Smart Agricultural Workcell follows the same logic at bench scale. Its positioning and gripping are linear, so they use cylinders. Any rotary task — turning a part for inspection, a rotary gripper — would use a motor. The machine's actuator choice is task-driven, exactly as in full-scale equipment. Recognizing which actuator a task demands is a core engineering judgment, not a default.

---

## 6. Worked example

**The machine's actuator selection, per task.** Assemble the actuator decision for the workcell's tasks.

| Task | Requirement | Actuator chosen | Why |
|------|-------------|-----------------|-----|
| Primary positioning | linear, 300 mm, high force, hold | Cylinder (50 mm bore) | linear force + position hold |
| Gripping | linear jaw, controlled force, hold | Cylinder (small bore) | controlled linear grip force |
| Part rotation (optional) | rotary, large angle, low torque | Motor (4 cc/rev) | continuous/large-angle rotation |

*For the two core linear tasks*, the cylinder is correct — and the primary cylinder's full specification is the Actuator Selection Report from Lesson 02. *For the optional rotary task*, a 4 cc/rev gear motor sized for ~5 N·m at 87 bar (Section 3) is the documented choice.

This completes the machine's actuator selection: the right type for each task, each justified by the task's requirements. The cylinder carries the machine's core force and positioning; a motor stands ready for rotation when needed.

---

## 7. Interactive demonstration

```python
import math

def choose_actuator(motion, continuous, needs_position_hold):
    """The machine's actuator selection logic."""
    if motion == "linear":
        return "CYLINDER (linear force, position hold, finite stroke)"
    elif motion == "rotary":
        if continuous:
            return "MOTOR (continuous rotation, speed control)"
        elif needs_position_hold:
            return "MOTOR + brake (rotary position hold needs a brake)"
        else:
            return "MOTOR (large-angle rotation)"
    return "unknown"

tasks = [
    ("primary positioning", "linear", False, True),
    ("gripping", "linear", False, True),
    ("continuous spin", "rotary", True, False),
    ("part rotation", "rotary", False, False),
]
for name, motion, cont, hold in tasks:
    print(f"  {name:20s} -> {choose_actuator(motion, cont, hold)}")
```

Run it. The actuator follows from the task's motion requirements — linear tasks get cylinders, rotary tasks get motors.

---

## 8. Coding exercise

Create `code/module07/actuator_selection.py` that:

1. Implements the cylinder-vs-motor decision logic from task requirements
2. Sizes a hydraulic motor (torque, speed) for a given rotary task
3. Produces a per-task actuator selection table (the decision matrix)
4. Confirms each choice meets the task within the machine's pressure/flow envelope

This codifies the machine's actuator-selection reasoning and completes the actuator model.

---

## 9. Knowledge check

1. What fundamental capability does a cylinder have that a motor lacks, and vice versa?
2. Why can a motor not naturally hold a precise position the way a cylinder can?
3. State the actuator-selection principle in one sentence (it is not "always use a cylinder").
4. For a continuous-rotation task, which actuator does the machine choose, and why?
5. How is sizing a hydraulic motor related to sizing a pump (Module 05)?

---

## 10. Challenge problem

The machine is given a new task: continuously rotate an inspection platform at 60 RPM, needing 8 N·m of torque.

**a)** Cylinder or motor? Justify from the task requirements.

**b)** Size the motor: with a 6 cc/rev gear motor at 90% mechanical efficiency, what pressure produces 8 N·m? Is it within the machine's 100 bar capability?

**c)** What flow does the motor need for 60 RPM (6 cc/rev, 92% volumetric efficiency)?

**d)** Does the workcell's existing pump (10.67 LPM) have enough flow to drive this motor at 60 RPM while also serving the primary cylinder? What does this imply about the machine's power budget?

---

## 11. Common mistakes

**Forcing one actuator type onto every task.** A cylinder cannot rotate continuously; a motor cannot hold a precise linear position. Match the actuator to the task's motion requirements.

**Using a motor for precise position hold without a brake.** A motor does not lock a static position the way a closed-center cylinder does. Holding a rotary position needs a brake or counterbalance — an extra component.

**Forgetting the power budget when adding a motor.** A motor draws flow from the same pump. Adding a rotary task may exceed the pump's flow if the cylinder is also active. Check the machine's total flow demand.

**Treating the choice as taxonomy.** The point is not to list actuator types — it is to *choose* the right one for each task from its requirements. The decision is the engineering.

---

## 12. Key takeaways

- Engineering actuator selection starts with the task's motion requirements, then chooses the type — never a default.
- Cylinders give linear force and precise position hold over a finite stroke; motors give continuous rotation and speed control.
- The workcell's core tasks (positioning, gripping) are linear → cylinders; rotary tasks → motors.
- A motor is sized like a pump run in reverse: torque from pressure × displacement, speed from flow ÷ displacement.
- The machine mixes actuator types by task, exactly as full-scale equipment does — the cylinder carries the core force, a motor stands ready for rotation.

---

## Machine Capability Added

> **Before this lesson the machine could not:** choose the right actuator for a task — it had a cylinder but no logic for when rotation demands a motor instead.
>
> **After this lesson the machine can:** select and size the correct actuator type for each task — cylinders for its linear positioning and gripping, a sized motor for any rotary task — matching actuator to requirement.

The machine now has **task-matched actuation**. You can decide, from a task's requirements, whether it needs a cylinder or a motor, and size either — completing the machine's actuation subsystem. The cylinder carries the core Force-Controlled Interaction; a motor extends the machine to rotary manipulation when a task demands it.

**Digital twin contribution:** the actuator-selection logic and motor model (torque, speed) are added to the twin, completing the actuation subsystem alongside the cylinder model. The twin can now represent whichever actuator a task requires — the full Subsystem 4 model.

---

## Module 07 Artifact — Actuator Selection Report

The deliverable of this module is the **Actuator Selection Report** for the Smart Agricultural Workcell: the complete specification of the primary cylinder (bore, rod, stroke, mounting, pressure rating, seals, buckling check — Lesson 02), the per-task actuator selection (this lesson), and the real-behavior parameters (friction, cushioning — Lesson 03). It is Subsystem 4 of the final machine, the actuator that Module 06's motion control commands and Module 08's circuit integrates.

---

*Lesson 04 — Version 0.1 | Module 07 lesson content complete. Next: Module 07 summary, exercises, code, and Lab 07.*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 07 (Actuators) of the Fluid-Powered Physical AI curriculum: "Choosing the machine's actuator type". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("Choosing the machine's actuator type", Module 07 — Actuators) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("Choosing the machine's actuator type") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("Choosing the machine's actuator type", Module 07 — Actuators) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
