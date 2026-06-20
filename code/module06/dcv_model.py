"""
dcv_model.py
Module 06 — Controlling the Machine's Motion

Models the Smart Agricultural Workcell's 4/3 closed-center directional control
valve: command -> flow paths -> cylinder velocity, including valve pressure drop.

Run:
    python dcv_model.py
"""

import math

BORE_MM, ROD_MM = 50.0, 28.0
A_BORE = math.pi * (BORE_MM / 2) ** 2
A_ROD = A_BORE - math.pi * (ROD_MM / 2) ** 2
FLOW_LPM = 10.67
RHO = 870
CD = 0.62
VALVE_AREA_MM2 = 12.0   # DCV port area (sized for low drop at rated flow)


def valve_drop_bar(flow_lpm, area_mm2=VALVE_AREA_MM2):
    """Pressure drop across a DCV flow path (orifice model)."""
    q = flow_lpm / 60000        # m^3/s
    a = area_mm2 * 1e-6         # m^2
    v = q / a
    dp = 0.5 * RHO * (v / CD) ** 2
    return dp / 1e5


def dcv_command(cmd, supply_bar=100.0):
    """Return the flow paths, cylinder velocity, and pressure reaching cylinder."""
    if cmd == "extend":
        v = FLOW_LPM * 1e6 / 60 / A_BORE
        drop = 2 * valve_drop_bar(FLOW_LPM)   # P->A and B->T
        return {
            "paths": "P->A (bore), B->T (rod drains)",
            "velocity_mm_s": round(v, 1),
            "valve_drop_bar": round(drop, 2),
            "pressure_at_cylinder_bar": round(supply_bar - drop, 1),
        }
    elif cmd == "retract":
        v = FLOW_LPM * 1e6 / 60 / A_ROD
        drop = 2 * valve_drop_bar(FLOW_LPM)
        return {
            "paths": "P->B (rod), A->T (bore drains)",
            "velocity_mm_s": round(v, 1),
            "valve_drop_bar": round(drop, 2),
            "pressure_at_cylinder_bar": round(supply_bar - drop, 1),
        }
    elif cmd == "hold":
        return {
            "paths": "all ports blocked (closed center)",
            "velocity_mm_s": 0.0,
            "valve_drop_bar": 0.0,
            "pressure_at_cylinder_bar": "locked (trapped fluid holds load)",
        }
    return {"error": "unknown command"}


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S DIRECTIONAL CONTROL (4/3 closed-center DCV)")
    print("=" * 56)
    for cmd in ("extend", "hold", "retract"):
        print(f"\nCommand: {cmd}")
        for k, val in dcv_command(cmd).items():
            print(f"  {k:24s}: {val}")
    print("=" * 56)
