"""
circuit_protection.py
Module 08 — Integrating the Machine's Hydraulic Circuit

Models the Smart Agricultural Workcell's fail-safe protection: load-holding
drift, port relief sizing, thermal spikes, and the power-loss scenario.

Run:
    python circuit_protection.py
"""

import math

A_BORE = math.pi * 25 ** 2   # mm^2


def leak_down_velocity_mm_s(leak_lpm):
    return leak_lpm * 1e6 / 60 / A_BORE


def thermal_spike_bar(delta_T, beta=0.0007, B_pa=1.5e9):
    """Pressure spike from heating trapped fluid."""
    return beta * B_pa * delta_T / 1e5


def power_loss_scenario(load_kn=2.0):
    """Trace the machine's response to power loss while holding a load."""
    steps = [
        "Power fails -> spring-centered DCV returns to closed-center (locks ports)",
        "Trapped fluid would leak past spool -> load would slowly sink",
        "Pilot-operated check valves block the leak path -> load STAYS HELD",
        "If load is shocked -> port reliefs cap the spike, protecting cylinder",
        f"Result: {load_kn} kN load held safely, no power, no drift",
    ]
    return steps


if __name__ == "__main__":
    print("=" * 60)
    print("THE MACHINE'S FAIL-SAFE PROTECTION")
    print("=" * 60)
    print("\n  Load-holding drift vs. leakage:")
    for leak, label in [(0.05, "bare spool"), (0.01, "good valve"),
                        (0.001, "pilot check valve")]:
        v = leak_down_velocity_mm_s(leak)
        print(f"    {label:18s}: {v:.3f} mm/s = {v*60:5.1f} mm/min")

    print("\n  Thermal spike in trapped fluid:")
    for dT in (5, 8, 10):
        print(f"    +{dT} C -> {thermal_spike_bar(dT):.0f} bar spike "
              f"(needs thermal relief)")

    print("\n  Power-loss scenario (holding 2 kN load):")
    for i, step in enumerate(power_loss_scenario(), 1):
        print(f"    {i}. {step}")
    print("=" * 60)
