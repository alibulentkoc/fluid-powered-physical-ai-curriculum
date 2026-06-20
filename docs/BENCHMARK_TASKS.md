# Benchmark Tasks

*The Smart Agricultural Workcell is defined by three recurring tasks. They are to this curriculum what fruit-harvesting is to a robotics curriculum: the concrete missions every module works toward. Progress is measured by how much better the machine performs these tasks.*

Every module advances at least one of them. The `MODULE_ARTIFACT_MAP.md` shows which.

---

## Task 1 — Precision Positioning

**Objective:** Move the end-effector to a target position in the workspace.

**What it looks like:** The machine is told "go to 150 mm" and the tool arrives there — quickly, smoothly, and accurately — and stays there.

**Why it matters:** Positioning is the foundation of every manipulation. You cannot grip, press, inspect, or place an object until you can reliably get the tool to where the object is.

**Success criteria:**
| Criterion | Target |
|-----------|--------|
| Steady-state position error | within ±1 mm of target |
| Settling time | reaches target within a defined cycle time |
| Overshoot | minimal; no damaging end-of-stroke impact |
| Repeatability | same command produces the same position, run to run |
| Holding | stays at the target when commanded to hold, under load |

**Developed most heavily in:** Modules 04–08
(Module 04 predicts the motion; 05 powers it; 06 controls it; 07 sizes the actuator; 08 integrates the circuit.)

**How we measure it:** position-vs-time response from the simulation (Module 04 onward) and, once sensors exist (Module 09), from the real position sensor compared against the digital twin.

---

## Task 2 — Force-Controlled Interaction

**Objective:** Apply a controlled force to an object without damaging it.

**What it looks like:** The machine grips a delicate object at a commanded force — say 20 N — holding firmly enough not to drop it and gently enough not to crush it.

**Why it matters:** Raw hydraulic power is enormous (the workcell cylinder can push ~20 kN). Intelligent manipulation requires *restraining* that power precisely. A machine that can only push at full force is useless for handling real objects.

**Success criteria:**
| Criterion | Target |
|-----------|--------|
| Force accuracy | applied force within a defined tolerance of the commanded force |
| No damage | object is held without crushing or marking |
| Stability | force does not oscillate or spike |
| Compliance | the machine yields appropriately to the object rather than fighting it |

**Developed most heavily in:** Modules 06–10
(Module 06 meters flow and pressure; 07 sizes the actuator for controllable force; 09 senses the actual force; 10 closes the loop to control it.)

**How we measure it:** commanded force vs. measured force (load cell and the two pressure transducers, from Module 09), compared against the twin's force prediction.

---

## Task 3 — Autonomous Manipulation

**Objective:** Sense a target and execute a complete manipulation sequence without human guidance.

**What it looks like:** The machine detects that an object is present, approaches it, grips it with controlled force, lifts and moves it to a destination, places it, and verifies the result — all on its own.

**Why it matters:** This is the machine being genuinely intelligent: combining perception, decision, action, and self-validation into autonomous behavior. It is the culmination of the other two tasks plus a brain to sequence them.

**Success criteria:**
| Criterion | Target |
|-----------|--------|
| Detection | correctly senses the target's presence and location |
| Sequencing | executes approach → grip → move → place → verify in order |
| Robustness | completes the sequence reliably across repeated attempts |
| Self-validation | the digital twin confirms each step; faults are detected |
| Autonomy | no human intervention once the task begins |

**Developed most heavily in:** Modules 09–12
(Module 09 adds perception; 10 adds the decision-making state machine; 11 adds the integrated twin for validation; 12 demonstrates the whole sequence.)

**How we measure it:** successful end-to-end task completion rate, plus the twin's residual staying within bounds throughout the sequence (a clean run means the machine did what it predicted it would).

---

## How the tasks build on each other

```
Precision Positioning   ──►  get the tool to the object
        +
Force-Controlled        ──►  interact with the object safely
        +
(perception + decision) ──►  Autonomous Manipulation
```

Autonomous Manipulation is not a fourth, separate skill — it is Positioning and Force-Controlled Interaction, combined and sequenced by an intelligent controller that perceives the world and validates itself. The three tasks are a ladder: each rung depends on the one below.

---

*For the machine that performs these tasks, see `MACHINE_STORY.md`. For which module advances which task, see `MODULE_ARTIFACT_MAP.md`.*
