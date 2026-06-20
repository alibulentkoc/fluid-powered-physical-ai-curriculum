# The machine closes every loop
## Module 12 · Lesson 02

*A commissioned machine can move and sense, but open-loop. This lesson activates the closed loops on the complete machine — position control, grip control, the full task sequence — with the twin watching live, turning the commissioned machine into an integrated, autonomous one.*

---

## Why The Machine Needs This

The commissioned machine (Lesson 01) works as one system, but its loops are not yet closed on the integrated hardware. The PID was tuned in simulation (Module 10); now it must run on the *real* complete machine, against the real valve's dead-band, the real friction, the real sensor noise — and meet spec there, not just in the twin. The task sequence (Module 10) must run end to end on the assembled machine. And the digital twin must connect to the *live* sensor stream, monitoring in real time rather than replaying logs.

The machine needs to close every loop on the complete hardware and confirm it performs to specification: the position step within <5% overshoot and <2 mm error, the task sequence completing without fault, the twin tracking live. This is the bridge from a commissioned machine to an autonomous one — the integration that makes the demonstrations possible.

**Benchmark task supported:** Precision Positioning (closed-loop position control on the real machine) and Autonomous Manipulation (the full task sequence running on the integrated hardware).

---

## 1. The machine's problem

The machine's control was designed and validated in simulation (Module 10), predicting <5% overshoot and <2 mm error. But simulation is not hardware. On the real machine, the valve's dead-band may differ slightly from the model, the friction may be higher, the sensor noise may disturb the loop — and the controller that met spec in the twin may overshoot, oscillate, or settle off-target on the real machine. The machine cannot assume its simulated tuning transfers perfectly.

There is also the integration of the *whole* control stack. The position loop, the grip-force loop, the task state machine, the safety logic, and the live twin must all run together, on real hardware, in real time. Each was tested in simulation; now they must coordinate on the physical machine — the state machine commanding the PID loops, the safety logic watching, the twin monitoring, all at once. Integration at this level surprises: timing issues, loop interactions, the twin lagging the live stream.

The machine's problem: close every control loop on the complete hardware, confirm the position control meets spec on the real machine (refining the simulation tuning as needed), run the full task sequence end to end, and connect the twin to the live stream — turning the commissioned machine into a working autonomous one.

---

## 2. The concept: closing the loops on hardware

**From simulated to real control.** The machine takes the PID gains tuned in the twin (Module 10) and runs them on the real cylinder. It then *confirms and refines* against the real step response:
- Run a position step (e.g., 200 mm), log the actual response.
- Measure the real overshoot, settling time, and steady-state error.
- If they meet spec, the simulation transferred well — the twin was faithful. If not, refine the gains on the real machine (a small adjustment, guided by the same symptom-reading from Module 10), and re-confirm.

Crucially, because the machine tuned in simulation first, this hardware tuning is a *small refinement*, not a blind search — the simulation got the machine close, and the real machine only needs minor adjustment. This is the payoff of simulation-first control: safe, fast convergence to a working tuning on hardware.

**Activating the full control stack.** With the position loop confirmed, the machine activates the rest:
- **Grip control** — the end-effector loop, regulating grip force (or position) the same way.
- **Task sequence** — the state machine (Module 10) drives the loops through the full task: approach → grip → lift → return, with sensor-confirmed transitions.
- **Safety logic** — the pressure/position limits and watchdog, active throughout.
- **Live twin** — the integrated twin (Module 11) connected to the real-time sensor stream, monitoring as the machine runs.

**The integration milestone.** The machine confirms integration when: the position step meets spec on hardware, and the task sequence completes without fault, repeatedly. This milestone certifies the machine as a working autonomous system — ready to demonstrate its benchmark tasks (Lesson 03).

**Real-time twin operation.** Unlike replay (Module 11), the live twin steps in lockstep with the running machine, fed the real-time sensor stream, producing predictions and residuals *as the machine operates*. This is the twin in its operational mode — watching the machine live, ready to flag a fault during a real task. The machine confirms the twin keeps pace with the live stream (no lag) and tracks the real machine (small residuals).

---

## 3. Mathematical model

**Hardware tuning refinement.** Starting from the simulation-tuned gains $\theta_{sim} = (K_p, K_i, K_d)$, the machine measures the real step response and adjusts:
$$\theta_{hw} = \theta_{sim} + \Delta\theta, \quad \Delta\theta \text{ small (refinement, not search)}$$
guided by the real symptoms (overshoot → more $K_d$ or less $K_p$; steady-state error → more $K_i$). The simulation-first approach makes $\|\Delta\theta\|$ small.

**Spec confirmation on hardware.** The machine confirms:
$$\text{overshoot}_{hw} < 5\%, \quad |\text{SSE}_{hw}| < 2\,\text{mm}, \quad t_{settle,hw} < 3\,\text{s}$$
measured from the real logged step — the capstone position spec.

**Task-sequence reliability.** The machine runs the full sequence $N$ times and confirms a fault-free completion rate:
$$\frac{\text{fault-free completions}}{N} \to 1 \quad (\text{target: 5/5 in commissioning})$$

**Live twin synchronization.** The real-time twin's prediction must track the live measurement with bounded residual and no growing lag:
$$|\varepsilon(t)| < \varepsilon_{threshold} \text{ and } \frac{d\,(\text{lag})}{dt} \approx 0$$
confirming the twin keeps pace operationally.

---

## 4. Visual explanation

> See figure: `assets/figures/system_pipeline.svg` (all loops active, the complete pipeline)

Picture the complete pipeline running with every loop closed: SENSE (sensors streaming) → UNDERSTAND (twin interpreting) → DECIDE (state machine sequencing) → COMMAND (PID computing) → ACTUATE (valves and cylinder moving) → VALIDATE (twin checking residuals), cycling continuously. The figure shows the full loop active — information flowing all the way around, the machine sensing, deciding, acting, and validating itself in one continuous cycle. Overlaid: the real step response meeting the spec band (<5% overshoot, settling within 2 mm), and the live twin's prediction tracking the measured position in real time. This is the complete machine with every loop closed — the integrated autonomous system, running.

---

## 5. Engineering example

**Why simulation-first makes hardware integration fast**

Imagine two teams integrating the same machine. The first never built a digital twin; they tune their control by trial-and-error directly on hardware. Each trial risks damage, takes time to set up, and the search is blind — they might spend days finding gains that work, with several near-misses that stress the machine. The second team tuned in simulation first (Module 10); they arrive at hardware integration with gains already close to right, needing only a small refinement against the real step response — and they confirm spec in an hour or two, safely.

The Smart Agricultural Workcell follows the second path, and this lesson is where it pays off. The simulation-first control (Module 10) and the validated twin (Module 11) mean the machine arrives at hardware integration already close — the twin predicted the real behavior, so the real tuning is a refinement, not a discovery. The whole curriculum's investment in a faithful twin converges here: integration is fast and safe *because* the machine understood itself in simulation first.

This is the professional reality of complex machine development: the simulation work front-loads the understanding, so hardware integration is confirmation and refinement, not blind struggle. The machine that knows itself in simulation integrates quickly in reality. The capstone demonstrates this directly — the loops close fast because the machine was designed to close them.

---

## 6. Worked example

**Closing the loops on the complete machine.** Activate and confirm the full control stack.

*Position loop on hardware:*
| Metric | Simulation | Hardware (with real friction) | Spec | Pass? |
|--------|-----------|-------------------------------|------|-------|
| Overshoot | 0.0% | ~1.5% | <5% | ✓ |
| Steady-state error | ~0.0 mm | ~1.7 mm | <2 mm | ✓ |
| Settling time | ~2.0 s | ~2.5 s | <3 s | ✓ |

The velocity-mode servo nulls the error cleanly in simulation; on real hardware, unmodeled friction and sensor noise add a small overshoot and steady-state error, but the response stays well within spec — the simulation tuning transferred with only minor real-world degradation. No re-tuning needed.

*Task sequence:* run approach → grip → lift → return five times. All five complete without fault. ✓ (milestone met)

*Live twin:* connected to the real-time stream; predicted position tracks measured within ~2 mm, no growing lag. ✓

*Integration milestone reached:* position control meets spec on hardware, the task sequence completes reliably, and the twin monitors live. The commissioned machine is now an *integrated autonomous machine* — every loop closed, performing to specification, watched by its twin. It is ready to demonstrate its benchmark tasks (Lesson 03).

---

## 7. Interactive demonstration

```python
def confirm_integration(overshoot_pct, sse_mm, settle_s,
                        task_runs_ok, twin_residual_mm):
    """Confirm the complete machine meets the integration milestone."""
    checks = {
        "position overshoot <5%": overshoot_pct < 5,
        "steady-state error <2mm": abs(sse_mm) < 2,
        "settling time <3s": settle_s < 3,
        "task sequence 5/5": task_runs_ok == 5,
        "twin tracks live <5mm": twin_residual_mm < 5,
    }
    for name, ok in checks.items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    return all(checks.values())

print("Integration milestone check (complete machine):")
ok = confirm_integration(overshoot_pct=1.5, sse_mm=1.7, settle_s=2.5,
                         task_runs_ok=5, twin_residual_mm=2.0)
print(f"\n  Machine integrated and ready to demonstrate: {ok}")
```

Run it. The complete machine confirms every integration criterion — loops closed, spec met, twin live.

---

## 8. Coding exercise

Create `code/module12/integration.py` that:

1. Runs the closed-loop position step on the (simulated) complete machine and measures the spec metrics
2. Runs the full task sequence multiple times and reports the fault-free rate
3. Connects the twin in live mode and confirms it tracks within tolerance
4. Confirms the integration milestone (all criteria met)

This is the machine closing every loop — the bridge from commissioned to autonomous.

---

## 9. Knowledge check

1. Why might the simulation-tuned controller need refinement on real hardware?
2. Why is the hardware tuning a *refinement* rather than a blind search?
3. What does the machine activate, in order, to close the full control stack?
4. What two conditions define the integration milestone?
5. How does the live twin differ from replay mode?

---

## 10. Challenge problem

The machine's simulation-tuned controller (0.6% overshoot in the twin) shows 7% overshoot on hardware — exceeding the 5% spec.

**a)** Is this a small or large discrepancy? What does it suggest about the twin's fidelity?

**b)** Which gain would the machine adjust to reduce the overshoot, and in which direction?

**c)** Why is this hardware refinement still fast and safe, given the simulation-first approach?

**d)** How would the machine use the 7%-vs-0.6% discrepancy to *improve* the twin for future work (connect to Module 11's parameter estimation)?

---

## 11. Common mistakes

**Assuming simulation tuning transfers perfectly.** Real hardware has unmodeled effects; the simulated tuning needs confirmation and possibly a small refinement. Always confirm on hardware.

**Re-tuning from scratch on hardware.** The simulation got the machine close; a blind hardware search wastes the simulation work and risks the machine. Refine from the simulated gains, guided by the real symptoms.

**Closing the loop before confirming the sensors (again).** As in commissioning, a bad sensor makes the loop chase phantoms. Confirm sensing before relying on it in the closed loop.

**Skipping the repeated task-sequence test.** One successful run is not reliability. Run the sequence several times to confirm it completes without fault before demonstrating.

---

## 12. Key takeaways

- A commissioned machine still has open loops; integration closes them on the real hardware and confirms spec there.
- Simulation-tuned control transfers to hardware as a small *refinement*, not a blind search — the payoff of simulation-first design.
- The machine activates the full stack in order: position loop → grip loop → task sequence → safety → live twin.
- The integration milestone is met when the position step meets spec on hardware and the task sequence completes reliably, with the twin tracking live.
- The live twin steps in lockstep with the running machine — the operational mode that watches for faults during real tasks.

---

## Machine Capability Added

> **Before this lesson the machine could not:** run its loops closed on the complete hardware, or perform its task sequence autonomously on the integrated machine.
>
> **After this lesson the machine can:** run every control loop closed on the real complete machine — meeting the position spec, completing the task sequence reliably, with the twin monitoring live.

The machine is now an **integrated autonomous system** — every loop closed on real hardware, performing to specification, watched by its live twin. You can confirm the machine's control meets spec on hardware, run its full task sequence reliably, and connect the twin in real time. This is the working autonomous machine, ready to demonstrate its benchmark capabilities.

**Digital twin contribution:** the twin now runs in its *operational* mode — connected to the live sensor stream, tracking the running machine in real time, ready to flag faults during actual tasks. The twin has progressed from a replay tool to a live monitoring instrument running alongside the operating machine, its ultimate role.

---

*Lesson 02 — Version 0.1 | Next: Lesson 03 — Demonstrating the machine's autonomous tasks*
