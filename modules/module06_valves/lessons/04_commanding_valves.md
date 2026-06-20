# The machine takes commands from its brain
## Module 06 · Lesson 04

*The machine can direct, protect, and throttle its flow — but so far a human sets every valve by hand. This lesson connects the valves to a controller, giving the machine its first ability to be commanded electronically, and previews the smooth variable control that makes true precision possible.*

---

## Why The Machine Needs This

The machine now has full mechanical motion control — direction (Lesson 01), pressure safety (Lesson 02), speed (Lesson 03). But every one of those valves is, so far, set by a human hand. An intelligent machine cannot have a person flipping its valves. For autonomy, the machine's *brain* — an embedded controller — must command the valves directly: energize this solenoid to extend, center to hold, drive that output to set a speed.

This lesson does two things. First, it connects the on/off directional valve to the controller, giving the machine its first electronically commanded motion — the literal first line of embedded control code for the workcell. Second, it introduces the proportional valve, which replaces crude on/off switching with smooth, variable control — the upgrade path that makes genuine closed-loop Precision Positioning possible (Module 10).

**Benchmark task supported:** Precision Positioning (electronic command is the prerequisite for automatic, closed-loop positioning) and Autonomous Manipulation (a machine that takes commands from its brain is the start of autonomy).

---

## 1. The machine's problem

Everything the machine can do mechanically is useless for autonomy if a human must operate it. Consider the gap: the machine has a directional valve that extends, holds, and retracts — but those states are selected by energizing solenoids, and right now nothing energizes them automatically. The machine has no link between a *decision* ("extend now") and the *action* (current flowing to the solenoid).

There is a second, subtler problem. The on/off directional valve is binary: full speed or stopped, with nothing in between. Even with a flow control valve setting a fixed speed, the machine cannot *smoothly vary* its speed on the fly — it cannot ease into a target, slowing continuously as it approaches. For the precise, smooth motion that high-accuracy positioning demands, the machine needs *proportional* control: a valve whose opening varies continuously with an electrical command.

The machine's problem: bridge decision to action electronically, and upgrade from on/off to smooth, variable command.

---

## 2. The concept: from solenoid switching to proportional control

**Commanding the on/off valve.** The workcell's directional valve is shifted by solenoids — electromagnets that move the spool when energized. A controller commands the valve by switching current to each solenoid:

- Drive solenoid A on → spool shifts left → **extend**
- Both solenoids off → springs center the spool → **hold**
- Drive solenoid B on → spool shifts right → **retract**

The controller (an Arduino or similar) cannot drive a solenoid directly — solenoids need more current than a microcontroller pin provides — so a **driver** (a relay or, better, a MOSFET) sits between them. The microcontroller switches a small signal; the MOSFET switches the solenoid's current. A **freewheeling diode** across the solenoid protects the circuit from the voltage spike when the solenoid switches off (a solenoid is an inductor, and switching it off without a diode produces a damaging spike). This is the machine's first electronic command path: a digital output, through a driver, to a solenoid, producing motion.

**The proportional valve.** An on/off solenoid valve has two states. A **proportional valve** has infinitely many: its spool position varies *continuously* with the current through its solenoid. Instead of "open or closed," the machine commands "30% open" or "70% open," and the valve meters flow accordingly. This gives smooth, variable speed control from a single valve — no separate flow control valve needed, and the speed can change continuously during a motion.

The machine commands a proportional valve with a **PWM** (pulse-width-modulated) output: rapidly switching the output on and off at a varying duty cycle produces an effective average current that sets the spool position. The relationship between command current and resulting flow (the **I–Q curve**) is roughly linear but has **hysteresis** — the valve responds slightly differently going up versus down — which the machine's control must account for (Module 10).

For the baseline workcell, the **on/off DCV** is simpler and sufficient to demonstrate commanded motion. The **proportional valve** is the documented upgrade: it costs more and needs a current-control amplifier, but it buys the smooth, continuously variable motion that high-precision closed-loop positioning requires. The machine starts with on/off and grows into proportional.

---

## 3. Mathematical model

**On/off command — a digital state.** The on/off valve's command is discrete:
$$u \in \{-1, 0, +1\} \;\rightarrow\; \{\text{retract, hold, extend}\}$$
Simple, but the speed within each state is fixed (set by the pump and flow control valve).

**Proportional command — a continuous mapping.** The proportional valve maps command to flow continuously. The spool opening is proportional to command current:
$$A_{valve}(u) = A_{max} \cdot u, \quad u \in [-1, +1]$$
and the flow follows the orifice model (Module 04):
$$Q(u, \Delta P) = C_d \, A_{max}\, u \sqrt{\frac{2\,\Delta P}{\rho}}$$

This is exactly the valve model the digital twin already uses — the proportional valve is the *physical realization* of the variable-command valve model built in Module 04. The machine's twin was, in a sense, always modeling a proportional valve; this lesson connects that model to real hardware.

**PWM to current.** The controller's PWM output at duty cycle $d$ produces an average solenoid current:
$$I \approx d \cdot I_{max}$$
which sets the spool position. The machine chooses the PWM frequency high enough that the solenoid sees a smooth average, not individual pulses.

---

## 4. Visual explanation

> See figure: `assets/figures/system_pipeline.svg` (the COMMAND stage — where the brain meets the hydraulics)

Picture the machine's command path as a chain from decision to motion: the controller decides "extend," sets a digital output high, the MOSFET driver switches the solenoid current, the solenoid shifts the spool, and fluid flows to the cylinder. For the proportional valve, the chain carries a *level*, not just a switch: the controller sets a PWM duty cycle, which becomes an average current, which sets a spool position, which meters a proportional flow. The figure shows the COMMAND stage of the pipeline — the exact point where the machine's intelligence reaches into its hydraulics and makes them move. This is the boundary the whole curriculum has been building toward.

---

## 5. Engineering example

**The machine's first line of autonomy**

Up to this lesson, the workcell has been a hydraulic machine that a human operates. The moment a controller energizes a solenoid in response to a command, the machine crosses a threshold: it becomes a machine that *acts on instructions*. That is the seed of autonomy.

In practice, the workcell's first control program is simple — a serial command interface where typing "extend," "hold," or "retract" drives the corresponding solenoid through a MOSFET. It is humble, but it is the first time the machine's hydraulics respond to a digital decision rather than a human hand. Every autonomous capability to come — closed-loop positioning (Module 10), the task state machine, the full manipulation sequence — is built on this foundation: a brain that can command the valves. The machine has started to listen to itself.

---

## 6. Worked example

**The machine's first control sequence.** Write the command logic for a basic extend–hold–retract cycle on the on/off DCV, driven by serial commands.

The control logic (pseudocode, realized in the coding exercise):
```
on command "extend":   solenoid_A = ON,  solenoid_B = OFF   # spool left, P->A
on command "hold":     solenoid_A = OFF, solenoid_B = OFF   # spring center, locked
on command "retract":  solenoid_A = OFF, solenoid_B = ON    # spool right, P->B
```

Tracing a full cycle the machine executes on command:
1. Receive "extend" → energize solenoid A → cylinder extends at 90 mm/s
2. Receive "hold" → de-energize both → closed-center locks the cylinder (relief handles pump flow, Lesson 02)
3. Receive "retract" → energize solenoid B → cylinder retracts at 132 mm/s
4. Receive "hold" → de-energize both → locked again

This is the machine's first embedded control: decisions arriving as commands, becoming solenoid states, becoming motion. Crude (on/off, fixed speed), but it is the machine acting on instruction — the doorway to everything in Modules 9–12.

---

## 7. Interactive demonstration

```python
class WorkcellValveController:
    """The machine's first embedded control logic (on/off DCV)."""
    def __init__(self):
        self.solenoid_A = False
        self.solenoid_B = False

    def command(self, cmd):
        if cmd == "extend":
            self.solenoid_A, self.solenoid_B = True, False
            return "spool left (P->A): cylinder extends at 90.6 mm/s"
        elif cmd == "retract":
            self.solenoid_A, self.solenoid_B = False, True
            return "spool right (P->B): cylinder retracts at 131.9 mm/s"
        elif cmd == "hold":
            self.solenoid_A, self.solenoid_B = False, False
            return "spring center: cylinder locked (closed-center hold)"
        return "unknown command"

ctrl = WorkcellValveController()
for cmd in ["extend", "hold", "retract", "hold"]:
    print(f"  command '{cmd:8s}' -> {ctrl.command(cmd)}")
```

Run it. This is the logic of the machine's first control program — decisions in, solenoid states and motion out.

---

## 8. Coding exercise

Create `code/module06/valve_controller.py` that:

1. Implements the on/off DCV controller (extend/hold/retract → solenoid states)
2. Adds a proportional-valve controller: a command in [-1, 1] → flow via the orifice model (reuse Module 04's `orifice_flow`)
3. Demonstrates a smooth approach: ramp the proportional command down as the cylinder nears a target (preview of closed-loop control)
4. Simulates an extend–hold–retract sequence, printing the cylinder state over time

This is the machine's first control code — the bridge from the digital twin's valve model to real commanded motion.

---

## 9. Knowledge check

1. Why can't a human-operated machine be autonomous? What must change?
2. How does a controller command the on/off directional valve's three states?
3. Why is a MOSFET driver (and a freewheeling diode) needed between the microcontroller and the solenoid?
4. How does a proportional valve differ from an on/off valve, and what does it give the machine?
5. How does the proportional valve relate to the valve model already in the digital twin (Module 04)?

---

## 10. Challenge problem

The machine is to perform a smooth approach: extend at 90 mm/s, then continuously slow to 15 mm/s over the last 20 mm before a target, using a proportional valve.

**a)** With an on/off DCV and a fixed flow control valve, can the machine slow *continuously* during the approach? Why or why not?

**b)** With a proportional valve, describe how the command would change over the last 20 mm to slow smoothly.

**c)** The proportional valve has hysteresis (responds differently up vs. down). Why does this complicate precise positioning, and which module addresses it?

**d)** Explain how this lesson's proportional valve is the hardware that the Module 04 valve model was implicitly describing all along.

---

## 11. Common mistakes

**Driving a solenoid directly from a microcontroller pin.** The pin cannot supply the solenoid's current, and the inductive switch-off spike will damage the controller. A MOSFET driver and a freewheeling diode are mandatory.

**Expecting smooth motion from an on/off valve.** On/off valves are binary — full speed or stopped. Smooth, continuously varying speed needs a proportional valve. Do not expect proportional behavior from a switch.

**Ignoring proportional-valve hysteresis.** The I–Q relationship is not perfectly repeatable up versus down. Open-loop proportional control drifts; precise positioning needs feedback (Module 10) to compensate.

**Thinking the on/off valve is a dead end.** It is not — it is the simple, correct starting point that demonstrates commanded motion. The machine grows into proportional control when precision demands it; both use the same underlying valve model.

---

## 12. Key takeaways

- An intelligent machine cannot be hand-operated; its controller must command the valves electronically — the start of autonomy.
- The on/off DCV is commanded by switching solenoid current through a MOSFET driver (with a protective freewheeling diode); this is the machine's first embedded control.
- A proportional valve varies its opening continuously with command current, giving smooth variable speed from one valve — commanded by PWM.
- The proportional valve is the physical realization of the variable-command valve model already in the digital twin (Module 04).
- The baseline machine uses the simple on/off DCV; the proportional valve is the documented upgrade for high-precision closed-loop positioning (Module 10).

---

## Machine Capability Added

> **Before this lesson the machine could not:** be commanded electronically — every valve was set by a human hand, making autonomy impossible.
>
> **After this lesson the machine can:** take motion commands from its controller — extend, hold, retract driven by solenoid outputs — and has a clear upgrade path to smooth proportional control. The machine acts on instructions for the first time.

The machine now has **electronically commanded motion** — the first bridge between its brain and its hydraulics. Combined with the directional, pressure, and speed control of Lessons 01–03, the machine has complete, commandable motion control: the Motion Control Architecture that is this module's artifact. This is the foundation every autonomous capability in Modules 9–12 builds on.

**Digital twin contribution:** the valve controller logic is added to the twin, connecting the command layer to the existing valve and cylinder models. The twin can now simulate a *commanded* motion sequence (extend–hold–retract) end-to-end, and the proportional-valve model unifies with Module 04's variable-command valve model — the twin is now a controllable simulation, not just a passive one.

---

## Module 06 Artifact — Motion Control Architecture

The deliverable of this module is the **Motion Control Architecture** for the Smart Agricultural Workcell: the complete specification of how the machine directs, protects, throttles, and commands its motion — the 4/3 closed-center DCV, the relief and counterbalance valves, the meter-out flow control, and the command path from controller through driver to solenoid. It is Subsystem 3 of the final machine, and the layer Modules 09–10 will close the loop around.

---

*Lesson 04 — Version 0.1 | Module 06 lesson content complete. Next: Module 06 summary, exercises, code, and Lab 06.*
