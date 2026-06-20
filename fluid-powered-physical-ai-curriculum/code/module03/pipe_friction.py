"""
pipe_friction.py
Module 03 — Hydraulic Fluids and Energy Transmission

Computes pressure drop in a hydraulic line using the Reynolds number and the
Darcy-Weisbach equation. Recommends the smallest standard line size that keeps
both flow velocity and pressure drop within acceptable limits for the workcell.

Run:
    python pipe_friction.py            # prints a sizing table
    python pipe_friction.py --plot     # also saves a plot
"""

import math
import sys

# Recommended maximum velocities (m/s)
V_MAX_SUCTION = 1.2
V_MAX_PRESSURE = 5.0
V_MAX_RETURN = 3.0

# Standard line inner diameters (mm)
STANDARD_DIAMETERS_MM = [6, 8, 10, 12, 16, 20]


def line_drop(flow_lpm, diameter_mm, length_m, nu_cst=46, rho=870):
    """
    Return (velocity_m_s, reynolds, pressure_drop_bar) for a hydraulic line.

    Laminar (Re < 2300): f = 64/Re.
    Turbulent: Blasius approximation f = 0.316 * Re^-0.25.
    """
    Q = flow_lpm / 60000              # m^3/s
    D = diameter_mm / 1000            # m
    nu = nu_cst * 1e-6               # m^2/s
    A = math.pi * (D / 2) ** 2
    v = Q / A
    Re = v * D / nu
    f = 64 / Re if Re < 2300 else 0.316 * Re ** -0.25
    dp_pa = f * (length_m / D) * (rho * v ** 2 / 2)
    return v, Re, dp_pa / 1e5


def recommend_line(flow_lpm, length_m, v_max=V_MAX_PRESSURE,
                   dp_max_bar=1.0, nu_cst=46, rho=870):
    """Recommend the smallest standard diameter meeting velocity and drop limits."""
    for d in STANDARD_DIAMETERS_MM:
        v, Re, dp = line_drop(flow_lpm, d, length_m, nu_cst, rho)
        if v <= v_max and dp <= dp_max_bar:
            return d, v, Re, dp
    return None


def print_table(flow_lpm=10, length_m=2.0):
    print("=" * 64)
    print("HYDRAULIC LINE PRESSURE DROP (Darcy-Weisbach)")
    print(f"Flow {flow_lpm} LPM, length {length_m} m, ISO VG 46 @40C (46 cSt)")
    print(f"Pressure-line velocity limit: {V_MAX_PRESSURE} m/s")
    print("=" * 64)
    print(f"  {'Dia (mm)':>9} | {'v (m/s)':>8} | {'Re':>6} | "
          f"{'regime':>9} | {'dP (bar)':>9}")
    print(f"  {'-'*9}-+-{'-'*8}-+-{'-'*6}-+-{'-'*9}-+-{'-'*9}")
    for d in STANDARD_DIAMETERS_MM:
        v, Re, dp = line_drop(flow_lpm, d, length_m)
        regime = "laminar" if Re < 2300 else "turbulent"
        v_flag = " !" if v > V_MAX_PRESSURE else ""
        print(f"  {d:>9} | {v:>8.2f} | {Re:>6.0f} | {regime:>9} | "
              f"{dp:>9.3f}{v_flag}")

    rec = recommend_line(flow_lpm, length_m)
    print()
    if rec:
        d, v, Re, dp = rec
        print(f"  Recommended: {d} mm  (v={v:.2f} m/s, dP={dp:.3f} bar)")
        print(f"  -> meets velocity (<={V_MAX_PRESSURE} m/s) and drop (<=1 bar) limits")
    else:
        print("  No standard size meets both limits; increase max or revisit flow.")
    print("=" * 64)


def make_plot(flow_lpm=10, length_m=2.0):
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib/numpy not available; skipping plot.")
        return
    diameters = np.linspace(5, 22, 200)
    drops = [line_drop(flow_lpm, d, length_m)[2] for d in diameters]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(diameters, drops, color="#185FA5", label="pressure drop")
    ax.axhline(1.0, color="gray", ls="--", lw=1, label="1 bar target")
    for d in STANDARD_DIAMETERS_MM:
        v, Re, dp = line_drop(flow_lpm, d, length_m)
        ax.plot(d, dp, "o", color="black", markersize=5)
    ax.set_xlabel("Inner diameter (mm)")
    ax.set_ylabel("Pressure drop (bar)")
    ax.set_ylim(0, 6)
    ax.set_title(f"Line pressure drop vs. diameter ({flow_lpm} LPM, {length_m} m)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("pipe_friction.png", dpi=120)
    print("Plot saved to pipe_friction.png")


if __name__ == "__main__":
    print_table()
    if "--plot" in sys.argv:
        make_plot()
