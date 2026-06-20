"""
cylinder_spec.py
Module 07 — Producing the Machine's Force and Motion

Generates and checks the Actuator Selection Report: buckling (Euler), pressure
rating with design factor, and the area ratio. Produces the module artifact.

Run:
    python cylinder_spec.py
"""

import math


def buckling_load_kn(rod_mm, effective_length_mm, K=2.0, E_gpa=210):
    """Euler critical buckling load (kN)."""
    d = rod_mm / 1000
    L = effective_length_mm / 1000
    I = math.pi * d**4 / 64
    return math.pi**2 * (E_gpa*1e9) * I / (K*L)**2 / 1000


def area_ratio(bore_mm, rod_mm):
    A_b = math.pi*(bore_mm/2)**2
    A_r = A_b - math.pi*(rod_mm/2)**2
    return A_b / A_r


def actuator_report(bore_mm=50, rod_mm=28, stroke_mm=300,
                    working_bar=100, extend_force_kn=19.63):
    eff_len = stroke_mm + 100
    F_cr = buckling_load_kn(rod_mm, eff_len)
    return {
        "bore_mm": bore_mm,
        "rod_mm": rod_mm,
        "stroke_mm": stroke_mm,
        "area_ratio": round(area_ratio(bore_mm, rod_mm), 2),
        "buckling_load_kn": round(F_cr),
        "buckling_SF": round(F_cr / extend_force_kn, 1),
        "buckling_ok": F_cr / extend_force_kn >= 3,
        "pressure_rating_min_bar": round(1.6 * working_bar),
        "seal": "Nitrile (NBR) for ISO VG 46 at bench temp",
        "mounting": "clevis/trunnion (allows alignment)",
    }


if __name__ == "__main__":
    print("=" * 56)
    print("ACTUATOR SELECTION REPORT — primary cylinder")
    print("=" * 56)
    rep = actuator_report()
    for k, v in rep.items():
        print(f"  {k:24s}: {v}")
    print("\n  Buckling load vs. stroke (28 mm rod):")
    for stroke in (300, 500, 800, 1200):
        fcr = buckling_load_kn(28, stroke+100)
        print(f"    {stroke:4d} mm: {fcr:5.0f} kN  (SF {fcr/19.63:.1f})")
    print("=" * 56)
