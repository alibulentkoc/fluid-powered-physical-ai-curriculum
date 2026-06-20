# The machine acts on what it perceives
## Module 10 · Lesson 01

*The machine can sense and it can move — but the two are not yet connected. It feels its position but does not steer toward a target; it perceives an error but does nothing about it. This lesson connects perception to action: the closed loop, the foundation of the machine's autonomy.*

---

## Why The Machine Needs This

The machine senses its position (Module 09) and commands its valves (Module 06), but those two abilities are still separate. Open-loop, the machine commands "extend" and hopes the cylinder lands on target — but friction, load, and the nonlinearity of hydraulics mean it never lands consistently. Sometimes it overshoots, sometimes it falls short, and the machine, though it *senses* the error, does nothing to correct it. A machine that perceives an error but cannot act on it is not yet intelligent.

The machine needs to *close the loop*: continuously read its position, compare it to the target, and adjust its valve command to drive the error to zero. This feedback — perception steering action — is the core of control, and the foundation of every autonomous capability. Before the machine can position precisely or grip gently, it must learn to act on what it perceives.

**Benchmark task supported:** Precision Positioning (closed-loop feedback is what makes positioning *accurate and repeatable*, not just approximate) and Force-Controlled Interaction (closed-loop force control is what makes gripping *gentle and precise*).

---

## 1. The machine's problem

Command the workcell cylinder, open-loop, to extend exactly 200 mm. The machine energizes the valve for the time it calculates should produce 200 mm. But the result varies: this time 196 mm, next time 204 mm, depending on the load, the fluid temperature (which changes viscosity and friction), and the breakaway stick-slip (Module 07). Open-loop, the machine has no way to correct — it commanded a motion and got *approximately* what it asked for, with no mechanism to close the gap.

Worse, hydraulics make this harder than it sounds. Unlike a DC motor (where speed is roughly proportional to voltage), a hydraulic actuator is **nonlinear**: flow depends on the square root of pressure drop (the orifice equation, Module 04), the valve has a dead-band (a range of small commands that produce no motion), fluid compressibility adds lag, and the velocity depends on the load. These make hydraulic control genuinely difficult — a controller tuned for one condition misbehaves in another.

The machine's problem: connect its position sensing to its valve command in a feedback loop that drives the cylinder to the target accurately and repeatably, despite the nonlinearity, friction, and load variation that defeat open-loop control.

---

## 2. The concept: the closed loop

A **closed-loop control system** continuously compares where the machine *is* to where it *should be*, and acts on the difference. The loop has four parts, cycling many times per second:

1. **Measure** — read the actual position from the sensor (Module 09).
2. **Compare** — compute the *error*: $e = x_{target} - x_{measured}$.
3. **Compute** — decide a valve command from the error (the controller's job).
4. **Act** — drive the valve, moving the cylinder, changing the position — which is measured again, closing the loop.

The defining feature is **feedback**: the result of the action (the new position) feeds back into the next decision. If the cylinder is short of target, the error is positive, the controller commands "extend more"; as the cylinder approaches, the error shrinks, the command eases; at the target, the error is zero, the command stops. The loop *automatically* drives the machine to the target and holds it there, correcting for whatever disturbance arises — exactly what open-loop cannot do.

**Why proportional response is the starting point.** The simplest controller commands a valve action proportional to the error: far from target → large command (move fast); near target → small command (ease in); at target → zero. This *proportional* control already vastly improves on open-loop, because it continuously corrects. But it has limits (it often leaves a small steady-state error and can oscillate) that motivate the fuller PID controller of Lesson 02. The key idea here is the loop itself: perception continuously steering action.

This is the machine's transition from *executing commands* to *pursuing goals*. Open-loop, the machine does what it is told; closed-loop, the machine does what it takes to *achieve a target*. That shift — from command to goal — is the essence of autonomy.

---

## 3. Mathematical model

**The error.** The signal the loop acts on:
$$e(t) = x_{target} - x_{measured}(t)$$

**Proportional control.** The valve command proportional to the error:
$$u(t) = K_p \cdot e(t)$$
where $K_p$ is the proportional gain and $u$ the valve command (e.g., a proportional-valve position, Module 06). Large $K_p$ responds aggressively (fast but prone to overshoot and oscillation); small $K_p$ responds gently (stable but slow and with larger residual error).

**Why hydraulics complicate this.** The valve command does not map linearly to cylinder velocity. The flow through the valve follows the orifice law:
$$Q = C_d A(u) \sqrt{\frac{2\Delta P}{\rho}}$$
so velocity depends on $\sqrt{\Delta P}$, which varies with load. A gain $K_p$ tuned for one load gives a different response at another — the **load-dependent velocity** problem. Add the valve dead-band (small $u$ produces no flow) and compressibility lag (pressure takes time to build), and the machine's response is nonlinear and condition-dependent. This is why hydraulic control needs careful tuning (Lesson 02) and why the digital twin — which models all these effects — is so valuable for predicting behavior before tuning on hardware.

**Steady-state error of proportional control.** With proportional control alone, holding against a constant load (like friction or gravity) requires a non-zero command, which requires a non-zero error: $u_{hold} = K_p \cdot e_{ss} \Rightarrow e_{ss} = u_{hold}/K_p$. The machine settles *near* the target but not exactly on it — the residual error that the integral term (Lesson 02) eliminates.

---

## 4. Visual explanation

![System Pipeline](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/system_pipeline.svg)

*Figure: system pipeline — see full diagram above.* (the full SENSE → DECIDE → COMMAND loop)

Picture the control loop as a cycle: the target enters, the measured position is subtracted to form the error, the controller turns the error into a valve command, the valve moves the cylinder, the sensor reads the new position, and that feeds back to the subtraction — round and round, many times a second. This block diagram is the machine's brain in its simplest form. Overlay two step-response traces: open-loop (the cylinder lands at a scattered, inconsistent position) versus closed-loop (the cylinder converges smoothly to the target every time). The figure shows the loop transforming inconsistent open-loop motion into precise, repeatable positioning — perception steering action.

---

## 5. Engineering example

**Why hydraulic control is harder than motor control**

A student who has controlled a DC motor might expect hydraulic control to be similar — but it is markedly harder, and understanding why is essential. A DC motor's speed is nearly proportional to its voltage: double the voltage, roughly double the speed, predictably and linearly. A hydraulic cylinder is nothing like this. Its velocity depends on the square root of the pressure drop, which changes with load; its valve ignores small commands (dead-band); its fluid compresses, adding lag; and its friction varies with velocity (Stribeck, Module 07).

The practical consequence: a PID controller tuned for the workcell extending against a light load will overshoot or oscillate when it retracts against gravity, or when the warm fluid lowers the friction. The machine cannot use a single fixed tuning blindly. This is why the curriculum spent Modules 04–08 building a *physics-based digital twin* — it captures exactly these nonlinearities, so the machine can predict how a given tuning will behave across conditions *before* risking hardware. The twin turns hydraulic control from trial-and-error guessing into informed design. The difficulty of hydraulic control is precisely what makes the twin worth building.

---

## 6. Worked example

**Open-loop vs. closed-loop positioning.** The workcell cylinder is commanded to 200 mm. Compare the open-loop and proportional closed-loop behavior against a friction load.

*Open-loop:* the machine energizes the valve for a calculated time. With nominal friction it lands at 200 mm; but a 20% friction increase (cold fluid) leaves it at ~190 mm, and the machine cannot correct — a 10 mm error, uncorrected.

*Proportional closed-loop ($K_p = 0.02$ /mm):* the machine continuously corrects. Far from target (error 200 mm), the command saturates the valve (full speed). As it approaches (error 20 mm), the command eases ($u = 0.4$). At a small residual error (say 2 mm holding against friction), $u = 0.04$ — just enough to hold. The machine settles at ~198 mm — a 2 mm steady-state error, *the same regardless of the friction change*, because the loop adapts.

The closed loop cut the error from 10 mm (and uncorrectable) to 2 mm (and consistent). The remaining 2 mm is the proportional controller's steady-state error, which the integral term (Lesson 02) will eliminate entirely. The machine has gone from hoping to *achieving* — the difference feedback makes.

---

## 7. Interactive demonstration

```python
def proportional_step(target, kp=0.02, friction=0.0, steps=500, dt=0.01):
    """Simulate the machine's proportional closed-loop step response."""
    pos = 0.0
    vel_gain = 90.0   # mm/s per unit command (approx, nominal load)
    for _ in range(steps):
        error = target - pos
        u = max(-1.0, min(1.0, kp * error))      # clamped valve command
        if abs(u) < 0.02:                        # valve dead-band
            u = 0.0
        vel = vel_gain * u
        if vel > 0:                              # friction opposes motion
            vel = max(0.0, vel - friction)
        pos += vel * dt
    return pos

for fric, label in [(0, "nominal"), (3, "cold fluid (more friction)")]:
    final = proportional_step(200, friction=fric)
    print(f"  {label:30s}: settles at {final:.1f} mm "
          f"(error {200-final:.1f} mm)")
```

Run it. Closed-loop control converges near the target and adapts to the friction change — where open-loop could not.

---

## 8. Coding exercise

Create `code/module10/closed_loop_basics.py` that:

1. Simulates open-loop positioning (showing inconsistency under load/friction variation)
2. Implements proportional control and simulates the closed-loop step response
3. Demonstrates the steady-state error of proportional-only control
4. Shows how the nonlinearity (dead-band, load-dependent velocity) affects the response

This establishes the closed loop — the foundation for the PID controller of Lesson 02.

---

## 9. Knowledge check

1. Why does open-loop positioning give inconsistent results for the machine?
2. Name the four steps of the closed-loop cycle.
3. What is the *error*, and how does proportional control use it?
4. Why is hydraulic control harder than DC motor control? Name three reasons.
5. Why does proportional-only control leave a steady-state error?

---

## 10. Challenge problem

The machine uses proportional control ($K_p = 0.02$/mm) to hold position against a gravity load that requires a constant valve command of $u = 0.06$ to support.

**a)** What steady-state error does the machine settle at? ($e_{ss} = u_{hold}/K_p$)

**b)** If the machine increases $K_p$ to 0.05 to reduce this error, what is the new steady-state error? What new problem might the higher gain cause?

**c)** Why can't the machine just keep raising $K_p$ to eliminate the error entirely?

**d)** What controller term (Lesson 02) eliminates the steady-state error without raising $K_p$, and how does it work conceptually?

---

## 11. Common mistakes

**Trusting open-loop positioning.** Without feedback, friction, load, and temperature variation make the result inconsistent and uncorrectable. Precision needs the closed loop.

**Treating hydraulics like a DC motor.** Hydraulic actuators are nonlinear (square-root flow, dead-band, compressibility lag, load-dependent velocity). A linear-motor intuition leads to bad tuning.

**Raising the proportional gain to fix steady-state error.** Higher $K_p$ reduces the error but causes overshoot and oscillation. The integral term, not more proportional gain, eliminates steady-state error.

**Tuning on hardware without the twin.** The twin predicts how a tuning behaves across conditions before risking hardware. Skipping it means blind trial-and-error on a machine that can damage itself.

---

## 12. Key takeaways

- The machine senses and moves, but until the loop is closed, it cannot act on the errors it perceives.
- Closed-loop control cycles measure → compare → compute → act, with feedback driving the error to zero.
- Proportional control commands a valve action proportional to the error — a vast improvement over open-loop, but with residual steady-state error.
- Hydraulic control is hard: square-root flow, valve dead-band, compressibility lag, and load-dependent velocity make it nonlinear and condition-dependent.
- The closed loop is the machine's shift from *executing commands* to *pursuing goals* — the essence of autonomy.

---

## Machine Capability Added

> **Before this lesson the machine could not:** act on the errors it perceived — it sensed its position but had no mechanism to correct toward a target.
>
> **After this lesson the machine can:** close the loop — continuously measuring its position, computing the error, and commanding the valve to drive toward the target, adapting to load and friction.

The machine now has **feedback control** — perception steering action. You can connect the machine's position sensing to its valve command in a closed loop that pursues a target accurately and repeatably, where open-loop only approximated. This is the foundation of autonomy: the machine pursuing goals, not just executing commands. The PID controller (Lesson 02) makes this precise.

**Digital twin contribution:** the closed-loop structure is added to the twin — the feedback connection from sensed position to valve command. The twin can now simulate *controlled* behavior, predicting how a given controller drives the machine to a target, the basis for tuning the PID in simulation before hardware (Lesson 04).

---

*Lesson 01 — Version 0.1 | Next: Lesson 02 — Giving the machine a precise controller (PID and tuning)*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 10 (Control) of the Fluid-Powered Physical AI curriculum: "The machine acts on what it perceives". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("The machine acts on what it perceives", Module 10 — Control) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("The machine acts on what it perceives") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("The machine acts on what it perceives", Module 10 — Control) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
