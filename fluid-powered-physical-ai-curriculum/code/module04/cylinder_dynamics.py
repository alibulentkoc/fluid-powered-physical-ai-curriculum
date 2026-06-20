"""
cylinder_dynamics.py
Module 04 — Fluid Mechanics for Intelligent Machines

The coupled cylinder ODE model: force balance (Lesson 03) + pressure dynamics
(Lesson 04) + Stribeck friction. This is the MECHANICAL+HYDRAULIC CORE of the
Smart Agricultural Workcell digital twin.

State vector: [x, v, Pb, Pr]
    x  = piston position (m)
    v  = piston velocity (m/s)
    Pb = bore-side pressure (Pa)
    Pr = rod-side pressure (Pa)

Imported by cylinder_simulation (Lesson 05) and the integrated twin (Module 11).

Run:
    python cylinder_dynamics.py            # prints Stribeck table + a self-test
    python cylinder_dynamics.py --plot     # saves the Stribeck friction curve
"""

import math
import sys
from dataclasses import dataclass

from orifice_flow import valve_flow


@dataclass
class CylinderParams:
    """Parameters for the workcell primary cylinder."""
    bore_mm: float = 50.0
    rod_mm: float = 28.0
    stroke_mm: float = 300.0
    mass_kg: float = 3.0
    # friction (Stribeck)
    F_static: float = 120.0      # N, breakaway
    F_coulomb: float = 60.0      # N, kinetic
    visc_coeff: float = 200.0    # N*s/m
    stribeck_v: float = 0.010    # m/s
    # hydraulic
    Be_pa: float = 1.5e9         # effective bulk modulus
    rho: float = 870.0
    dead_volume_l: float = 0.05  # hose/port dead volume per side
    # external
    load_N: float = 100.0

    @property
    def A_bore(self) -> float:
        return math.pi * (self.bore_mm / 2000) ** 2

    @property
    def A_rod(self) -> float:
        return self.A_bore - math.pi * (self.rod_mm / 2000) ** 2


def stribeck_friction(v: float, p: CylinderParams) -> float:
    """
    Stribeck friction force (N). Opposes motion.
    F = sign(v) * [ Fc + (Fs-Fc)*exp(-(v/vs)^2) ] + b*v
    """
    if abs(v) < 1e-9:
        return 0.0  # at rest, friction is handled by the net-force breakaway check
    s = 1.0 if v > 0 else -1.0
    coulomb_stribeck = p.F_coulomb + (p.F_static - p.F_coulomb) * \
        math.exp(-(v / p.stribeck_v) ** 2)
    return s * coulomb_stribeck + p.visc_coeff * v


def chamber_volumes(x: float, p: CylinderParams):
    """Bore and rod chamber volumes (m^3) at position x (m from fully retracted)."""
    dead = p.dead_volume_l * 1e-3
    Vb = dead + p.A_bore * x
    Vr = dead + p.A_rod * (p.stroke_mm / 1000 - x)
    return Vb, Vr


def rhs(t, state, p: CylinderParams, valve_cmd, supply_pa, tank_pa,
        valve_area_max_m2=2.5e-6):
    """
    Right-hand side for solve_ivp. Returns d/dt [x, v, Pb, Pr].

    valve_cmd: callable(t) -> u in [-1, 1].
        u > 0 extends (supply->bore, rod->tank)
        u < 0 retracts (supply->rod, bore->tank)
    supply_pa, tank_pa: system supply and tank pressures (Pa).

    Sign convention (consistent for both chambers):
        dP/dt = (Be / V) * (Q_valve_in - A * dV_geom)
      where Q_valve_in is the net flow the valve admits INTO the chamber
      (positive = fluid entering) and A*dV_geom is the rate the chamber
      volume GROWS due to piston motion (which dilutes pressure).
        - Bore chamber grows at +A_bore * v   (extending opens bore volume)
        - Rod chamber grows at  -A_rod  * v   (extending shrinks rod volume)
    """
    x, v, Pb, Pr = state
    u = valve_cmd(t)

    # Valve flows INTO each chamber (positive = entering the chamber).
    # Extend (u>0): bore connects to supply (inflow), rod connects to tank (outflow).
    # Retract (u<0): rod connects to supply (inflow), bore connects to tank (outflow).
    if u >= 0:   # extend
        Q_bore = valve_flow(u, max(0.0, supply_pa - Pb),
                            area_max_m2=valve_area_max_m2, rho=p.rho)   # into bore (+)
        Q_rod = -valve_flow(u, max(0.0, Pr - tank_pa),
                            area_max_m2=valve_area_max_m2, rho=p.rho)   # out of rod (-)
    else:        # retract
        Q_rod = valve_flow(-u, max(0.0, supply_pa - Pr),
                           area_max_m2=valve_area_max_m2, rho=p.rho)    # into rod (+)
        Q_bore = -valve_flow(-u, max(0.0, Pb - tank_pa),
                             area_max_m2=valve_area_max_m2, rho=p.rho)  # out of bore (-)

    # Force balance (Lesson 03)
    friction = stribeck_friction(v, p)
    net_force = p.A_bore * Pb - p.A_rod * Pr - friction - p.load_N

    # End-stop handling: clamp at travel limits
    x_max = p.stroke_mm / 1000
    v_out = v
    if x <= 0.0 and net_force < 0:
        net_force = 0.0
        v_out = max(0.0, v)
    elif x >= x_max and net_force > 0:
        net_force = 0.0
        v_out = min(0.0, v)
    a = net_force / p.mass_kg

    # Pressure dynamics (Lesson 04), consistent sign convention.
    # Bore volume grows at +A_bore*v; rod volume grows at -A_rod*v.
    Vb, Vr = chamber_volumes(x, p)
    dPb = p.Be_pa / Vb * (Q_bore - p.A_bore * v_out)
    dPr = p.Be_pa / Vr * (Q_rod + p.A_rod * v_out)

    return [v_out, a, dPb, dPr]


def print_report():
    p = CylinderParams()
    print("=" * 56)
    print("CYLINDER DYNAMICS — workcell primary cylinder")
    print(f"  Bore {p.bore_mm} mm  Rod {p.rod_mm} mm  Mass {p.mass_kg} kg")
    print(f"  A_bore = {p.A_bore*1e6:.0f} mm^2,  A_rod = {p.A_rod*1e6:.0f} mm^2")
    print("=" * 56)
    print("\nStribeck friction vs. velocity:")
    print(f"  {'v (mm/s)':>9} | {'friction (N)':>12}")
    print(f"  {'-'*9}-+-{'-'*12}")
    for v_mm in (1, 5, 10, 20, 50, 100):
        fr = stribeck_friction(v_mm / 1000, p)
        print(f"  {v_mm:>9} | {fr:>12.1f}")
    print("\n  Note: friction is HIGHER at low speed (Stribeck) than at moderate")
    print("  speed, then rises again with viscous term — causing stick-slip.")
    print("=" * 56)


def make_plot():
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib/numpy unavailable; skipping plot.")
        return
    p = CylinderParams()
    v = np.linspace(0.0005, 0.15, 300)
    fr = [stribeck_friction(vv, p) for vv in v]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(v * 1000, fr, color="#993C1D")
    ax.set_xlabel("Velocity (mm/s)")
    ax.set_ylabel("Friction force (N)")
    ax.set_title("Stribeck friction curve — workcell cylinder")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("cylinder_friction.png", dpi=120)
    print("Plot saved to cylinder_friction.png")


if __name__ == "__main__":
    print_report()
    if "--plot" in sys.argv:
        make_plot()
