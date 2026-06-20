# Module 11 — Problem Set

*The Integrated Digital Twin*

Work each by hand or with the Module 11 code. All answers verified against the curriculum code.

> Every problem completes the machine's **self-awareness** — the integrated twin that mirrors, monitors, and manages the machine.

---

## Section A — The twin becomes whole

**A1.** What single criterion distinguishes a digital twin from a simulation?

**A2.** Name the three parts of a digital twin.

**A3.** Classify these as measured or inferred: position, friction coefficient, bore pressure, valve dead-band, supply flow.

**A4.** Name the four phases of the twin lifecycle.

---

## Section B — Running alongside

**B1.** What three mismatches must be resolved to synchronize log and twin?

**B2.** Describe the replay loop in four steps.

**B3.** A log is at 50 Hz, the twin steps at 100 Hz. What operation aligns them?

**B4.** Why must the twin be *fed* inputs but *predict* outputs?

---

## Section C — Watching over

**C1.** Why are developing faults often invisible to direct sensors?

**C2.** Give the residual signature of: a seal leak, a sensor drift, valve hysteresis.

**C3.** Why does a small healthy residual require a validated, synchronized twin?

**C4.** Why does trend detection catch a slow fault earlier than a threshold on the instantaneous residual?

---

## Section D — Self-improving and observable

**D1.** Why are the twin's parameters never perfectly known, and what does the mismatch cause?

**D2.** How does fitting a parameter (friction) sharpen fault detection?

**D3.** Name the four key panels of the monitoring dashboard.

**D4.** Why must the machine distinguish "the machine aged (update twin)" from "the machine is faulty (flag)"?

---

## Section E — The machine

**E1.** State what the Integrated Digital Twin artifact comprises.

**E2.** *Reflection:* In two sentences, what did the machine gain in Module 11, and why is it the culmination of the digital-twin thread?

---

## Solutions

<details>
<summary>Reveal (verified against Module 11 code)</summary>

**A1.** Synchronization with a specific real machine — fed its actual inputs and continuously compared to its actual outputs (a simulation runs in isolation).

**A2.** Asset model (the physics), state estimator (infers hidden states), data connection (live measurements).

**A3.** Measured: position, bore pressure, supply flow. Inferred: friction coefficient, valve dead-band.

**A4.** Calibrate → operate → validate → update.

**B1.** Time alignment (match the clocks), resampling (common time grid), and input/output split (feed commands, predict outputs).

**B2.** (1) Read the logged input at this time; (2) feed it to the twin, advancing one step; (3) read the logged measured output; (4) compare predicted to measured.

**B3.** Resampling — interpolate the log onto the twin's 100 Hz grid (or vice versa) so both have values at the same instants.

**B4.** If the twin is given the measured output, there is nothing to predict and nothing to compare; it must predict the outputs from the inputs to produce a meaningful residual.

**C1.** They divert flow, drift the reading, or leak slowly without tripping any single sensor's threshold — but they show up as departures from the twin's prediction.

**C2.** Seal leak: pressure residual ramps down (measured below predicted). Sensor drift: position residual ramps linearly over time. Valve hysteresis: asymmetric residual (different extend vs. retract).

**C3.** Only a validated twin keeps healthy residuals small (near noise); if the twin is inaccurate, healthy residuals are large and faults hide in them. Small residual must reliably mean healthy.

**C4.** A slow fault crosses a fixed threshold only late; fitting the residual's slope detects the significant trend much earlier, before damage.

**D1.** They were assumed/estimated when the models were built and never exactly match the real machine; the mismatch leaves a baseline (healthy) residual that masks small faults.

**D2.** Fitting drives the parameter toward its true value, shrinking the healthy residual toward the noise floor — so a small fault that was hidden beneath the parameter-error residual now stands above it.

**D3.** Position tracking (command/measured/predicted), pressure (with normal bands), residuals (with thresholds), fault flags.

**D4.** If the twin re-fits to a fault, it silently absorbs the fault into its parameters and never flags it; only legitimate aging should update the parameters, while faults must be flagged.

**E1.** The assembled asset model (`workcell_twin.py`), the data synchronization and replay, the residual-based fault detection, and the parameter estimation and monitoring dashboard.

**E2.** The machine gained a complete, integrated digital twin — a live counterpart that mirrors, monitors, and refines itself. It is the culmination because the twin, born as a single cylinder model in Module 04 and grown through every module, is now whole: assembled, synchronized, vigilant, and observable.

</details>

---

*Problem Set 11 — Version 0.1*
