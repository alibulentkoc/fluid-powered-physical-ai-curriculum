# The machine fails safely
## Module 08 · Lesson 03

*Every machine eventually faces a fault — a power cut, a blocked line, a runaway load. An intelligent machine is not one that never fails, but one that fails safely. This lesson designs the circuit so the machine protects itself and whatever it is holding when things go wrong.*

---

## Why The Machine Needs This

The integrated circuit (Lesson 01) works when everything is normal. But real machines face faults: the power fails mid-task, a line blocks, a load tries to run away, the fluid overheats. If the machine is holding a workpiece when its DCV loses power, what happens? Does it drop the load? Spike its pressure? Damage itself? An intelligent machine must answer these questions *by design* — the circuit must be arranged so that faults lead to safe outcomes, not catastrophes.

The machine needs circuit protection: check valves, relief placement, counterbalance, and thermal protection arranged so that the predictable faults all resolve safely. This is what makes the machine trustworthy enough to hold a real load and work near people.

**Benchmark task supported:** Force-Controlled Interaction and Autonomous Manipulation (a machine cannot be trusted to hold loads or work autonomously unless it fails safely — protection is the precondition for trust).

---

## 1. The machine's problem

Walk through the faults the machine will actually face:

**Power loss while holding a load.** The DCV is spring-centered (Module 06): lose power, and the springs return it to closed-center, locking the cylinder. Good — but the trapped fluid must not leak, or the load slowly sinks. And the pump stops, so any leak path drops the load. The machine needs the held load to *stay held* even with the power off.

**A runaway (overhauling) load.** If the machine lowers a load that gravity pulls, and a line fails or the valve opens too far, the load can run away — dropping instead of lowering (the meter-out problem from Module 06, now a circuit-level safety concern).

**Pressure spikes.** A cylinder hitting an end stop, or an external shock to a held load, spikes the pressure. Without protection, the spike bursts a hose or blows a seal.

**Overheating.** The closed-center idle heat (Lesson 01) and general inefficiency raise the fluid temperature. Unchecked, the fluid degrades and viscosity drops out of range (Module 03).

The machine's problem: arrange the circuit so each of these faults resolves safely — the load stays held, pressure stays capped, the load cannot run away, and the fluid stays in range.

---

## 2. The concept: layered circuit protection

The machine protects itself with several components, each guarding against a specific fault. Together they form layered protection.

**Pilot-operated check valves (load holding).** A check valve allows flow one way and blocks it the other. Placed at the cylinder ports, a *pilot-operated* check valve locks the cylinder's fluid in place — the load cannot sink even if the DCV leaks or the power fails — yet releases when the machine deliberately commands motion (a pilot pressure opens it). This is what keeps a held load held during a power loss. It is the key protection for the machine's most important fault.

**System and port relief valves (pressure spikes).** The system relief (Module 05) caps the pump's pressure. Additional *port relief* valves at the cylinder cap spikes caused by external shocks to a held load — a load slammed while the closed-center valve traps the fluid would spike the trapped pressure far above the system relief, so port reliefs protect the cylinder directly.

**Counterbalance valve (runaway loads).** For an overhauling load, a counterbalance valve (Module 06) holds a back-pressure that supports the load, letting it move only under deliberate command — preventing runaway even if a line fails.

**Thermal protection (overheating).** A thermal relief valve and adequate reservoir/cooler (Lesson 04) keep the fluid in its temperature range. Thermal relief dumps fluid if trapped fluid expands with heat (which would otherwise spike pressure in a blocked section).

**The power-loss design.** Combining these: when power fails while holding a load, the spring-centered DCV closes (locks the cylinder), the pilot-operated check valves hold the trapped fluid (load cannot sink), and the port reliefs cap any spike. The machine holds its load safely with no power — a fail-safe by design.

---

## 3. Mathematical model

**Load-holding leak-down (why check valves matter).** Without a check valve, a held load sinks as fluid leaks past the closed valve spool at leakage rate $Q_{leak}$. The sink velocity:
$$v_{sink} = \frac{Q_{leak}}{A_{bore}}$$
Even a small spool leakage of, say, 0.05 LPM gives $v_{sink} = (0.05 \times 10^6/60)/1963 = 0.42$ mm/s — the load creeps down 25 mm per minute. For a machine that must hold precisely, this is unacceptable. A pilot-operated check valve cuts $Q_{leak}$ to near zero, holding the load indefinitely.

**Port relief setting (spike protection).** The port relief must sit above the maximum normal holding pressure but below the cylinder's burst rating:
$$P_{hold,max} < P_{port\,relief} < P_{cylinder\,burst}$$
Typically set ~10–20% above the system relief, so it only acts on genuine spikes, not normal operation.

**Thermal expansion (why thermal relief).** Trapped fluid heated by $\Delta T$ expands; if it cannot escape, pressure rises steeply (the bulk modulus from Module 03):
$$\Delta P = \beta_{thermal} \cdot B \cdot \Delta T$$
where $\beta_{thermal}$ is the fluid's thermal expansion coefficient (~0.0007/°C) and $B$ the bulk modulus (~1.5 GPa). A 10°C rise in trapped fluid can spike pressure by ~100 bar — which is why blocked sections need thermal relief.

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (circuit protection layer)

Picture the protection components placed on the circuit like guards at each vulnerable point: pilot-operated check valves at the cylinder ports (holding the load), port relief valves bridging the cylinder ports to tank (capping spikes), the system relief at the pump (capping supply pressure), a counterbalance valve in the line to an overhauling load, and thermal relief on any section that can be blocked with trapped fluid. A fault-tree view shows each fault — power loss, spike, runaway, overheat — flowing down to a safe outcome via its guarding component. The machine's safety is visible as this layer of protection over the working circuit.

---

## 5. Engineering example

**The power-loss scenario, resolved**

The manifest poses the sharp question: what happens if the workcell's DCV loses power while the cylinder is extended under load? Trace it through the protected circuit:

1. Power fails → the spring-centered DCV returns to closed-center, blocking all ports.
2. The cylinder's fluid is now trapped, but a closed valve spool leaks slowly — without more protection, the load would sink.
3. The pilot-operated check valves at the cylinder ports block the leak path entirely — the trapped fluid cannot escape, so the load *stays held* at its position.
4. If the held load is shocked (someone bumps it), the port relief valves cap the resulting pressure spike, protecting the cylinder.

The result: on power loss, the machine *safely holds its load in place*, indefinitely, with no power and no drift. This is fail-safe design — the machine's response to its worst fault is the safe one, achieved by the circuit's arrangement, not by luck or by the controller (which is also unpowered). A machine that can be trusted to hold a load must fail safely, and this circuit does.

---

## 6. Worked example

**Designing the machine's load-holding protection.** The workcell must hold a positioned load with no drift, even on power loss. Specify and check the protection.

*Without protection — leak-down:* spool leakage ~0.05 LPM gives:
$$v_{sink} = \frac{0.05 \times 10^6/60}{1963} = 0.42\ \text{mm/s} = 25\ \text{mm/min}$$
Unacceptable — the load drifts visibly.

*With pilot-operated check valves:* leakage cut to ~0.001 LPM:
$$v_{sink} = \frac{0.001 \times 10^6/60}{1963} = 0.008\ \text{mm/s} = 0.5\ \text{mm/min}$$
Essentially held — 50× better, drift negligible over a task.

*Port relief setting:* hold pressure max ~100 bar, cylinder burst ~480 bar (3× the 160 bar rating). Set port relief at ~140 bar (above system relief 115 bar, well below burst). Caps shock spikes without nuisance tripping.

The machine's load-holding protection: pilot-operated check valves (hold the load, no drift) plus port reliefs at 140 bar (cap spikes). On power loss, the load stays put. The circuit is fail-safe.

---

## 7. Interactive demonstration

```python
def leak_down_velocity(leak_lpm, bore_mm=50):
    """How fast a held load sinks for a given leakage."""
    import math
    A = math.pi*(bore_mm/2)**2
    return leak_lpm * 1e6/60 / A   # mm/s

print("Load-holding drift vs. leakage:")
for leak, label in [(0.05, "bare spool"), (0.01, "good valve"),
                    (0.001, "pilot check valve")]:
    v = leak_down_velocity(leak)
    print(f"  {label:18s} ({leak:.3f} LPM): {v:.3f} mm/s = {v*60:.1f} mm/min")

print("\nThermal spike in trapped fluid (10 C rise):")
beta, B = 0.0007, 1.5e9
print(f"  dP = {beta * B * 10 / 1e5:.0f} bar  -> needs thermal relief")
```

Run it. The pilot check valve cuts drift from 25 mm/min to 0.5 mm/min, and trapped fluid heating shows why thermal relief is needed.

---

## 8. Coding exercise

Create `code/module08/circuit_protection.py` that:

1. Computes load-holding drift for various leakage rates (showing the check-valve benefit)
2. Sizes port relief settings (above hold pressure, below burst)
3. Computes thermal expansion pressure spikes in trapped fluid
4. Simulates the power-loss scenario: DCV closes, check valves hold, load stays put

This models the machine's safety layer, feeding the digital twin's fault analysis (Module 11).

---

## 9. Knowledge check

1. What four faults must the machine's circuit protection handle?
2. What happens, step by step, when the machine loses power while holding a load?
3. Why does a held load drift without a pilot-operated check valve, and how does the check valve fix it?
4. Why are port relief valves needed in addition to the system relief?
5. Why does trapped fluid need thermal relief?

---

## 10. Challenge problem

The machine is holding a 2 kN load extended, when a maintenance worker accidentally cuts system power.

**a)** Trace what happens to the load through the protected circuit. Does it stay held?

**b)** The held cylinder has a bore-side volume of 0.3 L. If the trapped fluid is heated 8°C by the warm environment, what pressure spike results, and what component prevents damage?

**c)** While power is off, the worker bumps the load, applying a shock. Which component protects the cylinder, and at what pressure does it act?

**d)** Explain why this fail-safe behavior must be achieved by the *circuit*, not by the controller. (Hint: what state is the controller in during a power loss?)

---

## 11. Common mistakes

**Relying on the closed-center valve alone to hold a load.** A closed valve spool leaks; the load drifts. Pilot-operated check valves are needed for true, drift-free holding.

**Forgetting port reliefs.** The system relief protects the supply, but a shock to a held load spikes the *trapped* cylinder pressure, which the system relief never sees. Port reliefs protect the cylinder directly.

**Ignoring thermal expansion in trapped sections.** Heated trapped fluid spikes pressure dramatically (the bulk modulus is large). Any section that can be blocked with trapped fluid needs thermal relief.

**Assuming the controller provides safety.** During a power loss, the controller is dead. Fail-safe behavior must be built into the *circuit* (springs, check valves, reliefs) so it works with no power and no software.

---

## 12. Key takeaways

- An intelligent machine is not one that never fails, but one that *fails safely* — by circuit design.
- The machine's faults — power loss, pressure spike, runaway load, overheating — each need a guarding component.
- Pilot-operated check valves hold a load with no drift, even on power loss (cutting drift from ~25 mm/min to ~0.5 mm/min).
- Port reliefs cap spikes to a held load that the system relief never sees; counterbalance prevents runaway; thermal relief protects trapped fluid.
- On power loss the spring-centered DCV closes and the check valves hold the load — fail-safe by the circuit, independent of the (unpowered) controller.

---

## Machine Capability Added

> **Before this lesson the machine could not:** be trusted with a real load — a fault could drop it, spike the pressure, or let it run away.
>
> **After this lesson the machine can:** fail safely — holding its load with no drift on power loss, capping pressure spikes, and preventing runaway, all by circuit design independent of the controller.

The machine now has **fail-safe circuit protection** — the precondition for trusting it with a real load and autonomous operation. You can trace each predictable fault to a safe outcome, and you have designed the power-loss response so the machine holds its load even with no power. This is what makes the machine's force and autonomy trustworthy.

**Digital twin contribution:** the protection components (check valves, port reliefs, counterbalance, thermal relief) and their fault responses are added to the twin. The twin can now model the machine's behavior under faults — load-holding drift, spike capping, the power-loss scenario — the basis for the fault detection of Module 11.

---

*Lesson 03 — Version 0.1 | Next: Lesson 04 — The machine's complete energy budget and full-task simulation*
