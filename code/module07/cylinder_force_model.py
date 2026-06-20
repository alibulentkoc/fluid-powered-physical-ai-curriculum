"""
cylinder_force_model.py
Module 07 — Producing the Machine's Force and Motion

The Smart Agricultural Workcell's force model: extend/retract force vs. pressure,
bore sizing for a required force, and the pressure each task needs. Feeds the
digital twin the machine's true force behavior.

Run:
    python cylinder_force_model.py
"""

import math

BORE_MM, ROD_MM = 50.0, 28.0
A_BORE = math.pi * (BORE_MM/2)**2
A_ROD = A_BORE - math.pi * (ROD_MM/2)**2


def cylinder_force(pressure_bar, back_pressure_bar=0.0):
    """Extend and retract force (N) at a given bore pressure."""
    F_ext = (pressure_bar*A_BORE - back_pressure_bar*A_ROD) * 0.1
    F_ret = (pressure_bar*A_ROD - back_pressure_bar*A_BORE) * 0.1
    return F_ext, F_ret


def min_bore_mm(force_N, pressure_bar, design_factor=1.5):
    """Minimum bore to produce a required force with margin."""
    A_min = design_factor * force_N / (pressure_bar * 0.1)   # mm^2
    return math.sqrt(4 * A_min / math.pi)


def pressure_for_force(force_N):
    """Bore pressure needed to produce a given extend force."""
    return force_N / (A_BORE * 0.1)


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S FORCE MODEL (50 mm bore, 28 mm rod)")
    print("=" * 56)
    print(f"  A_bore = {A_BORE:.0f} mm^2, A_rod = {A_ROD:.0f} mm^2, "
          f"ratio = {A_BORE/A_ROD:.2f}")
    print(f"\n  {'bar':>5} | {'extend kN':>10} | {'retract kN':>11}")
    for p in (10, 25, 50, 75, 100):
        fe, fr = cylinder_force(p)
        print(f"  {p:>5} | {fe/1000:>10.2f} | {fr/1000:>11.2f}")

    print("\n  Pressure needed for each task force:")
    for name, F in [("gentle grip", 500), ("firm grip", 1500), ("press", 3000)]:
        p = pressure_for_force(F)
        print(f"    {name:12s} ({F:4d} N): {p:5.1f} bar "
              f"({p/100*100:.0f}% of system)")

    print("\n  Minimum bore for a required force (k=1.5, 100 bar):")
    for F in (500, 2000, 5000):
        print(f"    {F:4d} N -> {min_bore_mm(F, 100):.1f} mm bore")
    print("=" * 56)
