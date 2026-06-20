# How much power the machine actually delivers
## Module 05 · Lesson 03

*The machine's pump promises flow and pressure — but it never delivers all the power put into it. This lesson is about the gap between what the motor supplies and what the machine actually gets, and why that gap decides the motor size.*

---

## Why The Machine Needs This

The machine's motor spins the pump, and the pump delivers hydraulic power to do work. But some of the motor's effort is always lost — to internal leakage and to friction. If the machine ignores these losses, it will undersize its motor, and the workcell will stall under load, unable to position anything. Precision Positioning is impossible if the machine cannot reliably deliver the power its motions demand.

So the machine needs an honest accounting: how much power actually reaches the fluid, how much is lost, and therefore how big the motor must be. Efficiency is not an abstract figure of merit here — it is what determines whether the machine's power source is adequate.

**Benchmark task supported:** Precision Positioning (the machine cannot position reliably unless it delivers enough real power to move its load at the commanded speed).

---

## 1. The machine's problem

The machine needs to move its cylinder at a commanded speed against a load — say, 90 mm/s while exerting several kilonewtons. That requires a definite amount of hydraulic power reaching the cylinder. The motor must supply that power *plus* whatever is lost on the way.

Here is the trap: if the machine sizes its motor on the ideal hydraulic power alone, the motor will be too small. Under real load, internal leakage steals flow and friction steals torque, so the motor must work harder than the ideal suggests. An undersized motor bogs down, the pump slows, flow drops, and the machine fails to hit its commanded speed — Precision Positioning collapses.

The problem this lesson solves: quantify the machine's real power needs so its motor is correctly sized.

---

## 2. The concept: three efficiencies

The machine loses power in two distinct ways, captured by two efficiencies that combine into one.

**Volumetric efficiency ($\eta_v$)** — accounts for *flow* lost to internal leakage. Not all the fluid the pump should move actually reaches the outlet; some slips back past the gears, especially at high pressure. The machine gets less flow than displacement predicts.
$$\eta_v = \frac{Q_{actual}}{Q_{theoretical}}$$
Typical gear pump: 0.90–0.95. Falls as pressure rises (more leakage).

**Mechanical efficiency ($\eta_m$)** — accounts for *torque* lost to friction. The pump's bearings, gears, and seals rub; some of the motor's torque is spent overcoming that friction rather than pressurizing fluid. The machine must supply more torque than the ideal.
$$\eta_m = \frac{P_{ideal}}{P_{shaft\,for\,torque}}$$
Typical gear pump: 0.88–0.93.

**Overall efficiency ($\eta_o$)** — the total picture, the product of the two:
$$\eta_o = \eta_v \times \eta_m$$
For the workcell's pump: $0.92 \times 0.90 = 0.83$. The machine delivers about 83% of the motor's power to the fluid; 17% is lost as heat.

This is why the machine runs warm, and why the motor must be sized above the ideal hydraulic power.

---

## 3. Mathematical model

The machine's power accounting, start to finish.

**Hydraulic power delivered** (what reaches the fluid):
$$P_{hyd} = p \cdot Q_a$$
In working units: $P_{hyd}\,[\text{kW}] = \dfrac{p\,[\text{bar}] \times Q_a\,[\text{LPM}]}{600}$

**Shaft power required** (what the motor must supply):
$$P_{shaft} = \frac{P_{hyd}}{\eta_o}$$

The machine's motor must provide $P_{shaft}$, not $P_{hyd}$. The difference is the loss the machine must pay for.

> **The machine's power chain:**
> motor shaft power → (×$\eta_o$) → hydraulic power → moves the cylinder
> Sizing runs backward: required hydraulic power → (÷$\eta_o$) → required motor power.

---

## 4. Visual explanation

> See figure: `assets/figures/digital_twin_workflow.svg` (the pump model block)

Picture the machine's power as a flow that narrows at each loss. The motor supplies 100% at the shaft. Mechanical losses (friction) skim off ~10%. Volumetric losses (leakage) skim off another ~8%. What remains — about 83% — is the hydraulic power that actually moves the machine. A Sankey-style diagram shows the motor's power entering wide and the delivered power leaving narrower, with two loss streams branching off as heat. This picture is why the motor is bigger than the hydraulic output suggests.

A second key visual is the **efficiency-vs-pressure curve**: volumetric efficiency droops as pressure rises (leakage grows), so the machine is least efficient exactly when it works hardest. The digital twin needs this curve to predict the machine's real flow under load.

---

## 5. Engineering example

**Why efficiency sets the machine's running cost and heat**

Every watt the machine loses to inefficiency becomes heat in the fluid. That heat must be carried to the reservoir and shed, and it raises the fluid temperature (which, from Module 03, lowers viscosity and can push the fluid out of its safe window). A machine running at 83% efficiency turns 17% of its motor's power into heat continuously.

For the workcell, this connects three earlier decisions: the motor must be sized for the real (inefficient) power draw; the reservoir must be large enough to dissipate the loss heat (Lesson 04); and the fluid grade (Module 03) must tolerate the resulting temperature. Efficiency is not a number on a datasheet — it ripples through the whole machine's design. The machine that ignores efficiency overheats, underperforms, or both.

---

## 6. Worked example

**Sizing the machine's motor.** The workcell pump delivers 10.67 LPM actual at up to 100 bar. Volumetric efficiency 0.92, mechanical efficiency 0.90. What motor does the machine need?

Hydraulic power delivered:
$$P_{hyd} = \frac{100 \times 10.67}{600} = 1.78\ \text{kW}$$

Overall efficiency:
$$\eta_o = 0.92 \times 0.90 = 0.83$$

Shaft power the motor must supply:
$$P_{shaft} = \frac{1.78}{0.83} = 2.15\ \text{kW}$$

Adding a sensible margin for startup and transients, the machine relies on the motor's **service factor** — a standard motor rated 2.2 kW can continuously deliver $2.2 \times 1.15 = 2.53\ \text{kW}$, comfortably above the 2.15 kW demanded:
$$P_{motor} = \textbf{2.2 kW standard motor} \quad (2.53\ \text{kW with service factor} \geq 2.15\ \text{kW required})$$

This is the same motor frame established in Modules 01–02, now confirmed by the full efficiency accounting.

The machine's motor is sized on *real* power, not ideal. Had the machine used the 1.78 kW hydraulic figure, it would have chosen a 1.5 kW motor (service-factor capability ~1.7 kW) and stalled under load. Efficiency accounting is what makes the power source actually adequate.

---

## 7. Interactive demonstration

```python
def power_chain(pressure_bar, flow_lpm, eta_v=0.92, eta_m=0.90):
    """The machine's full power accounting."""
    p_hyd = pressure_bar * flow_lpm / 600          # kW delivered to fluid
    eta_o = eta_v * eta_m
    p_shaft = p_hyd / eta_o                          # kW the motor must supply
    p_lost = p_shaft - p_hyd                         # kW lost as heat
    return p_hyd, eta_o, p_shaft, p_lost

for p in [50, 80, 100, 120]:
    p_hyd, eta_o, p_shaft, p_lost = power_chain(p, 10.67)
    print(f"{p:3d} bar: deliver {p_hyd:.2f} kW | motor {p_shaft:.2f} kW | "
          f"lose {p_lost:.2f} kW as heat")
```

Run it. As the machine works harder (higher pressure), both the delivered power and the heat loss rise. The motor must cover the highest-pressure case the machine will face.

---

## 8. Coding exercise

Build the core of `code/module05/pump_performance_model.py`:

1. `hydraulic_power(pressure, flow)` and `shaft_power(p_hyd, eta_o)`
2. `volumetric_efficiency(pressure)` that droops with pressure (model the leakage trend)
3. A function that sizes the machine's motor from its peak operating point
4. A plot of delivered power, motor power, and heat loss vs. pressure

This is the power model the digital twin uses to predict the machine's real performance.

---

## 9. Knowledge check

1. What does volumetric efficiency account for? What does mechanical efficiency account for?
2. How do they combine into overall efficiency?
3. Why must the machine's motor be sized larger than the hydraulic power delivered?
4. What happens to the lost power? Why does that matter for the rest of the machine?
5. Why does volumetric efficiency fall as pressure rises?

---

## 10. Challenge problem

The machine is pushed to a harder duty: 120 bar at the same 10.67 LPM. At this higher pressure, volumetric efficiency drops to 0.88 and mechanical efficiency to 0.89.

**a)** Calculate the hydraulic power delivered at 120 bar.

**b)** Calculate the overall efficiency and the shaft power the motor must now supply.

**c)** Is the 2.2 kW motor still adequate, or must the machine step up a size?

**d)** The heat loss has increased. Connect this to two other subsystems of the machine that are affected (hint: reservoir, fluid).

---

## 11. Common mistakes

**Sizing the motor on hydraulic power.** The motor must supply *shaft* power, which is higher by 1/η_o. Sizing on the hydraulic figure undersizes the motor and the machine stalls.

**Treating efficiency as constant.** Volumetric efficiency falls with pressure. The machine is least efficient when working hardest — exactly when it most needs power. The twin must model this, not assume a fixed value.

**Forgetting the lost power becomes heat.** Inefficiency does not vanish — it heats the fluid, affecting viscosity, reservoir sizing, and fluid life. Efficiency couples to the whole machine.

**Confusing the two efficiencies.** Volumetric is about *flow* (leakage); mechanical is about *torque* (friction). They have different causes and different pressure dependence. Keep them distinct.

---

## 12. Key takeaways

- The machine never delivers all the power put into it: leakage costs flow (volumetric efficiency), friction costs torque (mechanical efficiency).
- Overall efficiency is their product; for the workcell pump, ~0.83 (about 17% lost as heat).
- Hydraulic power delivered is $P_{hyd} = p \cdot Q_a$; the motor must supply $P_{shaft} = P_{hyd}/\eta_o$.
- The workcell needs ~1.78 kW of hydraulic power at 100 bar, requiring a ~2.15 kW shaft input → a 2.2 kW motor.
- Efficiency ripples through the machine: it sets motor size, reservoir heat load, and fluid temperature.

---

## Machine Capability Added

> **Before this lesson the machine could not:** know how much real power its motions require, or how large a motor it needs.
>
> **After this lesson the machine can:** account for its power losses and size its motor on real shaft power (2.2 kW), guaranteeing it delivers enough power to position its load at the commanded speed.

The machine now has an **honest power budget**. You can compute the hydraulic power the workcell delivers, the losses it pays, and the motor it therefore requires — the accounting that makes the power source genuinely adequate rather than adequate-on-paper.

**Digital twin contribution:** the efficiency and power models are added to the twin — volumetric efficiency as a function of pressure, plus the hydraulic-and-shaft power calculation. The twin can now predict the machine's real delivered flow and power under load, not just its ideal values.

---

*Lesson 03 — Version 0.1 | Next: Lesson 04 — Designing the workcell's hydraulic power unit*
