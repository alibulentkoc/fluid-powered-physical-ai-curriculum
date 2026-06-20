"""
viscosity_model.py
Module 03 — Hydraulic Fluids and Energy Transmission

Models hydraulic fluid viscosity vs. temperature using the Walther equation
(the basis of the ASTM viscosity-temperature chart). Compares ISO VG grades
and identifies the usable temperature window for a gear pump.

Run:
    python viscosity_model.py            # prints tables and windows
    python viscosity_model.py --plot     # also saves a comparison plot
"""

import math
import sys

# Pump acceptable viscosity band (typical gear pump)
PUMP_MIN_CST = 13.0    # below this: inadequate lubrication / film
PUMP_MAX_CST = 80.0    # above this: hard to pump, cavitation risk at cold start

# ISO VG grades: kinematic viscosity at 40 C and 100 C (typical mineral oil)
ISO_GRADES = {
    "VG 32": (32.0, 5.4),
    "VG 46": (46.0, 6.8),
    "VG 68": (68.0, 8.7),
}


def walther_fit(t1_c, nu1, t2_c, nu2):
    """Fit Walther constants A, B from two (temperature_C, viscosity_cSt) points."""
    def Z(nu):
        return math.log10(math.log10(nu + 0.7))
    T1, T2 = t1_c + 273.15, t2_c + 273.15
    B = (Z(nu1) - Z(nu2)) / (math.log10(T2) - math.log10(T1))
    A = Z(nu1) + B * math.log10(T1)
    return A, B


def walther_viscosity(A, B, temp_c):
    """Predict kinematic viscosity (cSt) at temp_c using fitted Walther constants."""
    T = temp_c + 273.15
    Z = A - B * math.log10(T)
    return 10 ** (10 ** Z) - 0.7


def usable_window(A, B, t_lo=0, t_hi=100, step=0.5):
    """Return (t_min, t_max) where viscosity stays within the pump band."""
    temps_ok = []
    t = t_lo
    while t <= t_hi:
        nu = walther_viscosity(A, B, t)
        if PUMP_MIN_CST <= nu <= PUMP_MAX_CST:
            temps_ok.append(t)
        t += step
    if not temps_ok:
        return None
    return min(temps_ok), max(temps_ok)


def print_report():
    print("=" * 60)
    print("VISCOSITY-TEMPERATURE MODEL (Walther equation)")
    print(f"Pump acceptable band: {PUMP_MIN_CST}-{PUMP_MAX_CST} cSt")
    print("=" * 60)
    for grade, (nu40, nu100) in ISO_GRADES.items():
        A, B = walther_fit(40, nu40, 100, nu100)
        print(f"\n{grade}  ({nu40} cSt @40C, {nu100} cSt @100C)")
        print(f"  {'Temp (C)':>9} | {'Viscosity (cSt)':>16}")
        print(f"  {'-'*9}-+-{'-'*16}")
        for t in (10, 25, 40, 55, 70, 80):
            nu = walther_viscosity(A, B, t)
            mark = "" if PUMP_MIN_CST <= nu <= PUMP_MAX_CST else "  (outside band)"
            print(f"  {t:>9} | {nu:>14.1f}  {mark}")
        win = usable_window(A, B)
        if win:
            print(f"  Usable window: {win[0]:.0f} C to {win[1]:.0f} C")
        else:
            print("  Usable window: none in 0-100 C")

    print("\n" + "=" * 60)
    print("Workcell operates ~40-60 C indoors.")
    print("VG 46 at 40 C = 46.0 cSt, at 55 C ~25 cSt — comfortably mid-band.")
    print("Recommendation: ISO VG 46 for the indoor Smart Agricultural Workcell.")
    print("=" * 60)


def make_plot():
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib/numpy not available; skipping plot.")
        return
    temps = np.linspace(5, 90, 200)
    fig, ax = plt.subplots(figsize=(8, 5))
    for grade, (nu40, nu100) in ISO_GRADES.items():
        A, B = walther_fit(40, nu40, 100, nu100)
        visc = [walther_viscosity(A, B, t) for t in temps]
        ax.plot(temps, visc, label=grade)
    ax.axhline(PUMP_MIN_CST, color="gray", ls="--", lw=1)
    ax.axhline(PUMP_MAX_CST, color="gray", ls="--", lw=1)
    ax.axhspan(PUMP_MIN_CST, PUMP_MAX_CST, color="green", alpha=0.07,
               label="pump band")
    ax.set_xlabel("Temperature (C)")
    ax.set_ylabel("Kinematic viscosity (cSt)")
    ax.set_ylim(0, 200)
    ax.set_title("Viscosity vs. temperature — ISO VG grades (Walther model)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("viscosity_model.png", dpi=120)
    print("Plot saved to viscosity_model.png")


if __name__ == "__main__":
    print_report()
    if "--plot" in sys.argv:
        make_plot()
