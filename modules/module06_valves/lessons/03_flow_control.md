# The machine controls its speed
## Module 06 · Lesson 03

*The machine can direct its flow and cap its pressure — but it still moves at one speed, whatever the pump delivers. This lesson gives the machine fine control over how fast it moves, which is the difference between lunging at a target and approaching it precisely.*

---

## Why The Machine Needs This

The machine can extend, hold, and retract (Lessons 01–02), but always at the speed the pump dictates — about 90 mm/s. For Precision Positioning, that is a problem. Approaching a target at full speed means overshooting it; approaching a delicate workpiece at full speed means crushing it. The machine needs to *slow down* for the precise part of every motion: a fast traverse across open space, then a slow, controlled final approach.

Module 05 showed one way to change speed — vary the motor/pump speed. But that changes the speed of *everything*, is limited at the low end, and is slow to respond. The machine needs local, fast, fine speed control at the actuator itself. That is what flow control valves provide, and getting them right — especially the meter-in versus meter-out choice — is what makes the machine's motion smooth and safe.

**Benchmark task supported:** Precision Positioning (controlled approach speed is the core of accurate positioning) and Force-Controlled Interaction (slow, controlled motion is the precondition for gentle contact).

---

## 1. The machine's problem

Picture the machine extending toward a target at 90 mm/s. To stop *exactly* at the target, it must decelerate and approach slowly — you cannot hit a precise position at full speed without overshooting. The machine needs a slow final approach, perhaps 20 mm/s, for the last few millimeters.

Worse, consider the machine lowering a load. Gravity *assists* the motion — it pulls the cylinder in the direction it is already moving. If nothing resists, the load runs away: the cylinder lurches faster than the pump feeds it, drawing a vacuum on the supply side, and the motion becomes jerky and uncontrolled. This is the classic "running load" problem, and it is dangerous: the machine drops its load instead of lowering it.

The machine's problem: control the *speed* of its cylinder independently of the pump, and do it in a way that stays stable even when the load tries to run away.

---

## 2. The concept: flow control and where you put it

The machine's cylinder speed is set by the flow into it: $v = Q/A$. To control speed, control flow. A **flow control valve** is an adjustable restriction — a throttle — that limits how much flow passes, and therefore how fast the cylinder moves.

A simple **needle valve** or **throttle valve** restricts flow by a set amount. A **pressure-compensated flow control valve** is smarter: it holds the flow constant even as the load (and therefore the pressure drop) changes — giving the machine a *steady* speed regardless of load. For consistent positioning, the machine prefers pressure-compensated control.

But the crucial decision is not *which* flow control valve — it is *where* you put it relative to the cylinder. There are two choices, and they behave very differently:

**Meter-in** — the restriction is on the *supply* side, throttling flow *into* the cylinder. This works well when the load *resists* the motion (the machine pushes against something). But for a running/assisting load, meter-in fails: nothing stops the cylinder from being pulled faster than the throttled supply can fill it, so it cavitates and lurches.

**Meter-out** — the restriction is on the *return* side, throttling flow *out* of the cylinder. This controls speed by restricting the *exit* of fluid, which means it works even when the load assists the motion: the load cannot run away because the fluid leaving the cylinder is held back by the restriction. The cylinder is "cushioned" against running.

**The rule the machine follows: meter-out for resisting *and* running loads.** Meter-out controls speed in both cases, where meter-in only handles resisting loads. Because the machine may lower loads (where gravity assists), it uses **meter-out** flow control for safety and smoothness. This is one of the most important practical choices in hydraulic motion control, and getting it wrong produces a machine that drops its loads.

---

## 3. Mathematical model

The flow control valve is an orifice (Module 04), so the flow it passes follows the orifice equation:
$$Q = C_d \, A_{valve} \sqrt{\frac{2\,\Delta P}{\rho}}$$

The machine sets the cylinder speed by choosing the valve opening $A_{valve}$:
$$v = \frac{Q}{A_{cylinder}} = \frac{C_d \, A_{valve}}{A_{cylinder}}\sqrt{\frac{2\,\Delta P}{\rho}}$$

The problem the square-root reveals: speed depends on $\sqrt{\Delta P}$, and $\Delta P$ changes with load. A simple throttle gives a speed that *drifts* as the load changes — bad for precise positioning. This is why the machine prefers a **pressure-compensated** flow control valve, which internally maintains a constant $\Delta P$ across the throttle, so:
$$v = \frac{C_d \, A_{valve}}{A_{cylinder}}\sqrt{\frac{2\,\Delta P_{fixed}}{\rho}} = \text{constant for a given opening, regardless of load}$$

With pressure compensation, the machine commands a speed and *gets* that speed, load notwithstanding. This is what makes positioning repeatable.

**Meter-out back-pressure.** With meter-out, restricting the exit raises the pressure in the *return* chamber. The machine must check this back-pressure stays within limits — for a running load, the back-pressure is exactly what holds the load back, so it is a feature, not a bug, but it must not exceed component ratings.

---

## 4. Visual explanation

![System Pipeline](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/system_pipeline.svg)

*Figure: system pipeline — see full diagram above.* (the ACTUATE stage, speed regulation)

Picture two plumbing layouts. In **meter-in**, the throttle sits between the valve and the cylinder's inlet — it controls how fast fluid *arrives*. In **meter-out**, the throttle sits between the cylinder's outlet and tank — it controls how fast fluid *leaves*. For a running load, imagine the cylinder being yanked forward by gravity: with meter-in, nothing holds it back and it lurches; with meter-out, the exiting fluid is squeezed through the throttle, and that back-pressure restrains the load like a hydraulic brake. The figure shows the load held in check by the meter-out restriction — the machine lowering smoothly instead of dropping.

---

## 5. Engineering example

**Why excavators and lifts use meter-out**

Any hydraulic machine that lowers loads — an excavator boom, a scissor lift, a forklift — uses meter-out flow control (or its cousin, the counterbalance valve from Lesson 02) for exactly this reason. When the boom comes down, gravity assists the motion; without meter-out restraint, the boom would drop, not lower. The meter-out restriction (or counterbalance) provides the back-pressure that turns a free-fall into a controlled descent.

The Smart Agricultural Workcell inherits this logic. When its cylinder lowers the end-effector or a workpiece, gravity assists, and meter-out flow control keeps the motion smooth and controlled. The machine borrows a principle proven on every hydraulic lift and digger: control the fluid *leaving* the cylinder, and you control any load, resisting or running.

---

## 6. Worked example

**Sizing the machine's approach-speed control.** The workcell must do a precise positioning task: fast traverse at 90 mm/s (pump speed), then a slow final approach at 20 mm/s set by a meter-out flow control valve. The cylinder bore is 50 mm; on extend, the fluid leaving the rod side is metered.

*Flow for 20 mm/s approach (extend):* the bore fills at 20 mm/s, so the rod side expels:
$$Q_{out} = v \times A_{rod} = 20 \times 1348 = 26{,}960\ \text{mm}^3/\text{s} = 1.62\ \text{LPM}$$
The meter-out valve restricts the rod-side return to 1.62 LPM, slowing the cylinder to 20 mm/s.

*Excess pump flow during slow approach:* the pump still delivers 10.67 LPM, but the cylinder only accepts the flow corresponding to 20 mm/s. The excess goes over the relief valve (Lesson 02). The bore fills at $20 \times 1963 = 39{,}260\ \text{mm}^3/\text{s} = 2.36$ LPM, so $10.67 - 2.36 = 8.3$ LPM spills over relief — turning to heat. (A pressure-compensated pump or variable speed would avoid this waste; the simple machine accepts it.)

So the machine traverses fast on full pump flow, then the meter-out valve throttles it to a precise 20 mm/s approach. The machine now controls its speed, not just its direction.

---

## 7. Interactive demonstration


**▶ Interactive demo — Valve Flow-Control Demo**

[Open this demo in a new tab ↗](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/demos/module06/valve_flow_control.html)

This self-contained widget lets you explore the concepts of this module hands-on — adjust the inputs and watch the machine's numbers respond live, built from the same equations the tested code uses.

```python
import math

def approach_flow(velocity_mm_s, bore_mm=50, rod_mm=28, metering="out"):
    """Flow the machine's meter-out valve must pass for a target speed."""
    A_bore = math.pi*(bore_mm/2)**2
    A_rod = A_bore - math.pi*(rod_mm/2)**2
    # meter-out on extend restricts the rod-side return
    A_metered = A_rod if metering == "out" else A_bore
    q_mm3s = velocity_mm_s * A_metered
    return q_mm3s * 60 / 1e6   # LPM

print("Machine's meter-out flow for each approach speed (extend):")
for v in [90, 50, 30, 20, 10]:
    print(f"  {v:3d} mm/s -> meter rod-side return to {approach_flow(v):.2f} LPM")
```

Run it. To slow the machine, the meter-out valve throttles the rod-side return to the flow matching the target speed. Fine speed control, set at the actuator.

---

## 8. Coding exercise

Create `code/module06/flow_control.py` that:

1. Models a meter-out flow control valve: given a target velocity, returns the required valve flow setting
2. Compares meter-in vs. meter-out behavior for a *running* (assisting) load — showing meter-in cavitates while meter-out controls
3. Models pressure-compensated vs. simple throttle: speed drift as load changes
4. Plots cylinder velocity vs. valve opening for the workcell

This is the machine's speed-control layer, feeding the digital twin's motion prediction.

---

## 9. Knowledge check


*Formative — unlimited attempts, immediate feedback; does not affect your grade.*

[Open the interactive quiz in a new tab ↗](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/quizzes/module06/knowledge_check_quiz.html)

Or work through the written questions below.

1. Why does varying pump speed alone not give the machine good approach-speed control?
2. What is a flow control valve, and how does it set the machine's cylinder speed?
3. Explain meter-in vs. meter-out. Which does the machine use, and why?
4. What problem does a *running* (assisting) load cause, and how does meter-out solve it?
5. Why does the machine prefer a pressure-compensated flow control valve for positioning?

---

## 10. Challenge problem

The machine performs a two-phase motion: fast traverse at 90 mm/s, then slow approach at 15 mm/s, while lowering the end-effector (gravity assists the motion).

**a)** What flow must the meter-out valve pass for the 15 mm/s approach (extend, metering rod-side return)?

**b)** Because gravity assists, explain what would happen if the machine used meter-*in* instead of meter-out for this descent.

**c)** During the slow approach, most of the pump's 10.67 LPM spills over the relief valve. How much, and where does that energy go? (Connect to Lesson 02.)

**d)** Propose a change to the machine that would eliminate this wasted flow during slow approaches. (Hint: Module 05's variable speed, or a different pump strategy.)

---

## 11. Common mistakes

**Using meter-in for running loads.** Meter-in cannot control an assisting load — the cylinder runs away from the throttled supply and cavitates. For any load that might assist the motion, the machine must meter out.

**Forgetting the spilled flow becomes heat.** When the machine moves slowly, the excess pump flow spills over the relief and heats the fluid. Slow precise motion with a fixed pump is energy-wasteful. Account for it, or use variable pump speed.

**Using a simple throttle where load varies.** A plain needle valve gives a speed that drifts as the load (and pressure drop) changes. For repeatable positioning, the machine needs pressure-compensated flow control.

**Confusing flow control with directional control.** The DCV chooses *where* flow goes; the flow control valve sets *how fast*. They are different valves solving different problems, often used together.

---

## 12. Key takeaways

- The machine needs fine speed control for precise approaches; pump-speed variation alone is too coarse and slow.
- A flow control valve is an adjustable restriction that sets cylinder speed by limiting flow: $v = Q/A$.
- Meter-out (restricting the cylinder's *exit*) controls both resisting and running loads; meter-in fails for running loads. The machine uses meter-out.
- Pressure-compensated flow control holds speed constant as the load changes — essential for repeatable positioning.
- Slow motion with a fixed pump spills excess flow over the relief as heat — a cost the simple machine accepts.

---

## Machine Capability Added

> **Before this lesson the machine could not:** control its speed — it moved only at the single velocity the pump dictated, lunging at targets and unable to lower loads safely.
>
> **After this lesson the machine can:** set its cylinder speed precisely with a meter-out flow control valve — fast traverse, slow controlled approach — and lower assisting loads smoothly without them running away.

The machine now has **speed control of its motion**. Combined with the directional control of Lesson 01, the machine can move where it wants *and* how fast it wants — fast across open space, slow for the precise final approach. This is the complete motion-control capability that makes accurate Precision Positioning achievable.

**Digital twin contribution:** the flow control model is added to the twin — meter-out behavior, the velocity-from-valve-opening relationship, and the meter-in-versus-meter-out distinction for running loads. The twin can now predict the machine's controlled approach speed and correctly model load-lowering, a key step toward simulating full positioning motions.

---

*Lesson 03 — Version 0.1 | Next: Lesson 04 — Smooth control and commanding valves from the machine's brain (proportional valves + first control code)*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 06 (Valves) of the Fluid-Powered Physical AI curriculum: "The machine controls its speed". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("The machine controls its speed", Module 06 — Valves) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("The machine controls its speed") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("The machine controls its speed", Module 06 — Valves) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
