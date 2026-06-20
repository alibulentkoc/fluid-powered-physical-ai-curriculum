# The support system: reservoir, filter, hoses, fittings
## Module 02 · Lesson 04

*The components that get no glory and cause most failures. The reservoir, filter, hoses, and fittings keep the fluid clean, cool, and contained — and contamination through them is the number-one cause of hydraulic breakdown.*

---

## 1. Why this matters

Ask an experienced hydraulic technician what kills systems, and the answer is rarely "the pump failed" or "the cylinder broke." It is almost always contamination — dirt, water, or wear particles in the fluid that score valve spools, erode pump internals, and tear seals.

The support system exists to prevent this. It is unglamorous: a tank, a filter, some hoses, and fittings. But specifying it correctly is the difference between a workcell that runs for years and one that fails in months. This lesson closes Module 02 by completing the component picture and giving you the knowledge to specify the parts of the workcell that keep everything else alive.

---

## 2. Physical intuition

### The reservoir is not just a bucket

A hydraulic reservoir holds the fluid, yes. But it does three other jobs that matter more:

- **De-aeration:** fluid returning from the system carries entrained air bubbles. Given time and surface area in the reservoir, those bubbles rise and escape. Air in hydraulic fluid is bad — it compresses (ruining the incompressibility hydraulics depend on) and causes cavitation.
- **Heat rejection:** the reservoir's surface area sheds heat to the surrounding air. The fluid heats up from friction and throttling losses; the reservoir lets it cool.
- **Settling:** heavier contaminants settle to the bottom, away from the pump suction.

A good rule of thumb sizes the reservoir at 3–5 times the pump's per-minute flow. For the workcell at ~10 LPM, that suggests a 30–50 litre reservoir for continuous duty — though a bench workcell with intermittent operation can use less.

### The filter is the system's immune system

Filters trap particles before they reach sensitive components. The most sensitive component sets the required cleanliness. In the workcell, that is the directional control valve — its spool fits its bore with micron-scale clearances, and a particle of the wrong size jams or scores it.

### Hoses and fittings contain everything

Hoses carry fluid to moving parts. Fittings join everything together. Both are rated for pressure, and both are common leak points if mismatched or poorly installed.

---

## 3. Mathematical foundations

### Filter performance — the Beta ratio

A filter's effectiveness is quantified by its **Beta ratio** at a given particle size:

$$\beta_x = \frac{N_{upstream}}{N_{downstream}}$$

where $N$ is the number of particles larger than $x$ microns, upstream and downstream of the filter.

A filter with $\beta_{10} = 200$ lets only 1 in 200 particles larger than 10 μm pass. The capture efficiency is:

$$\text{Efficiency} = \left(1 - \frac{1}{\beta_x}\right) \times 100\%$$

So $\beta_{10} = 200$ gives $(1 - 1/200) \times 100 = 99.5\%$ efficiency at 10 μm.

### Reservoir sizing

$$V_{reservoir} \approx k \cdot Q_{pump}$$

with $k$ typically 3–5 (minutes). For $Q = 10$ LPM and $k = 4$: $V \approx 40$ L for continuous industrial duty.

### Pressure drop in a hose (preview of Module 04)

Fluid flowing through a hose loses pressure to friction. The Darcy-Weisbach relationship (developed fully in Module 04) shows this loss grows with flow velocity squared and with hose length, and falls sharply with larger diameter. The practical takeaway here: undersized hoses waste pressure as heat and starve the actuators.

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (Subsystem 2 — Fluid transport)

The fluid transport subsystem connects everything:

- **Suction line:** reservoir → pump inlet. Low pressure, large diameter (to avoid starving the pump and causing cavitation).
- **Pressure line:** pump → valves → actuators. High pressure, rated hose or rigid pipe.
- **Return line:** actuators → filter → reservoir. Low pressure; usually where the filter sits.
- **Filter:** typically on the return line (cheaper, lower-pressure housing) or the pressure line (protects valves directly). The workcell uses a return-line filter with a bypass and a clogging indicator.

### Fitting standards

Three common thread/seal standards you will encounter:

- **BSP** (British Standard Pipe) — common in Europe and agricultural equipment
- **JIC** (37° flare) — common in North American mobile hydraulics
- **SAE ORB** (O-ring boss) — reliable sealing for port connections

Mixing standards causes leaks. The workcell should standardize on one family — for agricultural compatibility, BSP or the regional norm.

---

## 5. Engineering example

**Why contamination control matters in the field**

Agricultural hydraulic systems operate in the dirtiest environments imaginable — dust, mud, water, plant debris. Studies of hydraulic component failures consistently attribute the majority to contamination, not mechanical wear or manufacturing defects.

The practical defenses are exactly the support-system components:
- A properly rated **filter** captures wear particles and ingested dirt.
- A **sealed reservoir** with a quality **breather** (the vent that lets the fluid level rise and fall) keeps airborne dust out.
- **Good fittings**, properly torqued, prevent both leaks out and contamination in.

For the workcell, even though it runs in a cleaner indoor setting, the same principles apply. The DCV is the most contamination-sensitive component, so the filter is sized to protect it: a target cleanliness expressed as an ISO 4406 code (covered in Module 03), achieved with a filter of appropriate Beta ratio.

---

## 6. Worked example

**Problem:** The workcell's most sensitive component is its directional control valve, which requires fluid cleaner than ISO 18/16/13 (a cleanliness code covered in Module 03). The chosen return-line filter is rated $\beta_{10} = 100$.

(a) What is the filter's capture efficiency at 10 μm?
(b) If the return line carries 10 LPM and the recommended reservoir factor is k = 4 minutes, what reservoir volume is suggested for continuous duty?
(c) The workcell runs intermittently (30% duty cycle). Estimate a practical reservoir size.

**Solution:**

*(a) Efficiency*
$$\left(1 - \frac{1}{100}\right) \times 100 = 99\%\ \text{at 10 μm}$$

*(b) Continuous-duty reservoir*
$$V = 4 \times 10 = 40\ \text{L}$$

*(c) Intermittent practical size*
At 30% duty, heat generation is lower, so a smaller reservoir can shed heat adequately. A practical bench workcell might use 12–20 L, accepting that sustained continuous operation would require the larger size. (This is an engineering judgment, documented as such — not a precise formula.)

---

## 7. Interactive demonstration

```python
def filter_efficiency(beta):
    return (1 - 1/beta) * 100

def reservoir_volume(flow_lpm, k=4):
    return k * flow_lpm

for beta in [10, 75, 100, 200, 1000]:
    print(f"Beta_10 = {beta:4d}  →  {filter_efficiency(beta):.2f}% efficient at 10 um")

print(f"\nReservoir for 10 LPM continuous (k=4): {reservoir_volume(10)} L")
```

Notice how quickly efficiency climbs: even a modest $\beta_{10}=75$ filter captures over 98% of 10 μm particles. The difference between $\beta=200$ and $\beta=1000$ is small in percentage but matters for the largest, most damaging particles over long service.

---

## 8. Coding exercise

Write `code/module02/support_system_sizer.py` that, given pump flow and the most sensitive component's cleanliness requirement, recommends:
- A reservoir volume range (continuous and intermittent)
- A minimum filter Beta ratio
- A suction-line minimum diameter (to keep suction velocity below ~1.2 m/s, a standard guideline to avoid cavitation)

Use the continuity equation from Module 01 for the line-sizing part.

---

## 9. Knowledge check

1. Name three jobs the reservoir does besides storing fluid.
2. What is the Beta ratio, and what does $\beta_{10} = 100$ mean?
3. Why is the filter usually placed on the return line rather than the pressure line?
4. Why must the suction line be larger in diameter than the pressure line?
5. Why does mixing fitting standards (e.g., BSP and JIC) cause problems?

---

## 10. Challenge problem

A workcell is being commissioned and the DCV begins sticking intermittently after two weeks of operation.

**a)** Based on this module, what is the single most likely root cause?

**b)** List the support-system components you would inspect, in priority order, and what you would look for in each.

**c)** The filter's clogging indicator has not tripped. Does that rule out contamination? Explain. (Hint: consider whether the contamination entered before or after the filter, and whether the filter's Beta ratio is adequate for the DCV's sensitivity.)

**d)** Propose two changes to the support system that would reduce the chance of recurrence, and connect each to a quantity from this lesson (Beta ratio, reservoir size, breather rating, fitting standard).

---

## 11. Common mistakes

**Treating the reservoir as an afterthought.** An undersized reservoir runs hot and does not de-aerate properly, causing cascading problems (oxidized fluid, cavitation, seal failure). Size it deliberately.

**Under-filtering to save cost.** A cheaper, lower-Beta filter that does not match the most sensitive component's needs guarantees premature valve failure. The filter must be matched to the cleanest-required component, not the average.

**Undersizing the suction line.** Starving the pump inlet causes cavitation — vapor bubbles that collapse violently and erode the pump. The suction line must be large enough to keep velocity low. This is a frequent and damaging beginner error.

**Ignoring the breather.** The reservoir breathes as fluid level changes. A poor or missing breather filter lets dust straight into the tank, defeating the main filter. The breather is part of the contamination defense, not an optional vent.

---

## 12. Key takeaways

- The support system (reservoir, filter, hoses, fittings) prevents the contamination that causes most hydraulic failures.
- The reservoir de-aerates, rejects heat, and lets contaminants settle — sized at roughly 3–5× pump flow for continuous duty.
- Filter effectiveness is the Beta ratio: $\beta_x = N_{up}/N_{down}$; efficiency $= (1 - 1/\beta_x)$. Match the filter to the most sensitive component (the workcell's DCV).
- Suction lines are larger than pressure lines to prevent pump cavitation.
- Fitting standards (BSP, JIC, SAE ORB) must not be mixed; standardize the workcell on one.
- This lesson completes the component picture. You can now identify every part of the workcell's hydraulic hardware and explain why it is there.

---

## Module 02 deliverable

With all four lessons complete, produce the first **Component Map** of the Smart Agricultural Workcell: a block diagram naming the actual components for Subsystems 1 and 2 (pump type and size, valve types, cylinder dimensions, reservoir volume, filter rating, fitting standard). This is the foundation for the detailed sizing work in Modules 05–08.

---

*Lesson 04 — Version 0.1 | Module 02 lesson content complete. Next: Module 02 summary, exercises, and the pump flow code.*
