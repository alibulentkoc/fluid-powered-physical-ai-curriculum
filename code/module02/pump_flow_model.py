"""
pump_flow_model.py
Module 02 — Hydraulic Components and System Architecture

Models a fixed-displacement gear pump and plots actual flow versus shaft speed
for several volumetric efficiencies. Marks the Smart Agricultural Workcell's
operating point (8 cc/rev, 1450 RPM) and its 10 LPM flow requirement.

Run:
    python pump_flow_model.py            # prints a table
    python pump_flow_model.py --plot     # also saves a plot (needs matplotlib)
"""

import sys


def theoretical_flow_lpm(displacement_cc: float, speed_rpm: float) -> float:
    """Theoretical pump flow: Q_t = D * n. Returns LPM."""
    return displacement_cc * speed_rpm / 1000


def actual_flow_lpm(displacement_cc: float, speed_rpm: float,
                    vol_eff: float = 0.92) -> float:
    """Actual delivered flow: Q_a = Q_t * vol_eff. Returns LPM."""
    return theoretical_flow_lpm(displacement_cc, speed_rpm) * vol_eff


def required_displacement_cc(target_lpm: float, speed_rpm: float,
                             vol_eff: float = 0.92) -> float:
    """Displacement needed to deliver target actual flow at a given speed."""
    theoretical_needed = target_lpm / vol_eff
    return theoretical_needed * 1000 / speed_rpm


def input_power_kw(pressure_bar: float, flow_lpm: float,
                   overall_eff: float = 0.85) -> float:
    """Motor input power: P = (p*Q/600) / overall_eff. Returns kW."""
    hydraulic_kw = pressure_bar * flow_lpm / 600
    return hydraulic_kw / overall_eff


# Workcell baseline parameters
WORKCELL_DISPLACEMENT = 8.0     # cc/rev
WORKCELL_SPEED = 1450           # RPM
WORKCELL_TARGET_FLOW = 10.0     # LPM
WORKCELL_PRESSURE = 100.0       # bar


def print_table() -> None:
    print("=" * 58)
    print("GEAR PUMP FLOW MODEL — Smart Agricultural Workcell")
    print("=" * 58)
    print(f"  Displacement      : {WORKCELL_DISPLACEMENT} cc/rev")
    print(f"  Target flow       : {WORKCELL_TARGET_FLOW} LPM")
    print()
    print(f"  {'Speed (RPM)':>12} | {'Theoretical':>12} | {'Actual @0.92':>13}")
    print(f"  {'-'*12}-+-{'-'*12}-+-{'-'*13}")
    for rpm in (1000, 1200, 1450, 1800, 2200, 3000):
        qt = theoretical_flow_lpm(WORKCELL_DISPLACEMENT, rpm)
        qa = actual_flow_lpm(WORKCELL_DISPLACEMENT, rpm)
        flag = "  <- baseline" if rpm == WORKCELL_SPEED else ""
        print(f"  {rpm:>12} | {qt:>10.2f} L | {qa:>11.2f} L{flag}")

    print()
    qa_base = actual_flow_lpm(WORKCELL_DISPLACEMENT, WORKCELL_SPEED)
    print(f"  At baseline (8 cc/rev, 1450 RPM): {qa_base:.2f} LPM actual")
    print(f"  Requirement: {WORKCELL_TARGET_FLOW} LPM  ->  "
          f"{'MET' if qa_base >= WORKCELL_TARGET_FLOW else 'NOT MET'} "
          f"(margin {qa_base - WORKCELL_TARGET_FLOW:+.2f} LPM)")
    motor = input_power_kw(WORKCELL_PRESSURE, qa_base)
    print(f"  Motor power at {WORKCELL_PRESSURE:.0f} bar: {motor:.2f} kW "
          f"-> select 2.2 kW standard motor")
    print("=" * 58)


def make_plot() -> None:
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib/numpy not available; skipping plot.")
        return

    speeds = np.linspace(500, 3000, 200)
    fig, ax = plt.subplots(figsize=(8, 5))
    for eff in (0.85, 0.90, 0.95):
        flows = [actual_flow_lpm(WORKCELL_DISPLACEMENT, s, eff) for s in speeds]
        ax.plot(speeds, flows, label=f"vol. eff. = {eff:.2f}")

    ax.axhline(WORKCELL_TARGET_FLOW, color="gray", linestyle="--",
               label=f"requirement = {WORKCELL_TARGET_FLOW} LPM")
    qa_base = actual_flow_lpm(WORKCELL_DISPLACEMENT, WORKCELL_SPEED)
    ax.plot(WORKCELL_SPEED, qa_base, "o", color="black", markersize=8,
            label=f"baseline ({WORKCELL_SPEED} RPM, {qa_base:.1f} LPM)")

    ax.set_xlabel("Shaft speed (RPM)")
    ax.set_ylabel("Actual flow (LPM)")
    ax.set_title("Fixed-displacement gear pump (8 cc/rev) — flow vs. speed")
    ax.legend()
    ax.grid(True, alpha=0.3)
    out = "pump_flow_model.png"
    fig.tight_layout()
    fig.savefig(out, dpi=120)
    print(f"Plot saved to {out}")


if __name__ == "__main__":
    print_table()
    if "--plot" in sys.argv:
        make_plot()
