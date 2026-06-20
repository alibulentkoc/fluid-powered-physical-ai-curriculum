"""
bulk_modulus_demo.py
Module 03 — Hydraulic Fluids and Energy Transmission

Demonstrates how bulk modulus (and entrained air, which lowers effective bulk
modulus) affects fluid compression and system pressure-rise rate.

Run:
    python bulk_modulus_demo.py            # prints comparison
    python bulk_modulus_demo.py --plot     # also saves a plot
"""

import sys


def volume_compression_ml(volume_l, pressure_bar, bulk_modulus_gpa):
    """How much a fluid volume compresses (mL) under a pressure rise."""
    V = volume_l * 1e-3            # m^3
    dP = pressure_bar * 1e5        # Pa
    B = bulk_modulus_gpa * 1e9     # Pa
    return (V * dP / B) * 1e6      # mL


def pressure_rise_rate(bulk_modulus_gpa, volume_l, inflow_lpm):
    """dP/dt = B/V * Q_in.  Returns bar/s for a fixed inflow with no outflow."""
    B = bulk_modulus_gpa * 1e9     # Pa
    V = volume_l * 1e-3            # m^3
    Q = inflow_lpm / 60000        # m^3/s
    dPdt_pa = B / V * Q            # Pa/s
    return dPdt_pa / 1e5           # bar/s


CASES = [
    ("clean oil",          1.8),
    ("0.5% entrained air", 0.8),
    ("1% entrained air",   0.4),
]

if __name__ == "__main__":
    print("=" * 56)
    print("BULK MODULUS DEMONSTRATION")
    print("Bore-side volume 0.5 L, pressure rise to 100 bar")
    print("=" * 56)
    print(f"  {'condition':22s} | {'B (GPa)':>7} | {'compression':>12} | {'dP/dt':>9}")
    print(f"  {'-'*22}-+-{'-'*7}-+-{'-'*12}-+-{'-'*9}")
    for label, B in CASES:
        comp = volume_compression_ml(0.5, 100, B)
        rate = pressure_rise_rate(B, 0.5, 10)   # 10 LPM inflow
        print(f"  {label:22s} | {B:>7.1f} | {comp:>9.2f} mL | {rate:>6.0f} b/s")
    print()
    print("  Entrained air lowers effective bulk modulus, so the fluid")
    print("  compresses more and pressure builds more slowly -> spongy,")
    print("  sluggish response. This is why de-aeration and bleeding matter.")
    print("=" * 56)

    if "--plot" in sys.argv:
        try:
            import numpy as np
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib/numpy not available; skipping plot.")
            sys.exit(0)
        pressures = np.linspace(0, 150, 200)
        fig, ax = plt.subplots(figsize=(8, 5))
        for label, B in CASES:
            comp = [volume_compression_ml(0.5, p, B) for p in pressures]
            ax.plot(pressures, comp, label=f"{label} (B={B} GPa)")
        ax.set_xlabel("Pressure (bar)")
        ax.set_ylabel("Volume compression (mL)")
        ax.set_title("Fluid compression vs. pressure — effect of entrained air")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig("bulk_modulus_demo.png", dpi=120)
        print("Plot saved to bulk_modulus_demo.png")
