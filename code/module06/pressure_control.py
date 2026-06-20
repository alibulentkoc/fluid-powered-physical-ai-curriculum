"""
pressure_control.py
Module 06 — Controlling the Machine's Motion

Models the Smart Agricultural Workcell's pressure protection: the relief valve
that caps system pressure (making the closed-center hold safe) and the heat it
dissipates, plus counterbalance load holding.

Run:
    python pressure_control.py
"""

import math

PUMP_LPM = 10.67
RELIEF_BAR = 115.0
A_ROD = math.pi * 25 ** 2 - math.pi * 14 ** 2  # mm^2


def relief_state(system_bar, relief_bar=RELIEF_BAR):
    if system_bar < relief_bar:
        return f"relief shut ({system_bar:.0f} bar) - machine works normally"
    return f"RELIEF OPEN - pressure capped at {relief_bar:.0f} bar, excess to tank"


def hold_heat_kw(relief_bar=RELIEF_BAR, flow_lpm=PUMP_LPM):
    """All pump power becomes heat during a closed-center hold."""
    return relief_bar * flow_lpm / 600


def counterbalance_setting_bar(load_N, margin=1.3):
    """Back-pressure to hold an overhauling load on the rod side."""
    load_pressure_bar = load_N / A_ROD * 10   # N/mm^2 -> bar (x10)
    return load_pressure_bar * margin


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S PRESSURE PROTECTION (relief + counterbalance)")
    print("=" * 56)
    print("\nRelief valve caps the machine's pressure:")
    for p in (60, 100, 115, 140, 200):
        print(f"  {relief_state(p)}")
    print(f"\nHeat during a closed-center hold: {hold_heat_kw():.2f} kW")
    print(f"  (entire pump output as heat - fine for intermittent bench duty)")

    print("\nCounterbalance load holding:")
    for load in (500, 1000, 2000):
        cb = counterbalance_setting_bar(load)
        print(f"  {load:4d} N load -> counterbalance setting {cb:.1f} bar")
    print("=" * 56)
