# Bernoulli and the energy equation
## Module 04 · Lesson 01

*Energy is conserved as fluid moves. Bernoulli's equation tracks the trade between pressure, velocity, and elevation — the starting point for understanding flow through the workcell.*

---

## Why The Machine Needs This

The machine's intelligence will depend on predicting how its fluid behaves. Before modeling valves and cylinders, you need the energy bookkeeping that explains why pressure changes as fluid speeds up and slows down through the workcell. The machine needs a conservation law to predict its own flows.

**Benchmark task supported:** Precision Positioning (predicting flow, the basis of motion).

---

## 1. Why this matters

The machine's intelligence rests on a single ability: predicting what its own fluid will do. The digital twin cannot model a valve or a cylinder until it can answer a more basic question — when fluid speeds up through a narrowing and slows in a widening, how does its pressure change? Get this wrong and every downstream prediction is wrong.

That question is answered by energy conservation for a moving fluid: Bernoulli's equation. It is the foundation the valve model (next lesson) and the cylinder model are built on. Before the machine can predict how it moves, it must account for where its fluid's energy goes.

---

## 2. Physical intuition

A moving fluid carries energy in three forms:

- **Pressure energy** — the energy stored in the fluid's pressure
- **Kinetic energy** — the energy of the fluid's motion (its velocity)
- **Potential energy** — the energy of its height in a gravitational field

Bernoulli's insight: in steady, frictionless, incompressible flow, the *sum* of these three is constant along a streamline. If one goes up, another must come down.

The everyday consequence you already know: when fluid flows through a narrowing (a nozzle, a partly closed valve), it speeds up. Where does the kinetic energy come from? From pressure energy. So pressure *drops* where velocity rises. This is why a fast jet of fluid leaving a nozzle is at lower pressure than the slow fluid feeding it.

In hydraulics, the velocities are usually modest and pressure dominates, so Bernoulli is often a small correction rather than the main effect. But understanding it is essential — it underlies the orifice equation (next lesson), which *is* the main effect at valves.

---

## 3. Mathematical foundations

### Bernoulli's equation

For steady, incompressible, frictionless flow along a streamline:

$$P + \frac{1}{2}\rho v^2 + \rho g h = \text{constant}$$

- $P$ = static pressure (Pa)
- $\frac{1}{2}\rho v^2$ = dynamic pressure (the kinetic term)
- $\rho g h$ = elevation term
- $\rho$ = density, $v$ = velocity, $g$ = gravity, $h$ = height

Between two points 1 and 2 on the same streamline:

$$P_1 + \frac{1}{2}\rho v_1^2 + \rho g h_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g h_2$$

### The "head" form

Dividing through by $\rho g$ expresses each term as a *head* (a height, in metres):

$$\frac{P}{\rho g} + \frac{v^2}{2g} + h = \text{constant}$$

- Pressure head $P/\rho g$
- Velocity head $v^2/2g$
- Elevation head $h$

Engineers often think in heads because they add intuitively and have units of length.

### Where Bernoulli breaks down

Bernoulli assumes **no friction** and **steady flow**. Real hydraulic lines have friction (Module 03's Darcy-Weisbach loss) and real systems have unsteady transients. So Bernoulli is an idealization. The complete energy equation adds a head-loss term:

$$\frac{P_1}{\rho g} + \frac{v_1^2}{2g} + h_1 = \frac{P_2}{\rho g} + \frac{v_2^2}{2g} + h_2 + h_{loss}$$

where $h_{loss}$ captures friction (from Module 03). This is the practical form for the workcell.

> **Workcell relevance:** Estimating the velocity and pressure at the pump outlet, and tracking how pressure changes between the pump and the cylinder, uses this energy equation with the friction loss term from Module 03.

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (Subsystem 2 — flow path)

Picture the energy as a fixed budget moving along the flow path. At the pump outlet the budget is mostly pressure head. As fluid accelerates into a narrower line, some pressure head converts to velocity head. As fluid passes through the line, friction skims energy off as $h_{loss}$ (heat). At the cylinder, what remains is the pressure available to do work.

A "head diagram" — pressure head plotted along the flow path — slopes downward overall (due to friction loss) with local dips where velocity rises (restrictions) and recoveries where it falls. This picture is the energy story of the workcell's fluid path.

---

## 5. Engineering example

**Velocity rise through a valve restriction**

When fluid flows through a partly open valve, the opening is much smaller than the line, so the fluid must accelerate dramatically to pass through. By continuity ($Q = Av$), a 10× area reduction means a 10× velocity increase. By Bernoulli, that velocity rise comes from a pressure drop.

This is exactly what happens at the workcell's flow control valve. The fluid speeds up through the restriction (pressure drops), then slows again downstream (pressure partially recovers). The *net* pressure drop across the valve is what the orifice equation (next lesson) predicts — and it is what sets the cylinder's speed.

Bernoulli explains *why* there is a pressure drop at a restriction; the orifice equation quantifies *how much*. Together they model every valve in the workcell.

---

## 6. Worked example

**Problem:** Hydraulic oil (ρ = 870 kg/m³) flows in the workcell's 10 mm supply line at 2.12 m/s (from Module 03). It then accelerates into a 4 mm restriction. Ignoring friction for this estimate:

(a) What is the velocity in the restriction?
(b) What is the pressure drop from the line to the restriction, by Bernoulli?

**Solution:**

*(a)* By continuity, $A_1 v_1 = A_2 v_2$:
$$v_2 = v_1 \frac{A_1}{A_2} = v_1 \left(\frac{D_1}{D_2}\right)^2 = 2.12 \times \left(\frac{10}{4}\right)^2 = 2.12 \times 6.25 = 13.25\ \text{m/s}$$

*(b)* By Bernoulli (same elevation, $h_1 = h_2$):
$$P_1 - P_2 = \frac{1}{2}\rho(v_2^2 - v_1^2) = \frac{1}{2}(870)(13.25^2 - 2.12^2)$$
$$= 435 \times (175.6 - 4.5) = 435 \times 171.1 = 74{,}400\ \text{Pa} = 0.74\ \text{bar}$$

So accelerating the fluid into the restriction costs about 0.74 bar of pressure head. (In a real valve, additional losses from turbulence and friction make the actual drop larger — the orifice equation captures this with its discharge coefficient.)

---

## 7. Interactive demonstration

```python
def bernoulli_pressure_drop(v1, d1_mm, d2_mm, rho=870):
    """Pressure drop (bar) accelerating from diameter d1 to d2, by Bernoulli."""
    v2 = v1 * (d1_mm / d2_mm) ** 2
    dp_pa = 0.5 * rho * (v2**2 - v1**2)
    return v2, dp_pa / 1e5

for d2 in [8, 6, 4, 3, 2]:
    v2, dp = bernoulli_pressure_drop(2.12, 10, d2)
    print(f"restriction {d2:2d} mm: v = {v2:6.1f} m/s, ideal drop = {dp:5.2f} bar")
```

Run it. As the restriction shrinks, velocity climbs steeply and the pressure drop grows with its square — the same nonlinearity that makes valves behave the way they do.

---

## 8. Coding exercise

Write `code/module04/bernoulli_demo.py` that:

1. Implements the Bernoulli pressure drop between two pipe diameters
2. Plots pressure drop vs. restriction diameter for the workcell's supply line velocity
3. Overlays the velocity in the restriction on a second axis
4. Marks where cavitation risk begins (when local pressure would fall below the fluid's vapor pressure — a note for Lesson 02)

Use NumPy and Matplotlib.

---

## 9. Knowledge check

1. Name the three forms of energy Bernoulli's equation tracks.
2. If fluid speeds up through a restriction, what happens to its pressure? Why?
3. What two assumptions does Bernoulli's equation make that real hydraulic systems violate?
4. What term must be added to Bernoulli to make it practical for real lines?
5. In hydraulics, is the velocity (kinetic) term usually large or small compared to the pressure term? What does that imply?

---

## 10. Challenge problem

The workcell's pump outlet (12 mm diameter) feeds the 10 mm supply line, which feeds a 4 mm flow control restriction, at 10 LPM.

**a)** Calculate the velocity at each of the three diameters (12, 10, 4 mm) using continuity.

**b)** Using Bernoulli (ignore friction), calculate the pressure change from the pump outlet to the supply line, and from the supply line to the restriction.

**c)** Now add the Module 03 friction loss for the 10 mm supply line (~0.54 bar over 2 m). What is the total pressure change from pump outlet to the restriction entrance?

**d)** Explain why the pressure *recovers* somewhat downstream of the restriction where the line widens again — and why it does not fully recover to the upstream value.

---

## 11. Common mistakes

**Applying Bernoulli where friction dominates.** Over a long line, friction loss (Darcy-Weisbach) is the main effect, not the Bernoulli velocity trade. Use the full energy equation with $h_{loss}$ for real lines.

**Forgetting that Bernoulli is per-streamline and steady.** It does not apply across unsteady transients (valve switching, pressure spikes). Those need the dynamic equations of Lessons 3–4.

**Ignoring the velocity term entirely.** While pressure usually dominates in hydraulics, at restrictions the velocity term becomes large and important. That is exactly where the orifice equation lives.

**Confusing static and dynamic pressure.** The pressure a gauge reads is static pressure. The dynamic term ($\frac12\rho v^2$) is additional energy in the motion. Bernoulli relates them; do not add them blindly.

---

## 12. Key takeaways

- Bernoulli's equation is energy conservation for a moving fluid: pressure + kinetic + elevation energy is constant along a streamline (ideal case).
- Where velocity rises (a restriction), pressure falls; where velocity falls, pressure recovers.
- Real systems add a friction head-loss term ($h_{loss}$, from Module 03) to make the energy equation practical.
- In hydraulics, pressure usually dominates, but at valve restrictions the velocity term becomes large — the domain of the orifice equation.
- This energy bookkeeping is the foundation for the valve model (Lesson 02) and the cylinder dynamics (Lessons 03–04) that become the digital twin.

---


## Machine Capability Added

> **Before this lesson the machine could not:** account for where its fluid's energy goes as it moves.
>
> **After this lesson the machine can:** track how pressure trades against velocity along its flow path — the foundation of the valve and cylinder models.

The machine's **fluid energy can now be accounted for**. You can track how pressure trades against velocity along the workcell's flow path — the foundation for the valve and cylinder models that become the digital twin.

---

*Lesson 01 — Version 0.1 | Next: Lesson 02 — Orifice flow and the valve model (the first digital twin component)*
