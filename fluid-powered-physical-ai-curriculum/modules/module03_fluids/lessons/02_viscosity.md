# Viscosity and the viscosity-temperature relationship
## Module 03 · Lesson 02

*Viscosity is the single most important fluid property. It changes with temperature, and that change defines the safe operating window of the whole system.*

---

## 1. Why this matters

If you remember one number about a hydraulic fluid, it is its viscosity. Viscosity controls how easily the fluid flows, how well it seals clearances, how much energy is lost to friction, and whether the pump can draw it at startup.

The complication is that viscosity changes dramatically with temperature. The same oil that flows perfectly at operating temperature may be too thick to pump at cold startup and too thin to seal when overheated. Selecting the workcell's fluid means choosing a viscosity grade whose temperature behavior keeps the system inside a safe window. This lesson gives you the tools to do that.

---

## 2. Physical intuition

Viscosity is a fluid's resistance to flow — its internal friction. Honey is highly viscous; water is not. Hydraulic oil sits in between, and where exactly it sits is chosen deliberately.

Now the key fact: **viscosity falls as temperature rises.** Cold oil is thick and sluggish. Hot oil is thin and runny. This is not a small effect — viscosity can change by a factor of ten or more across a normal operating temperature range.

This creates a tension. At cold startup, thick oil resists being drawn into the pump, risking cavitation and high power draw. At high operating temperature, thin oil leaks past clearances and fails to maintain a lubricating film, causing wear and efficiency loss.

The fluid must be thick enough when hot to seal and lubricate, but thin enough when cold to pump. The chosen viscosity grade is a compromise that keeps the fluid in its usable band across the expected temperatures.

---

## 3. Mathematical foundations

### Dynamic vs. kinematic viscosity

Two related measures:

- **Dynamic (absolute) viscosity** $\mu$ — resistance to shear, units Pa·s.
- **Kinematic viscosity** $\nu$ — dynamic viscosity divided by density, units mm²/s (cSt, centistokes).

$$\nu = \frac{\mu}{\rho}$$

Hydraulic fluids are normally specified by kinematic viscosity.

### ISO VG grades

The ISO Viscosity Grade (VG) system labels a fluid by its kinematic viscosity at 40°C, in cSt:

| ISO VG | Kinematic viscosity at 40°C (cSt) |
|--------|-----------------------------------|
| VG 22 | 22 |
| VG 32 | 32 |
| VG 46 | 46 |
| VG 68 | 68 |
| VG 100 | 100 |

The workcell baseline is **ISO VG 46** — 46 cSt at 40°C, a common general-purpose grade.

### Viscosity Index (VI)

The **Viscosity Index** measures how much viscosity changes with temperature. A high VI means viscosity is relatively stable across temperature — desirable. A low VI means viscosity swings wildly. Premium fluids and those with VI improvers have high VI (150+); basic mineral oils are lower (~95–105).

### The Walther equation (viscosity vs. temperature)

Viscosity-temperature behavior is modeled by the Walther equation, the basis of the ASTM viscosity-temperature chart:

$$\log_{10}\log_{10}(\nu + 0.7) = A - B \log_{10}(T)$$

where $\nu$ is kinematic viscosity (cSt), $T$ is absolute temperature (K), and $A$, $B$ are constants fit to two known viscosity points. With viscosity known at two temperatures (e.g., 40°C and 100°C, both on the datasheet), you can predict it at any temperature in between.

> **Workcell relevance:** Using the Walther equation with the VG 46 datasheet values, you can plot viscosity from 10°C (cool startup) to 80°C (warm operation) and confirm the fluid stays inside the pump's acceptable viscosity range — typically 10–100 cSt for a gear pump. This is the Module 03 modeling task.

---

## 4. Visual explanation

> See figure: `assets/figures/capstone_architecture.svg` (Subsystem 2)

A viscosity-temperature plot is the central visual for this lesson. Picture the curve: high viscosity at low temperature, falling steeply, then leveling as temperature rises. Overlay two horizontal lines marking the pump's acceptable viscosity band (say, minimum 13 cSt for lubrication, maximum 80 cSt for pumpability). The temperature range where the curve sits between those lines is the fluid's usable operating window.

A higher-VI fluid has a flatter curve, giving a wider operating window. A lower-VI fluid's steeper curve narrows the window. This is exactly why VI matters.

---

## 5. Engineering example

**Why agricultural equipment often uses high-VI or multigrade fluids**

A tractor started on a cold morning and worked into a hot afternoon experiences a huge temperature swing. A single-grade oil with low VI might be unpumpably thick at dawn and dangerously thin by mid-afternoon. Agricultural and mobile equipment therefore often use high-VI or multigrade hydraulic fluids that hold usable viscosity across a wide range.

The workcell, indoors and thermally stable, does not face this. ISO VG 46 with standard VI is sufficient because its operating temperature stays in a narrow band. Again: the environment sets the requirement. The workcell's relaxed thermal conditions allow a simpler, cheaper fluid — a deliberate, documented choice.

---

## 6. Worked example

**Problem:** An ISO VG 46 oil has a kinematic viscosity of 46 cSt at 40°C and 6.8 cSt at 100°C. Using the Walther equation, estimate its viscosity at 25°C (a cool startup) and at 70°C (warm operation). The gear pump requires viscosity between 13 and 80 cSt for proper operation.

**Solution (outline — full computation in the coding exercise):**

The Walther equation is fit using the two known points to find constants A and B, then evaluated at the target temperatures. Carrying out the fit (verified in the coding exercise):

- At 25°C: ν ≈ 99 cSt (just above the thick limit of 80 cSt — cold-start caution)
- At 70°C: ν ≈ 15 cSt (just above the thin limit of 13 cSt)

So between roughly 27°C and 72°C, the VG 46 oil stays within the pump's 13–80 cSt window. Below ~27°C it becomes too thick (cold-start caution); above ~72°C it approaches too thin. The workcell, operating around 40–60°C indoors, sits comfortably in the middle of this window — at 40°C the viscosity is exactly 46 cSt and at 55°C about 25 cSt — confirming VG 46 is a sound choice.

*(The coding exercise implements the Walther fit so you can compute these precisely and plot the full curve.)*

---

## 7. Interactive demonstration

```python
import math

def walther_fit(t1_c, nu1, t2_c, nu2):
    """Fit Walther constants A, B from two (temp_C, viscosity_cSt) points."""
    def Z(nu): return math.log10(math.log10(nu + 0.7))
    T1, T2 = t1_c + 273.15, t2_c + 273.15
    B = (Z(nu1) - Z(nu2)) / (math.log10(T2) - math.log10(T1))
    A = Z(nu1) + B * math.log10(T1)
    return A, B

def walther_viscosity(A, B, temp_c):
    """Predict kinematic viscosity (cSt) at a temperature using Walther constants."""
    T = temp_c + 273.15
    Z = A - B * math.log10(T)
    return 10 ** (10 ** Z) - 0.7

A, B = walther_fit(40, 46, 100, 6.8)   # ISO VG 46
for t in [10, 25, 40, 55, 70, 80]:
    print(f"{t:3d} °C: {walther_viscosity(A, B, t):6.1f} cSt")
```

Run it to see the full viscosity-temperature curve for VG 46. Note how steeply viscosity climbs at low temperature — this is the cold-start concern.

---

## 8. Coding exercise

Write `code/module03/viscosity_model.py` that:

1. Implements the Walther fit and evaluation (as above)
2. Plots viscosity vs. temperature for ISO VG 32, VG 46, and VG 68 on one chart
3. Draws the pump's acceptable viscosity band (13–80 cSt) as horizontal lines
4. Identifies and prints the usable temperature window for each grade
5. Recommends which grade gives the workcell the widest window around its 40–60°C operating range

Use NumPy and Matplotlib.

---

## 9. Knowledge check

1. What is viscosity, in plain terms?
2. Which way does viscosity change as temperature rises?
3. What does "ISO VG 46" tell you precisely?
4. What does a high Viscosity Index mean for a fluid's behavior?
5. Why is there a tension between cold-start pumpability and hot-running sealing?

---

## 10. Challenge problem

The workcell is being considered for a semi-outdoor deployment in a barn, where temperatures range from 5°C in winter mornings to 75°C during sustained summer operation.

**a)** Using the Walther model, would the current ISO VG 46 oil stay within the 13–80 cSt pump window across 5–75°C? Where does it fail?

**b)** Would a higher-VI fluid help? Explain what changes about the curve.

**c)** Would switching to a different ISO VG grade help more than a higher VI, or less? Consider both the cold and hot ends.

**d)** Recommend a fluid strategy for the semi-outdoor workcell and justify it. Note any tradeoff (cost, availability) you are accepting.

---

## 11. Common mistakes

**Treating viscosity as a single fixed number.** Viscosity is always temperature-dependent. A datasheet value at 40°C tells you nothing about cold-start or hot-running behavior without the VI or a second data point.

**Ignoring cold-start viscosity.** Thick cold oil starves the pump and can cause cavitation. Many systems are damaged at startup, not during operation. Always check the cold end of the operating range.

**Choosing too high a grade "to be safe."** A thicker fluid increases friction losses (wasted energy as heat) and worsens cold-start. Higher is not safer — match the grade to the temperature range.

**Confusing dynamic and kinematic viscosity.** ISO VG grades use kinematic viscosity (cSt) at 40°C. Mixing up the two units gives nonsense results. Hydraulic specs are almost always kinematic.

---

## 12. Key takeaways

- Viscosity is a fluid's resistance to flow — the most important hydraulic fluid property.
- Viscosity falls as temperature rises, often by a factor of ten or more across the operating range.
- ISO VG grades label fluids by kinematic viscosity at 40°C; the workcell uses VG 46.
- Viscosity Index measures temperature stability; high VI means a flatter curve and a wider operating window.
- The Walther equation predicts viscosity at any temperature from two known points.
- The fluid must stay within the pump's acceptable viscosity band across the operating temperature range; VG 46 suits the indoor workcell's 40–60°C window.

---

*Lesson 02 — Version 0.1 | Next: Lesson 03 — Contamination, filtration, and ISO cleanliness*
