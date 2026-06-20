# The machine becomes one circuit
## Module 08 · Lesson 01

*The machine has four working subsystems — but they are still four separate pieces. This lesson joins them into one complete hydraulic circuit, and makes the single design choice that governs how the whole machine behaves at rest.*

---

## Why The Machine Needs This

The machine now has a power source (Module 05), motion control (Module 06), and an actuator (Module 07) — every physical piece it needs. But they exist as separate designs. A machine is not a collection of correct components; it is those components *connected into one circuit* that carries fluid from the pump, through the valves, to the actuator, and back. Until they are joined, the machine cannot run as a whole.

Joining them is not just plumbing. The way the circuit is arranged — especially the center condition of the directional valve — determines how the entire machine behaves when idle: whether it wastes energy, generates heat, and holds position. The machine needs its subsystems integrated into one coherent circuit, with the topology chosen deliberately.

**Benchmark task supported:** Precision Positioning (the complete, integrated circuit is what finally lets the machine execute a full positioning motion from pump to rod — the whole actuation path validated as one system).

---

## 1. The machine's problem

Lay the four subsystems on the bench: the HPU (pump, motor, relief, reservoir), the valve block (DCV, flow control, pressure control), the cylinder, and the lines between them. Each works in isolation. But the machine cannot run until they are connected into a complete loop — fluid must have an unbroken path from the reservoir, through the pump, to the cylinder, and back to the reservoir.

And there is a decision hidden in how they connect. When the machine is idle — the valve centered, no motion commanded — what does the pump's flow do? The answer depends on the circuit's center condition, and it determines whether the idle machine wastes its full power as heat or sits efficiently. This is not a detail; it is the choice that governs the machine's energy behavior whenever it is not actively moving, which for a positioning machine is much of the time (every hold is an idle).

The machine's problem: connect the subsystems into one circuit, and choose the center condition that fits how the machine actually operates.

---

## 2. The concept: the complete circuit and its center condition

A hydraulic circuit is the complete fluid path: reservoir → pump → pressure line → directional valve → actuator → return line → filter → reservoir. The machine's four subsystems map onto this loop:

- **HPU (S1)** — the pump pushes fluid into the pressure line; the relief valve caps pressure; the reservoir stores and conditions the fluid.
- **Transport (S2)** — the lines and filter carry fluid to the valves and back.
- **Motion control (S3)** — the DCV directs flow; flow and pressure valves regulate it.
- **Actuation (S4)** — the cylinder converts the flow to force and motion.

**The center-condition decision.** The defining choice is what the DCV does in its neutral (centered) position, because that sets the idle behavior of the whole machine:

- **Open-center circuit:** in neutral, the pump's flow passes freely back to tank (P→T). The idle machine wastes little energy — the pump pushes against almost no pressure. But the cylinder is *not* locked; a load can move it.
- **Closed-center circuit:** in neutral, all valve ports are blocked. The cylinder is locked solid (precise holding), but the pump's flow is trapped and must spill over the relief valve — dumping the full pump power as heat during every idle.

This is the same closed-center vs. open-center tradeoff seen at the valve level in Module 06, but now its *system-wide* consequence is clear: the center condition sets the machine's idle energy behavior. The workcell chooses **closed-center** because Precision Positioning demands rock-solid holding, accepting the idle-heat cost (managed by intermittent duty and the reservoir). A continuous-duty machine might instead choose open-center, or add an unloading valve, to avoid the idle heat. The circuit topology is chosen to match how the machine operates.

---

## 3. Mathematical model

**Idle power, by center condition.** The power the machine consumes at rest depends entirely on the center condition:

*Closed-center idle* — pump flow spills over the relief at the relief pressure:
$$P_{idle} = \frac{P_{relief} \cdot Q_{pump}}{600} = \frac{115 \times 10.67}{600} = 2.04\ \text{kW (all as heat)}$$

*Open-center idle* — pump flow returns to tank at only the line/valve drop (a few bar):
$$P_{idle} = \frac{P_{drop} \cdot Q_{pump}}{600} = \frac{5 \times 10.67}{600} = 0.09\ \text{kW}$$

The difference is dramatic: closed-center wastes ~2 kW at idle, open-center ~0.09 kW. For a machine that holds position often, this is the central energy consequence of the topology choice — and the reason the center condition is "the single design choice that governs idle behavior."

**The complete pressure path.** The pressure reaching the cylinder is the supply minus every drop along the circuit (lines, filter, valve paths):
$$P_{cylinder} = P_{pump} - \Delta P_{lines} - \Delta P_{filter} - \Delta P_{valve}$$
Integrating the subsystems means summing these drops to confirm the cylinder still receives enough pressure to do its work — the machine's first whole-circuit pressure budget.

---

## 4. Visual explanation

![Capstone Architecture](https://alibulentkoc.github.io/fluid-powered-physical-ai-curriculum/assets/figures/capstone_architecture.svg)

*Figure: capstone architecture — see full diagram above.* (the complete circuit)

Picture the four subsystems joined into one loop. Fluid leaves the reservoir, the pump lifts it to system pressure, it travels the pressure line to the DCV, the DCV routes it to the cylinder (extend or retract), the returning fluid passes through the filter, and it drops back into the reservoir to shed heat and de-aerate. The relief valve branches off the pressure line, ready to cap pressure or handle trapped idle flow. This single closed loop is the machine as one system — the ISO 1219 schematic that is this module's artifact. Every component from Modules 05–07 appears in its place, connected.

---

## 5. Engineering example

**Why the center condition is a whole-machine decision, not a valve detail**

In Module 06, the closed-center choice looked like a valve-level decision about holding. Now, integrated, its true scope is visible: it sets the energy behavior of the *entire machine* whenever idle. A closed-center workcell holding position for 30 seconds dumps ~2 kW × 30 s = 60 kJ of heat into its fluid. Over a duty cycle with frequent holds, this dominates the machine's heat budget and drives the reservoir and cooler sizing (Lesson 04).

This is why integration matters: a decision that seemed local (how the valve holds) has system-wide consequences (idle energy, heat, reservoir size) that only become clear when the subsystems are joined. The machine's designer must see the whole circuit to understand the true cost of each choice. The workcell accepts the closed-center idle heat because its bench duty is intermittent and holding precision is worth more than idle efficiency — but that judgment requires the system view this module provides.

---

## 6. Worked example

**The machine's whole-circuit pressure budget.** Confirm the cylinder receives adequate pressure once all subsystems are connected. Pump 100 bar, 10.67 LPM. Drops: supply line ~0.54 bar (Module 03), filter ~1 bar, DCV ~5 bar total (Module 06).

*Pressure reaching the cylinder on extend:*
$$P_{cylinder} = 100 - 0.54 - 1.0 - 5.0 = 93.5\ \text{bar}$$

*Force available at the cylinder:* at 93.5 bar on the 1963 mm² bore:
$$F = 93.5 \times 0.1 \times 1963 = 18{,}354\ \text{N} = 18.35\ \text{kN}$$

The integrated circuit delivers 18.35 kN — down from the ideal 19.63 kN, the ~1.3 kN difference lost to the circuit's pressure drops. This is still far more than any task needs (Module 07), so the machine is well-margined. The whole-circuit budget confirms the integration works: every subsystem connected, and the cylinder still receives ample pressure to do its job.

---

## 7. Interactive demonstration

```python
def idle_power_kw(center, relief_bar=115, idle_drop_bar=5, flow_lpm=10.67):
    """The machine's idle power consumption by center condition."""
    p = relief_bar if center == "closed" else idle_drop_bar
    return p * flow_lpm / 600

def cylinder_pressure(pump_bar=100, line=0.54, filt=1.0, valve=5.0):
    """Pressure reaching the cylinder after circuit drops."""
    return pump_bar - line - filt - valve

print("Idle power by center condition:")
for c in ("closed", "open"):
    print(f"  {c}-center: {idle_power_kw(c):.2f} kW at idle")

pc = cylinder_pressure()
print(f"\nPressure reaching cylinder: {pc:.1f} bar")
print(f"Force available: {pc*0.1*3.14159*25**2/1000:.2f} kN "
      f"(vs 19.63 kN ideal)")
```

Run it. The center condition sets idle power (2 kW vs 0.09 kW), and the circuit drops cost ~1.3 kN of force — both consequences of integrating the subsystems.

---

## 8. Coding exercise

Create `code/module08/circuit_model.py` that:

1. Assembles the four subsystem models (pump, valve, cylinder) into one circuit
2. Computes the whole-circuit pressure budget (pump to cylinder, summing all drops)
3. Compares idle power for open-center vs. closed-center
4. Reports the force available at the cylinder after circuit losses

This is the integrated circuit model — the foundation for the full task simulation (Lesson 04).

---

## 9. Knowledge check

1. Why is a collection of correct subsystems not yet a machine?
2. Trace the complete fluid path of the machine's circuit, reservoir to reservoir.
3. What does the center condition of the DCV determine about the whole machine?
4. Compare the idle power of open-center vs. closed-center for the workcell.
5. Why does the cylinder receive less than full pump pressure in the integrated circuit?

---

## 10. Challenge problem

The workcell is being considered for continuous duty: holding position 50% of the time, with the pump always running.

**a)** With closed-center, how much heat does the machine generate during the holding (idle) half of its duty? (Use 2.04 kW at idle.)

**b)** With open-center, how much idle heat instead? What does the machine give up by switching to open-center?

**c)** Propose a third option (hint: an unloading valve) that keeps closed-center holding but avoids the idle heat. How does it work?

**d)** For the continuous-duty workcell, which center condition (or option) would you choose, and how does it change the reservoir/cooler sizing (preview of Lesson 04)?

---

## 11. Common mistakes

**Treating integration as just plumbing.** Connecting the subsystems involves real decisions — center condition, drop budget — with system-wide consequences. It is design, not assembly.

**Ignoring the circuit pressure drops.** The cylinder receives pump pressure *minus* every line, filter, and valve drop. Assuming full pressure reaches the cylinder overestimates the machine's force.

**Forgetting the idle-energy cost of closed-center.** A closed-center machine dumps its full power as heat whenever it holds. For frequent or long holds, this dominates the heat budget. Account for it in reservoir/cooler sizing.

**Choosing the center condition by habit.** Open-center and closed-center each fit different duties. The choice should follow how the machine actually operates (holding need vs. idle efficiency), not a default.

---

## 12. Key takeaways

- A machine is its subsystems *connected into one circuit*, not a collection of correct parts.
- The complete circuit is a loop: reservoir → pump → pressure line → DCV → actuator → return → filter → reservoir.
- The DCV center condition governs the whole machine's idle behavior: closed-center holds precisely but dumps full power as heat at idle; open-center is efficient at idle but does not lock the cylinder.
- The workcell uses closed-center for holding precision, accepting ~2 kW idle heat (managed by intermittent duty).
- The cylinder receives pump pressure minus all circuit drops (~93.5 bar of 100), still well-margined for its tasks.

---

## Machine Capability Added

> **Before this lesson the machine could not:** run as a whole — its four subsystems were separate designs with no complete fluid path between them.
>
> **After this lesson the machine can:** operate as one integrated circuit, with fluid flowing pump-to-cylinder-and-back, and an idle behavior chosen deliberately by its center condition.

The machine now exists as **one complete hydraulic circuit**. You can trace the whole fluid path, budget the pressure from pump to rod, and understand how the center-condition choice governs the machine's idle energy. This is the physical machine made whole — the foundation for sequencing, protection, and the full task simulation.

**Digital twin contribution:** the integrated circuit model is added to the twin — the four subsystem models (pump, valve, cylinder) connected into one, with the whole-circuit pressure budget. The twin can now represent the complete machine as a single system, the basis for simulating a full task cycle (Lesson 04).

---

*Lesson 01 — Version 0.1 | Next: Lesson 02 — How the machine sequences its actions (multi-actuator circuits)*


---

## AI Learning Companion

Copy any prompt below into Claude, ChatGPT, or another AI assistant.

**Tutor prompt** — explain it another way

```
Re-explain this lesson from Module 08 (Circuit) of the Fluid-Powered Physical AI curriculum: "The machine becomes one circuit". Teach it through the running machine — the Smart Agricultural Workcell — using physical intuition first, then the math. Keep hydraulic terminology precise.
```

**Practice prompt** — generate more exercises

```
Give me 5 practice problems for this lesson ("The machine becomes one circuit", Module 08 — Circuit) on the Smart Agricultural Workcell, with full worked solutions. Mix conceptual and numerical.
```

**Explore prompt** — connect it to the real world

```
Show me how this lesson's concept ("The machine becomes one circuit") appears in real agricultural, construction, or industrial hydraulic machines, with concrete examples and typical numbers.
```

## Global Learning Support

Need this lesson in another language? Copy a prompt below into an AI assistant. English remains the authoritative source.

**Supported languages (initial):** English · Español · 中文 (Simplified Chinese) · Türkçe

```
I just studied this lesson ("The machine becomes one circuit", Module 08 — Circuit) from the Fluid-Powered Physical AI curriculum.
Explain it in [Spanish / Simplified Chinese / Turkish]. Keep hydraulic and mathematical terminology in English where commonly used.
Then provide: a short summary, three practice questions, and one challenge problem.
```
