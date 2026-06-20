# Which pump the machine should use
## Module 05 · Lesson 02

*The machine needs to generate flow — but several kinds of pump could do it. This lesson is the machine's selection decision: which pump fits the workcell's mission, and why the others do not.*

---

## Why The Machine Needs This

The machine knows it needs a pump (Lesson 01). But "a pump" is not a decision — there are gear pumps, vane pumps, and piston pumps, each with different cost, robustness, pressure capability, and control. The machine must *choose*. The wrong choice burdens the workcell with cost and fragility it does not need, or starves it of capability it does.

This lesson is not a tour of pump types for their own sake. It is the engineering decision the machine's designer must make: given the workcell's mission — bench-scale, robust, affordable, ~100 bar, fixed flow — which pump is right, and why are the alternatives wrong for *this* machine?

**Benchmark task supported:** Precision Positioning (the pump's character — its flow stability and pressure capability — sets the quality of every motion the machine makes).

---

## 1. The machine's problem

The machine needs flow, and it has a specific operating envelope: around 100 bar of pressure, roughly 10 LPM of flow, a constant duty that does not need its flow varied on the fly, and a tight budget because the workcell is meant to be buildable and affordable. It also lives a bench life that may involve less-than-perfect fluid cleanliness.

Several pump families can generate flow. But a pump that is perfect for a 350 bar aircraft actuator is wrong for this machine — overcomplex, overpriced, overkill. A pump optimized for moving huge volumes of water at low pressure cannot build the workcell's pressure at all.

The machine's problem: choose the pump whose strengths match the workcell's mission and whose weaknesses do not matter here.

---

## 2. The concept: matching the pump to the mission

All the pumps the machine would consider are **positive-displacement** (Lesson 01 ruled out centrifugal — it cannot build hydraulic pressure). Within that family, three types are candidates. The machine evaluates each against its mission.

**Gear pump** — two meshing gears carry fluid around in their tooth pockets.
- *Strengths:* simple, cheap, rugged, tolerant of contamination, reliable fixed flow.
- *Weaknesses:* moderate efficiency, fixed displacement only, some flow pulsation, moderate maximum pressure (but well above the workcell's 100 bar).
- *Fit for the machine:* **excellent.** Robust and affordable, exactly matching a bench-scale agricultural machine that values reliability over peak performance.

**Vane pump** — a slotted rotor with sliding vanes sweeps fluid inside a cam ring.
- *Strengths:* quieter and smoother than gear pumps, can be made variable-displacement, good mid-pressure performance.
- *Weaknesses:* more complex, less contamination-tolerant, more expensive than a gear pump.
- *Fit for the machine:* acceptable but unnecessary. The workcell does not need its quietness or variable displacement, and it gives up some robustness.

**Piston pump** — pistons in a rotating barrel driven by a swashplate.
- *Strengths:* highest pressure (350+ bar), highest efficiency, precise variable displacement.
- *Weaknesses:* most complex, most expensive, least tolerant of contamination, demanding clean fluid and careful maintenance.
- *Fit for the machine:* **overkill.** Its high-pressure, high-efficiency, variable-flow capabilities are wasted on a 100 bar fixed-flow bench machine, while its cost and fragility actively hurt the mission.

The decision writes itself once the machine's mission is the criterion: the **gear pump** wins. Not because it is the "best" pump in the abstract — the piston pump is more capable — but because it is the best pump *for this machine*. The strengths it offers (robustness, low cost, reliable fixed flow) are exactly what the workcell needs; the strengths it lacks (variable displacement, extreme pressure) are exactly what the workcell does not.

---

## 3. Mathematical model

The selection is justified, but the machine must confirm the chosen gear pump can actually meet its numbers. Two checks:

**Pressure capability.** The gear pump's rated maximum pressure must exceed the workcell's operating pressure plus relief-valve margin:
$$P_{rated} \geq P_{operating} \times (1 + \text{margin})$$
For the workcell: $P_{rated} \geq 100 \times 1.2 = 120\ \text{bar}$. Standard gear pumps are rated 150–250 bar — comfortably sufficient.

**Flow capability.** The displacement and speed must deliver the required actual flow (Lesson 01):
$$Q_a = \frac{D \cdot n}{1000}\,\eta_v \geq Q_{required}$$
For the workcell: $\frac{8 \times 1450}{1000} \times 0.92 = 10.7 \geq 10\ \text{LPM}$. ✓

Both checks pass. The machine's gear pump selection is confirmed against its actual requirements, not just chosen by reputation.

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (Subsystem 1)

Picture the three candidate pumps side by side on a simple decision space: cost on one axis, capability (pressure and control sophistication) on the other. The piston pump sits high on both — expensive and highly capable. The gear pump sits low on both — cheap and adequately capable. The workcell's mission marker lands squarely in the gear pump's region: it needs modest capability at low cost. The figure makes the selection visible — the machine picks the pump whose region contains its mission, not the most capable pump available.

---

## 5. Engineering example

**Why the same machine class uses different pumps at different scales**

A small garden tractor uses a gear pump. A large agricultural harvester with precise hydrostatic drives uses piston pumps. Same broad domain — agriculture — different pump choices, because the *missions* differ. The harvester needs variable flow for smooth speed control and high pressure for heavy loads; the cost of piston pumps is justified by the machine's value and demands. The garden tractor needs robust, cheap, adequate flow; a gear pump is correct.

The Smart Agricultural Workcell is closer to the garden tractor in its needs: bench-scale, robust, affordable, modest pressure. The gear pump is the right call for the same reason. The lesson generalizes: you do not pick the most capable pump, you pick the pump whose profile matches the machine's mission.

---

## 6. Worked example

**Confirming the machine's pump choice.** The workcell requires 10 LPM actual flow at up to 100 bar, driven by a 1450 RPM motor, with a tight budget and bench-level fluid cleanliness. Evaluate the gear pump choice.

*Flow:* 8 cc/rev × 1450 RPM × 0.92 / 1000 = 10.7 LPM actual ≥ 10 LPM required. ✓
*Pressure:* gear pump rated ~200 bar ≥ 120 bar (100 + 20% relief margin). ✓
*Cost:* gear pump is the lowest-cost option. ✓ (matches tight budget)
*Robustness:* gear pump is the most contamination-tolerant option. ✓ (matches bench cleanliness)
*Control need:* workcell needs fixed flow; gear pump provides exactly that. ✓ (variable displacement not required)

Every check aligns. The machine's pump is an 8 cc/rev gear pump rated ≥150 bar. The selection is not a guess — it is the documented result of matching pump strengths to the workcell's mission.

---

## 7. Interactive demonstration

```python
def evaluate_pump(name, max_pressure_bar, rel_cost, contamination_tolerance,
                  variable_displacement,
                  req_pressure=120, budget="low", need_variable=False):
    """Score a pump against the workcell's mission. Higher score = better fit."""
    score = 0
    notes = []
    if max_pressure_bar >= req_pressure:
        score += 1
    else:
        notes.append("FAILS pressure requirement")
    if budget == "low" and rel_cost <= 2:
        score += 1
    elif budget == "low":
        notes.append("over budget")
    if contamination_tolerance >= 2:
        score += 1
    else:
        notes.append("needs cleaner fluid than bench provides")
    if variable_displacement and not need_variable:
        notes.append("variable displacement unused (wasted cost)")
    return name, score, notes

pumps = [
    evaluate_pump("Gear",   200, rel_cost=1, contamination_tolerance=3, variable_displacement=False),
    evaluate_pump("Vane",   175, rel_cost=2, contamination_tolerance=2, variable_displacement=True),
    evaluate_pump("Piston", 350, rel_cost=4, contamination_tolerance=1, variable_displacement=True),
]
for name, score, notes in pumps:
    print(f"{name:8s}: fit score {score}/3  {notes}")
```

Run it. The gear pump scores highest *for this machine's mission*. The piston pump's superior pressure does not help, while its cost and fragility hurt.

---

## 8. Coding exercise

Add a `recommend_pump()` function to `code/module05/pump_performance_model.py` that:

1. Takes the machine's mission (required pressure, flow, budget level, cleanliness, variable-flow need)
2. Scores each pump type against that mission
3. Returns the recommended pump with justification
4. Confirms the recommendation meets the flow and pressure checks numerically

The point is to make the *selection logic* explicit and reusable — the machine's reasoning, in code.

---

## 9. Knowledge check

1. Why are all the machine's candidate pumps positive-displacement (not centrifugal)?
2. Name the three positive-displacement pump types and one strength of each.
3. Why is the piston pump — the most capable — the wrong choice for the workcell?
4. What two numerical checks confirm a pump can meet the machine's requirements?
5. State the selection principle in one sentence (it is not "pick the best pump").

---

## 10. Challenge problem

A research team wants to upgrade the workcell to do smooth variable-speed precision tasks at up to 180 bar, with a generous budget and a commitment to high fluid cleanliness.

**a)** Does the gear pump still win for this *new* mission? Why or why not?

**b)** Which pump type now becomes attractive, and which mission requirement drives that?

**c)** What does the team give up (besides money) by switching to a piston pump?

**d)** State the general lesson: when does a more capable pump become the right choice?

---

## 11. Common mistakes

**Picking the "best" pump instead of the right pump.** The piston pump is objectively more capable, but capability the machine does not need is wasted cost and added fragility. Match the pump to the mission.

**Treating pump types as a taxonomy to memorize.** The point is not to recite pump types — it is to *choose* one for a specific machine. The types matter only as options in a decision.

**Ignoring the operating environment.** A bench machine with imperfect fluid cleanliness punishes contamination-sensitive piston pumps. The environment is part of the selection criteria, not an afterthought.

**Over-provisioning "to be safe."** A pump rated far beyond the machine's needs costs more, may run less efficiently at low load, and does not make the machine better. Size to the mission with sensible margin, not to the catalog maximum.

---

## 12. Key takeaways

- All the machine's candidate pumps are positive-displacement; the choice is among gear, vane, and piston.
- The machine picks the pump whose strengths match its mission, not the most capable pump available.
- For the workcell — bench-scale, robust, affordable, ~100 bar, fixed flow — the gear pump wins decisively.
- The piston pump is overkill: its high-pressure, high-efficiency, variable-flow strengths are wasted, while its cost and fragility hurt the mission.
- The selection is confirmed by two numerical checks: pressure rating ≥ operating + margin, and actual flow ≥ required flow.

---

## Machine Capability Added

> **Before this lesson the machine could not:** justify which pump it should use — "a pump" was an unmade decision.
>
> **After this lesson the machine can:** specify exactly which pump it uses (an 8 cc/rev gear pump rated ≥150 bar) and defend that choice against the alternatives on mission grounds.

The machine now has a **justified power-source selection**. You can choose the workcell's pump by matching pump strengths to the machine's mission, and confirm the choice meets the pressure and flow requirements numerically — a decision, not a default.

**Digital twin contribution:** the selected pump's defining parameters (gear type, 8 cc/rev displacement, rated pressure, nominal volumetric efficiency) are fixed as the configuration the twin's pump model will use — pinning down the model's identity before its performance curves are built in Lesson 03.

---

*Lesson 02 — Version 0.1 | Next: Lesson 03 — How much power the machine actually delivers (efficiency)*
