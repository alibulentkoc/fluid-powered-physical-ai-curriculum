# Giving the machine a precise controller
## Module 10 · Lesson 02

*Proportional control gets the machine close, but not exact, and not always smoothly. This lesson gives the machine the full PID controller — proportional, integral, and derivative working together — and teaches it to tune that controller for precise, stable positioning.*

---

## Why The Machine Needs This

Proportional control (Lesson 01) improved the machine vastly over open-loop, but it left two problems: a residual steady-state error (it settles *near* the target, not *on* it), and a tendency to overshoot or oscillate if pushed for speed. For Precision Positioning with a target of under 2 mm steady-state error and under 5% overshoot, proportional alone is not enough. The machine needs a controller that eliminates the steady-state error *and* damps the oscillation.

The PID controller does exactly this, by adding two terms to the proportional response: an *integral* term that eliminates steady-state error, and a *derivative* term that damps overshoot. But a PID controller is only as good as its tuning, and hydraulic systems are notoriously hard to tune (Lesson 01). The machine needs both the controller and the method to tune it — and the digital twin to predict the tuning before risking hardware.

**Benchmark task supported:** Precision Positioning (PID is what achieves the accuracy and smoothness positioning demands) and Force-Controlled Interaction (PID regulates grip force precisely).

---

## 1. The machine's problem

The machine's proportional controller settles at, say, 198 mm when commanded to 200 mm — a 2 mm steady-state error it cannot remove without raising the gain, which causes overshoot. And if the machine raises the gain for a faster response, the cylinder overshoots the target and oscillates around it before settling, or never quite settles — chattering the valve and wearing it.

These are the two classic failures the machine must overcome:
- **Steady-state error:** the cylinder settles persistently off-target because holding against friction or load requires a command that proportional control can only produce with a non-zero error.
- **Overshoot and oscillation:** an aggressive response overshoots the target and rings around it, because the controller does not anticipate the approach and "brake" in time.

The machine needs a controller that drives the steady-state error to *zero* and approaches the target *smoothly* without overshoot — meeting the Precision Positioning targets of <2 mm error and <5% overshoot. That controller is PID, properly tuned.

---

## 2. The concept: the three terms of PID

A **PID controller** computes its valve command from three terms, each addressing a specific aspect of the error:

**Proportional (P) — responds to the present error.**
$$u_P = K_p \cdot e$$
The bigger the error now, the bigger the command. This is the main driving force (Lesson 01), but alone it leaves a steady-state error.

**Integral (I) — responds to the accumulated past error.**
$$u_I = K_i \int e\,dt$$
The integral *accumulates* the error over time. As long as any error persists, the integral grows, increasing the command until the error is driven to *zero*. This is what eliminates the steady-state error: the integral keeps pushing until the machine is exactly on target, supplying the steady holding command that proportional could only produce with a residual error.

**Derivative (D) — responds to the rate of change of error.**
$$u_D = K_d \frac{de}{dt}$$
The derivative reacts to how fast the error is changing — anticipating the approach. As the cylinder rushes toward the target (error shrinking fast), the derivative term *brakes*, damping the overshoot. It is the controller's anticipation, smoothing the approach.

**The full PID command:**
$$u(t) = K_p e + K_i \int e\,dt + K_d \frac{de}{dt}$$

Together: P drives toward the target, I eliminates the residual error, D damps the overshoot. Tuned well, the machine approaches the target quickly, smoothly, and settles exactly on it. This is the controller that meets the Precision Positioning targets.

**The practical hazards.** Real PID implementation has three traps the machine must handle:
- **Integral windup:** if the valve saturates (maxed out) while error persists, the integral keeps accumulating to a huge value, then overshoots wildly when the error finally reverses. *Anti-windup* (clamping or freezing the integral when saturated) prevents this.
- **Derivative kick:** a sudden target change makes $de/dt$ spike, jolting the valve. *Filtering the derivative* (or computing it from the measurement, not the error) smooths this.
- **Output saturation:** the valve command must be clamped to its physical range; commanding beyond full open is meaningless.

---

## 3. Mathematical model

**Discrete-time PID (as implemented on the Arduino).** The machine runs PID in discrete steps at a fixed sample rate. At each step $k$:
$$e_k = x_{target} - x_k$$
$$I_k = I_{k-1} + e_k \cdot \Delta t \quad\text{(accumulate, with anti-windup)}$$
$$D_k = \frac{e_k - e_{k-1}}{\Delta t} \quad\text{(or filtered)}$$
$$u_k = K_p e_k + K_i I_k + K_d D_k \quad\text{(then clamp to } [u_{min}, u_{max}])$$

**Anti-windup (clamping method).** Only accumulate the integral when the output is not saturated:
$$I_k = \begin{cases} I_{k-1} + e_k \Delta t & \text{if } u_{k-1} \text{ not saturated} \\ I_{k-1} & \text{if saturated} \end{cases}$$

**Tuning — Ziegler–Nichols (a starting point).** One classic method finds the gains from the system's open-loop step response (its delay $L$ and rate $R$):
$$K_p = \frac{1.2}{RL}, \quad K_i = \frac{K_p}{2L}, \quad K_d = 0.5 K_p L$$
These give a starting point; the machine then refines by observing the step response (overshoot, settling, steady-state error) and adjusting — ideally in the digital twin first.

**Reading the symptoms.** The machine diagnoses its tuning from the step response:
- Persistent steady-state error → increase $K_i$.
- Overshoot and oscillation → increase $K_d$ or decrease $K_p$.
- Sluggish response → increase $K_p$.
- Slow oscillation that won't settle → too much $K_i$ (reduce it).

---

## 4. Visual explanation

![Digital Twin Workflow](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/digital_twin_workflow.svg)

*Figure: digital twin workflow — see full diagram above.* (the control loop with PID)

Picture four step-response curves for the machine commanded to 200 mm, each a different tuning:
- **P only:** rises, settles *below* target (steady-state error), flat thereafter.
- **P + I:** rises, overshoots, oscillates, but eventually settles *exactly* on target (I removed the error).
- **P + I + D (under-tuned D):** still some overshoot.
- **P + I + D (well-tuned):** rises smoothly, minimal overshoot, settles exactly on target quickly.

The figure shows each term's contribution: I pulls the curve onto the target, D tames the overshoot, and the well-tuned combination hits the <5% overshoot, <2 mm error goal. Reading these curves is how the machine (and the engineer) diagnoses and refines the tuning.

---

## 5. Engineering example

**Why the machine tunes in simulation first**

Tuning a PID controller by trial-and-error on real hardware is slow and risky: a badly-tuned gain can make the hydraulic cylinder slam its end stops, oscillate violently, or spike pressure. Each trial requires running the machine, and a bad trial can damage it. For the workcell — and especially for larger hydraulic machines — blind hardware tuning is genuinely dangerous.

The digital twin changes this. Because the twin (Modules 04–08) models the machine's real nonlinear behavior — the orifice flow, the friction, the compressibility — the machine can tune its PID *in simulation* first: try a set of gains, see the predicted step response, refine, repeat, all in software with no risk. Only when the simulation predicts a good response (<5% overshoot, <2 mm error) does the machine try those gains on hardware. The twin turns dozens of risky hardware trials into safe simulated ones, with maybe one or two hardware confirmations.

This is one of the digital twin's most practical payoffs, and a major reason the curriculum invested in building a physics-based twin rather than a simple lookup model: only a physics-based twin predicts how a *new, untested* tuning will behave. The machine tunes safely because it has a faithful model of itself.

---

## 6. Worked example

**Tuning the machine's position controller.** The workcell must achieve a 200 mm step with <5% overshoot and <2 mm steady-state error. Tune the PID in the twin.

*Start (P only, $K_p = 0.02$):* settles at 198 mm — 2 mm error, no overshoot but at the error limit. Not good enough (no margin).

*Add I ($K_i = 0.002$):* the integral accumulates the residual error and drives it out — settles essentially on target. But the integral introduces some overshoot before settling. Error ✓, overshoot to manage.

*Add D ($K_d = 0.04$):* the derivative brakes the approach — overshoot drops below 1%. Error <2 mm ✓, overshoot <5% ✓. **Target met.**

*Verify anti-windup:* during the initial fast approach the valve saturates; with anti-windup, the integral does not accumulate during saturation, so there is no windup overshoot. Without it, the overshoot would be substantially larger.

Final tuning: $K_p = 0.02$, $K_i = 0.002$, $K_d = 0.04$, with anti-windup and derivative filtering. The machine meets the Precision Positioning targets (0.9% overshoot, 1.8 mm steady-state error) — in simulation. The next step is a single hardware confirmation, and a comparison of predicted vs. actual to validate the twin (Lesson 04). The machine tuned itself safely, in software, before touching hardware.

---

## 7. Interactive demonstration


**▶ Interactive demo — PID Tuner**

[Open this demo in a new tab ↗](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/demos/module10/pid_tuner.html)

This self-contained widget lets you explore the concepts of this module hands-on — adjust the inputs and watch the machine's numbers respond live, built from the same equations the tested code uses.

```python
class PID:
    """The machine's PID controller (discrete, with anti-windup + clamping)."""
    def __init__(self, kp, ki, kd, u_min=-1.0, u_max=1.0):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.u_min, self.u_max = u_min, u_max
        self.integral = 0.0
        self.prev_error = 0.0

    def step(self, error, dt):
        deriv = (error - self.prev_error) / dt
        u_unclamped = self.kp*error + self.ki*self.integral + self.kd*deriv
        u = max(self.u_min, min(self.u_max, u_unclamped))
        # anti-windup: only integrate if not saturated
        if u == u_unclamped:
            self.integral += error * dt
        self.prev_error = error
        return u

def simulate(pid, target=200, steps=800, dt=0.01):
    pos, peak = 0.0, 0.0
    for _ in range(steps):
        u = pid.step(target - pos, dt)
        if abs(u) < 0.02: u = 0.0          # dead-band
        vel = 90.0 * u
        pos += vel * dt
        peak = max(peak, pos)
    overshoot = max(0, (peak - target)/target*100)
    return pos, overshoot

for name, pid in [("P only", PID(0.02, 0, 0)),
                  ("P+I", PID(0.02, 0.01, 0)),
                  ("P+I+D", PID(0.02, 0.01, 0.02))]:
    final, os = simulate(pid)
    print(f"  {name:8s}: settles {final:6.1f} mm, overshoot {os:4.1f}%")
```

Run it. Watch the integral remove the steady-state error and the derivative tame the overshoot.

---

## 8. Coding exercise

Create `code/module10/pid_controller.py` that:

1. Implements a discrete-time PID with anti-windup, derivative filtering, and output clamping
2. Simulates the step response and measures overshoot, settling time, and steady-state error
3. Demonstrates tuning: P only → P+I → P+I+D, showing each term's effect
4. Finds gains meeting the <5% overshoot, <2 mm error target (the workcell spec)

This is the machine's precise controller — the core of its closed-loop positioning.

---

## 9. Knowledge check


*Formative — unlimited attempts, immediate feedback; does not affect your grade.*

[Open the interactive quiz in a new tab ↗](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/quizzes/module10/knowledge_check_quiz.html)

Or work through the written questions below.

1. What does each PID term respond to (present, past, rate of change)?
2. Which term eliminates steady-state error, and how?
3. Which term damps overshoot, and how?
4. What is integral windup, and how does anti-windup prevent it?
5. Why does the machine tune its PID in the digital twin before hardware?

---

## 10. Challenge problem

The machine's position controller shows a 12% overshoot and settles at exactly 200 mm with no steady-state error, but it oscillates two or three times before settling.

**a)** Which symptom points to which tuning problem? (overshoot/oscillation vs. steady-state error)

**b)** Which gain(s) should the machine adjust, and in which direction, to reduce the overshoot?

**c)** The steady-state error is already zero — what does that tell you about the integral term?

**d)** Explain how the machine would test the adjustment safely before running it on hardware.

---

## 11. Common mistakes

**Using proportional gain to remove steady-state error.** Raising $K_p$ reduces but never eliminates the error and causes overshoot. The integral term removes it cleanly.

**Forgetting anti-windup.** If the valve saturates while error persists, an unprotected integral winds up to a huge value and causes massive overshoot. Anti-windup is essential, not optional.

**Ignoring derivative kick.** A sudden target change spikes the derivative, jolting the valve. Filter the derivative or compute it from the measurement.

**Tuning blindly on hardware.** A bad gain can slam the cylinder or spike pressure. Tune in the twin first, then confirm on hardware with one or two runs.

---

## 12. Key takeaways

- PID combines three terms: P (present error, the main drive), I (accumulated error, eliminates steady-state error), D (rate of error, damps overshoot).
- The integral term drives steady-state error to zero by accumulating until the machine is exactly on target.
- The derivative term anticipates the approach and brakes, damping overshoot.
- Practical PID needs anti-windup (prevents saturation overshoot), derivative filtering (prevents kick), and output clamping.
- The machine tunes its PID in the digital twin first — safe, fast, and only possible because the twin models the real nonlinear behavior.

---

## Machine Capability Added

> **Before this lesson the machine could not:** position precisely — proportional control left a steady-state error and risked overshoot.
>
> **After this lesson the machine can:** position to specification (<2 mm error, <5% overshoot) with a tuned PID controller, eliminating steady-state error and damping overshoot — tuned safely in simulation first.

The machine now has **precise closed-loop control**. You can give the machine a PID controller that drives its positioning error to zero and approaches smoothly, meeting the Precision Positioning targets, and tune that controller safely in the digital twin before hardware. This is the controller that turns "close" into "exact."

**Digital twin contribution:** the PID controller is added to the twin, which becomes a tuning environment — predicting the closed-loop step response (overshoot, settling, error) for any set of gains. The twin lets the machine tune safely in simulation, the payoff of the physics-based model built across Modules 04–08.

---

*Lesson 02 — Version 0.1 | Next: Lesson 03 — Giving the machine task logic and safety (the state machine)*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 10 (Control) of the Fluid-Powered Physical AI curriculum: "Giving the machine a precise controller". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("Giving the machine a precise controller", Module 10 — Control) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("Giving the machine a precise controller") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("Giving the machine a precise controller", Module 10 — Control) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
