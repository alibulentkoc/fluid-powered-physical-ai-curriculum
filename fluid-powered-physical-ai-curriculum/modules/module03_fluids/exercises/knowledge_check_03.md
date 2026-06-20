# Module 03 — Knowledge Check

*Hydraulic Fluids and Energy Transmission*

Attempt all before checking the key. Target: 8 of 10.

---

## Conceptual

**Q1.** Name the four jobs hydraulic fluid does simultaneously.

**Q2.** What does bulk modulus measure, and what does entrained air do to the *effective* bulk modulus?

**Q3.** Which way does viscosity change as temperature rises? Name one danger at the cold end and one at the hot end.

**Q4.** In ISO 4406, does a lower code number mean cleaner or dirtier fluid?

**Q5.** Why is pressure loss in a line so sensitive to the line's diameter?

---

## Calculation

**Q6.** A cylinder holds 0.4 L of oil (B = 1.8 GPa). How much does it compress (mL) at 90 bar?

**Q7.** ISO VG 46 oil is 46 cSt at 40°C. Is the workcell's 40–60°C operating range inside the pump's 13–80 cSt band? (You may reason qualitatively or use `viscosity_model.py`.)

**Q8.** A filter is rated $\beta_{10} = 200$. Efficiency at 10 μm? Particles passed of 1,000,000?

**Q9.** A 10 LPM flow of VG 46 oil through a 10 mm, 2 m line gives roughly what pressure drop? (Recall the worked example.)

---

## System reasoning

**Q10.** State the workcell's complete Fluid Specification (fluid type, VG grade, cleanliness target, filter Beta minimum, supply-line diameter) and give the single most important reason for each choice.

---

## Answer key

<details>
<summary>Reveal</summary>

**A1.** Power transmission, lubrication, sealing, heat removal.

**A2.** Bulk modulus measures resistance to compression (system stiffness). Entrained air sharply lowers the effective bulk modulus because air compresses thousands of times more easily than oil.

**A3.** Viscosity falls as temperature rises. Cold end: oil too thick to pump, risking cavitation/starvation. Hot end: oil too thin to seal and lubricate, causing leakage and wear.

**A4.** Lower = cleaner (fewer particles).

**A5.** Loss scales with velocity squared, and velocity scales with 1/D² for fixed flow; combined with the L/D term, small diameter changes produce large loss changes.

**A6.** $\Delta V = (0.4\times10^{-3} \times 90\times10^5)/(1.8\times10^9) = 2.0\times10^{-6}\ \text{m}^3 = 2.0$ mL.

**A7.** Yes. At 40°C VG 46 is 46 cSt; at ~55°C ~25 cSt; both inside the 13–80 cSt band. The usable window is roughly 29–74°C, so 40–60°C sits comfortably mid-band.

**A8.** Efficiency $= (1-1/200)\times100 = 99.5\%$. Particles passed $= 1{,}000{,}000/200 = 5{,}000$.

**A9.** About 0.54 bar (10 mm line, 10 LPM, 2 m — the Lesson 04 worked example).

**A10.** Mineral oil (indoor — no spill/biodegradability concern). ISO VG 46 (mid-band viscosity across 40–60°C). Cleanliness 18/16/13 (set by the solenoid DCV). Filter $\beta_{10} \geq 100$ (achieves/holds the target). Supply line 10 mm (low loss ~0.54 bar, velocity within the 5 m/s limit).

**Scoring:** 8–10 → ready for Module 04. 5–7 → review Lessons 02 and 04. Below 5 → rework the module.

</details>

---

*Knowledge Check 03 — Version 0.1*
