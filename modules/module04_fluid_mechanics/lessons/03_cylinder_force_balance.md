# Cylinder dynamics: the force balance
## Module 04 · Lesson 03

*Newton's second law applied to a hydraulic cylinder. This is the equation that predicts how the cylinder accelerates — the mechanical half of the digital twin's core.*

---

## Why The Machine Needs This

The machine's twin must predict how the cylinder *accelerates*, not just how hard it pushes. That requires Newton's second law applied to the moving piston — including the friction that makes slow, precise motion difficult. The machine needs the mechanical half of its cylinder model.

---

## 1. Why this matters

In Module 01 you calculated the *static* force a cylinder produces. But a moving cylinder is a dynamic system: it accelerates, fights friction, carries a load, and responds to changing pressures. Predicting its actual motion over time requires Newton's second law — a force balance.

This force balance is the mechanical half of the cylinder's equations of motion. Combined with the pressure dynamics of Lesson 04, it forms the coupled ODE system that *is* the cylinder's digital twin (Lesson 05). This lesson sets up the forces; the next adds the pressures; the one after solves them together.

---

## 2. Physical intuition

Picture the workcell's primary cylinder mid-stroke. Several forces act on the piston-and-rod assembly:

- **Driving force:** pressure on the bore side pushes the piston out.
- **Resisting back-pressure:** pressure on the rod side pushes back.
- **Friction:** the seals and rod guide resist motion, always opposing the direction of travel.
- **External load:** the weight of the end effector and any workpiece, plus whatever the cylinder is pushing against.
- **Inertia:** the mass of the moving assembly resists acceleration.

Newton's second law ties them together: the *net* force equals mass times acceleration. If the driving force exceeds the resisting forces, the piston accelerates outward. When they balance, it moves at constant velocity. When the load wins, it decelerates.

The subtle force is friction. It is not constant — it depends on velocity in a characteristic way (the Stribeck effect): high at the instant of breakaway from rest, dropping as motion begins, then rising again with speed. Capturing friction realistically is what separates a crude cylinder model from an accurate one.

---

## 3. Mathematical foundations

### The force balance (Newton's second law)

For the piston-and-rod assembly of mass $m$ and position $x$:

$$m\ddot{x} = A_b P_b - A_r P_r - F_{friction} - F_{load}$$

- $m\ddot{x}$ = mass times acceleration (inertia term)
- $A_b P_b$ = bore-side area times bore-side pressure (driving force on extend)
- $A_r P_r$ = rod-side area times rod-side pressure (back-pressure)
- $F_{friction}$ = friction force (opposes motion)
- $F_{load}$ = external load force

This is a second-order differential equation: acceleration $\ddot{x}$ depends on position-dependent and velocity-dependent terms.

### The friction model (Stribeck, simplified)

A practical friction model has three components:

$$F_{friction} = \underbrace{F_c \cdot \text{sign}(\dot{x})}_{\text{Coulomb}} + \underbrace{b \cdot \dot{x}}_{\text{viscous}} + \underbrace{(F_s - F_c)e^{-(\dot{x}/v_s)^2}\text{sign}(\dot{x})}_{\text{Stribeck}}$$

- $F_c$ = Coulomb (kinetic) friction — constant magnitude, opposes motion
- $b\dot{x}$ = viscous friction — grows with velocity
- $F_s$ = static (breakaway) friction — highest, at zero velocity
- $v_s$ = Stribeck velocity — sets how fast static friction decays into kinetic

The Stribeck term captures the "stiction" you feel when something just starts to move: it takes more force to break free than to keep going. For the workcell, this matters at the start and end of each stroke and during slow, precise positioning.

### Reducing to first-order form for simulation

A second-order ODE is solved numerically by splitting it into two first-order equations. Let $v = \dot{x}$:

$$\dot{x} = v$$
$$\dot{v} = \frac{1}{m}\left(A_b P_b - A_r P_r - F_{friction}(v) - F_{load}\right)$$

This pair is what the ODE solver integrates (Lesson 05).

> **Workcell relevance:** This is the force balance for the workcell's primary cylinder. The load is the end effector plus any gripped workpiece (Module 01's example: ~1.5 kg effector + payload). The friction parameters come from the cylinder's seals. These equations become `cylinder_dynamics.py`.

---

## 4. Visual explanation

> See figure: `assets/figures/digital_twin_workflow.svg` (the cylinder ODE block)

In the digital twin workflow, the "Cylinder ODE" block is the mechanical core. It receives flow (which sets pressures, via Lesson 04) and outputs the cylinder's position and velocity over time.

A free-body diagram is the key visual here: the piston with arrows for each force — a large arrow for the driving pressure force, a smaller opposing arrow for back-pressure, a friction arrow always pointing against motion, and the load arrow. The net of these arrows, divided by mass, is the acceleration. Watching how the arrows change as the cylinder moves is the intuition for the dynamics.

The Stribeck friction curve is the second visual: friction force vs. velocity, showing the high breakaway peak at zero velocity, the dip as motion begins, and the rise with speed.

---

## 5. Engineering example

**Why precise positioning is hard at low speed**

When the workcell positions its end effector precisely — approaching a workpiece slowly — it operates in the low-velocity regime where Stribeck friction dominates. Near zero velocity, static friction is high and changes rapidly with small velocity changes. This makes smooth slow motion difficult: the cylinder tends to "stick" then "slip," producing jerky motion (stick-slip).

This is a real and well-known challenge in hydraulic positioning. The friction model in this lesson predicts it, and the closed-loop control of Module 10 must compensate for it. Understanding the force balance — specifically the Stribeck friction term — is what lets you anticipate and design around stick-slip in the workcell's precision tasks.

---

## 6. Worked example

**Problem:** The workcell's primary cylinder (50 mm bore, 28 mm rod) is extending. At a given instant:
- Bore pressure $P_b$ = 80 bar, rod pressure $P_r$ = 5 bar
- Moving mass $m$ = 3 kg (piston, rod, end effector)
- Velocity $v$ = 50 mm/s
- Coulomb friction $F_c$ = 60 N, viscous coefficient $b$ = 200 N·s/m
- External load (effector + workpiece weight, horizontal so no gravity component along stroke) $F_{load}$ = 100 N

Calculate the instantaneous acceleration. (Ignore the Stribeck peak at this non-zero velocity; use Coulomb + viscous.)

**Solution:**

Areas:
$$A_b = \pi(0.025)^2 = 1.963\times10^{-3}\ \text{m}^2,\quad A_r = A_b - \pi(0.014)^2 = 1.348\times10^{-3}\ \text{m}^2$$

Driving force: $A_b P_b = 1.963\times10^{-3} \times 80\times10^5 = 15{,}708\ \text{N}$

Back-pressure: $A_r P_r = 1.348\times10^{-3} \times 5\times10^5 = 674\ \text{N}$

Friction (extending, v > 0): $F_c + b v = 60 + 200(0.050) = 60 + 10 = 70\ \text{N}$

Net force: $15{,}708 - 674 - 70 - 100 = 14{,}864\ \text{N}$

Acceleration: $\ddot{x} = 14{,}864 / 3 = 4{,}955\ \text{m/s}^2$

That enormous instantaneous acceleration shows the cylinder is far from force balance — it will accelerate hard until back-pressure and flow limits bring it to steady velocity. (In the full simulation, pressures adjust dynamically via Lesson 04, preventing unrealistic runaway.)

---

## 7. Interactive demonstration

```python
import math

def cylinder_acceleration(Pb_bar, Pr_bar, v, m=3.0,
                          bore_mm=50, rod_mm=28,
                          Fc=60, b=200, F_load=100):
    Ab = math.pi * (bore_mm/2000)**2      # m^2
    Ar = Ab - math.pi * (rod_mm/2000)**2
    drive = Ab * Pb_bar*1e5
    back  = Ar * Pr_bar*1e5
    friction = (Fc + b*abs(v)) * (1 if v >= 0 else -1)
    net = drive - back - friction - F_load
    return net / m

print(f"Acceleration: {cylinder_acceleration(80, 5, 0.050):.0f} m/s^2")
# Explore: how does acceleration change as back-pressure rises?
for Pr in [5, 20, 40, 60, 78]:
    a = cylinder_acceleration(80, Pr, 0.050)
    print(f"  Pr={Pr:2d} bar: a = {a:7.0f} m/s^2")
```

Run it. As back-pressure rises toward the driving pressure, net force and acceleration fall toward zero — the cylinder approaches force balance and steady velocity. This is the dynamic the full simulation captures.

---

## 8. Coding exercise

Write `code/module04/cylinder_dynamics.py` that:

1. Implements the full Stribeck friction model (static, Coulomb, viscous)
2. Implements the cylinder force balance returning acceleration
3. Plots the Stribeck friction curve (friction force vs. velocity)
4. Provides the right-hand-side function `rhs(t, state)` returning `[dx/dt, dv/dt]` ready for `solve_ivp` (used in Lesson 05)

Structure the force balance and friction as importable functions — Lesson 05's simulation will use them.

---

## 9. Knowledge check

1. Write Newton's second law for a hydraulic cylinder and name each term.
2. Why is friction not a constant force? Name the three components of the friction model.
3. What is the Stribeck effect, and when does it matter most for the workcell?
4. Why must a second-order ODE be split into two first-order equations for numerical solution?
5. What is stick-slip, and which friction component causes it?

---

## 10. Challenge problem

The workcell must position its end effector to within 1 mm during a slow approach at 5 mm/s.

**a)** At 5 mm/s, the cylinder is deep in the Stribeck regime. Using $F_s = 120$ N (static), $F_c = 60$ N (Coulomb), $v_s = 10$ mm/s, calculate the Stribeck friction contribution at v = 5 mm/s. (Use the Stribeck term from the model.)

**b)** Compare the total friction at 5 mm/s versus at 50 mm/s. Which is higher? Does this match the stick-slip intuition?

**c)** Explain why this velocity-dependent friction makes the slow approach prone to jerky stick-slip motion.

**d)** Propose how closed-loop control (Module 10) might compensate — what would the controller need to do differently at low speed?

---

## 11. Common mistakes

**Treating friction as a constant.** Friction depends on velocity (Stribeck, Coulomb, viscous). A constant-friction model misses stick-slip and mispredicts slow-speed behavior — exactly where precision matters.

**Forgetting the back-pressure term.** The rod-side pressure pushes against extension. Omitting $A_r P_r$ overpredicts the net driving force.

**Sign errors on friction.** Friction always opposes motion. Its sign flips with velocity direction. Getting this wrong makes the simulation unstable or unphysical.

**Solving the second-order ODE directly.** Numerical solvers integrate first-order systems. Always reduce $m\ddot{x} = F$ to the pair $\dot{x}=v$, $\dot{v}=F/m$ before simulating.

---

## 12. Key takeaways

- The cylinder force balance is Newton's second law: $m\ddot{x} = A_b P_b - A_r P_r - F_{friction} - F_{load}$.
- Friction is velocity-dependent: static (breakaway), Coulomb (constant kinetic), and viscous (grows with speed), combined in the Stribeck model.
- The Stribeck effect causes stick-slip at low velocity — a real challenge for the workcell's precision positioning.
- For simulation, the second-order ODE is split into two first-order equations: $\dot{x}=v$, $\dot{v}=F_{net}/m$.
- This force balance is the mechanical core of the cylinder's digital twin, paired with pressure dynamics in Lesson 04.

---


## Machine Capability Added

The machine can now **predict its cylinder's acceleration**. The force balance (with Stribeck friction) is the mechanical core of the twin — and it explains the stick-slip that threatens Precision Positioning at low speed.

---

*Lesson 03 — Version 0.1 | Next: Lesson 04 — Pressure dynamics and bulk modulus*
