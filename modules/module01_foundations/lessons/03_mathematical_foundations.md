# Mathematical foundations
## Module 01 · Lesson 03

*Three equations govern every hydraulic system. This lesson derives them clearly, connects each to the workcell, and builds computational fluency.*

---

## Why The Machine Needs This

The machine must hit specific numbers: ~20 kN of grip force, ~85 mm/s of motion, under 2 kW of power. Intuition alone cannot size a cylinder or pick a motor. The machine needs the three governing equations that turn its required behavior into concrete dimensions.

---

## 1. Why this matters

The workcell's cylinder must exert 500 N to grip a fruit without damaging it. The pump delivers 12 LPM. The maximum system pressure is 120 bar. Can the system do the job? Which cylinder bore is needed? How fast will the piston extend?

These are engineering questions. They have numerical answers. This lesson gives you the three equations that answer every question of this type — and the unit fluency to use them without error.

---

## 2. Physical intuition

You already have the intuition from Lesson 02. Now we give it mathematical form.

The three governing equations are:

1. **Pascal's Law** — connects pressure, force, and area
2. **Continuity** — connects flow rate, area, and velocity
3. **Hydraulic power** — connects pressure, flow, and power

These are not approximations. They follow directly from the definition of pressure, the incompressibility of liquids, and conservation of energy. They apply in every hydraulic system, at every scale.

---

## 3. Mathematical foundations

### Equation 1 — Pascal's Law

$$\boxed{P = \frac{F}{A}}$$

**Definitions:**
- $P$ = pressure (Pa, bar, or PSI)
- $F$ = force (N or kN)
- $A$ = area (m² or mm²)

**Derivation from first principles:**

Pressure is defined as force per unit area. If a piston of area $A$ exerts a force $F$ on a fluid, the pressure in the fluid is $P = F/A$.

For an incompressible fluid in a closed container, that pressure acts equally on every surface. A second piston of area $A_2$ on the same fluid therefore experiences a force:

$$F_2 = P \cdot A_2 = \frac{F_1}{A_1} \cdot A_2$$

This is the complete statement of Pascal's Law. No assumptions beyond fluid incompressibility.

**Unit conversion essential:**

| Pressure unit | Equivalent |
|---------------|-----------|
| 1 bar | 100,000 Pa = 100 kPa |
| 1 bar | 14.504 PSI |
| 1 N/mm² | 10 bar |
| 1 MPa | 10 bar |

For cylinder force calculations, the most convenient form uses bar and mm²:

$$F\ [\text{N}] = P\ [\text{bar}] \times A\ [\text{mm}^2] \times 0.1$$

The factor 0.1 converts bar to N/mm²: $1\ \text{bar} = 0.1\ \text{N/mm}^2$.

**Workcell example:**

Primary cylinder bore: 50 mm  
System pressure: 100 bar  
Bore area: $A = \pi(25)^2 = 1963\ \text{mm}^2$  
Extend force: $F = 100 \times 1963 \times 0.1 = 19{,}630\ \text{N} = 19.63\ \text{kN}$

---

### Equation 2 — Continuity (incompressible flow)

$$\boxed{Q = A \cdot v}$$

**Definitions:**
- $Q$ = volumetric flow rate (m³/s, LPM, or GPM)
- $A$ = piston bore area (m² or mm²)
- $v$ = piston velocity (m/s or mm/s)

**Derivation from first principles:**

An incompressible fluid cannot be compressed. Every cubic millimetre that enters one end of a cylinder must displace a cubic millimetre of piston travel at the other end. In time $\Delta t$:

$$\text{Volume in} = Q \cdot \Delta t = A \cdot v \cdot \Delta t = \text{Volume displaced by piston}$$

Therefore $Q = A \cdot v$, which rearranges to:

$$v = \frac{Q}{A}$$

**Unit conversion essential:**

The most common practical conversion:

$$Q\ [\text{LPM}] \rightarrow Q\ [\text{mm}^3/\text{s}] = Q_{\text{LPM}} \times \frac{10^6}{60} \approx Q_{\text{LPM}} \times 16{,}667$$

Then:

$$v\ [\text{mm/s}] = \frac{Q\ [\text{mm}^3/\text{s}]}{A\ [\text{mm}^2]}$$

**Workcell example:**

Flow rate: 10 LPM → $166{,}667\ \text{mm}^3/\text{s}$  
Bore area: $1963\ \text{mm}^2$  
Extend velocity: $v = 166{,}667 / 1963 = 84.9\ \text{mm/s}$

**Note on differential cylinder effect:**

The rod side has a smaller effective area:

$$A_{rod} = \pi\left(\frac{D_{bore}}{2}\right)^2 - \pi\left(\frac{D_{rod}}{2}\right)^2$$

The same flow rate into the rod side produces a higher velocity. This is the differential cylinder effect. Retract is always faster than extend (for the same flow), and retract force is always less than extend force (for the same pressure).

---

### Equation 3 — Hydraulic power

$$\boxed{P_{hyd} = p \cdot Q}$$

**Definitions:**
- $P_{hyd}$ = hydraulic power (W or kW)
- $p$ = pressure (Pa)
- $Q$ = flow rate (m³/s)

**Derivation from first principles:**

Power is work per unit time: $P = W/t = F \cdot d / t = F \cdot v$.

For a hydraulic actuator: $F = p \cdot A$ and $v = Q/A$, therefore:

$$P = F \cdot v = (p \cdot A) \cdot \left(\frac{Q}{A}\right) = p \cdot Q$$

The area cancels. This is why hydraulic power depends only on pressure and flow — independent of which cylinder is doing the work.

**Unit conversion essential:**

$$P_{hyd}\ [\text{kW}] = \frac{p\ [\text{bar}] \times Q\ [\text{LPM}]}{600}$$

This is the single most useful practical formula. Memorise it.

Derivation: $1\ \text{bar} = 10^5\ \text{Pa}$, $1\ \text{LPM} = 10^{-3}/60\ \text{m}^3/\text{s}$, so $p \cdot Q = \frac{p_{\text{bar}} \times Q_{\text{LPM}} \times 10^5}{60 \times 10^3} = \frac{p_{\text{bar}} \times Q_{\text{LPM}}}{600}\ \text{kW}$.

**Workcell example:**

System: 100 bar, 10 LPM  
Hydraulic power: $P = \frac{100 \times 10}{600} = 1.67\ \text{kW}$

Motor power required: $P_{motor} = \frac{P_{hyd}}{\eta_{pump}} = \frac{1.67}{0.85} \approx 1.96\ \text{kW}$

A 2.2 kW motor is the next standard size — this is the basis for the workcell motor selection.

---

### Efficiency

Real systems have losses. Three efficiency terms appear throughout the curriculum:

**Volumetric efficiency** $\eta_v$: actual flow / theoretical flow. Losses from internal leakage.

$$Q_{actual} = Q_{theoretical} \times \eta_v$$

**Mechanical efficiency** $\eta_m$: actual torque / theoretical torque. Losses from friction.

**Overall efficiency** $\eta = \eta_v \times \eta_m$: used to relate shaft power to hydraulic power.

For a gear pump at moderate pressure: $\eta_v \approx 0.90–0.95$, $\eta \approx 0.80–0.88$.

---

## 4. Visual explanation

> See figure: `assets/figures/system_pipeline.svg`

The ACTUATE stage of the pipeline is governed entirely by the three equations in this lesson:

- Pressure at the cylinder determines force (Pascal's Law)
- Flow rate to the cylinder determines speed (continuity)
- The product of both determines power

The digital twin's cylinder model (added in Module 04) uses these same equations as its core. The difference is that the twin also models transient dynamics — what happens in the fractions of a second while pressure builds and the piston accelerates.

---

## 5. Engineering example

**Tractor hydraulic outlet specifications**

A standard Category II tractor hydraulic remote outlet delivers:
- Flow rate: 35–60 LPM
- Maximum pressure: 175–200 bar
- Maximum hydraulic power: $\frac{175 \times 35}{600} = 10.2\ \text{kW}$ to $\frac{200 \times 60}{600} = 20\ \text{kW}$

This is the power budget available to any intelligent attachment mounted on the tractor. The Smart Agricultural Workcell, running at 10 LPM and 100 bar (1.67 kW), uses less than 20% of the smallest available tractor outlet. There is substantial headroom.

This is why the workcell design is tractor-compatible: it can be powered entirely from a standard remote hydraulic outlet without additional power units.

---

## 6. Worked example — full system calculation

**Problem:** Specify the hydraulic system for a workcell task: grip a 2 kg object with 200 N of grip force, then lift it 250 mm in under 3 seconds.

**Step 1 — Gripping cylinder:**

Required grip force: 200 N (each jaw pushes 100 N)  
Available pressure: 80 bar  
Required bore area: $A = F / (P \times 0.1) = 100 / (80 \times 0.1) = 12.5\ \text{mm}^2$  
Minimum bore: $D = 2\sqrt{A/\pi} = 2\sqrt{12.5/\pi} = 3.99\ \text{mm}$

Use a 10 mm bore cylinder (standard size, large margin of safety for position control).

**Step 2 — Lifting cylinder:**

Required lift force: $F = m \times g = 2 \times 9.81 = 19.6\ \text{N}$ plus the weight of the end effector (assume 1.5 kg → 14.7 N)  
Total: $34.3\ \text{N}$ (negligible pressure requirement — bore size driven by stability, not force)  
Use: 25 mm bore cylinder at 80 bar → extend force = $80 \times \pi(12.5)^2 \times 0.1 = 3927\ \text{N}$ (far more than needed — minimum pressure for this task is 0.07 bar)

**Step 3 — Velocity and flow:**

Required: 250 mm in 3 s → $v = 250/3 = 83.3\ \text{mm/s}$  
Bore area (25 mm): $A = \pi(12.5)^2 = 491\ \text{mm}^2$  
Required flow: $Q = A \times v = 491 \times 83.3 = 40{,}891\ \text{mm}^3/\text{s} = 2.45\ \text{LPM}$

**Step 4 — Power:**

$P_{hyd} = \frac{80 \times 2.45}{600} = 0.33\ \text{kW}$

A 0.75 kW motor (next standard size above the minimum) with a gear pump at 2.5 LPM displacement is entirely sufficient.

This is a small, efficient workcell — confirming the design intent.

---

## 7. Interactive demonstration

The Pascal's Law calculator in `code/module01/pascals_law.py` implements all three equations. Add this function to explore the power equation:

```python
def system_power_budget(pressure_bar, flow_lpm, pump_efficiency=0.85):
    """
    Calculate hydraulic power and required motor power.

    Args:
        pressure_bar: System pressure in bar
        flow_lpm: Flow rate in LPM
        pump_efficiency: Overall pump efficiency (0–1)

    Returns:
        dict with hydraulic_power_kw and motor_power_kw
    """
    hydraulic_kw = (pressure_bar * flow_lpm) / 600
    motor_kw = hydraulic_kw / pump_efficiency
    return {
        "hydraulic_power_kw": round(hydraulic_kw, 3),
        "motor_power_kw": round(motor_kw, 3),
    }

# Standard workcell operating point
print(system_power_budget(100, 10))
# {'hydraulic_power_kw': 1.667, 'motor_power_kw': 1.961}
```

Explore: at what pressure and flow does the system require a 2.2 kW motor? Plot the iso-power contours on a pressure-flow chart.

---

## 8. Coding exercise

Write `code/module01/unit_converter.py` with the following functions:

```python
def bar_to_pa(bar: float) -> float: ...
def pa_to_bar(pa: float) -> float: ...
def lpm_to_m3s(lpm: float) -> float: ...
def m3s_to_lpm(m3s: float) -> float: ...
def hp_to_kw(hp: float) -> float: ...
def kw_to_hp(kw: float) -> float: ...
def mm2_to_m2(mm2: float) -> float: ...
def bore_area_mm2(diameter_mm: float) -> float: ...
```

Then write a `HydraulicSystem` dataclass that stores pressure (bar), flow (LPM), and bore diameter (mm), and provides methods `.extend_force_kN()`, `.extend_velocity_mms()`, and `.power_kw()`.

This module is used in every subsequent code file in the curriculum.

---

## 9. Knowledge check

1. State Pascal's Law in words. What is the SI unit of pressure?

2. A cylinder with a 63 mm bore operates at 160 bar. Calculate the extend force in kN.

3. A pump delivers 20 LPM to a cylinder with a 50 mm bore. Calculate the piston velocity in mm/s.

4. What hydraulic power (kW) does a 200 bar / 15 LPM system produce? Use the 1/600 formula.

5. Convert: 3000 PSI to bar. 15 GPM to LPM. 5 HP to kW.

6. A cylinder has a 40 mm bore and a 22 mm rod. At 10 LPM, what is the extend velocity? The retract velocity? Which is faster, and why?

---

## 10. Challenge problem

The workcell is being specified for a heavier variant: gripping and lifting 5 kg objects at 5 cycles per minute, 300 mm stroke, extend velocity 100 mm/s, system pressure 120 bar.

**a)** What bore diameter is needed to lift 5 kg (plus 2 kg end effector) at 120 bar with a safety factor of 3?

**b)** What flow rate is needed to achieve 100 mm/s with that bore?

**c)** What hydraulic power is required?

**d)** Assuming 85% pump efficiency, what motor power is needed?

**e)** If the duty cycle is 5 cycles per minute with 2 s extend and 2 s retract per cycle, what is the average (time-averaged) hydraulic power?

---

## 11. Common mistakes

**Mixing units without converting.** The formula $P = p \cdot Q$ requires Pa and m³/s for watts. Using bar and LPM without the 1/600 factor gives an answer 60,000× too large. Always check units explicitly.

**Applying Pascal's Law to moving systems without caution.** Strictly, Pascal's Law applies to static fluids. In a moving system, pressure varies between inlet and outlet due to friction and inertia. For steady-state engineering estimates it is a good approximation. Module 04 introduces the dynamic pressure equations.

**Forgetting the rod-side area.** The retract force is not equal to the extend force. Always calculate rod-side area separately: $A_{rod-side} = \pi(R_{bore}^2 - R_{rod}^2)$.

**Treating efficiency as 100%.** A pump with 85% efficiency delivering 2 kW of hydraulic power requires a 2.35 kW motor. Undersizing the motor causes overheating and premature failure. Always include efficiency.

---

## 12. Key takeaways

- Three equations govern all hydraulic systems: Pascal's Law (force), continuity (velocity), hydraulic power. Memorise the practical forms.
- Pascal's Law: $F = P \times A \times 0.1$ (with P in bar, A in mm², F in N)
- Continuity: $v\ [\text{mm/s}] = Q\ [\text{LPM}] \times 16667 / A\ [\text{mm}^2]$
- Power: $P_{kW} = (p_{bar} \times Q_{LPM}) / 600$
- The differential cylinder effect means retract is always faster and weaker than extend at equal pressure and flow.
- Efficiency is never 100%. Always size the motor for $P_{hyd} / \eta_{pump}$.
- The Smart Agricultural Workcell at baseline (10 LPM, 100 bar) requires approximately 2 kW from the motor — a small machine with substantial force capability.

---


## Machine Capability Added

The machine can now be **quantified**. You can compute its force, velocity, and power from first principles — the calculations that size every actuator and that the digital twin will eventually evaluate in real time.

---

*Lesson 03 — Version 0.1 | Next: Lesson 04 — Visual explanation (the workcell and its subsystems)*
