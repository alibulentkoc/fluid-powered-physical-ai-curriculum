# Module 06 — Problem Set

*Controlling the Machine's Motion*

Work each by hand, then verify with the Module 06 code. All answers verified against the curriculum code.

> Every problem advances **Precision Positioning** (and begins **Force-Controlled Interaction**) — the machine learning to move where, how fast, and how safely it chooses.

---

## Section A — Directing flow

**A1.** Why can the machine not position anything with the pump connected straight to the cylinder?

**A2.** Name the four ports and three positions of the workcell's 4/3 DCV, and what each position does.

**A3.** Why does the machine's retract (131.9 mm/s) move faster than its extend (90.6 mm/s) at the same flow?

**A4.** Why does the machine use a closed-center spool rather than open-center?

---

## Section B — Pressure control

**B1.** What two pressure dangers does directional control create, and which valve addresses each?

**B2.** The machine operates at 100 bar with 150 bar-rated components. Give a valid relief setting and justify it.

**B3.** During a closed-center hold at 115 bar relief and 10.67 LPM, how much power becomes heat?

**B4.** A 1.5 kN overhauling load acts on the rod side (area 1348 mm²). What counterbalance setting holds it with 30% margin?

---

## Section C — Flow control

**C1.** Why is varying pump speed alone insufficient for the machine's approach-speed control?

**C2.** For a 25 mm/s extend approach, what flow must the meter-out valve pass (metering rod-side return)?

**C3.** Explain meter-in vs. meter-out. Why must the machine meter *out* for a load that assists the motion?

**C4.** Why does the machine prefer a pressure-compensated flow control valve?

---

## Section D — Commanding valves

**D1.** How does the controller command the on/off DCV's three states?

**D2.** Why is a MOSFET driver and freewheeling diode required between microcontroller and solenoid?

**D3.** How does a proportional valve differ from an on/off valve, and what does it give the machine?

**D4.** How does the proportional valve relate to the valve model already in the digital twin (Module 04)?

---

## Section E — The machine

**E1.** State the machine's complete Motion Control Architecture (directional, pressure, flow, command elements).

**E2.** *Reflection:* In two sentences, what capability did the machine gain in Module 06, and how does it advance Precision Positioning?

---

## Solutions

<details>
<summary>Reveal (verified against Module 06 code)</summary>

**A1.** Raw flow is undirected — it can only push the cylinder one way until it bottoms out, with no path to retract, stop partway, or hold. Positioning requires choosing where flow goes, moment by moment.

**A2.** Ports: P (pressure), T (tank), A (bore side), B (rod side). Positions: left (P→A, B→T = extend), center (all blocked = hold), right (P→B, A→T = retract).

**A3.** The rod occupies area on the rod side, making the rod-side area (1348 mm²) smaller than the bore area (1963 mm²). The same flow into a smaller area gives a higher velocity, so retract is faster.

**A4.** Closed-center blocks all ports in neutral, hydraulically locking the cylinder so the machine holds position precisely under load. Open-center connects P→T in neutral, leaving the cylinder free to be pushed by a load — unacceptable for positioning.

**B1.** (1) Trapped pump flow during a closed-center hold → the relief valve dumps it safely. (2) Load-induced pressure spikes or running loads → counterbalance (and the relief as backstop).

**B2.** 115 bar (1.15× operating). Check: 100 < 115 < 150 — above operating so it does not nuisance-trip, below ratings so it protects components.

**B3.** $P_{heat} = 115 \times 10.67 / 600 = 2.05$ kW — the entire pump output as heat during the hold.

**B4.** Load pressure $= 1500 / 1348 \times 10 = 11.1$ bar. Counterbalance $= 11.1 \times 1.3 = 14.5$ bar.

**C1.** Pump-speed variation changes the speed of everything, is limited at the low end (motor stall), and responds slowly. The machine needs local, fast, fine speed control at the actuator — a flow control valve.

**C2.** $Q = 25 \times 1348 \times 60 / 10^6 = 2.02$ LPM (rod-side return metered).

**C3.** Meter-in throttles flow *into* the cylinder (supply side); meter-out throttles flow *out* (return side). For an assisting load, meter-in cannot stop the cylinder being pulled faster than the supply fills it (it cavitates and runs away); meter-out restrains the load by holding back the exiting fluid, controlling the speed.

**C4.** A simple throttle gives a speed that drifts as the load (and pressure drop) changes, because flow ∝ √ΔP. A pressure-compensated valve holds ΔP constant, so the commanded speed stays constant regardless of load — essential for repeatable positioning.

**D1.** Extend: energize solenoid A (spool left). Hold: de-energize both (springs center). Retract: energize solenoid B (spool right).

**D2.** The microcontroller pin cannot supply the solenoid's current, so a MOSFET switches the higher current. The freewheeling diode absorbs the inductive voltage spike when the solenoid switches off, protecting the circuit.

**D3.** An on/off valve has two states (open/closed); a proportional valve's opening varies continuously with command current, giving smooth variable speed from one valve. It lets the machine ease into a target rather than switch between full speed and stop.

**D4.** The proportional valve is the physical realization of Module 04's variable-command valve model $Q = C_d A_{max} u \sqrt{2\Delta P/\rho}$ — the twin was already modeling a continuously-variable valve; the proportional valve is that model in hardware.

**E1.** 4/3 closed-center solenoid DCV (direction); 115 bar relief + counterbalance (pressure/holding); meter-out pressure-compensated flow control (speed); controller → MOSFET → solenoid command path, with a proportional-valve upgrade option.

**E2.** The machine gained complete commandable motion control — direction, pressure safety, speed, and electronic command. It advances Precision Positioning by letting the machine drive to a target from either side, hold there under load, and slow to a precise controlled approach.

</details>

---

*Problem Set 06 — Version 0.1*
