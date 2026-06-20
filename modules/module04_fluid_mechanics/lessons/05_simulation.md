# Simulation: the first ODE in Python
## Module 04 · Lesson 05

*Everything comes together. The valve model, the force balance, and the pressure dynamics combine into a coupled ODE — and we solve it in Python. The workcell's cylinder comes alive in software. This is the digital twin's first breath.*

---

## 1. Why this matters

This is the payoff lesson of Module 04, and arguably of the curriculum's first half. The previous four lessons built the pieces: the valve flow model (Lesson 02), the force balance (Lesson 03), and the pressure dynamics (Lesson 04). Now we assemble them into a single coupled system of differential equations and solve it numerically.

The result is the first *simulation* of the workcell's cylinder — a software model that takes a valve command and predicts how the real cylinder will move, instant by instant. This is precisely what a digital twin does. When you finish this lesson, you will have run the first working component of the Smart Agricultural Workcell's digital twin, and you will understand both how it works and where its limits are.

---

## 2. Physical intuition

A simulation answers a simple question repeatedly: *given where the system is right now, where will it be a tiny moment later?*

The ODE gives the rates of change — velocity (how fast position changes), acceleration (how fast velocity changes), and pressure rise rates (how fast pressures change). A numerical solver takes those rates, steps forward a tiny time increment, updates the state, and repeats — thousands of times — to trace the system's evolution.

The art is in two places. First, the equations must be *coupled correctly*: the pressures drive the motion (force balance), and the motion changes the pressures (pressure dynamics), so they must be solved together. Second, the solver must handle the system's character. Hydraulic systems are **stiff** — pressures change on a microsecond timescale while the piston moves on a second timescale. That separation of timescales is real physics, and it shapes how we simulate.

This lesson confronts both honestly: a robust model that works reliably, and the full model that reveals the stiffness challenge.

---

## 3. Mathematical foundations

### The coupled system (recap)

The full cylinder model is four coupled first-order ODEs:

$$\dot{x} = v$$
$$\dot{v} = \frac{1}{m}\left(A_b P_b - A_r P_r - F_{friction}(v) - F_{load}\right)$$
$$\dot{P_b} = \frac{B_e}{V_b}\left(Q_{in} - A_b v\right)$$
$$\dot{P_r} = \frac{B_e}{V_r}\left(A_r v - Q_{out}\right)$$

with $Q_{in}, Q_{out}$ from the valve model (Lesson 02). The state vector is $[x, v, P_b, P_r]$.

### The stiffness problem

The pressure equations have a huge coefficient $B_e/V$. For the workcell's small bore chamber ($V \approx 0.05$ L) and high bulk modulus ($B_e \approx 1.5$ GPa), this coefficient is about $3\times10^{13}$ — meaning pressures respond in microseconds. The piston, by contrast, takes about a second to complete its stroke. A ratio of a million between the fast and slow timescales makes the system **stiff**: explicit solvers (like RK45) take impossibly small steps, and even implicit solvers (BDF) struggle over long horizons.

This is not a flaw in the model. It is the genuine physics of hydraulics — pressure really does build almost instantly compared to mechanical motion. Recognizing and handling stiffness is a core simulation skill.

### The quasi-static simplification

When pressure equilibrates quickly relative to motion, we can make an excellent approximation: assume the pressure is always at the value that satisfies flow continuity *right now*. This collapses the two pressure states. Instead of integrating $\dot{P_b}$ and $\dot{P_r}$, we *solve* for $P_b$ and $P_r$ at each instant from the condition that valve flow equals the displacement rate:

$$Q_{valve}(u, P_{supply} - P_b) = A_b v \quad\Rightarrow\quad P_b = P_{supply} - \frac{\rho}{2}\left(\frac{A_b v}{C_d A(u)}\right)^2$$

This leaves a simple 2-state system $[x, v]$ that is non-stiff and integrates robustly. It is the *primary* model for this lesson. The full 4-state model remains available to demonstrate the stiffness directly.

> **Workcell relevance:** This is `cylinder_simulation.py`. The quasi-static model is the reliable workhorse; the full model shows the stiffness reality. Both agree on the steady state — validating the approximation.

---

## 4. Visual explanation

> See figure: `assets/figures/digital_twin_workflow.svg`

The simulation realizes the entire twin-side of the digital twin workflow figure: the valve orifice model feeds the cylinder ODE, which outputs position, velocity, and pressure over time. Running the simulation *is* running the twin.

Three time-series plots tell the story:
- **Position vs. time:** rises steadily while the valve is open, then flattens (holds) when it closes.
- **Velocity vs. time:** ramps up as the valve opens, holds at a steady extend speed, drops to zero on hold.
- **Pressure vs. time:** bore pressure builds, settles to the value that balances the load during motion, then rises toward supply pressure on hold; rod pressure mirrors it.

Watching these three together is watching the cylinder "think out loud" — the twin's prediction of what the real cylinder will do.

---

## 5. Engineering example

**The simulation as a design tool**

Before building any hardware, the simulation answers design questions. How fast will the cylinder extend with this valve? Does it reach the target position in the cycle time budget? How much does the load slow it down? What pressure does the system actually run at during motion?

For the workcell, the simulation confirms the design intent from Modules 01–03: with the baseline valve sizing, the cylinder extends at about 82 mm/s — matching the ~85 mm/s target computed analytically in Module 01. This agreement between the dynamic simulation and the static hand-calculation is a powerful validation: two independent methods, consistent answer. The simulation then goes further, showing the *transient* — how the cylinder gets up to speed, something the static calculation cannot reveal.

---

## 6. Worked example

**Problem:** Run the quasi-static simulation of the workcell cylinder: 50 mm bore, 28 mm rod, 100 bar supply, extend for 1.0 s then hold. Predict the trajectory.

**Solution (the simulation output):**

| Time (s) | Position (mm) | Velocity (mm/s) |
|----------|---------------|-----------------|
| 0.00 | 0.0 | 0.0 |
| 0.05 | 2.9 | 82.3 |
| 0.10 | 7.0 | 82.3 |
| 0.25 | 19.3 | 82.3 |
| 0.50 | 39.9 | 82.3 |
| 1.00 | 81.0 | 82.3 |
| 1.20 | 82.3 | 0.0 (held) |
| 2.00 | 82.3 | 0.0 (held) |

**Interpretation:** The cylinder ramps quickly to a steady extend velocity of 82.3 mm/s, travels about 81 mm during the 1.0 s the valve is open, then holds at 82.3 mm when the valve closes. The steady velocity matches Module 01's analytical estimate (~85 mm/s) closely — the small difference is the friction and load the dynamic model includes that the simple static calculation omitted.

**Cross-check with the full model:** The full 4-state model, run over its reliable short window, shows the pressure building from 2 to ~73 bar in the first 10 ms (piston still nearly stationary), then the piston breaking free and settling to the *same* 82.3 mm/s with bore pressure ~26 bar and rod pressure ~37 bar during motion. Two models, consistent steady state — strong validation.

---

## 7. Interactive demonstration

```python
# Requires scipy. From the code/module04 directory:
from cylinder_simulation import simulate_quasistatic, summarize

sol, p = simulate_quasistatic(supply_bar=100, t_extend=1.0)
summarize(sol, p)

# Experiment: how does supply pressure affect extend speed?
for supply in [60, 80, 100, 120]:
    sol, p = simulate_quasistatic(supply_bar=supply)
    final = sol.y[0][-1] * 1000
    peak_v = max(abs(sol.y[1])) * 1000
    print(f"{supply} bar: peak {peak_v:.0f} mm/s, reached {final:.0f} mm")
```

Run it. Higher supply pressure gives a larger pressure drop across the valve, more flow, and faster extension — but the relationship is square-root (Lesson 02), so doubling pressure does not double speed.

---

## 8. Coding exercise

Complete and explore `code/module04/cylinder_simulation.py`:

1. Run the quasi-static simulation and reproduce the trajectory table
2. Run the full 4-state model over a 0.3 s window and observe the pressure build-up and breakaway transient
3. Compare the two models' steady-state velocity and pressures — confirm they agree
4. Add a `retract` phase after the hold (valve command goes negative) and simulate a full extend-hold-retract cycle
5. Plot position, velocity, and pressure for the complete cycle

Reflect in a comment: why does the quasi-static model integrate so much more easily than the full model? What did you give up by using it? (Answer: you give up the fast pressure transient detail — the first few milliseconds — in exchange for robust, fast integration of the motion.)

---

## 9. Knowledge check

1. What does a numerical ODE solver actually do, step by step?
2. Why must the force balance and pressure dynamics be solved together rather than separately?
3. What makes a hydraulic cylinder simulation "stiff"? Is stiffness a modeling error or real physics?
4. What does the quasi-static approximation assume, and what does it let you avoid?
5. The simulation predicts ~82 mm/s; Module 01's hand calculation predicted ~85 mm/s. Why is this agreement meaningful?

---

## 10. Challenge problem

You want the workcell to complete a full pick cycle: extend 200 mm, hold 0.5 s (gripping), retract 200 mm — within a target cycle time.

**a)** Using the simulation, estimate how long the 200 mm extend takes at the baseline ~82 mm/s.

**b)** Retract uses the rod side (smaller area), so for the same valve and flow it is faster. Predict whether retract takes more or less time than extend, and roughly estimate it.

**c)** Add up extend + grip-hold + retract to estimate the total cycle time. How many cycles per minute does this allow?

**d)** If the target is 8 cycles per minute, does the baseline design meet it? If not, name two changes (from Modules 02–04) that would speed the cycle, and predict their effect using the equations you have built.

---

## 11. Common mistakes

**Using an explicit solver on a stiff system.** RK45 and similar explicit methods take impossibly small steps on stiff hydraulic ODEs and effectively stall. Use a stiff solver (BDF, Radau) for the full model, or the quasi-static simplification.

**Forgetting to reduce to first-order form.** `solve_ivp` integrates first-order systems. The second-order force balance must be split into $\dot{x}=v$ and $\dot{v}=F/m$.

**Mismatched units in the state vector.** Mixing mm and m, or bar and Pa, inside the ODE is a frequent and silent error. Keep the integration in SI (m, m/s, Pa) and convert only for display.

**Trusting a simulation without cross-checking.** Always validate against an independent estimate. Here, the simulation's steady velocity matches Module 01's hand calculation — that agreement is what lets you trust the result. A simulation that disagrees with a sound hand-calculation has a bug (as one did during this module's development — a pressure-dynamics sign error caught exactly this way).

---

## 12. Key takeaways

- The simulation assembles the valve model, force balance, and pressure dynamics into a coupled ODE solved numerically — the first working piece of the digital twin.
- Hydraulic cylinder ODEs are *stiff*: pressures change in microseconds, motion in seconds. This is real physics, not a flaw.
- The quasi-static model (collapsing the pressure states via flow continuity) is robust and reliable; the full 4-state model demonstrates the stiffness directly. Both agree on the steady state.
- The simulated steady velocity (~82 mm/s) matches Module 01's analytical estimate (~85 mm/s) — independent validation.
- Always cross-check a simulation against an independent calculation; agreement builds trust, disagreement reveals bugs.

---

## Module 04 deliverable

With all five lessons complete, you have built the **cylinder digital twin core**: a working simulation (`cylinder_simulation.py`) that predicts the workcell cylinder's motion from a valve command, validated against analytical estimates. This is the foundation that Modules 05–10 extend (real pump, valve, sensor models) and that Module 11 integrates into the full workcell digital twin.

Save your simulation. Every later module adds to it.

---

*Lesson 05 — Version 0.1 | Module 04 lesson content complete. This is the mathematical and computational core of the curriculum's first half — the digital twin is now alive.*
