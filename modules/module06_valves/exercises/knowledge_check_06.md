# Module 06 — Knowledge Check

*Controlling the Machine's Motion*

Attempt all before checking the key. Target: 8 of 10.

> Keep asking: what can the machine *do* now that it could not before?

---

## Conceptual

**Q1.** Why is the machine's power useless until it can be directed?

**Q2.** What does the closed-center spool give the machine in neutral?

**Q3.** Why is the relief valve what makes the closed-center hold *safe*?

**Q4.** Meter-in or meter-out for a load that assists the motion? Why?

**Q5.** Why must an intelligent machine command its valves electronically rather than by hand?

---

## Calculation

**Q6.** At 10.67 LPM, what are the machine's extend and retract velocities (bore 50 mm, rod 28 mm)?

**Q7.** During a closed-center hold at 115 bar and 10.67 LPM, how much power becomes heat?

**Q8.** For a 30 mm/s extend approach, what flow must the meter-out valve pass (rod-side return)?

**Q9.** A 1 kN overhauling load on the rod side (1348 mm²) — what counterbalance setting holds it with 30% margin?

---

## The machine

**Q10.** State the Module 06 Machine Capability Added, Benchmark Task Advanced, and Digital Twin Contribution (one sentence each).

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** Undirected flow can only push the cylinder one way until it stalls; the machine cannot retract, stop, or hold, so it cannot position anything.

**A2.** The closed-center spool blocks all ports, hydraulically locking the cylinder so the machine holds position precisely under load.

**A3.** The closed-center valve traps the running pump's flow; without the relief valve, pressure would spike until something burst. The relief caps the pressure by dumping the trapped flow to tank.

**A4.** Meter-out. An assisting load would run away from a metered-in supply (cavitating); meter-out restrains it by holding back the exiting fluid.

**A5.** Autonomy is impossible if a human must operate the valves; the controller must command them so the machine can act on its own decisions.

**A6.** Extend $= 10.67 \times 10^6/60/1963 = 90.6$ mm/s. Retract $= 10.67 \times 10^6/60/1348 = 131.9$ mm/s.

**A7.** $115 \times 10.67/600 = 2.05$ kW.

**A8.** $30 \times 1348 \times 60/10^6 = 2.43$ LPM.

**A9.** $1000/1348 \times 10 = 7.4$ bar load pressure; $\times 1.3 = 9.6$ bar counterbalance.

**A10.** Capability: complete commandable motion control (direct, protect, throttle, command). Benchmark: Precision Positioning advanced — the machine can move to a target from either side, hold under load, and slow to a controlled approach. Twin: the full motion-control layer (DCV, pressure, flow control, controller logic) was added, making the twin a controllable simulation.

**Scoring:** 8–10 → ready for Module 07. 5–7 → review Lessons 02 and 03. Below 5 → rework the module.

</details>

---

*Knowledge Check 06 — Version 0.1*
