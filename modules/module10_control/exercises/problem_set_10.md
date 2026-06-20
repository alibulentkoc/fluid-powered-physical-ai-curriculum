# Module 10 — Problem Set

*Embedded Control — The Machine Decides and Acts*

Work each by hand, then verify with the Module 10 code. All answers verified against the curriculum code.

> Every problem builds the machine's **brain** — turning perception into precise, autonomous, safe action.

---

## Section A — Acting on perception

**A1.** Why does open-loop positioning give inconsistent results?

**A2.** Name the four steps of the closed-loop cycle.

**A3.** Name three reasons hydraulic control is harder than DC motor control.

**A4.** With proportional control ($K_p=0.02$/mm) holding against a load needing $u=0.06$, what is the steady-state error?

---

## Section B — The PID controller

**B1.** What does each PID term respond to?

**B2.** Which term eliminates steady-state error, and how?

**B3.** Which term damps overshoot, and how?

**B4.** What is integral windup, and how does anti-windup prevent it?

---

## Section C — State machine and safety

**C1.** Why can't a single PID loop run the machine's full task?

**C2.** Name the workcell's task states in order.

**C3.** Name the three safety checks and what each prevents.

**C4.** Why is the watchdog placed in the Arduino firmware, below the task logic?

---

## Section D — Simulation-first control

**D1.** Why is running untested control on hardware dangerous?

**D2.** How does the machine close the loop in simulation?

**D3.** What does comparing predicted to actual hardware response reveal?

**D4.** The tuned controller ($K_p=0.02, K_i=0.002, K_d=0.04$) — what overshoot and error does the simulation predict?

---

## Section E — The machine

**E1.** State what the Embedded Control System artifact comprises.

**E2.** *Reflection:* In two sentences, what did the machine gain in Module 10, and how does it complete Precision Positioning?

---

## Solutions

<details>
<summary>Reveal (verified against Module 10 code)</summary>

**A1.** Without feedback, friction, load, and temperature variation make the achieved position inconsistent, and the machine cannot correct it.

**A2.** Measure (read position) → compare (compute error) → compute (controller command) → act (drive valve), with feedback closing the loop.

**A3.** Square-root flow (orifice), valve dead-band, compressibility lag, load-dependent velocity (any three).

**A4.** $e_{ss} = u_{hold}/K_p = 0.06/0.02 = 3$ mm.

**B1.** P: present error; I: accumulated (past) error; D: rate of change of error.

**B2.** The integral — it accumulates the error over time, growing the command until the error is driven to zero.

**B3.** The derivative — it responds to how fast the error is shrinking, braking the approach to damp overshoot.

**B4.** When the valve saturates while error persists, the integral keeps accumulating to a huge value, causing massive overshoot when the error reverses. Anti-windup stops accumulating the integral while saturated.

**C1.** A single PID loop knows only "go to position X"; a task is a sequence of states with decisions and safety checks between them, requiring higher-level logic.

**C2.** IDLE → APPROACH → GRIP → LIFT → MOVE → RELEASE (→ IDLE), with FAULT reachable from any state.

**C3.** Pressure limit (prevents burst), position limit (prevents slamming the end stop), watchdog (returns to safe state if communication is lost).

**C4.** So it works independently of the Pi's task logic — if the Pi crashes or communication is lost, the Arduino still forces a safe state. Safety must survive a higher-level failure.

**D1.** A mis-tuned controller can slam the cylinder, oscillate violently, or spike pressure — with real force and real damage.

**D2.** It wraps the PID controller around the integrated machine model (Module 08), simulating the same closed loop the real machine runs, in software.

**D3.** Whether the twin accurately predicts the real closed-loop behavior — validating the twin and the controller, or revealing an unmodeled effect to refine.

**D4.** ~0.6% overshoot, ~1.2 mm steady-state error — meeting the <5%, <2 mm spec.

**E1.** The closed-loop PID controller, the autonomous task state machine, the safety logic, and the simulation-validated control design.

**E2.** The machine gained a validated control brain — perception turned into precise, autonomous, safe action. It completes Precision Positioning by achieving <5% overshoot and <2 mm error in closed-loop control, validated in simulation and confirmed on hardware.

</details>

---

*Problem Set 10 — Version 0.1*
