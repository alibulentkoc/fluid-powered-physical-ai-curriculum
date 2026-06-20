# Module 09 — Problem Set

*Sensing — The Machine Perceives*

Work each by hand, then verify with the Module 09 code. All answers verified against the curriculum code.

> Every problem builds the machine's **perception** — the foundation of all its intelligence.

---

## Section A — Perceiving state

**A1.** Why is the physically-complete machine of Modules 01–08 still "blind"? Name two things it cannot do.

**A2.** A bore transducer reads 13.5 mA (range 0–160 bar), rod reads 4.2 mA. Convert both to pressure.

**A3.** Compute the cylinder force from those two pressures.

**A4.** Why do industrial transducers output 4–20 mA instead of voltage? What does 0 mA indicate?

---

## Section B — Cleaning signals

**B1.** Name three sources of sensor noise.

**B2.** A moving average of N=9 samples: by what factor does it cut noise, and what is its lag at 10 ms sampling?

**B3.** Why must position be filtered *before* differentiating for velocity?

**B4.** Why does the machine use lighter filtering for position than for a monitoring signal?

---

## Section C — Detecting the invisible

**C1.** Why is internal pump leakage invisible to pressure, position, and force sensors?

**C2.** A turbine meter (K=0.5 LPM/Hz) reads 19.6 Hz. What flow? What is the leakage residual vs. 10.67 LPM expected?

**C3.** Why does computing a residual require the digital twin?

**C4.** The residual grows from 0.2 to 1.17 LPM over 10 weeks. Estimate when it reaches a 2.0 LPM failure criterion.

---

## Section D — Logging and the twin

**D1.** Describe the machine's data pipeline from sensor to twin.

**D2.** What does comparing the log to the twin's prediction reveal?

**D3.** A position RMS residual of 1.2 mm over a 150 mm stroke — what does this tell the machine?

**D4.** A large pressure residual appears only at the hold phase. Machine fault or twin error? How would you tell?

---

## Section E — The machine

**E1.** State what the Sensor Layer artifact comprises.

**E2.** *Reflection:* In two sentences, what did the machine gain in Module 09, and why is it the foundation of intelligence?

---

## Solutions

<details>
<summary>Reveal (verified against Module 09 code)</summary>

**A1.** It operates open-loop with no feedback: it cannot confirm a commanded motion actually happened, cannot tell if its grip is gentle or crushing, and cannot detect drift or faults.

**A2.** Bore: $0 + (13.5-4)/16 \times 160 = 95$ bar. Rod: $(4.2-4)/16 \times 160 = 2.0$ bar.

**A3.** $F = (95 \times 1963 - 2.0 \times 1348) \times 0.1 = 18{,}379$ N = 18.38 kN.

**A4.** Current signals are immune to wire resistance and noise (same current regardless of wire length); 0 mA indicates a broken wire (free fault detection).

**B1.** Electromagnetic interference, ground loops, ADC quantization.

**B2.** Noise cut by $1/\sqrt{9} = 1/3$; lag $= (9-1)/2 \times 10 = 40$ ms.

**B3.** Differentiating raw noise produces spikes proportional to noise/Δt, often larger than the real velocity. Filter first to make the derivative usable.

**B4.** Position feeds a fast control loop that cannot tolerate much lag; a monitoring signal cares about trends, so it can be smoothed more heavily.

**C1.** Leakage diverts flow internally without changing the pressure (still builds), the eventual position (just slower), or the force — no single sensor sees it.

**C2.** $Q = 0.5 \times 19.6 = 9.8$ LPM. Residual $= 10.67 - 9.8 = 0.87$ LPM (8.2% leakage).

**C3.** The residual needs an *expected* value to compare against, which only the twin can predict for the current command and conditions.

**C4.** Rate $= (1.17 - 0.2)/10 = 0.097$ LPM/week. Weeks to 2.0 from 1.17: $(2.0 - 1.17)/0.097 ≈ 8.6$ more weeks.

**D1.** Sensors → Arduino (read + filter) → serial → Raspberry Pi → CSV log → digital twin.

**D2.** How well the twin's prediction matches reality (per-signal residuals) — validating the twin, detecting faults, and revealing where to refine the model.

**D3.** The twin tracks the real machine to ~0.8% of stroke — excellent agreement, confirming both an accurate twin and a healthy machine.

**D4.** Likely a twin model error (a machine fault would usually show a physical symptom and often across more of the cycle). A hold-only residual suggests the twin's hold/relief-timing model is slightly off; refining the model would remove it, whereas a fault would persist.

**E1.** Pressure/position/force/flow sensors, signal conditioning and filtering, residual-based self-diagnosis, and the data pipeline connecting sensors to the digital twin.

**E2.** The machine gained perception — the ability to sense and diagnose its own state and connect it to the twin. It is the foundation of intelligence because the machine cannot decide, control, or self-monitor without first perceiving.

</details>

---

*Problem Set 09 — Version 0.1*
