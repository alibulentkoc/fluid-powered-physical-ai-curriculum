"""
pascals_law.py
Module 01 — Foundations of Fluid Power and Physical AI

Hydraulic cylinder force and velocity calculator.
Applies Pascal's Law and the continuity equation to a double-acting cylinder.

Usage:
    python pascals_law.py

Or import as a module:
    from pascals_law import hydraulic_cylinder_force, piston_velocity
"""

import math


def bore_area(bore_mm: float) -> float:
    """
    Calculate the full bore area of a hydraulic cylinder.

    Args:
        bore_mm: Cylinder bore diameter in millimeters.

    Returns:
        Area in square millimeters (mm²).
    """
    return math.pi * (bore_mm / 2) ** 2


def rod_side_area(bore_mm: float, rod_mm: float) -> float:
    """
    Calculate the annular (rod side) area of a double-acting cylinder.

    Args:
        bore_mm: Cylinder bore diameter in millimeters.
        rod_mm: Rod diameter in millimeters.

    Returns:
        Annular area in square millimeters (mm²).
    """
    return bore_area(bore_mm) - bore_area(rod_mm)


def hydraulic_cylinder_force(
    bore_mm: float,
    rod_mm: float,
    pressure_bar: float,
) -> dict:
    """
    Calculate hydraulic cylinder extend and retract forces.

    Applies Pascal's Law: F = P × A
    (with unit conversion from bar and mm² to kN)

    Args:
        bore_mm: Cylinder bore diameter in millimeters.
        rod_mm: Rod diameter in millimeters.
        pressure_bar: Applied pressure in bar.

    Returns:
        Dictionary with:
            extend_force_kN   — force on full bore side
            retract_force_kN  — force on rod (annulus) side
            bore_area_mm2     — full bore area
            rod_side_area_mm2 — annular area
            area_ratio        — bore area / rod-side area
    """
    # Convert bar to N/mm² (1 bar = 0.1 N/mm²)
    pressure_n_per_mm2 = pressure_bar * 0.1

    a_bore = bore_area(bore_mm)
    a_rod_side = rod_side_area(bore_mm, rod_mm)

    extend_force_n = pressure_n_per_mm2 * a_bore
    retract_force_n = pressure_n_per_mm2 * a_rod_side

    return {
        "extend_force_kN": extend_force_n / 1000,
        "retract_force_kN": retract_force_n / 1000,
        "bore_area_mm2": round(a_bore, 2),
        "rod_side_area_mm2": round(a_rod_side, 2),
        "area_ratio": round(a_bore / a_rod_side, 3),
    }


def piston_velocity(flow_lpm: float, area_mm2: float) -> float:
    """
    Calculate piston velocity from flow rate and piston area.

    Applies continuity: Q = A × v  →  v = Q / A

    Args:
        flow_lpm: Volumetric flow rate in litres per minute (LPM).
        area_mm2: Piston area in square millimeters (mm²).

    Returns:
        Piston velocity in millimeters per second (mm/s).
    """
    # Convert LPM to mm³/s: 1 LPM = 1000 cm³/min = 1,000,000 mm³/min = 16666.7 mm³/s
    flow_mm3_per_s = flow_lpm * 1_000_000 / 60
    return flow_mm3_per_s / area_mm2


def hydraulic_power(pressure_bar: float, flow_lpm: float) -> float:
    """
    Calculate hydraulic power.

    P_hyd = p × Q

    Args:
        pressure_bar: System pressure in bar.
        flow_lpm: Flow rate in litres per minute.

    Returns:
        Power in kilowatts (kW).
    """
    # Convert: bar → Pa (×1e5), LPM → m³/s (÷60,000)
    pressure_pa = pressure_bar * 1e5
    flow_m3_per_s = flow_lpm / 60_000
    power_w = pressure_pa * flow_m3_per_s
    return power_w / 1000  # return kW


def print_cylinder_summary(
    bore_mm: float,
    rod_mm: float,
    pressure_bar: float,
    flow_lpm: float | None = None,
) -> None:
    """
    Print a formatted summary of cylinder forces and (optionally) velocities.
    """
    forces = hydraulic_cylinder_force(bore_mm, rod_mm, pressure_bar)

    print("=" * 50)
    print("HYDRAULIC CYLINDER SUMMARY")
    print("=" * 50)
    print(f"  Bore diameter     : {bore_mm:.1f} mm")
    print(f"  Rod diameter      : {rod_mm:.1f} mm")
    print(f"  Applied pressure  : {pressure_bar:.1f} bar")
    print()
    print(f"  Bore area         : {forces['bore_area_mm2']:.1f} mm²")
    print(f"  Rod-side area     : {forces['rod_side_area_mm2']:.1f} mm²")
    print(f"  Area ratio (B/R)  : {forces['area_ratio']:.3f}")
    print()
    print(f"  Extend force      : {forces['extend_force_kN']:.2f} kN")
    print(f"  Retract force     : {forces['retract_force_kN']:.2f} kN")

    if flow_lpm is not None:
        v_extend = piston_velocity(flow_lpm, forces["bore_area_mm2"])
        v_retract = piston_velocity(flow_lpm, forces["rod_side_area_mm2"])
        power_kw = hydraulic_power(pressure_bar, flow_lpm)

        print()
        print(f"  Flow rate         : {flow_lpm:.1f} LPM")
        print(f"  Extend velocity   : {v_extend:.1f} mm/s")
        print(f"  Retract velocity  : {v_retract:.1f} mm/s")
        print(f"  Hydraulic power   : {power_kw:.2f} kW")

    print("=" * 50)


# ---------------------------------------------------------------------------
# Example: parameters loosely representative of the capstone manipulation cell
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print_cylinder_summary(
        bore_mm=50.0,
        rod_mm=25.0,
        pressure_bar=100.0,
        flow_lpm=10.0,
    )

    print()
    print("Exercise: What extend force does a 63mm bore cylinder produce at 150 bar?")
    result = hydraulic_cylinder_force(bore_mm=63.0, rod_mm=35.0, pressure_bar=150.0)
    print(f"  Answer: {result['extend_force_kN']:.2f} kN")
