# Specifying the machine's actuator
## Module 07 · Lesson 02

*Knowing the force is not the same as specifying a buildable actuator. This lesson turns the force requirement into a complete cylinder specification — bore, rod, stroke, mounting, and the safety checks a real machine demands.*

---

## Why The Machine Needs This

The machine knows what force it needs (Lesson 01), but "a 50 mm cylinder" is not yet a buildable specification. A real actuator has a rod that must not buckle under load, a stroke that must reach the work envelope, a mounting that must transfer force without bending, a pressure rating that must exceed the working pressure with margin, and seals that must suit the fluid and temperature. Miss any of these and the machine fails in service — the rod buckles, the mount cracks, the seals leak.

The machine needs a *complete actuator specification*: every parameter pinned down and checked, so the cylinder can be ordered, mounted, and trusted. This is the engineering that produces the module's artifact — the Actuator Selection Report.

**Benchmark task supported:** Force-Controlled Interaction (a properly specified, structurally sound actuator is what lets the machine apply force reliably) and Precision Positioning (stroke and mounting rigidity set the machine's reach and accuracy).

---

## 1. The machine's problem

The force calculation gives a bore. But a cylinder that produces the right force can still fail for reasons the force equation never mentions:

- **The rod can buckle.** Under compressive extend load, a long thin rod can buckle like an overloaded column — a sudden, catastrophic failure unrelated to the force rating.
- **The stroke can be wrong.** Too short and the machine cannot reach its work envelope; too long and the rod is more prone to buckling and the cylinder is bulky.
- **The mounting can fail.** Force must transfer from the cylinder to the machine's frame. A poorly chosen mount bends, misaligns the rod, or cracks under cyclic load.
- **The pressure rating can be exceeded.** The working pressure must sit safely below the cylinder's rated pressure, with a design margin.
- **The seals can be wrong.** Seal material must suit the fluid (Module 03) and the temperature, or it swells, hardens, or leaks.

The machine's problem: convert the force requirement into a *complete, checked specification* that will not fail in any of these ways.

---

## 2. The concept: the complete cylinder specification

A buildable cylinder specification pins down every parameter the machine depends on:

**Bore** — sized for force (Lesson 01), with design factor. The workcell's is 50 mm.

**Rod diameter** — sized for buckling resistance and the area ratio. A thicker rod resists buckling but reduces the rod-side area (lowering retract force and raising retract speed). The workcell's 28 mm rod gives a sensible area ratio (~1.46) and ample buckling margin.

**Stroke** — sized for the work envelope. The workcell's 300 mm stroke covers its reach. Longer strokes need buckling re-checks because the effective column length grows.

**Mounting style** — how the cylinder attaches to the frame and transfers force. Common styles (flange, clevis, trunnion, foot) suit different load paths. A clevis or trunnion allows slight angular alignment; a rigid flange demands precise alignment but is stiffest. The machine chooses a mount that transfers its force without bending the rod.

**Pressure rating** — the cylinder's rated pressure must exceed the working pressure with a design factor. Working at 100 bar, the machine specifies a cylinder rated to ≥160 bar (1.6× design factor), so the relief setting (115 bar) and any transient stay well within the rating.

**Seal material** — chosen for the fluid and temperature. For ISO VG 46 mineral oil (Module 03) at bench temperatures, standard nitrile (NBR) seals suffice; higher temperatures or different fluids would demand Viton or other materials.

Together these form the Actuator Selection Report — the specification a supplier could fulfill and a builder could mount with confidence.

---

## 3. Mathematical model

**Buckling check (Euler column).** The compressive force a rod can carry before buckling:
$$F_{cr} = \frac{\pi^2 E I}{(K L)^2}, \quad I = \frac{\pi d^4}{64}$$

- $E$ = elastic modulus (steel ≈ 210 GPa)
- $I$ = second moment of area of the rod
- $d$ = rod diameter
- $L$ = effective column length (stroke + extension at full extension)
- $K$ = end-condition factor (1.0 pinned-pinned, 2.0 fixed-free worst case, 0.7 fixed-pinned)

For the workcell rod (28 mm, ~400 mm effective length), even the worst-case fixed-free condition gives $F_{cr} \approx 98\ \text{kN}$ — five times the 19.63 kN extend force. The rod is safe against buckling with large margin. The machine *checks* buckling even when it passes easily, because a long-stroke variant could fail it.

**Pressure rating with design factor.** The rated pressure must exceed the working pressure:
$$P_{rated} \geq k_p \cdot P_{working}, \quad k_p \approx 1.5\text{–}2$$
For the workcell: $P_{rated} \geq 1.6 \times 100 = 160\ \text{bar}$.

**Area ratio.** The ratio of bore to rod-side area sets the extend/retract asymmetry:
$$\phi = \frac{A_{bore}}{A_{rod}} = \frac{1963}{1348} = 1.46$$
This ratio appears in force (extend is 1.46× retract) and speed (retract is 1.46× extend) — a single number capturing the cylinder's asymmetry.

---

## 4. Visual explanation

![Capstone Architecture](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/capstone_architecture.svg)

*Figure: capstone architecture — see full diagram above.* (Subsystem 4, cylinder detail)

Picture the cylinder specification as a labeled drawing: bore and rod diameters as concentric circles, stroke as the travel length, the mounting as the interface to the frame, and the rod under compressive load as a column that must not buckle. A buckling chart — critical load vs. effective length — shows the workcell's operating point sitting far below the buckling curve, in the safe region, with the margin visible as the vertical gap. For a much longer stroke, the operating point would slide right along the curve toward the danger zone, showing why long-stroke cylinders need fatter rods.

---

## 5. Engineering example

**Why mounting style is a real decision, not a detail**

A cylinder that produces perfect force still fails if mounted wrong. Consider a cylinder pushing a load that is slightly misaligned with the cylinder's axis. A rigid flange mount transfers that side-load straight into the rod and seals, causing uneven wear, leaks, and eventually a bent rod. A clevis or trunnion mount, which allows slight pivoting, lets the cylinder self-align with the load path, sparing the rod the side-load.

For the workcell, the mounting choice depends on how the cylinder couples to the end-effector mechanism. If the load is always axial, a flange gives maximum rigidity (best for positioning accuracy). If there is any angular movement, a clevis protects the rod. This is a genuine engineering decision the Actuator Selection Report must record — the machine's force is only as reliable as the mount that transfers it.

---

## 6. Worked example

**The machine's primary cylinder specification.** Assemble the complete Actuator Selection Report for the workcell's primary cylinder.

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Type | Double-acting cylinder | linear force + position hold (Lesson 04) |
| Bore | 50 mm | force capacity 19.63 kN at 100 bar, margin for all tasks (L01) |
| Rod diameter | 28 mm | buckling margin (F_cr ≈ 98 kN ≫ 19.63 kN); area ratio 1.46 |
| Stroke | 300 mm | covers the work envelope |
| Mounting | Clevis or trunnion | allows slight alignment, protects the rod |
| Pressure rating | ≥ 160 bar | 1.6× the 100 bar working pressure |
| Seal material | Nitrile (NBR) | suits ISO VG 46 oil at bench temperature |
| Area ratio φ | 1.46 | extend 1.46× retract force; retract 1.46× extend speed |

*Buckling check:* $F_{cr} = \pi^2 \times 210\times10^9 \times (\pi \times 0.028^4/64) / (2.0 \times 0.4)^2 = 98\ \text{kN}$, against a 19.63 kN extend force — a safety factor of 5. ✓

*Pressure check:* 160 bar rating vs. 100 bar working (115 bar relief) — design factor 1.6. ✓

This table *is* the module artifact for the primary actuator. Every parameter is justified and checked. A supplier could quote it; a builder could mount it.

---

## 7. Interactive demonstration

```python
import math

def buckling_load_kn(rod_mm, effective_length_mm, K=2.0, E_gpa=210):
    """Euler critical buckling load for the machine's rod."""
    d = rod_mm / 1000
    L = effective_length_mm / 1000
    I = math.pi * d**4 / 64
    F_cr = math.pi**2 * (E_gpa*1e9) * I / (K*L)**2
    return F_cr / 1000   # kN

def spec_checks(extend_force_kn=19.63, working_bar=100):
    print(f"Buckling: F_cr = {buckling_load_kn(28, 400):.0f} kN vs "
          f"{extend_force_kn} kN extend  -> SF {buckling_load_kn(28,400)/extend_force_kn:.1f}")
    rated = 1.6 * working_bar
    print(f"Pressure: rated >= {rated:.0f} bar vs {working_bar} bar working -> OK")

spec_checks()
# How buckling margin shrinks with stroke
print("\nBuckling load vs. stroke (28 mm rod):")
for stroke in [300, 500, 800, 1200]:
    print(f"  {stroke} mm stroke: F_cr = {buckling_load_kn(28, stroke+100):.0f} kN")
```

Run it. The 28 mm rod is safe at 300 mm stroke, but the buckling load falls sharply as stroke grows — showing why long-stroke cylinders need fatter rods.

---

## 8. Coding exercise

Create `code/module07/cylinder_spec.py` that:

1. Performs the Euler buckling check for a given rod and stroke
2. Computes the area ratio and the pressure-rating requirement with design factor
3. Generates the complete Actuator Selection Report (spec table) for given requirements
4. Flags whether a proposed cylinder passes all checks (force, buckling, pressure)

This produces the module artifact and feeds the digital twin the cylinder's true parameters.

---

## 9. Knowledge check

1. Name four ways a correctly-force-sized cylinder can still fail in service.
2. What is buckling, and what cylinder parameters most affect it?
3. Why does the machine check buckling even when it passes with large margin?
4. Why might the machine choose a clevis mount over a rigid flange?
5. What is the area ratio, and what two cylinder behaviors does it govern?

---

## 10. Challenge problem

The machine is to be adapted for a long-reach task needing an 800 mm stroke, same 100 bar system, same 19.63 kN extend force.

**a)** With the existing 28 mm rod, compute the buckling load at 800 mm stroke (effective length ~900 mm, K = 2.0). Is it still safe against the 19.63 kN extend force?

**b)** If the buckling margin is now too small, what rod diameter restores a safety factor of at least 3? (Buckling load scales with d⁴.)

**c)** A fatter rod changes the area ratio. How does that affect the machine's retract force and speed?

**d)** State how the long-reach adaptation changes the Actuator Selection Report, and why stroke and rod diameter are coupled decisions.

---

## 11. Common mistakes

**Skipping the buckling check.** A cylinder rated for the force can still buckle if the rod is too thin for the stroke. Buckling is a separate failure mode from force rating — always check it.

**Ignoring mounting.** The mount transfers the machine's force to its frame. A wrong mount bends the rod, misaligns the seals, and fails under cyclic load. Mounting is a real design decision.

**Working too close to the pressure rating.** Specifying a cylinder rated exactly at the working pressure leaves no margin for the relief setting, transients, or spikes. Use a design factor of 1.5–2.

**Forgetting seal compatibility.** Seals must suit the fluid and temperature. The wrong material swells or hardens and leaks. Specify the seal for the actual operating conditions (Module 03).

---

## 12. Key takeaways

- A force-sized cylinder still needs a complete specification: rod, stroke, mounting, pressure rating, and seals — each a real failure mode if wrong.
- Buckling (Euler column) is a separate failure mode; the workcell's 28 mm rod gives a safety factor of ~5 at 300 mm stroke, but margin shrinks sharply with stroke.
- Pressure rating must exceed working pressure with a design factor (workcell: ≥160 bar for 100 bar working).
- The area ratio (1.46) governs both the extend/retract force asymmetry and the speed asymmetry.
- The complete specification is the Actuator Selection Report — the module's artifact, every parameter justified and checked.

---

## Machine Capability Added

> **Before this lesson the machine could not:** be built — its actuator was a force figure, not a complete, structurally-checked specification.
>
> **After this lesson the machine can:** be specified as a buildable, safe actuator — bore, rod, stroke, mounting, pressure rating, and seals, with buckling and pressure checks passed.

The machine now has a **complete, buildable actuator specification** — the Actuator Selection Report. You can convert a force requirement into a real cylinder that will not buckle, leak, or fail, and justify every parameter. This is what makes the machine's force capacity trustworthy in service.

**Digital twin contribution:** the cylinder's true geometric and structural parameters (bore, rod, stroke, area ratio, pressure rating) are finalized in the twin, replacing the placeholder values from Module 04. The twin now models the *specified* actuator, not a generic one — tightening every force and motion prediction.

---

*Lesson 02 — Version 0.1 | Next: Lesson 03 — The machine's real actuator behavior (friction, cushioning, and the twin)*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 07 (Actuators) of the Fluid-Powered Physical AI curriculum: "Specifying the machine's actuator". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("Specifying the machine's actuator", Module 07 — Actuators) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("Specifying the machine's actuator") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("Specifying the machine's actuator", Module 07 — Actuators) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
