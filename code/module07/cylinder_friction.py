"""
cylinder_friction.py
Module 07 — Producing the Machine's Force and Motion

The real cylinder's friction, breakout, and cushioning models for the Smart
Agricultural Workcell digital twin. Captures the Stribeck stick-slip behavior
that determines how precisely the machine can position and how gently it can push.

Run:
    python cylinder_friction.py
"""

import math

# Specified cylinder friction parameters
F_STATIC = 120.0    # N, breakout
F_COULOMB = 70.0    # N, kinetic
V_STRIBECK = 10.0   # mm/s
VISC_B = 200.0      # N*s/m
A_BORE = math.pi * 25 ** 2   # mm^2


def stribeck_friction(v_mm_s):
    """Friction force (N) at a given velocity (mm/s)."""
    if abs(v_mm_s) < 1e-6:
        return F_STATIC   # breakout
    s = 1 if v_mm_s > 0 else -1
    v = v_mm_s
    return s * (F_COULOMB + (F_STATIC - F_COULOMB) *
                math.exp(-(v / V_STRIBECK) ** 2)) + VISC_B * (v / 1000)


def breakout_pressure_bar(load_N=0.0):
    """Minimum bore pressure to start motion against static friction + load."""
    return (F_STATIC + load_N) / (A_BORE * 0.1)


def cushion_deceleration(v0_mm_s, cushion_mm):
    """Approx constant deceleration (m/s^2) in the end cushion zone."""
    v0 = v0_mm_s / 1000
    Lc = cushion_mm / 1000
    return v0 ** 2 / (2 * Lc)


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S REAL CYLINDER BEHAVIOR (friction model)")
    print("=" * 56)
    print(f"\n  {'v (mm/s)':>9} | {'friction (N)':>12}")
    for v in (0, 2, 5, 10, 20, 50, 90):
        print(f"  {v:>9} | {stribeck_friction(v):>12.1f}")
    print("\n  Friction is highest at breakaway and in the slow-approach")
    print("  range -- where precise positioning is hardest (stick-slip).")

    print(f"\n  Breakout pressure (no load): {breakout_pressure_bar():.2f} bar")
    print(f"  Smallest controllable force ~ static friction: {F_STATIC:.0f} N")
    print(f"  Cushion decel (90 mm/s into 10 mm): "
          f"{cushion_deceleration(90, 10):.2f} m/s^2 (gentle stop)")
    print("=" * 56)
