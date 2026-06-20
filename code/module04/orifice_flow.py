"""
orifice_flow.py
Module 04 — Fluid Mechanics for Intelligent Machines

The valve flow model: the FIRST component of the Smart Agricultural Workcell
digital twin. Models any valve as a variable orifice using the orifice equation.

This module is imported by the cylinder simulation (Lesson 05) and the
integrated digital twin (Module 11). Keep the interface stable.

Run:
    python orifice_flow.py            # prints a demonstration table
    python orifice_flow.py --plot     # also saves flow-vs-pressure plots
"""

import math
import sys


def valve_flow(u: float, dp_pa: float, cd: float = 0.62,
               area_max_m2: float = 4e-6, rho: float = 870) -> float:
    """
    Valve flow model (orifice equation). Returns flow in m^3/s.

    Q = Cd * A(u) * sqrt(2 * dP / rho),  with A(u) = area_max * u

    Args:
        u: valve command, 0 (closed) to 1 (fully open)
        dp_pa: pressure drop across the valve, Pa (must be >= 0)
        cd: discharge coefficient (~0.62 sharp-edged orifice)
        area_max_m2: fully-open orifice area, m^2
        rho: fluid density, kg/m^3

    Returns:
        Volumetric flow rate, m^3/s. Zero if u<=0 or dp<=0.
    """
    if u <= 0 or dp_pa <= 0:
        return 0.0
    area = area_max_m2 * max(0.0, min(1.0, u))
    return cd * area * math.sqrt(2 * dp_pa / rho)


def valve_flow_lpm(u: float, dp_bar: float, cd: float = 0.62,
                   area_max_mm2: float = 4.0, rho: float = 870) -> float:
    """Convenience wrapper: command and bar in, LPM out."""
    q = valve_flow(u, dp_bar * 1e5, cd, area_max_mm2 * 1e-6, rho)
    return q * 60000


def print_demo():
    print("=" * 56)
    print("VALVE FLOW MODEL (orifice equation)")
    print("First digital twin component — Cd=0.62, A_max=4 mm^2")
    print("=" * 56)
    print("\nEffect of valve opening (constant 30 bar drop):")
    for u in (0.25, 0.50, 0.75, 1.00):
        print(f"  u = {u:.2f}  ->  {valve_flow_lpm(u, 30):6.2f} LPM")
    print("  (flow is LINEAR in opening area)")

    print("\nEffect of pressure drop (constant full opening):")
    for dp in (7.5, 15, 30, 60):
        print(f"  dP = {dp:5.1f} bar  ->  {valve_flow_lpm(1.0, dp):6.2f} LPM")
    print("  (flow scales with the SQUARE ROOT of pressure drop)")

    base = valve_flow_lpm(1.0, 30)
    half_dp = valve_flow_lpm(1.0, 15)
    print(f"\n  Halving pressure (30->15 bar): {base:.2f} -> {half_dp:.2f} LPM "
          f"(x{half_dp/base:.3f} = sqrt(0.5))")
    print("=" * 56)


def make_plots():
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib/numpy unavailable; skipping plots.")
        return
    dp = np.linspace(0, 80, 200)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
    for u in (0.25, 0.5, 0.75, 1.0):
        flows = [valve_flow_lpm(u, d) for d in dp]
        ax1.plot(dp, flows, label=f"u = {u:.2f}")
    ax1.set_xlabel("Pressure drop (bar)")
    ax1.set_ylabel("Flow (LPM)")
    ax1.set_title("Flow vs. pressure drop (square-root)")
    ax1.legend(); ax1.grid(True, alpha=0.3)

    u = np.linspace(0, 1, 100)
    for d in (15, 30, 60):
        flows = [valve_flow_lpm(uu, d) for uu in u]
        ax2.plot(u, flows, label=f"dP = {d} bar")
    ax2.set_xlabel("Valve command u")
    ax2.set_ylabel("Flow (LPM)")
    ax2.set_title("Flow vs. command (linear in opening)")
    ax2.legend(); ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig("orifice_flow.png", dpi=120)
    print("Plots saved to orifice_flow.png")


if __name__ == "__main__":
    print_demo()
    if "--plot" in sys.argv:
        make_plots()
