# Energy losses in fluid transmission
## Module 03 · Lesson 04

*Moving fluid through pipes and hoses costs energy. This lesson quantifies that loss with the Reynolds number and the Darcy-Weisbach equation — and shows why line sizing matters more than beginners expect.*

---

## Why The Machine Needs This

The machine loses pressure to friction as fluid travels from pump to cylinder — and undersized lines waste that pressure as heat, starving the actuator. The workcell needs its lines sized so the power generated actually reaches the muscle. The machine needs an efficient path for its fluid.

---

## 1. Why this matters

The ideal equations of Module 01 assumed pressure transmitted perfectly from pump to actuator. Reality is lossier. As fluid flows through hoses, pipes, and fittings, friction converts some of the pressure energy into heat. The pump must supply that lost pressure on top of what the actuator needs.

For the workcell, these losses determine the real pressure that reaches the cylinder, the heat the system generates, and — critically — they reveal why undersized lines are a costly mistake. This lesson also introduces the friction model that becomes part of the digital twin in Module 04. It closes Module 03 by connecting fluid properties (viscosity, density) to system performance (pressure drop, heat).

---

## 2. Physical intuition

Push fluid through a pipe and it resists. The resistance comes from two sources: the fluid's own internal friction (viscosity) and the turbulence it generates at higher speeds.

Two flow regimes exist:

- **Laminar flow:** at low velocity, the fluid moves in smooth, orderly layers, like cards sliding over each other. Losses come purely from viscous friction between layers. Predictable and relatively low.
- **Turbulent flow:** at high velocity, the fluid churns chaotically. Eddies and mixing dramatically increase the friction. Losses rise steeply.

The transition between them is governed by the Reynolds number — a single dimensionless quantity that tells you which regime you are in.

The crucial practical insight: **pressure loss is extremely sensitive to pipe diameter.** Halving the diameter does not double the loss — it can increase it tenfold or more, because the fluid must move much faster through the smaller cross-section, and loss grows with velocity. Line sizing is one of the highest-leverage decisions in hydraulic design.

---

## 3. Mathematical foundations

### Flow velocity

From continuity (Module 01), velocity in a pipe is flow divided by area:

$$v = \frac{Q}{A} = \frac{Q}{\pi (D/2)^2}$$

### Reynolds number

The dimensionless number that predicts laminar vs. turbulent flow:

$$Re = \frac{v \cdot D}{\nu}$$

- $v$ = flow velocity (m/s)
- $D$ = pipe inner diameter (m)
- $\nu$ = kinematic viscosity (m²/s)

Rule of thumb: $Re < 2300$ is laminar; $Re > 4000$ is turbulent; in between is transitional. Hydraulic supply lines are often laminar or transitional.

### Darcy-Weisbach pressure drop

The pressure lost to friction over a length of pipe:

$$\Delta P = f \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2}$$

- $f$ = friction factor (dimensionless)
- $L$ = pipe length (m)
- $D$ = inner diameter (m)
- $\rho$ = fluid density (kg/m³)
- $v$ = velocity (m/s)

### Friction factor

For laminar flow, the friction factor depends only on Reynolds number:

$$f = \frac{64}{Re}$$

For turbulent flow in smooth pipes, an approximation is $f \approx 0.316 \cdot Re^{-0.25}$ (Blasius).

> **Workcell relevance:** With these equations you can estimate the pressure drop between the pump and the primary cylinder — the first real (non-ideal) calculation of how much pressure actually reaches the actuator. This pipe-friction model becomes a component of the digital twin (Module 04).

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (Subsystem 2 — supply line)

Imagine the pressure as a quantity that drops steadily along the supply line from pump to cylinder. The steeper the drop, the more energy is lost to friction (and turned into heat). A wide, short, smooth line gives a gentle drop; a narrow, long, fitting-laden line gives a steep one.

The velocity-squared term in Darcy-Weisbach is the key visual: because loss scales with $v^2$, and velocity scales with $1/D^2$ (smaller pipe, much faster fluid), the loss is extraordinarily sensitive to diameter. A plot of pressure drop vs. pipe diameter falls off a cliff as diameter shrinks.

---

## 5. Engineering example

**Why hydraulic hoses come in standard sizes**

Hydraulic hose and tube are sold in standard inner diameters precisely because line sizing is a balance: too small and friction losses (and heat) become unacceptable; too large and the hose is heavy, expensive, and unwieldy. Manufacturers publish recommended flow-velocity ranges:

- Suction lines: ≤ 1.2 m/s (low, to protect the pump from cavitation)
- Pressure lines: ≤ 5 m/s (moderate)
- Return lines: ≤ 3 m/s

A designer picks the smallest standard line that keeps velocity within the recommended range for its flow. For the workcell at 10 LPM, this selection determines whether the pressure reaching the cylinder is nearly full system pressure or noticeably reduced by line losses.

---

## 6. Worked example

**Problem:** The workcell supply line carries 10 LPM of ISO VG 46 oil (ν = 46 cSt = 46×10⁻⁶ m²/s, ρ = 870 kg/m³) over a 2 m length. Compare a 10 mm inner diameter line with a 6 mm one.

**Solution:**

**10 mm line:**

Area: $A = \pi(0.005)^2 = 7.85\times10^{-5}\ \text{m}^2$
Velocity: $v = \frac{10/60000}{7.85\times10^{-5}} = 2.12\ \text{m/s}$
Reynolds: $Re = \frac{2.12 \times 0.010}{46\times10^{-6}} = 461$ → **laminar**
Friction factor: $f = 64/461 = 0.139$
Pressure drop: $\Delta P = 0.139 \times \frac{2}{0.010} \times \frac{870 \times 2.12^2}{2} = 54{,}400\ \text{Pa} = 0.54\ \text{bar}$

**6 mm line:**

Velocity: $v = 5.89\ \text{m/s}$
Reynolds: $Re = 769$ → still laminar
Pressure drop: $\Delta P \approx 4.19\ \text{bar}$

**Comparison:** Shrinking the line from 10 mm to 6 mm increases the pressure loss from 0.54 bar to 4.19 bar — nearly **8 times more loss** — for the same flow. And the 6 mm line's velocity (5.9 m/s) exceeds the recommended pressure-line limit of 5 m/s. The 10 mm line is the correct choice: low loss, acceptable velocity.

This is the worked demonstration of why line sizing matters. A 4 bar loss on a 100 bar system is 4% of system pressure wasted as heat — significant over continuous operation.

---

## 7. Interactive demonstration

```python
import math

def line_pressure_drop(flow_lpm, diameter_mm, length_m,
                       nu_cst=46, rho=870):
    Q = flow_lpm / 60000                 # m^3/s
    D = diameter_mm / 1000               # m
    nu = nu_cst * 1e-6                    # m^2/s
    A = math.pi * (D/2)**2
    v = Q / A
    Re = v * D / nu
    f = 64/Re if Re < 2300 else 0.316 * Re**-0.25
    dp = f * (length_m/D) * (rho * v**2 / 2)
    return v, Re, dp/1e5                  # m/s, -, bar

print(f"{'Dia (mm)':>9} | {'v (m/s)':>8} | {'Re':>6} | {'dP (bar)':>9}")
print("-" * 42)
for d in [6, 8, 10, 12, 16]:
    v, Re, dp = line_pressure_drop(10, d, 2)
    print(f"{d:>9} | {v:>8.2f} | {Re:>6.0f} | {dp:>9.3f}")
```

Run it. Watch the pressure drop collapse as diameter grows — and note where velocity exceeds the 5 m/s pressure-line guideline.

---

## 8. Coding exercise

Write `code/module03/pipe_friction.py` that:

1. Implements the Reynolds number and Darcy-Weisbach calculation (laminar and turbulent friction factors)
2. Plots pressure drop vs. inner diameter for the workcell's 10 LPM supply line
3. Marks the recommended pressure-line velocity limit (5 m/s) as a constraint
4. Recommends the smallest standard line size (6, 8, 10, 12, 16 mm) that keeps both velocity and pressure drop acceptable

This pipe-friction model is reused in the digital twin (Module 04) and the energy analysis (Module 08).

---

## 9. Knowledge check

1. What two flow regimes exist, and what physically distinguishes them?
2. What does the Reynolds number predict, and what is the approximate laminar threshold?
3. In the Darcy-Weisbach equation, pressure drop scales with velocity to what power?
4. Why is pressure drop so sensitive to pipe diameter?
5. Why are suction lines sized for lower velocity than pressure lines?

---

## 10. Challenge problem

The workcell's primary cylinder is mounted at the end of a moving arm, requiring a 3.5 m flexible hose run (longer than the rigid 2 m supply line) at 10 LPM.

**a)** Using the 10 mm line result as a starting point, estimate the pressure drop for a 3.5 m hose of the same diameter. (Loss scales linearly with length.)

**b)** If this loss is unacceptable (say you want under 1 bar), what diameter hose would you need? Use the demonstration code to find it.

**c)** A larger hose is heavier and stiffer, which resists the arm's motion. Describe the tradeoff you are balancing.

**d)** How would this line loss appear in the digital twin? If the twin assumes zero line loss, would it over- or under-predict the pressure available at the cylinder?

---

## 11. Common mistakes

**Ignoring line losses entirely.** Beginners assume full system pressure reaches the actuator. Real lines lose pressure to friction, and undersized lines lose a lot. Always estimate the drop.

**Undersizing lines to save space or cost.** A line one size too small can multiply the pressure loss several-fold and overheat the system. The velocity guidelines exist for good reason.

**Forgetting the velocity-squared relationship.** Because loss grows with $v^2$ and velocity grows with $1/D^2$, the diameter sensitivity is dramatic. Small diameter changes have large loss consequences.

**Using the wrong friction factor.** Laminar ($f = 64/Re$) and turbulent (Blasius or Moody) friction factors are different formulas. Check the Reynolds number first to know which regime — and which formula — applies.

---

## 12. Key takeaways

- Moving fluid through lines costs pressure energy, lost as heat to friction.
- The Reynolds number $Re = vD/\nu$ predicts laminar (smooth, <2300) vs. turbulent (chaotic, >4000) flow.
- Darcy-Weisbach gives the loss: $\Delta P = f \cdot (L/D) \cdot \rho v^2/2$; laminar friction factor is $f = 64/Re$.
- Pressure loss is extremely sensitive to diameter; the workcell's 10 mm supply line loses ~0.54 bar where a 6 mm line would lose ~4.2 bar at the same flow.
- Velocity guidelines (suction ≤1.2, pressure ≤5, return ≤3 m/s) drive line sizing.
- This pipe-friction model becomes part of the digital twin and the Module 08 energy analysis.

---

## Module 03 deliverable

With all four lessons complete, produce the **Fluid Specification Document** for the Smart Agricultural Workcell — one page covering: fluid type (mineral-based), ISO VG grade (46), operating temperature range and the usable viscosity window, ISO 4406 cleanliness target (18/16/13), filter specification ($\beta_{10} \geq 100$), and the supply-line sizing (10 mm). Include the rationale for each choice, grounded in the workcell's indoor operating environment.

---


## Machine Capability Added

The machine's **fluid path can now be sized**. You can compute line losses and choose the workcell's supply line (10 mm, ~0.54 bar loss) so power reaches the cylinder efficiently — completing the Fluid Specification.

---

*Lesson 04 — Version 0.1 | Module 03 lesson content complete. Next: Module 03 summary, exercises, code, and Lab 03.*
