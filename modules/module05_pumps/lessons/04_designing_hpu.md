# Designing the machine's power unit
## Module 05 · Lesson 04

*Every piece is now in hand: the pump, the flow, the efficiency, the motor. This lesson assembles them into the machine's actual Hydraulic Power Unit — the integrated subsystem that gives the workcell its power.*

---

## Why The Machine Needs This

The machine has the individual decisions — which pump, how much flow, how big a motor. But a pile of correct components is not a power unit. They must be integrated into one working subsystem: pump coupled to motor, drawing from a properly sized reservoir, protected by a relief valve, plumbed to feed the rest of the machine. Until this integration happens, the workcell still cannot operate.

This lesson produces the machine's **Hydraulic Power Unit (HPU) Design** — the artifact that becomes Subsystem 1 of the final Smart Agricultural Workcell. It is the moment the machine's power source stops being a set of calculations and becomes a buildable design.

**Benchmark task supported:** Precision Positioning (a complete, integrated power unit is what finally lets the machine move — the prerequisite for all positioning).

---

## 1. The machine's problem

The machine has a pump (8 cc/rev gear), a flow target (10.7 LPM), and a motor (2.2 kW). But consider what is still undecided. How big must the reservoir be to feed the pump without starving it and to shed the heat the machine generates? How is the motor coupled to the pump? Where does the relief valve go, and at what pressure? How do the pieces fit together into something that can be mounted, filled, and switched on?

A real machine needs these integration decisions resolved. A pump with no reservoir cavitates. A motor with no coupling cannot drive anything. A system with no relief valve destroys itself the first time the cylinder hits a hard stop. The machine's problem in this lesson: turn correct components into a coherent, safe, buildable power unit.

---

## 2. The concept: the hydraulic power unit

A **Hydraulic Power Unit (HPU)** is the integrated assembly that generates and conditions the machine's hydraulic power. For the workcell it comprises:

**Prime mover (motor)** — the 2.2 kW electric motor (Lesson 03), spinning at 1450 RPM. Converts electrical energy to shaft rotation.

**Pump** — the 8 cc/rev gear pump (Lessons 01–02), coupled to the motor shaft, converting rotation to flow.

**Coupling** — a flexible coupling joining motor to pump, tolerating slight misalignment and damping shock. Often the two are joined by a bell housing that also positions them precisely.

**Reservoir** — the tank holding the machine's fluid. It does four jobs: stores enough fluid to feed the pump, lets entrained air separate out, lets contaminants settle, and sheds the heat the machine's inefficiency generates (Lesson 03).

**Relief valve** — the machine's pressure safety. Set just above the operating pressure, it dumps flow back to tank if pressure climbs too high (a cylinder hitting a stop, a blocked line), protecting every downstream component.

**Filter and breather** — keeping the fluid clean (Module 03) and letting the reservoir breathe as fluid level changes.

Integrated, these form the machine's power source: a unit that draws clean fluid, pressurizes it safely, and feeds it to the rest of the workcell on demand.

---

## 3. Mathematical model

The integration decisions the machine must compute.

**Reservoir sizing.** The standard rule is 3–5× the pump's per-minute flow, giving fluid time to de-aerate and cool:
$$V_{reservoir} = k \cdot Q_a, \quad k = 3\text{–}5$$
For the workcell: $3 \times 10.67 = 32\ \text{L}$ to $5 \times 10.67 = 53\ \text{L}$. A **40 L reservoir** sits comfortably in range, giving good thermal margin for the machine's ~0.37 kW continuous heat load.

**Relief valve setting.** Above operating pressure, below component ratings:
$$P_{relief} = P_{operating} \times 1.1\text{–}1.2$$
For the workcell: $100 \times 1.15 \approx 115\ \text{bar}$. Set the machine's relief at ~115 bar — high enough not to nuisance-trip during normal 100 bar operation, low enough to protect the pump (rated ≥150 bar) and other components.

**Heat load check.** The continuous power lost to inefficiency (Lesson 03) must be dissipated by the reservoir (and a cooler if needed):
$$P_{heat} = P_{shaft}(1 - \eta_o) = 2.15 \times 0.17 \approx 0.37\ \text{kW}$$
A 40 L reservoir with normal surface area can shed this for intermittent bench duty; continuous heavy duty would add a cooler.

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (Subsystem 1, fully assembled)

Picture the machine's HPU as a single mounted assembly. At the base, the reservoir — a tank of oil. On top, the motor and pump joined by a bell housing, the pump's suction line reaching down into the tank, its pressure line rising to feed the machine. The relief valve sits at the pressure outlet, its return line dropping back to the tank. The filter sits in the return path; the breather caps the tank. This is the machine's power source as a physical object — the thing a student could mount on a bench and wire up. Every arrow of fluid traces from tank, through pump, out to the machine, and back.

---

## 5. Engineering example

**The HPU as the machine's foundation**

In any hydraulic machine, the HPU is built and commissioned first, because nothing else can be tested without it. The workcell follows the same logic: the HPU is Subsystem 1, the foundation the other subsystems plug into. Its design choices set hard limits on everything downstream — the flow it produces caps the machine's speed, the pressure it sustains caps the machine's force, the cleanliness it maintains protects the machine's valves.

This is why Module 05 comes where it does. The machine's architecture, fluid, and behavior models (Modules 01–04) had to come first to *specify* the HPU, but the HPU itself is the first physical subsystem the machine actually gets. After this lesson, the workcell has a power source — and the modules that follow give it the means to *use* that power: valves to direct it (06), actuators sized to it (07), a circuit to integrate it (08).

---

## 6. Worked example

**The machine's complete HPU specification.** Assemble every decision into the artifact.

| Parameter | Value | Source |
|-----------|-------|--------|
| Pump type | Gear, fixed displacement | Lesson 02 (mission match) |
| Pump displacement | 8 cc/rev | Lesson 01 (flow budget) |
| Motor speed | 1450 RPM | standard induction motor |
| Actual flow | 10.67 LPM | Lesson 01 |
| Operating pressure | 100 bar | system spec |
| Hydraulic power | 1.78 kW | Lesson 03 |
| Overall efficiency | 0.83 | Lesson 03 |
| Motor power | 2.2 kW | Lesson 03 (shaft power + margin) |
| Reservoir volume | 40 L | this lesson (≈4× flow, standard size) |
| Relief setting | 115 bar | this lesson (1.15× operating) |
| Heat load | ~0.37 kW | this lesson |
| Filter | β₁₀ ≥ 100, return line | Module 03 |
| Fluid | ISO VG 46 mineral | Module 03 |

This table *is* the Hydraulic Power Unit Design — the machine's power subsystem, fully specified and ready to build. Every number traces to a documented decision.

---

## 7. Interactive demonstration

```python
def design_hpu(flow_lpm, operating_bar, eta_o=0.83, k_reservoir=4):
    """Produce the machine's HPU design from its requirements."""
    p_hyd = operating_bar * flow_lpm / 600
    p_shaft = p_hyd / eta_o
    reservoir_l = k_reservoir * flow_lpm
    relief_bar = operating_bar * 1.15
    heat_kw = p_shaft * (1 - eta_o)
    return {
        "hydraulic_power_kW": round(p_hyd, 2),
        "motor_power_kW": round(p_shaft, 2),
        "reservoir_L": round(reservoir_l),
        "relief_setting_bar": round(relief_bar),
        "heat_load_kW": round(heat_kw, 2),
    }

design = design_hpu(10.67, 100)
for k, v in design.items():
    print(f"  {k}: {v}")
```

Run it. This function generates the machine's power unit design from its flow and pressure requirements — the HPU artifact, in code.

---

## 8. Coding exercise

Complete `code/module05/pump_performance_model.py` so it can:

1. Produce the full HPU design dictionary (as above)
2. Generate the pump's performance curves (flow vs. speed, efficiency vs. pressure, power vs. pressure)
3. Size the motor and reservoir from requirements
4. Export the HPU design as a formatted specification (the artifact)

This is the complete pump model the digital twin uses, and the tool that produces the module artifact.

---

## 9. Knowledge check

1. Name the components of the machine's HPU and the job of each.
2. Why does the reservoir need to be several times the pump's per-minute flow?
3. How is the relief valve setting chosen relative to operating pressure?
4. Why must the HPU be the first physical subsystem the machine gets?
5. What three downstream limits does the HPU design set for the machine?

---

## 10. Challenge problem

The workcell is to be deployed in a continuous-duty role (running hours at a time) rather than intermittent bench use, at 100 bar and 10.67 LPM.

**a)** The heat load is ~0.37 kW continuous. Will a 40 L reservoir alone keep the fluid in its safe temperature window indefinitely? What additional component might the machine need?

**b)** If a cooler is added, where in the HPU does it go, and what does it protect (connect to Module 03's viscosity window)?

**c)** Continuous duty may justify a larger reservoir. Recalculate the reservoir for k = 5. What does the extra volume buy the machine?

**d)** State how this changes the HPU Design artifact, and why the machine's *duty cycle* is a first-class design input.

---

## 11. Common mistakes

**Treating the HPU as loose parts.** A pump, motor, and tank are not a power unit until integrated — coupled, sized to each other, protected, and plumbed. Integration is the deliverable.

**Undersizing the reservoir.** Too small a tank starves the pump, fails to de-aerate the fluid, and overheats. The 3–5× rule exists to give the machine thermal and air-separation margin.

**Forgetting the relief valve.** Without it, the first pressure spike (a cylinder bottoming out) destroys the pump. The relief valve is not optional; it is the machine's pressure safety.

**Ignoring the heat load.** The machine's inefficiency becomes continuous heat. A power unit that cannot shed it will cook its own fluid. Size the reservoir (and cooler, if needed) for the heat the machine actually generates.

---

## 12. Key takeaways

- A pile of correct components is not a power unit; the HPU integrates pump, motor, coupling, reservoir, relief valve, and filter into one working subsystem.
- The machine's reservoir is sized at 3–5× pump flow (40 L for the workcell) to feed, de-aerate, and cool.
- The relief valve is set ~1.15× operating pressure (115 bar) to protect the machine without nuisance tripping.
- The HPU is the machine's first physical subsystem and sets hard limits on its speed, force, and reliability.
- The complete HPU specification is the module's artifact — Subsystem 1 of the Smart Agricultural Workcell.

---

## Machine Capability Added

> **Before this lesson the machine could not:** operate at all — its power components were specified but not integrated into a working subsystem.
>
> **After this lesson the machine can:** generate hydraulic power from a complete, integrated, safe Hydraulic Power Unit — pump, 2.2 kW motor, 40 L reservoir, 115 bar relief — ready to feed the rest of the workcell.

The machine now has a **complete power source**. The Hydraulic Power Unit Design is the workcell's Subsystem 1 — the foundation every other subsystem plugs into. This is the artifact that turns the machine from an idea with calculations into a buildable system with a real source of power.

**Digital twin contribution:** the full pump-and-power model — flow, efficiency, hydraulic and shaft power, and the HPU parameters (reservoir volume, relief setting) — is now a complete twin subsystem. The twin can predict the machine's flow, power, efficiency, and motor load across its operating range, giving the Module 04 cylinder simulation a realistic power source instead of an assumed constant supply.

---

## Module 05 Artifact — Hydraulic Power Unit Design

The deliverable of this module is the **Hydraulic Power Unit Design** for the Smart Agricultural Workcell: the complete specification table from the worked example (Section 6), justified by Lessons 01–04 and generated by `pump_performance_model.py`. It is Subsystem 1 of the final machine, and the foundation Modules 06–08 build on.

---

*Lesson 04 — Version 0.1 | Module 05 lesson content complete. Next: Module 05 summary, exercises, code, and Lab 05.*
