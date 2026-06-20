# Module 08 — Problem Set

*Integrating the Machine's Hydraulic Circuit*

Work each by hand, then verify with the Module 08 code. All answers verified against the curriculum code.

> Every problem completes the **physical machine** — joining, sequencing, protecting, and validating it as one system.

---

## Section A — Becoming one circuit

**A1.** Trace the complete fluid path of the machine's circuit, reservoir to reservoir.

**A2.** Compute the pressure reaching the cylinder (pump 100 bar; drops: line 0.54, filter 1.0, valve 5.0 bar). What force is then available?

**A3.** Compute the idle power for closed-center (relief 115 bar) vs. open-center (5 bar drop) at 10.67 LPM.

**A4.** Why does the workcell accept the higher closed-center idle power?

---

## Section B — Sequencing

**B1.** Why is a pick-and-place task not a single motion? List its four steps.

**B2.** Why does the machine sequence its actuators rather than run them in parallel?

**B3.** Compute the time to position 150 mm (extend, 90.6 mm/s) and move 150 mm (retract, 131.9 mm/s).

**B4.** Compare hydraulic vs. programmed sequencing. Which does the workcell use and why?

---

## Section C — Failing safely

**C1.** What happens, step by step, when the machine loses power while holding a load?

**C2.** Compute the load-holding drift for a bare spool (0.05 LPM leak) vs. a pilot check valve (0.001 LPM), 50 mm bore.

**C3.** What pressure spike results from heating 0.3 L of trapped fluid by 10°C (β=0.0007/°C, B=1.5 GPa)?

**C4.** Why must fail-safe behavior be built into the circuit, not the controller?

---

## Section D — Energy and simulation

**D1.** Name the five phases of the machine's full task cycle and the four signals the simulation tracks.

**D2.** Compute the useful work per cycle (800 N load, 150 mm stroke each way) and the hold heat (2.04 kW, 1.0 s hold).

**D3.** What fraction of the per-cycle energy is useful work? What dominates the rest?

**D4.** At 13 cycles/min, what is the average heat load? Does the 40 L reservoir suffice for bench duty?

---

## Section E — The machine

**E1.** State what the Integrated Hydraulic Circuit artifact comprises.

**E2.** *Reflection:* In two sentences, what did the machine become in Module 08, and why is it the culmination of the physical machine?

---

## Solutions

<details>
<summary>Reveal (verified against Module 08 code)</summary>

**A1.** Reservoir → pump → pressure line → directional valve → actuator (cylinder) → return line → filter → reservoir.

**A2.** $P_{cyl} = 100 - 0.54 - 1.0 - 5.0 = 93.5$ bar. Force $= 93.5 \times 0.1 \times 1963 = 18{,}354$ N = 18.35 kN.

**A3.** Closed: $115 \times 10.67/600 = 2.05$ kW. Open: $5 \times 10.67/600 = 0.09$ kW.

**A4.** Closed-center locks the cylinder for precise position holding, which Precision Positioning requires; the idle heat is acceptable for intermittent bench duty.

**B1.** A task needs coordinated steps in order: position → grip → move → release. Wrong order fails (grips air, carries nothing, drops the load).

**B2.** With one pump, parallel operation shares flow, making each actuator's speed depend on the other's load (unpredictable). Sequencing gives each the full flow and a known speed, and enforces order.

**B3.** Position: $150/90.6 = 1.66$ s. Move: $150/131.9 = 1.14$ s.

**B4.** Hydraulic sequencing (sequence valves) fires on pressure — rigid, plumbing-fixed. Programmed sequencing (controller + sensors) waits for true completion — flexible and precise. The workcell uses programmed, because it is becoming intelligent.

**C1.** Power fails → spring-centered DCV closes (locks ports) → trapped fluid would leak past the spool → pilot-operated check valves block the leak → load stays held; port reliefs cap any shock spike.

**C2.** Bare spool: $0.05 \times 10^6/60/1963 = 0.42$ mm/s = 25.5 mm/min. Pilot check: $0.001 \times 10^6/60/1963 = 0.008$ mm/s = 0.5 mm/min.

**C3.** $\Delta P = 0.0007 \times 1.5\times10^9 \times 10 / 10^5 = 105$ bar. (Volume-independent for the spike magnitude; thermal relief required.)

**C4.** During a power loss the controller is unpowered and cannot act. Safety must come from passive circuit elements (springs, check valves, reliefs) that work with no power.

**D1.** Phases: startup → extend → hold → retract → stop. Signals: pressure, flow, position, force.

**D2.** Useful work $= 800 \times 0.15 \times 2 = 240$ J. Hold heat $= 2040 \times 1.0 = 2040$ J.

**D3.** Useful work is ~7% of the ~3320 J per cycle; the rest is heat, dominated by the closed-center hold (~62%).

**D4.** $3320 \times 13/60 = 719$ W ≈ 0.72 kW. Yes — the 40 L reservoir sheds this for intermittent bench duty.

**E1.** The complete ISO 1219 schematic (all four subsystems joined), the sequencing logic, the fail-safe protection design, and the validated full-task simulation with energy budget — the complete physical machine.

**E2.** The machine became one complete, integrated, fail-safe system, validated end to end through a full task cycle. It is the culmination because all four physical subsystems are now proven to work together as a whole — the physical machine made complete, ready for intelligence.

</details>

---

*Problem Set 08 — Version 0.1*
