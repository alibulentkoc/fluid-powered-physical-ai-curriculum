# Cylinders and motors
## Module 02 · Lesson 03

*Cylinders convert fluid power into linear motion; motors convert it into rotation. These are the actuators — where pressurized fluid finally becomes useful mechanical work.*

---

## 1. Why this matters

The cylinder is the component that does the work the workcell exists to do. Everything upstream — pump, valves, hoses — exists to deliver pressurized fluid to this point, where it becomes force and motion.

In Module 01 you calculated cylinder forces and velocities treating the cylinder as an ideal device. This lesson opens the cylinder and shows you its real anatomy: the bore, the rod, the seals, the cushions, the mounts. Each feature has a purpose, and each has consequences for how the workcell performs and how long it lasts. You will also meet the cylinder's rotary cousin, the hydraulic motor, and learn when each is the right choice.

---

## 2. Physical intuition

A hydraulic cylinder is a tube with a piston inside. Pressurized fluid enters one end, pushes the piston, and the piston pushes a rod that sticks out through a sealed opening. That is the whole idea. The engineering is in the details that make it reliable.

A **double-acting cylinder** has fluid ports at both ends. Pressurize the bore (cap) end and the rod extends. Pressurize the rod end and it retracts. This is the workcell's primary actuator type — it can push and pull under power.

The rod side has less area than the bore side, because the rod itself occupies part of the cross-section. You already met the consequence in Module 01: for the same pressure, retract force is lower; for the same flow, retract speed is higher. This is the **differential effect**, and it is a direct result of the cylinder's geometry.

A **hydraulic motor** is, loosely, a pump run backward. Instead of mechanical rotation forcing fluid out, pressurized fluid forces the internals to rotate, producing a continuous output torque. Where a cylinder gives finite linear stroke, a motor gives unlimited rotation.

---

## 3. Mathematical foundations

### Cylinder force (recap and extension)

Extend force (bore side):
$$F_{ext} = p \cdot A_{bore} = p \cdot \pi \left(\frac{D}{2}\right)^2$$

Retract force (rod side):
$$F_{ret} = p \cdot A_{rod\text{-}side} = p \cdot \pi \left[\left(\frac{D}{2}\right)^2 - \left(\frac{d}{2}\right)^2\right]$$

where $D$ = bore diameter, $d$ = rod diameter.

### Hydraulic motor torque

A motor's output torque depends on its displacement and the pressure across it:

$$T = \frac{D_m \cdot \Delta p}{2\pi} \cdot \eta_m$$

- $T$ = output torque
- $D_m$ = motor displacement (volume per revolution)
- $\Delta p$ = pressure drop across the motor
- $\eta_m$ = mechanical efficiency

### Motor speed

$$n = \frac{Q \cdot \eta_v}{D_m}$$

Higher flow spins the motor faster; larger displacement spins it slower but with more torque. This is the rotary equivalent of the cylinder's force-velocity tradeoff.

> **Workcell relevance:** If the workcell's end effector is a rotating gripper or a tool spindle, a hydraulic motor sizes it. If it is a linear gripper or a lift, a cylinder sizes it. The same pressure and flow, two different actuator geometries.

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (Subsystem 4 — Actuation)

### Anatomy of a double-acting cylinder

From cap end to rod end:

- **Cap (blank) end** — sealed end with the bore-side fluid port
- **Barrel** — the precision tube the piston travels in
- **Piston** — the moving disc, carrying the piston seal
- **Piston seal** — prevents fluid crossing from one side to the other
- **Rod** — transmits force to the load
- **Rod-side port** — fluid port for the annular (rod) side
- **Rod seal and wiper** — prevent fluid leaking out and dirt getting in around the moving rod
- **Rod guide / bearing** — supports the rod against side loads
- **Cushions** (optional) — restrict flow near end of stroke to decelerate the piston smoothly, avoiding a hard slam
- **Mounts** — clevis, flange, or trunnion features that connect the cylinder to the structure and the load

Every one of these can fail or wear. The seals are the usual culprit. Contamination (Module 03) is the usual cause.

### Motor types (mirror the pump types)

- **Gear motor** — robust, cheap, moderate efficiency
- **Vane motor** — smoother, mid-range
- **Piston motor** — high torque, high efficiency, expensive

---

## 5. Engineering example

**Cylinder vs. motor in agricultural equipment**

Consider two attachments on the same tractor:

A **loader arm** uses cylinders. The motion is linear (raise/lower), finite in travel, and must hold position under load (a full bucket). A cylinder is ideal: it gives linear force directly, holds position when the valve closes, and the stroke matches the lift range.

An **auger** or **rotary cutter** uses a hydraulic motor. The motion is continuous rotation with no defined endpoint. A motor delivers sustained torque at speed, which a cylinder cannot do.

The workcell follows the same logic. Its primary positioning actuator is a **cylinder** — finite, linear, position-holding. Its end effector may be either: a linear gripper uses a small **cylinder**; a rotating tool head uses a small **motor**. The choice flows from the motion the task requires.

---

## 6. Worked example

**Problem:** The workcell's primary cylinder has a 50 mm bore and a 28 mm rod, operating at 100 bar.

Calculate: (a) extend force, (b) retract force, (c) the ratio of extend to retract force. Then (d): if the same cylinder were replaced by a hydraulic motor of 8 cc/rev displacement at the same 100 bar with 90% mechanical efficiency, what output torque would the motor produce?

**Solution:**

*(a) Extend force*
$$A_{bore} = \pi(25)^2 = 1963\ \text{mm}^2,\quad F_{ext} = 100 \times 0.1 \times 1963 = 19{,}630\ \text{N} = 19.6\ \text{kN}$$

*(b) Retract force*
$$A_{rod\text{-}side} = \pi(25^2 - 14^2) = \pi(625 - 196) = 1348\ \text{mm}^2$$
$$F_{ret} = 100 \times 0.1 \times 1348 = 13{,}480\ \text{N} = 13.5\ \text{kN}$$

*(c) Ratio*
$$\frac{F_{ext}}{F_{ret}} = \frac{19.6}{13.5} = 1.46$$

*(d) Motor torque*
$$T = \frac{D_m \cdot \Delta p}{2\pi}\eta_m = \frac{(8 \times 10^{-6}\ \text{m}^3) \times (100 \times 10^5\ \text{Pa})}{2\pi} \times 0.9 = \frac{80}{6.283}\times 0.9 = 11.5\ \text{N·m}$$

The cylinder gives linear force; the motor gives rotary torque. Same pressure, same displacement scale, different output type.

---

## 7. Interactive demonstration

```python
import math

def cylinder_forces(bore_mm, rod_mm, pressure_bar):
    a_bore = math.pi * (bore_mm/2)**2
    a_rod  = a_bore - math.pi * (rod_mm/2)**2
    f_ext = pressure_bar * 0.1 * a_bore / 1000
    f_ret = pressure_bar * 0.1 * a_rod / 1000
    return f_ext, f_ret

def motor_torque(disp_cc, dp_bar, mech_eff=0.9):
    return (disp_cc*1e-6 * dp_bar*1e5) / (2*math.pi) * mech_eff

f_ext, f_ret = cylinder_forces(50, 28, 100)
print(f"Extend: {f_ext:.1f} kN   Retract: {f_ret:.1f} kN   Ratio: {f_ext/f_ret:.2f}")
print(f"Motor torque (8cc, 100 bar): {motor_torque(8, 100):.1f} N·m")
```

Try varying the rod diameter. A thicker rod reduces the rod-side area, increasing the extend/retract force asymmetry — and increasing buckling resistance for long strokes.

---

## 8. Coding exercise

Write `code/module02/actuator_selector.py` that, given a required force (or torque), pressure, and motion type (linear or rotary), recommends:
- For linear: the minimum bore diameter (round up to the next standard size: 25, 32, 40, 50, 63, 80 mm)
- For rotary: the minimum motor displacement

Include a function that warns if a long-stroke cylinder may be at risk of buckling (rod length-to-diameter ratio > 10 as a simple flag — full Euler analysis comes in Module 07).

---

## 9. Knowledge check

1. What is the difference between a single-acting and a double-acting cylinder?
2. Why is the retract force always less than the extend force for a given pressure?
3. Name four internal components of a double-acting cylinder and state the function of each.
4. When would you choose a hydraulic motor over a cylinder?
5. Two motors receive the same flow. Motor A has twice the displacement of Motor B. Which spins faster, and which produces more torque?

---

## 10. Challenge problem

The workcell's end-effector task requires a rotating gripper that must apply 6 N·m of torque and complete a 90° rotation in 0.5 seconds.

**a)** At 80 bar with 90% mechanical efficiency, what motor displacement (cc/rev) delivers 6 N·m?

**b)** A 90° rotation in 0.5 s is 30 RPM (check this). What flow rate (LPM) spins the motor you chose in (a) at 30 RPM, assuming 92% volumetric efficiency?

**c)** Compare: could a linear cylinder driving a rack-and-pinion achieve the same rotation? What would be one advantage and one disadvantage versus the direct motor?

**d)** Which actuator would you specify for the workcell's rotating gripper, and why?

---

## 11. Common mistakes

**Treating the cylinder as just a tube.** The seals, rod guide, and cushions are what make it work reliably. A cylinder specified without attention to seal material (fluid and temperature compatibility) or rod guide (side-load capacity) will fail early.

**Ignoring the differential effect in design.** If a task needs equal force in both directions, a standard double-acting cylinder cannot provide it — extend is always stronger. Designs requiring symmetric force use double-rod cylinders (rod out both ends, equal areas).

**Sizing a motor by torque alone.** Torque sets the displacement, but you also need enough flow to achieve the required speed. A correctly torqued but flow-starved motor turns too slowly.

**Forgetting cushioning on fast cylinders.** A piston arriving at end of stroke at high speed slams the end cap. Cushions (or external deceleration via flow control) prevent shock damage. The workcell's fast motions need this consideration.

---

## 12. Key takeaways

- Cylinders produce linear motion and force; motors produce continuous rotation and torque.
- A double-acting cylinder pushes and pulls under power; the rod-side area is smaller, causing the differential effect (weaker but faster retract).
- Cylinder anatomy — barrel, piston, seals, rod guide, cushions, mounts — each feature has a purpose and a failure mode.
- Motor torque $T = D_m \Delta p / 2\pi \cdot \eta_m$; motor speed scales with flow over displacement.
- Choose a cylinder for finite linear motion with position holding; choose a motor for continuous rotation.
- The workcell's primary actuator is a cylinder; the end effector may use either, depending on the task.

---

*Lesson 03 — Version 0.1 | Next: Lesson 04 — The support system: reservoir, filter, hoses, fittings*
