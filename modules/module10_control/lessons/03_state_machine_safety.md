# The machine runs its own task, safely
## Module 10 · Lesson 03

*A precise position controller can hit one target — but a real task is a sequence of targets, with decisions and safety checks between them. This lesson gives the machine the state machine that runs its whole task autonomously, and the safety logic that keeps it from harming itself or anyone near it.*

---

## Why The Machine Needs This

The PID controller (Lesson 02) lets the machine reach one position precisely. But Autonomous Manipulation is not one motion — it is a coordinated sequence (position → grip → lift → move → release, Module 08), with decisions between steps (has it arrived? is the grip secure?) and the constant possibility of something going wrong (pressure too high, lost communication, a jammed cylinder). The machine needs logic that *runs the whole task on its own*, deciding what to do next based on what it senses, and that *keeps it safe* throughout.

This is the machine's executive function: a state machine that sequences the task autonomously, and safety logic that overrides everything if a danger appears. A fluid-powered machine moves with great force; safety is not an afterthought but a core requirement. This lesson gives the machine the brain that runs its task and the guardian that keeps it safe.

**Benchmark task supported:** Autonomous Manipulation (the state machine *is* the autonomous task execution) and all benchmarks (safety logic is the precondition for trusting the machine to run unattended).

---

## 1. The machine's problem

The machine can position precisely, but consider what running a full pick-and-place task actually requires. The machine must: approach the workpiece, *check* it arrived before gripping, grip with controlled force, *check* the grip is secure before lifting, lift, move, release, and return — a sequence of states, each with an entry condition, an action, and an exit condition. A single PID loop cannot express this; it knows only "go to position X." The machine needs higher-level logic that orchestrates the PID loops into a task.

And it must do this *safely*. What if the pressure spikes above the safe limit mid-task? What if the cylinder is commanded past its physical stroke? What if the Raspberry Pi (running the task logic) loses communication with the Arduino (running the control)? An unprotected machine would plow ahead — slamming an end stop, bursting a line, or running blind. With the forces a hydraulic machine commands, these failures are dangerous to the machine and to people near it. The machine needs safety logic that detects these conditions and forces a safe state, overriding the task.

The machine's problem: orchestrate its PID-controlled motions into a complete autonomous task, with safety logic that overrides the task whenever a danger appears.

---

## 2. The concept: the state machine and safety logic

**The state machine.** The machine runs its task as a **finite state machine** — a set of states, with defined transitions between them. Each state has an action and a guard (the condition to move on). The workcell's task states:

- **IDLE** — at rest, awaiting a task command.
- **APPROACH** — PID-drive the cylinder to the workpiece position. *Guard to next:* position reached (within tolerance).
- **GRIP** — close the end-effector with controlled force. *Guard:* grip force reached.
- **LIFT** — raise the workpiece. *Guard:* lift position reached.
- **MOVE / RETURN** — carry the workpiece to its destination. *Guard:* destination reached.
- **RELEASE** — open the end-effector. *Guard:* released.
- **FAULT** — a safe state entered from *any* state if a danger is detected; the machine stops and holds safely.

The machine transitions through these states based on its *sensors* (Module 09): it does not move from APPROACH to GRIP on a timer, but when the position sensor *confirms* arrival. This sensor-driven sequencing (foreshadowed in Module 08) is what makes the task robust — the machine waits for each step to truly complete. The state machine runs on the Raspberry Pi (task logic), commanding the Arduino (which runs the PID loops) over a serial protocol.

**The safety logic.** Layered over the state machine, the safety logic continuously checks for danger and can force the FAULT state from anywhere:

- **Pressure limit:** if system pressure exceeds a threshold, override the valve command and stop — preventing a burst.
- **Position limit:** enforce a hard stop before the physical end of stroke — preventing the cylinder slamming its end cap.
- **Watchdog timer:** if the Pi↔Arduino communication is lost (no message within a timeout), the Arduino independently returns the machine to a safe state — so a software crash or cable fault cannot leave the machine running blind.

The safety logic has *priority over the task*: no matter what the state machine wants, if a safety check fails, the machine goes to FAULT and holds safely. This priority is the principle that safety is not an afterthought — it is the top of the machine's decision hierarchy. The watchdog especially embodies fail-safe design (Module 08): safety that works even when the higher-level logic fails.

---

## 3. Mathematical model

**State transitions as guarded logic.** Each transition is a guard condition on the sensors:
$$\text{APPROACH} \xrightarrow{|x - x_{target}| < \epsilon} \text{GRIP}$$
$$\text{GRIP} \xrightarrow{F_{grip} \geq F_{target}} \text{LIFT}$$
and so on. The machine evaluates these guards each control cycle, advancing only when the sensed condition is met.

**Safety checks as overrides.** Each cycle, before executing the state's action, the machine evaluates the safety predicates:
$$\text{if } P > P_{limit} \text{ OR } x > x_{limit} \text{ OR } t_{since\_comm} > t_{watchdog} \;\Rightarrow\; \text{state} \leftarrow \text{FAULT}$$
The FAULT state's action is to hold the machine safely (close the valve to its safe center, stop motion).

**Watchdog timing.** The Arduino tracks the time since the last valid command from the Pi. If it exceeds the watchdog timeout (e.g., 200 ms), the Arduino acts independently:
$$t_{now} - t_{last\_command} > t_{watchdog} \;\Rightarrow\; \text{safe state}$$
The timeout must be long enough not to trip on normal communication jitter, short enough that the machine stops quickly if control is truly lost.

**The control hierarchy.** The machine's decision-making is layered: safety (highest priority, can override anything) → task state machine (sequences the task) → PID controllers (execute each motion). Each layer runs at its appropriate rate — PID fast (e.g., 100 Hz on the Arduino), state machine slower (e.g., 10 Hz on the Pi), safety continuously at the fastest rate.

---

## 4. Visual explanation

![System Pipeline](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/system_pipeline.svg)

*Figure: system pipeline — see full diagram above.* (the DECIDE stage — the state machine)

Picture the task as a state diagram: circles for each state (IDLE, APPROACH, GRIP, LIFT, MOVE, RELEASE, FAULT), arrows for transitions labeled with their guard conditions. The normal task flows in a loop: IDLE → APPROACH → GRIP → LIFT → MOVE → RELEASE → IDLE. But from *every* state, a red arrow leads to FAULT, labeled with the safety conditions — the override that can fire at any moment. The figure shows the machine's autonomous decision logic at a glance: the orderly task progression, and the ever-present safety escape that keeps it safe. This state diagram is the machine's executive brain — the DECIDE stage of the pipeline.

---

## 5. Engineering example

**Why safety lives below the task, in independent logic**

It might seem natural to put safety checks inside the task logic — the state machine checks the pressure before each move. But this is fragile: if the task logic crashes or hangs, the safety checks crash with it, and the machine is left running with no protection. This is why the workcell puts the most critical safety — the watchdog and the pressure/position limits — in the *Arduino firmware*, below the Raspberry Pi's task logic, running independently.

The consequence: even if the Pi crashes, the Python task logic hangs, or the communication cable is cut, the Arduino independently detects the lost communication (watchdog) and the over-pressure or over-travel (limits), and forces the machine to a safe state on its own. Safety does not depend on the higher-level brain working. This is the same fail-safe principle as the circuit protection of Module 08 (which works even with no power), now applied to the control software: the safety layer is independent of and below the task layer, so it survives the task layer's failure.

This layered, independent safety is a defining practice of real machine control. A machine is trustworthy not because its task logic is perfect, but because its safety works *even when the task logic fails*. The Smart Agricultural Workcell embodies this: the watchdog is its last line of defense, and it lives where it cannot be taken down by a software fault above it.

---

## 6. Worked example

**The machine runs its task with safety.** Trace a pick-and-place cycle through the state machine, including a safety event.

*Normal flow:*
1. **IDLE** → command received → **APPROACH** (PID drives to 200 mm). Position reaches 200±2 mm → guard passes.
2. **GRIP** (close jaw, PID-regulate to 50 N). Force reaches 50 N → guard passes.
3. **LIFT** (raise 50 mm). Lift position reached → guard passes.
4. **MOVE** (carry to destination). Destination reached → guard passes.
5. **RELEASE** (open jaw). Released → back to **IDLE**.

*Safety event (mid-MOVE):* suppose during MOVE the system pressure spikes to 120 bar (above the 118 bar limit) because the load jammed. The safety logic, checked every cycle, fires: state → **FAULT**. The machine immediately closes the valve to safe center, stops, and signals the fault. It does *not* continue the MOVE — safety overrode the task. Once the jam is cleared and the fault acknowledged, the machine returns to IDLE, ready to retry.

*Watchdog event:* suppose the Pi crashes during APPROACH. No commands reach the Arduino. After 200 ms, the Arduino's watchdog fires independently: it drives the valve to safe center and holds. The machine is safe even though its task brain has died.

The machine runs its full task autonomously, and stays safe through faults — the executive function and the guardian, working together. This is autonomous operation that can be trusted.

---

## 7. Interactive demonstration

```python
class WorkcellStateMachine:
    """The machine's autonomous task logic with safety override."""
    STATES = ["IDLE", "APPROACH", "GRIP", "LIFT", "MOVE", "RELEASE", "FAULT"]

    def __init__(self, p_limit=118, x_limit=295, watchdog_ms=200):
        self.state = "IDLE"
        self.p_limit, self.x_limit, self.watchdog_ms = p_limit, x_limit, watchdog_ms

    def safety_check(self, pressure, position, ms_since_comm):
        if pressure > self.p_limit:
            return "FAULT (over-pressure)"
        if position > self.x_limit:
            return "FAULT (over-travel)"
        if ms_since_comm > self.watchdog_ms:
            return "FAULT (watchdog: comm lost)"
        return None

    def step(self, sensors, guard_met):
        fault = self.safety_check(sensors["P"], sensors["x"], sensors["comm_ms"])
        if fault:
            self.state = "FAULT"
            return fault
        # normal task progression
        flow = {"IDLE":"APPROACH","APPROACH":"GRIP","GRIP":"LIFT",
                "LIFT":"MOVE","MOVE":"RELEASE","RELEASE":"IDLE"}
        if guard_met and self.state in flow:
            self.state = flow[self.state]
        return self.state

sm = WorkcellStateMachine()
# normal progression
for _ in range(3):
    print(f"  -> {sm.step({'P':95,'x':150,'comm_ms':50}, guard_met=True)}")
# safety event
print(f"  pressure spike: {sm.step({'P':125,'x':150,'comm_ms':50}, guard_met=True)}")
```

Run it. The machine sequences its task, and a safety event forces FAULT, overriding the task.

---

## 8. Coding exercise

Create `code/module10/state_machine.py` that:

1. Implements the workcell state machine (IDLE → APPROACH → GRIP → LIFT → MOVE → RELEASE)
2. Uses sensor-based guards for transitions (position, force)
3. Implements the safety logic (pressure limit, position limit, watchdog) with priority override to FAULT
4. Simulates a full task cycle, including a safety event that forces FAULT

This is the machine's executive brain — autonomous task logic with independent safety.

---

## 9. Knowledge check

1. Why can't a single PID loop run the machine's full task?
2. Name the workcell's task states and what triggers each transition.
3. What three safety checks does the machine run, and what does each prevent?
4. Why does the safety logic have priority over the task logic?
5. Why is the watchdog placed in the Arduino firmware, below the Pi's task logic?

---

## 10. Challenge problem

During a task, the machine is in the LIFT state when the Raspberry Pi (running the task logic) freezes due to a software bug.

**a)** What happens to the commands reaching the Arduino?

**b)** Which safety mechanism responds, and after how long? What does the machine do?

**c)** Why would the machine be unsafe if this safety mechanism were instead implemented in the Pi's task logic?

**d)** Explain how this mirrors the fail-safe circuit design of Module 08, and state the general principle both embody.

---

## 11. Common mistakes

**Sequencing the task on timers instead of sensors.** Advancing states on fixed delays assumes each step takes a known time; sensor-based guards wait for *actual* completion, which is robust to variation.

**Putting safety inside the task logic.** If the task logic crashes, embedded safety crashes with it. Critical safety (watchdog, limits) belongs below the task logic, in independent firmware.

**Making the watchdog timeout too short or too long.** Too short trips on normal communication jitter (nuisance faults); too long lets the machine run dangerously after control is truly lost. Tune it to the communication rate.

**Treating FAULT as a dead end.** FAULT should hold the machine safely *and* allow recovery (acknowledge, clear, return to IDLE). A fault state with no recovery path makes the machine brittle.

---

## 12. Key takeaways

- A full task is a sequence of states, not one motion; the machine runs it as a finite state machine (IDLE → APPROACH → GRIP → LIFT → MOVE → RELEASE).
- Transitions are guarded by *sensors* (position reached, grip force achieved) — robust, sensor-driven sequencing.
- The state machine runs on the Pi (task logic), commanding the Arduino (PID loops) over serial; the control hierarchy is safety > task > PID.
- Safety logic (pressure limit, position limit, watchdog) has priority and can force FAULT from any state.
- Critical safety lives in the Arduino firmware, below the task logic, so it survives a higher-level failure — fail-safe by design.

---

## Machine Capability Added

> **Before this lesson the machine could not:** run a complete task on its own, or protect itself if something went wrong mid-task.
>
> **After this lesson the machine can:** execute its full pick-and-place task autonomously as a sensor-driven state machine, with independent safety logic that forces a safe state whenever a danger appears.

The machine now has **autonomous task execution with safety** — its executive brain and its guardian. You can give the machine a state machine that sequences its whole task from sensor feedback, and safety logic that overrides the task to keep the machine safe even when its higher-level logic fails. This is the core of trustworthy Autonomous Manipulation.

**Digital twin contribution:** the state machine and safety logic are added to the twin, which can now simulate the machine's *complete autonomous task* — the state progression, the sensor-driven transitions, and the safety overrides. The twin can verify the task logic and test safety responses in simulation before they run on hardware.

---

*Lesson 03 — Version 0.1 | Next: Lesson 04 — Closing the loop in simulation (validating control before hardware)*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 10 (Control) of the Fluid-Powered Physical AI curriculum: "The machine runs its own task, safely". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("The machine runs its own task, safely", Module 10 — Control) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("The machine runs its own task, safely") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("The machine runs its own task, safely", Module 10 — Control) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
