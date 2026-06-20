"""
sensor_models.py
Module 09 — Sensing (the machine perceives)

The Smart Agricultural Workcell's sensing layer: pressure transducers (4-20 mA),
position transducer, load cell, and force-from-differential-pressure.

Run:
    python sensor_models.py
"""

import math

A_BORE = math.pi * 25 ** 2
A_ROD = A_BORE - math.pi * 14 ** 2


def current_to_pressure(mA, p_min=0.0, p_max=160.0):
    """4-20 mA transducer -> pressure. <3.5 mA = broken wire."""
    if mA < 3.5:
        return None
    return p_min + (mA - 4) / 16 * (p_max - p_min)


def force_from_pressure(p_bore_bar, p_rod_bar):
    """Cylinder force from differential pressure (N)."""
    return (p_bore_bar * A_BORE - p_rod_bar * A_ROD) * 0.1


class LoadCell:
    """End-effector load cell with taring."""
    def __init__(self, calibration_N_per_count=0.01):
        self.cal = calibration_N_per_count
        self.tare_offset = 0.0

    def tare(self, raw_count):
        self.tare_offset = raw_count

    def force_N(self, raw_count):
        return (raw_count - self.tare_offset) * self.cal


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S SENSING LAYER")
    print("=" * 56)
    print("\n  Pressure transducer (4-20 mA, 0-160 bar):")
    for mA in (4, 8, 13.5, 20, 0):
        p = current_to_pressure(mA)
        print(f"    {mA:4.1f} mA -> {p if p is None else f'{p:.0f} bar'}"
              f"{'  (BROKEN WIRE)' if p is None else ''}")

    print("\n  Cylinder force from differential pressure:")
    for pb, pr in [(93.5, 3), (50, 2), (95, 2)]:
        print(f"    bore {pb} bar, rod {pr} bar -> "
              f"{force_from_pressure(pb, pr)/1000:.2f} kN")

    print("\n  Load cell (with taring):")
    lc = LoadCell()
    lc.tare(1050)   # zero with jaw weight
    for raw in (1050, 1080, 1150):
        print(f"    raw {raw} -> {lc.force_N(raw):.1f} N grip")
    print("=" * 56)
