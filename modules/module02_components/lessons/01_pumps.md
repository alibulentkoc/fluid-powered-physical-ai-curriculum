# Pumps: the heart of the system
## Module 02 · Lesson 01

*The pump converts mechanical rotation into pressurized flow. It is where every hydraulic system begins, and its selection drives the design of everything downstream.*

---

## Why The Machine Needs This

The machine cannot move until it has a source of pressurized flow. Everything the workcell does — every motion, every grip — begins with hydraulic power, and that power begins at the pump. The machine's first physical need is a heart that pushes fluid.

---

## 1. Why this matters

In Module 01 you treated the pump as a source — flow appeared at a given pressure and you used it. Now you open the box.

The pump is the single component that determines what the rest of the workcell can do. Its displacement sets the flow. Its flow sets the actuator speeds. Its pressure rating caps the available force. Choose the pump wrong and no amount of clever control downstream can recover the lost capability.

This lesson gives you the knowledge to select, size, and reason about the pump in the Smart Agricultural Workcell — and to understand why a fixed-displacement gear pump is the right baseline choice.

---

## 2. Physical intuition

A hydraulic pump does not create pressure. It creates *flow*. Pressure arises only when that flow meets resistance.

Picture a gear pump: two meshing gears in a close-fitting housing. As the gears turn, fluid is trapped in the spaces between the gear teeth and the housing wall, carried around the outside from inlet to outlet, and squeezed out as the teeth re-mesh. Every revolution moves a fixed volume of fluid. That fixed volume per revolution is the pump's **displacement**.

If the outlet is wide open, the fluid flows out freely at near-zero pressure. If the outlet is restricted — by a load on a cylinder, by a partly closed valve — the fluid still wants to come out at the same rate, so pressure builds until either the load moves or the relief valve opens.

This is the key intuition: **the pump pushes a fixed flow; the system decides the pressure.**

A positive-displacement pump (gear, vane, piston) traps and moves discrete volumes. This is different from a centrifugal pump (like a water pump in a car), which flings fluid outward and cannot build the high pressures hydraulics require. Hydraulic systems almost always use positive-displacement pumps for exactly this reason.

---

## 3. Mathematical foundations

### Theoretical flow

The flow a pump *should* produce, ignoring losses:

$$Q_t = D \cdot n$$

- $Q_t$ = theoretical flow rate
- $D$ = displacement (volume per revolution, cc/rev)
- $n$ = shaft speed (rev/min)

In practical units: $Q_t\ [\text{LPM}] = \dfrac{D\ [\text{cc/rev}] \times n\ [\text{RPM}]}{1000}$

### Actual flow and volumetric efficiency

Real pumps leak internally — some fluid slips back past the gears, especially at high pressure. The actual delivered flow is:

$$Q_a = Q_t \cdot \eta_v$$

where $\eta_v$ is the **volumetric efficiency** (typically 0.90–0.95 for a gear pump at moderate pressure). As pressure rises, internal leakage increases and $\eta_v$ falls.

### Input power

The mechanical power the pump draws from the motor:

$$P_{in} = \frac{p \cdot Q_a}{\eta_{overall}}$$

where $\eta_{overall} = \eta_v \cdot \eta_m$ combines volumetric and mechanical (friction) losses.

> **Workcell calculation:** The workcell needs 10 LPM at 100 bar. If we choose a gear pump and drive it at 1450 RPM (a standard motor speed), what displacement do we need?
>
> Rearranging: $D = \dfrac{Q_t \times 1000}{n}$. Allowing for $\eta_v = 0.92$, the theoretical flow must be $Q_t = 10/0.92 = 10.9\ \text{LPM}$.
>
> $D = \dfrac{10.9 \times 1000}{1450} = 7.5\ \text{cc/rev}$.
>
> An 8 cc/rev gear pump is the next standard size and gives a small margin. This is the workcell pump.

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (Subsystem 1 — Hydraulic power)

The pump sits at the heart of S1. Trace the path: the electric motor shaft drives the pump; the pump draws oil from the reservoir through the inlet (suction) line; pressurized oil leaves through the outlet toward the valves. The pressure relief valve branches off the outlet, ready to dump flow back to the reservoir if pressure exceeds its setting.

Three pump types you should recognize:

**Gear pump** — two meshing gears. Simple, cheap, robust, tolerant of contamination. Fixed displacement. Moderate efficiency. The workcell's choice.

**Vane pump** — a slotted rotor with sliding vanes inside a cam ring. Quieter than gear pumps, can be variable displacement. Mid-range cost and pressure.

**Piston pump** — pistons in a rotating barrel, driven by a swashplate. Highest pressure, highest efficiency, can be variable displacement, most expensive. Used where high pressure or variable flow justifies the cost.

---

## 5. Engineering example

**Why tractors use gear pumps for auxiliary hydraulics**

A typical agricultural tractor uses a fixed-displacement gear pump for its auxiliary and implement hydraulics. The reasons map directly onto the workcell's needs:

- **Robustness:** field environments are dirty. Gear pumps tolerate contamination better than tight-tolerance piston pumps.
- **Cost:** gear pumps are inexpensive and easy to replace.
- **Simplicity:** no variable-displacement mechanism to maintain.
- **Adequate performance:** for lifting, tilting, and actuating implements, fixed flow at a capped pressure is sufficient.

The workcell inherits this logic. It does not need the efficiency of a piston pump or the variable flow of a swashplate design. A fixed-displacement gear pump matches the application — robust, affordable, simple.

---

## 6. Worked example

**Problem:** A gear pump has a displacement of 8 cc/rev and a volumetric efficiency of 0.92. It is driven at 1450 RPM. The system operates at 100 bar with an overall efficiency of 0.85.

Calculate: (a) theoretical flow, (b) actual flow, (c) input power required from the motor.

**Solution:**

*(a) Theoretical flow*
$$Q_t = \frac{D \times n}{1000} = \frac{8 \times 1450}{1000} = 11.6\ \text{LPM}$$

*(b) Actual flow*
$$Q_a = Q_t \times \eta_v = 11.6 \times 0.92 = 10.67\ \text{LPM}$$

*(c) Input power*
$$P_{in} = \frac{p \times Q_a}{\eta_{overall}} = \frac{(100 \times 10.67)/600}{0.85} = \frac{1.78}{0.85} = 2.09\ \text{kW}$$

A 2.2 kW motor is the next standard size. This confirms the workcell motor selection from Module 01.

---

## 7. Interactive demonstration

Run the pump flow model (build it in the coding exercise, or use this snippet):

```python
def gear_pump(displacement_cc, speed_rpm, vol_eff=0.92):
    """Return theoretical and actual flow in LPM."""
    q_theoretical = displacement_cc * speed_rpm / 1000
    q_actual = q_theoretical * vol_eff
    return q_theoretical, q_actual

for rpm in [1000, 1450, 1800, 2200]:
    qt, qa = gear_pump(8, rpm)
    print(f"{rpm} RPM:  theoretical {qt:.1f} LPM,  actual {qa:.1f} LPM")
```

Observe: flow scales linearly with speed. This is the defining property of a fixed-displacement pump — to change flow, you change speed. (A variable-displacement pump changes flow by tilting a swashplate at constant speed.)

---

## 8. Coding exercise

Write `code/module02/pump_flow_model.py` that:

1. Models a fixed-displacement gear pump
2. Plots actual flow vs. shaft speed for several volumetric efficiencies (0.85, 0.90, 0.95)
3. Adds a horizontal line at the workcell's required 10 LPM
4. Marks the operating point (8 cc/rev, 1450 RPM)

Use NumPy and Matplotlib. The plot should make clear at what speed the 8 cc/rev pump meets the 10 LPM requirement.

```python
import numpy as np
import matplotlib.pyplot as plt

def actual_flow(displacement_cc, speed_rpm, vol_eff):
    return displacement_cc * speed_rpm / 1000 * vol_eff

# implement the plot
```

---

## 9. Knowledge check

1. Does a pump create pressure or flow? Explain what determines the other quantity.
2. What is displacement, and what are its units?
3. A 10 cc/rev pump runs at 1800 RPM with 90% volumetric efficiency. What is the actual flow in LPM?
4. Why does volumetric efficiency decrease as pressure increases?
5. Why is a fixed-displacement gear pump the right choice for the workcell rather than a variable-displacement piston pump?

---

## 10. Challenge problem

The workcell is being upgraded for a faster duty cycle requiring 18 LPM at up to 120 bar.

**a)** The existing 8 cc/rev pump runs at 1450 RPM. Can it supply 18 LPM at 92% volumetric efficiency? If not, by how much does it fall short?

**b)** Option 1: increase the pump speed. What speed would the 8 cc/rev pump need to reach 18 LPM actual? Is that speed reasonable for a gear pump (typical max ~3000 RPM)?

**c)** Option 2: increase displacement. What displacement at 1450 RPM gives 18 LPM actual?

**d)** At 120 bar and 18 LPM, what motor power is required (assume 85% overall efficiency)? Does the existing 2.2 kW motor suffice?

---

## 11. Common mistakes

**Thinking the pump sets the pressure.** It does not. The pump sets the flow. The load and the relief valve set the pressure. A pump rated "250 bar" can survive that pressure — it does not produce it on its own.

**Confusing theoretical and actual flow.** Datasheets often quote displacement, from which you compute theoretical flow. The delivered flow is always lower because of internal leakage. Always apply volumetric efficiency.

**Ignoring the speed-flow relationship.** For a fixed-displacement pump, flow is proportional to speed. If the motor runs slower than rated, the flow drops proportionally — and your actuators move slower than designed.

**Oversizing the pump.** A bigger pump than needed wastes energy (more flow over the relief valve as heat) and money. Size the pump to the requirement plus a modest margin, not to the largest available.

---

## 12. Key takeaways

- A pump produces flow, not pressure. Pressure arises when flow meets resistance.
- Positive-displacement pumps (gear, vane, piston) trap and move fixed volumes — essential for the high pressures hydraulics require.
- Theoretical flow $Q_t = D \cdot n$; actual flow $Q_a = Q_t \cdot \eta_v$.
- For a fixed-displacement pump, flow scales linearly with shaft speed.
- The workcell uses an 8 cc/rev gear pump at 1450 RPM, delivering ~10.7 LPM actual — matching the 10 LPM requirement with a small margin.
- Pump selection drives the whole system: it sets flow, which sets actuator speed, and its pressure rating caps available force.

---


## Machine Capability Added

The machine now has a **defined power source**. You can specify the pump that gives the workcell its flow (8 cc/rev gear pump at 1450 RPM → ~10.7 LPM) and explain why its choice caps every downstream capability.

---

*Lesson 01 — Version 0.1 | Next: Lesson 02 — Valves: direction, pressure, and flow*
