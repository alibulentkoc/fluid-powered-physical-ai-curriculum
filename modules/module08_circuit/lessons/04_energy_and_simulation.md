# The machine, simulated end to end
## Module 08 · Lesson 04

*Every subsystem model is built; every component is integrated. This lesson combines them into one simulation of a complete task cycle — the digital twin executing a full job for the first time — and accounts for all the energy the machine uses. The physical machine, made whole.*

---

## Why The Machine Needs This

The machine has a model for each subsystem — pump (Module 05), valves (Module 06), cylinder (Module 07) — and an integrated circuit (Lessons 01–03). But these models have never run *together* through a complete task. A real machine does not execute one subsystem at a time; it runs them all at once, coupled, through startup, motion, holding, and stopping. The machine needs a single simulation that combines all its models and reproduces a full task cycle — because that is the only way to validate that the integrated machine actually works as a system, and the foundation the digital twin needs to predict, monitor, and eventually control the real machine.

The machine also needs to know its complete energy budget: how much power it draws, how much becomes useful work, and how much becomes heat — which sizes the reservoir and decides whether it needs a cooler. This lesson delivers both: the energy accounting and the integrated simulation, completing the physical machine.

**Benchmark task supported:** Precision Positioning (the integrated simulation validates the complete actuation path — the full Precision Positioning capability, end to end, as one system).

---

## 1. The machine's problem

Two related problems close out the physical machine.

**The validation problem.** Each subsystem model works alone, but do they work *together*? When the pump ramps up, the valve directs flow, the cylinder moves against friction and load, the closed-center valve holds, and the cylinder retracts — do the models couple correctly? Does the simulated machine reproduce the real machine's behavior through a complete cycle? Until the models run together through a full task, the machine's digital twin is a set of parts, not a working whole. The machine needs an integrated simulation.

**The energy problem.** The machine draws power from its motor, delivers some as useful work at the cylinder, and dissipates the rest as heat. For continuous duty, that heat must be shed, or the fluid overheats (Module 03). The machine needs a complete energy budget — power in, work out, heat generated — to size its reservoir and decide on a cooler. This budget is only meaningful for the *integrated* machine, since the heat comes from every subsystem's losses plus the idle behavior (Lesson 01).

The machine's problem: combine all subsystem models into one validated full-cycle simulation, and account for all the energy the integrated machine uses.

---

## 2. The concept: the integrated simulation and the energy budget

**The integrated simulation.** The machine's full-task simulation combines all three subsystem models into one time-domain run through a complete cycle: **startup → extend → hold → retract → stop.**

- **Startup:** the pump flow ramps from zero to 10.67 LPM (Module 05) over a brief transient.
- **Extend:** flow drives the bore side; the cylinder moves at 90.6 mm/s against friction and load (Modules 06, 07).
- **Hold:** the closed-center valve locks the cylinder; pump flow spills over the relief at 115 bar (Modules 05, 06).
- **Retract:** flow reverses to the rod side; the cylinder retracts faster (131.9 mm/s) due to the smaller area (Module 07).
- **Stop:** motion ceases; the machine returns to idle.

The simulation tracks pressure, flow, position, and force through the whole cycle — the four signals that describe the machine's complete behavior. This is the digital twin running a full job, the validation that the integrated machine works.

**The energy budget.** The machine's power accounting over a cycle:

- **Power in:** the motor's shaft power (2.15 kW at full load, Module 05).
- **Useful work:** the energy delivered to move the load through its stroke (force × distance).
- **Heat:** everything else — pump inefficiency (17%, Module 05), circuit pressure drops, friction (Module 07), and the closed-center idle heat during holds (~2 kW, Lesson 01).

For the workcell, the dominant heat source during a cycle with holds is the closed-center idle heat. The reservoir (40 L, Module 05) sheds this for intermittent bench duty; continuous duty would add a cooler. The energy budget tells the machine exactly how much heat it must handle.

---

## 3. Mathematical model

**Useful work per cycle.** The energy delivered to the load over the extend and retract strokes:
$$W_{useful} = F_{load} \cdot d_{extend} + F_{load} \cdot d_{retract}$$
For an 800 N load over a 150 mm stroke each way: $W = 800 \times 0.15 \times 2 = 240\ \text{J}$.

**Heat per cycle.** The largest term is usually the hold heat (closed-center idle):
$$Q_{hold} = P_{idle} \cdot t_{hold} = 2040\ \text{W} \times 1.0\ \text{s} = 2040\ \text{J}$$
plus the pump and friction losses during motion. The hold heat alone dwarfs the useful work — a key insight: a closed-center machine that holds spends far more energy holding than moving. This is why the center-condition choice (Lesson 01) dominates the energy budget.

**Reservoir heat-shedding.** The reservoir sheds heat to the air at a rate roughly proportional to its surface area and the temperature difference. For the workcell's intermittent duty, the 40 L reservoir keeps the fluid in range; the continuous-duty heat load (Lesson 01's ~1 kW average at 50% holding) approaches the point where a cooler is warranted:
$$\dot{Q}_{continuous} = P_{idle} \times \text{(fraction of time holding)}$$

**The coupled simulation.** The full-cycle simulation integrates the machine's state forward in time, at each step computing flow (pump), routing (valve), and motion/force (cylinder) together — the three models coupled into one. The result is the time history of pressure, flow, position, and force that describes the complete machine.

---

## 4. Visual explanation

![Digital Twin Workflow](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/digital_twin_workflow.svg)

*Figure: digital twin workflow — see full diagram above.* (the integrated twin)

The defining visual is the four-panel plot from the integrated simulation: **position, pressure, flow, and force**, each vs. time, across the full cycle. Position ramps up (extend), plateaus (hold), ramps down faster (retract), and flattens (stop). Pressure sits at the working level during motion and jumps to the relief setting (115 bar) during the hold. Flow to the cylinder is full during motion and zero during the hold. Force shows the extend push, the holding force, and the retract. Reading these four panels together, the machine's entire task is visible at a glance — the validation that all the subsystem models work as one. This plot *is* the integrated machine, on a screen.

---

## 5. Engineering example

**What the integrated simulation reveals that the parts could not**

Each subsystem model, alone, told a partial story. Only the integrated simulation reveals the *system* behaviors:

- The **hold dominates the energy budget.** The 1-second hold dumps ~2040 J of heat — nearly nine times the 240 J of useful work in the whole cycle. No subsystem model alone showed this; it emerges from combining the closed-center valve (Module 06) with the pump (Module 05) over a real task timeline.
- The **retract is faster than the extend**, so the machine returns quicker than it reaches — visible only when the cylinder's area asymmetry (Module 07) runs through the actual cycle.
- The **startup transient** briefly limits force until the pump reaches full flow — a coupling between pump dynamics and cylinder motion invisible in either model alone.

This is why integration is the climax of the physical machine: the whole behaves in ways the parts do not predict individually. The simulation is the tool that reveals the system, and the digital twin that will monitor and control the real machine (Modules 10–11) is built on exactly this integrated model.

---

## 6. Worked example

**The machine's complete cycle and energy budget.** Run the integrated simulation and account for the energy.

*Cycle (from the simulation):*
| Phase | Duration | Behavior |
|-------|----------|----------|
| Startup + extend | ~1.7 s | pump ramps, cylinder to 150 mm at 90.6 mm/s |
| Hold | 1.0 s | closed-center lock, pressure at 115 bar relief |
| Retract | ~1.1 s | cylinder to 0 at 131.9 mm/s |
| Stop | — | idle |
| **Total** | **~3.9 s** | full cycle |

*Energy budget per cycle:*
- Useful work: $800 \times 0.15 \times 2 = 240$ J
- Hold heat: $2040 \times 1.0 = 2040$ J
- Plus pump/friction losses during the ~2.8 s of motion: roughly $0.37\ \text{kW} \times 2.8\ \text{s} \approx 1040$ J
- **Total energy per cycle ≈ 3320 J**, of which only 240 J (~7%) is useful work.

The machine spends most of its energy on heat — dominated by the hold. At ~13 cycles/minute, the average heat load is ~0.7 kW, which the 40 L reservoir handles for bench duty. Continuous high-duty operation would justify a cooler. The integrated simulation and energy budget together confirm the machine works as a system and tell it exactly how much heat to manage — completing the physical machine.

---

## 7. Interactive demonstration


**▶ Interactive demo — Task-Sequence Stepper**

[Open this demo in a new tab ↗](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/demos/module08/task_sequencer.html)

This self-contained widget lets you explore the concepts of this module hands-on — adjust the inputs and watch the machine's numbers respond live, built from the same equations the tested code uses.

```python
# The machine's energy budget per cycle (conceptual)
def cycle_energy(load_N=800, stroke_mm=150, hold_s=1.0,
                 idle_kw=2.04, motion_loss_kw=0.37, motion_s=2.8):
    useful_J = load_N * (stroke_mm/1000) * 2          # extend + retract
    hold_heat_J = idle_kw * 1000 * hold_s
    motion_heat_J = motion_loss_kw * 1000 * motion_s
    total = useful_J + hold_heat_J + motion_heat_J
    return useful_J, hold_heat_J, motion_heat_J, total

useful, hold, motion, total = cycle_energy()
print(f"  Useful work:  {useful:6.0f} J  ({useful/total*100:.0f}%)")
print(f"  Hold heat:    {hold:6.0f} J  ({hold/total*100:.0f}%)")
print(f"  Motion heat:  {motion:6.0f} J  ({motion/total*100:.0f}%)")
print(f"  Total/cycle:  {total:6.0f} J")
print(f"\n  At 13 cycles/min: {total*13/60/1000:.2f} kW average heat load")
```

Run it. Most of the machine's energy is heat, dominated by the hold — the system insight that drives reservoir and cooler sizing.

---

## 8. Coding exercise

Complete `code/module08/integrated_simulation.py` (the module's centerpiece) so it:

1. Combines the pump (Module 05), valve (Module 06), and cylinder (Module 07) models into one time-domain simulation
2. Runs a full cycle: startup → extend → hold → retract → stop
3. Plots pressure, flow, position, and force vs. time (the four-panel figure)
4. Computes the energy budget per cycle (useful work vs. heat)

This is the digital twin executing a complete task — the integrated machine, simulated end to end.

---

## 9. Knowledge check


*Formative — unlimited attempts, immediate feedback; does not affect your grade.*

[Open the interactive quiz in a new tab ↗](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/quizzes/module08/knowledge_check_quiz.html)

Or work through the written questions below.

1. Why must the machine's subsystem models be run *together*, not just individually?
2. Name the five phases of the machine's full task cycle.
3. What four signals does the integrated simulation track, and why those four?
4. In the machine's energy budget, what dominates the heat — and why?
5. What fraction of the machine's per-cycle energy is useful work? What does the rest become?

---

## 10. Challenge problem

The workcell is run at continuous high duty: 18 cycles/minute, each with a 1.5 s hold.

**a)** What is the average heat load from the holds alone (closed-center idle 2.04 kW)?

**b)** Add the motion losses (~0.37 kW during ~2.8 s of motion per cycle). What is the total average heat load?

**c)** The 40 L reservoir sheds roughly 0.5 kW passively at bench conditions. Does the machine need a cooler at this duty? Size the cooler's required capacity.

**d)** Propose a circuit change (Lesson 01) that would dramatically cut the hold heat, and explain the tradeoff. (Hint: the center condition.)

---

## 11. Common mistakes

**Validating subsystems only individually.** Models that work alone can fail when coupled. The integrated simulation is what validates the machine as a system — it reveals behaviors (hold-dominated heat, startup coupling) the parts hide.

**Ignoring the hold in the energy budget.** For a closed-center machine, the hold often dominates the heat — far exceeding the useful work. Budgeting only the motion energy drastically underestimates the heat load.

**Under-sizing the reservoir/cooler for real duty.** The heat load scales with how often the machine holds. A duty cycle with frequent or long holds needs more cooling than the motion alone suggests.

**Treating the simulation as the real machine.** The integrated simulation is a *model* — useful and validated, but it predicts the real machine, which has parameter spread and unmodeled effects. The twin's value comes from comparing its prediction to the real machine (Module 11), not from being taken as ground truth.

---

## 12. Key takeaways

- The integrated simulation combines the pump, valve, and cylinder models into one full-cycle run — the validation that the machine works as a system.
- The full cycle is startup → extend → hold → retract → stop, tracking pressure, flow, position, and force.
- System behaviors emerge only from integration: the hold dominates the heat, the retract is faster than the extend, the startup transient briefly limits force.
- The energy budget shows most of the machine's energy becomes heat (~93%), dominated by the closed-center hold — which drives reservoir and cooler sizing.
- The integrated simulation is the digital twin executing a complete task — the foundation for the monitoring and control of Modules 10–11.

---

## Machine Capability Added

> **Before this lesson the machine could not:** be validated or understood as a complete system — its subsystem models had never run together through a full task.
>
> **After this lesson the machine can:** execute a complete task cycle in simulation (startup → extend → hold → retract → stop), with a full energy budget — the integrated machine, validated end to end.

The machine now exists as a **complete, validated, integrated system** — physically whole. You can simulate its entire task cycle with all subsystem models coupled, read its behavior in the four-panel plot, and account for every joule of its energy. This is the culmination of the physical machine: power, transport, motion control, and actuation, integrated and proven to work together.

**Digital twin contribution:** the integrated full-task simulation *is* the digital twin's coming-of-age — the pump, valve, and cylinder models unified into one system that executes a complete task and accounts for all energy. The twin can now predict the real machine's full behavior through a cycle, the foundation for the closed-loop control (Module 10) and fault detection (Module 11) to come.

---

## Module 08 Artifact — Integrated Hydraulic Circuit

The deliverable of this module is the **Integrated Hydraulic Circuit** for the Smart Agricultural Workcell: the complete ISO 1219 schematic joining all four physical subsystems (Lesson 01), the multi-actuator sequencing logic (Lesson 02), the fail-safe protection design (Lesson 03), and the validated full-task simulation with energy budget (this lesson). It is the complete physical machine — every hydraulic subsystem integrated, protected, and proven to work as one. Modules 09–12 now add the sensing and intelligence that make this physical machine autonomous.

---

*Lesson 04 — Version 0.1 | Module 08 lesson content complete. The physical machine is whole. Next: Module 08 summary, exercises, lab — then Modules 09–12 (sensing and intelligence).*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 08 (Circuit) of the Fluid-Powered Physical AI curriculum: "The machine, simulated end to end". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("The machine, simulated end to end", Module 08 — Circuit) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("The machine, simulated end to end") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("The machine, simulated end to end", Module 08 — Circuit) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
