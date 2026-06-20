"""
circuit_model.py
Module 08 — Integrating the Machine's Hydraulic Circuit

Assembles the four subsystem models into one circuit: whole-circuit pressure
budget, idle power by center condition, and force available at the cylinder
after all circuit losses.

Run:
    python circuit_model.py
"""

import math

A_BORE = math.pi * 25 ** 2   # mm^2
PUMP_LPM = 10.67


def cylinder_pressure(pump_bar=100.0, line_drop=0.54, filter_drop=1.0,
                      valve_drop=5.0):
    """Pressure reaching the cylinder after all circuit drops."""
    return pump_bar - line_drop - filter_drop - valve_drop


def force_available_kn(pump_bar=100.0):
    pc = cylinder_pressure(pump_bar)
    return pc * 0.1 * A_BORE / 1000


def idle_power_kw(center, relief_bar=115, idle_drop_bar=5, flow_lpm=PUMP_LPM):
    """Idle power consumption by center condition (all becomes heat)."""
    p = relief_bar if center == "closed" else idle_drop_bar
    return p * flow_lpm / 600


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE AS ONE CIRCUIT")
    print("=" * 56)
    pc = cylinder_pressure()
    print(f"\n  Whole-circuit pressure budget (100 bar pump):")
    print(f"    pump 100.0 - line 0.54 - filter 1.0 - valve 5.0 = {pc:.1f} bar")
    print(f"    force available: {force_available_kn():.2f} kN "
          f"(vs 19.63 kN ideal)")
    print(f"\n  Idle power by center condition:")
    for c in ("closed", "open"):
        print(f"    {c}-center: {idle_power_kw(c):.2f} kW")
    print("=" * 56)
