# The machine needs to perceive its own state
## Module 09 · Lesson 01

*The physical machine is complete — but blind. It moves and holds and protects itself, yet it has no idea where it is, how hard it is pushing, or what its pressure is. This lesson gives the machine its first senses: the ability to feel its own state.*

---

## Why The Machine Needs This

The machine of Modules 01–08 is physically complete, but it operates entirely open-loop and blind. It commands the cylinder to extend, but it cannot tell whether the cylinder actually arrived. It applies a gripping force, but it cannot feel how hard it is gripping. It builds pressure, but it cannot measure it. A blind machine can only execute fixed motions and hope — it cannot position accurately, control force, or know if anything went wrong.

For the machine to become *intelligent*, it must first *perceive*. Sensing is the SENSE stage of the pipeline — the foundation of everything in the intelligence half of the curriculum. Before the machine can decide (Module 10) or self-monitor (Module 11), it must measure its own state: pressure, position, and force. This lesson gives the machine its senses.

**Benchmark task supported:** Autonomous Manipulation (a machine cannot manipulate autonomously without perceiving its state), Precision Positioning (positioning accuracy requires position feedback), and Force-Controlled Interaction (force control requires force sensing).

---

## 1. The machine's problem

The machine commands its cylinder to extend 150 mm. Did it? Open-loop, the machine assumes it did — but friction (Module 07), load variation, or a fault could leave it short or long, and the machine would never know. It commands a gentle grip. Is it gentle, or is it crushing the workpiece? Without force sensing, the machine cannot tell. It holds a position. Is the load drifting (Module 08)? Without position sensing, the drift is invisible.

Every capability the machine built in Modules 01–08 is executed *blind*. The machine acts, but it does not perceive the results of its actions. This is the fundamental limit of an open-loop machine: it cannot adapt, correct, or verify, because it has no feedback. The gap between "command" and "knowing what actually happened" is exactly what sensing fills.

The machine's problem: measure its own physical state — the pressure in its lines, the position of its cylinder, the force at its end-effector — so that it can know, not just assume, what it is doing.

---

## 2. The concept: the machine's three core senses

The machine needs to perceive three quantities, each measured by a specific sensor.

**Pressure (the machine's effort).** Pressure transducers measure the hydraulic pressure in the machine's lines. A strain-gauge transducer uses a Wheatstone bridge: pressure deforms a diaphragm, straining gauges whose resistance changes, unbalancing the bridge to produce a signal proportional to pressure. The workcell places transducers on the **bore side and rod side** of the primary cylinder. From these two pressures, the machine computes the cylinder's actual force — its sense of how hard it is pushing.

**Position (the machine's location).** A position transducer on the cylinder rod tells the machine where the cylinder is. A linear potentiometer (a resistive divider — simple and cheap) suffices for the workcell; a magnetostrictive transducer offers higher accuracy for longer strokes. From the position, the machine knows whether it reached its target, and by differentiating, estimates its velocity. This is the machine's sense of where it is.

**Force (the machine's touch).** A load cell at the end-effector jaw measures the gripping force directly. Like the pressure transducer, it uses a strain-gauge bridge, amplified (by an HX711 or INA125) to a readable signal. Force sensing lets the machine detect *contact* (the moment the jaw touches the workpiece) and *limit* its grip — the difference between holding a workpiece and crushing it. This is the machine's sense of touch.

Together, pressure, position, and force give the machine a complete picture of its own physical state — the raw perception that intelligence is built on.

---

## 3. Mathematical model

**Force from differential pressure.** The machine's most important derived sense: the cylinder's actual force, computed from the bore-side and rod-side pressures:
$$F_{actual} = P_{bore} \cdot A_{bore} - P_{rod} \cdot A_{rod}$$

For the workcell at 93.5 bar bore and 3 bar rod back-pressure:
$$F = (93.5 \times 1963 - 3 \times 1348) \times 0.1 = 17{,}950\ \text{N} = 17.95\ \text{kN}$$

This is powerful: by measuring two pressures, the machine knows its actual output force *without a force sensor on the cylinder* — the differential pressure *is* the force (scaled by area). The machine senses its effort directly from its hydraulics.

**The 4–20 mA current signal.** Industrial pressure transducers output a current (4–20 mA) rather than a voltage, because current signals are immune to wire-resistance and noise (the same current flows regardless of wire length, and electromagnetic interference adds negligible current). The machine reads this with a shunt resistor (converting current to a voltage the ADC can read):
$$V_{ADC} = I_{signal} \cdot R_{shunt}, \quad P = P_{min} + \frac{I - 4\,\text{mA}}{16\,\text{mA}}(P_{max} - P_{min})$$
4 mA maps to minimum pressure, 20 mA to maximum — and a reading of 0 mA signals a *broken wire* (a built-in fault indication the machine gets for free).

**Velocity from position.** The machine estimates velocity by differentiating position:
$$v \approx \frac{x_k - x_{k-1}}{\Delta t}$$
But naive differentiation amplifies noise (a small position-measurement jitter becomes a large velocity spike), which is why filtering (Lesson 02) is essential before differentiating.

---

## 4. Visual explanation

> See figure: `assets/figures/system_pipeline.svg` (the SENSE stage)

Picture the machine's circuit now studded with sensors at the points that matter: pressure transducers on both sides of the primary cylinder, a position transducer along the rod, a load cell at the gripper jaw, and a flow sensor on the supply line (Lesson 03). Each sensor turns a physical quantity into an electrical signal that flows to the machine's controller. The figure shows the SENSE stage lighting up — the first stage of the pipeline, where the physical machine connects to its emerging intelligence. Arrows of information flow *from* the hydraulics *to* the controller, the reverse of the command arrows from Module 06. The machine is beginning to perceive.

---

## 5. Engineering example

**Why the machine senses force two ways**

The workcell measures force through *two* independent paths: the differential cylinder pressure (computed force) and the end-effector load cell (direct force). This redundancy is deliberate and valuable.

The differential-pressure force tells the machine the *cylinder's* output — how hard the actuator is pushing, useful for the primary positioning and for detecting load changes. The load cell tells the machine the *contact* force at the jaw — what the workpiece actually feels, essential for gentle gripping. They measure different things at different points, and together they give the machine a richer sense of force than either alone.

This redundancy also enables self-checking: if the computed force (from pressure) and the measured force (from the load cell) disagree beyond their expected relationship, something is wrong — a leak, a sensor fault, a mechanical problem. The machine's two force senses can validate each other. This is a recurring theme of intelligent machines: multiple senses cross-check, turning raw measurement into reliable perception.

---

## 6. Worked example

**The machine reads its state.** The primary cylinder is mid-task. The sensors report: bore pressure 93.5 bar, rod pressure 3 bar, position 150 mm, end-effector load cell 0 N (not yet gripping). What does the machine know?

*Cylinder force (from differential pressure):*
$$F = (93.5 \times 1963 - 3 \times 1348) \times 0.1 = 17{,}950\ \text{N} = 17.95\ \text{kN}$$
The cylinder is pushing with ~18 kN — consistent with full-pressure extension against the circuit (Module 08).

*Position:* 150 mm — the cylinder has reached its target. The machine *knows* it arrived, rather than assuming.

*End-effector force:* 0 N — the gripper has not yet contacted the workpiece. When it does, the load cell will register the contact force, and the machine will know to stop closing.

From three sensor readings, the machine has a complete picture: it is at its target, pushing with known force, not yet gripping. This is perception — the machine knowing its actual state. Every intelligent action in the modules to come depends on this picture being available and accurate.

---

## 7. Interactive demonstration

```python
import math

A_BORE = math.pi * 25**2
A_ROD = A_BORE - math.pi * 14**2

def force_from_pressure(p_bore_bar, p_rod_bar):
    """The machine's force, sensed from differential pressure."""
    return (p_bore_bar * A_BORE - p_rod_bar * A_ROD) * 0.1   # N

def current_to_pressure(mA, p_min=0, p_max=160):
    """Convert a 4-20 mA transducer signal to pressure."""
    if mA < 3.5:
        return None   # broken wire / fault
    return p_min + (mA - 4) / 16 * (p_max - p_min)

# The machine reads its sensors
print("Machine state from sensors:")
print(f"  cylinder force: {force_from_pressure(93.5, 3)/1000:.2f} kN")
print(f"  pressure from 13.5 mA signal: {current_to_pressure(13.5):.0f} bar")
print(f"  pressure from 0 mA signal: {current_to_pressure(0)} (broken wire!)")
```

Run it. The machine computes its force from two pressures and reads a transducer's current signal — its first perceptions.

---

## 8. Coding exercise

Create `code/module09/sensor_models.py` that:

1. Models a pressure transducer: 4–20 mA output, conversion to pressure, broken-wire detection
2. Computes cylinder force from bore and rod pressures
3. Models a position transducer with realistic resolution
4. Models a load cell with taring (zero offset) and calibration

This is the machine's sensing layer — the SENSE stage that feeds the digital twin.

---

## 9. Knowledge check

1. Why is the physically-complete machine of Modules 01–08 still "blind"? What can it not do?
2. Name the machine's three core senses and the sensor for each.
3. How does the machine compute its cylinder force from pressure measurements?
4. Why do industrial pressure transducers output 4–20 mA instead of a voltage?
5. Why does the machine sense force two ways (differential pressure and load cell)?

---

## 10. Challenge problem

The machine's bore-side pressure transducer reads 13.5 mA (range 0–160 bar) and the rod-side reads 4.2 mA. The position transducer reads 150 mm.

**a)** Convert both current signals to pressures.

**b)** Compute the cylinder's actual force from these two pressures.

**c)** The end-effector load cell reads 0 N but the cylinder force is high. What does this tell the machine about the task state?

**d)** Suddenly the bore-side transducer reads 0 mA. What has happened, and why is this fault easy to detect with a 4–20 mA signal?

---

## 11. Common mistakes

**Assuming open-loop commands succeed.** Without sensing, the machine cannot know if a commanded motion actually happened. Friction, load, or faults can defeat the command silently. Sensing is what turns "commanded" into "confirmed."

**Differentiating raw position for velocity.** Naive differentiation amplifies measurement noise into large velocity spikes. Position must be filtered (Lesson 02) before differentiating.

**Using voltage signals over long wires.** Wire resistance and noise corrupt voltage signals. Current (4–20 mA) signals are immune, which is why industry uses them — and they detect broken wires for free (0 mA).

**Forgetting to tare the load cell.** A load cell has a zero offset that must be subtracted (taring) before its readings mean anything. An untared load cell reports the weight of the jaw itself, not the grip force.

---

## 12. Key takeaways

- The physically-complete machine is blind; sensing is the SENSE stage that gives it perception, the foundation of all intelligence.
- The machine's three core senses are pressure (transducers), position (rod transducer), and force (load cell) — plus flow (Lesson 03).
- The machine computes its cylinder force directly from differential pressure: $F = P_{bore}A_{bore} - P_{rod}A_{rod}$.
- Industrial transducers output 4–20 mA for noise immunity and free broken-wire detection (0 mA = fault).
- The machine senses force two ways (pressure and load cell), enabling richer perception and self-checking.

---

## Machine Capability Added

> **Before this lesson the machine could not:** perceive anything — it acted entirely blind, assuming its commands succeeded.
>
> **After this lesson the machine can:** sense its own physical state — pressure, position, and force — knowing what it is actually doing rather than assuming.

The machine now has **perception** — its first senses. You can measure the machine's pressure, position, and force, and compute its actual cylinder force from differential pressure. This is the SENSE stage, the foundation on which all the machine's intelligence is built: it can now know, not just assume, its state.

**Digital twin contribution:** the sensor models are added to the twin — the measurement layer that connects the physical machine to its digital model. The twin can now receive real measurements to compare against its predictions (Lesson 04), the basis for the residual analysis and fault detection that make the twin truly useful.

---

*Lesson 01 — Version 0.1 | Next: Lesson 02 — Cleaning the machine's senses (signal conditioning and filtering)*
