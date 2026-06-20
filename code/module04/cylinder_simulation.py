"""
cylinder_simulation.py
Module 04 — Fluid Mechanics for Intelligent Machines

The FIRST SIMULATION of the Smart Agricultural Workcell's primary cylinder.
Integrates the cylinder dynamics over time in response to a valve command,
using scipy.integrate.solve_ivp.

Two models are provided:

  * simulate_quasistatic()  — the primary, robust model. Assumes pressure
    equilibrates quickly relative to piston motion (valid for stiff, well-bled
    hydraulic fluid). Pressures are found each instant from flow continuity.
    This is a 2-state ODE [x, v]: non-stiff and reliable.

  * simulate_full()         — the advanced 4-state model [x, v, Pb, Pr] using the
    explicit pressure-dynamics ODE (Lesson 04). It is STIFF (fast pressure
    transients vs. slow motion) and is provided to demonstrate that stiffness
    is a real engineering reality, not a flaw. Use a stiff solver and expect it
    to be slower and more delicate than the quasi-static model.

This is where the digital twin first comes alive: software predicting the
cylinder's position, velocity, and pressures over time.

Run:
    python cylinder_simulation.py            # quasi-static trajectory summary
    python cylinder_simulation.py --plot     # save plots
"""

import sys
import math

from cylinder_dynamics import (CylinderParams, stribeck_friction, valve_flow,
                               rhs)


# ---------------------------------------------------------------------------
# Valve command
# ---------------------------------------------------------------------------
def extend_then_hold(t, t_extend=1.0, ramp=0.03):
    """
    Valve command in [0, 1]: ramp open over `ramp` s, hold open until t_extend,
    ramp closed, then hold (u=0). The finite ramp represents a real solenoid
    valve's shift time and avoids an unphysical instantaneous opening.
    """
    if t < ramp:
        return t / ramp
    elif t < t_extend:
        return 1.0
    elif t < t_extend + ramp:
        return 1.0 - (t - t_extend) / ramp
    else:
        return 0.0


# ---------------------------------------------------------------------------
# Quasi-static pressure model (primary)
# ---------------------------------------------------------------------------
def _pressures_quasistatic(v, u, supply_pa, tank_pa, p, area_max_m2):
    """
    Find bore and rod pressures that satisfy flow continuity at this instant.
    Bore inflow through the valve must equal A_bore*v; rod outflow A_rod*v.
    Inverts the orifice equation analytically (Q = C*sqrt(dP) -> dP = (Q/C)^2).
    """
    from cylinder_dynamics import valve_flow  # noqa
    cd, rho = 0.62, p.rho
    area = area_max_m2 * max(0.0, min(1.0, u))
    if area <= 0:
        return supply_pa, tank_pa

    def drop_for_flow(Q):
        # Q = cd*area*sqrt(2*dP/rho)  ->  dP = (Q/(cd*area))^2 * rho/2
        if Q <= 0:
            return 0.0
        return (Q / (cd * area)) ** 2 * rho / 2

    Pb = supply_pa - drop_for_flow(p.A_bore * v)      # bore: drop from supply
    Pr = tank_pa + drop_for_flow(p.A_rod * v)         # rod: drop to tank
    return Pb, Pr


def simulate_quasistatic(t_end=2.0, t_extend=1.0,
                         supply_bar=100.0, tank_bar=2.0,
                         area_max_mm2=2.0, params=None):
    """Integrate the robust 2-state quasi-static model. Returns (sol, params)."""
    from scipy.integrate import solve_ivp

    p = params or CylinderParams()
    supply_pa, tank_pa = supply_bar * 1e5, tank_bar * 1e5
    area_max_m2 = area_max_mm2 * 1e-6
    x_max = p.stroke_mm / 1000

    def f(t, y):
        x, v = y
        u = extend_then_hold(t, t_extend)
        if u < 1e-6:
            # valve closed: cylinder holds; damp any residual velocity to rest
            return [v, -v / 0.01]
        Pb, Pr = _pressures_quasistatic(v, u, supply_pa, tank_pa, p, area_max_m2)
        net = p.A_bore * Pb - p.A_rod * Pr - stribeck_friction(v, p) - p.load_N
        if (x <= 0 and net < 0) or (x >= x_max and net > 0):
            net = 0.0
        return [v, net / p.mass_kg]

    sol = solve_ivp(f, (0, t_end), [0.0, 0.0], method="RK45",
                    max_step=2e-3, rtol=1e-6, atol=1e-9, dense_output=True)
    return sol, p


# ---------------------------------------------------------------------------
# Full 4-state model (advanced; stiff)
# ---------------------------------------------------------------------------
def simulate_full(t_end=0.3, t_extend=1.0, supply_bar=100.0, tank_bar=2.0,
                  area_max_m2=2.0e-6, params=None):
    """
    Integrate the full 4-state model [x, v, Pb, Pr] with explicit pressure
    dynamics (Lesson 04). This system is STIFF: the pressure transient timescale
    (microseconds, set by bulk modulus over a small chamber volume) is far
    faster than the piston-motion timescale (seconds). That separation is a
    genuine engineering reality, not a modeling error.

    Because of the stiffness, even a BDF solver struggles to integrate this over
    long horizons — it is reliable for short windows (the initial pressure
    build-up and break-away, ~0.3 s) but may stall over a full stroke. This is
    precisely why the quasi-static model is used as the primary simulation: when
    pressure equilibrates quickly, collapsing the pressure states removes the
    stiffness and the motion integrates robustly.

    Returns (sol, params). Check sol.success — over long windows it may be False.
    """
    from scipy.integrate import solve_ivp

    p = params or CylinderParams()
    supply_pa, tank_pa = supply_bar * 1e5, tank_bar * 1e5
    y0 = [0.0, 0.0, tank_pa, tank_pa]

    def f(t, y):
        return rhs(t, y, p, lambda tt: extend_then_hold(tt, t_extend),
                   supply_pa, tank_pa, valve_area_max_m2=area_max_m2)

    sol = solve_ivp(f, (0, t_end), y0, method="BDF", max_step=1e-3,
                    rtol=1e-5, atol=1e-7, dense_output=True)
    return sol, p


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def summarize(sol, p, model="quasi-static"):
    import numpy as np
    has_P = sol.y.shape[0] == 4
    print("=" * 62)
    print(f"CYLINDER SIMULATION ({model}) — workcell primary cylinder")
    print(f"  Supply 100 bar, extend 1.0 s then hold, stroke limit "
          f"{p.stroke_mm:.0f} mm")
    print("=" * 62)
    header = f"  {'t (s)':>6} | {'x (mm)':>8} | {'v (mm/s)':>9}"
    if has_P:
        header += f" | {'Pb (bar)':>9} | {'Pr (bar)':>9}"
    print(header)
    if not sol.success:
        print(f"  [solver stopped early at t={sol.t[-1]:.4f}: {sol.message}]")
    for tq in (0.0, 0.05, 0.1, 0.25, 0.5, 1.0, 1.2, 2.0):
        if tq <= sol.t[-1]:
            y = sol.sol(tq)
            line = f"  {tq:>6.2f} | {y[0]*1000:>8.1f} | {y[1]*1000:>9.1f}"
            if has_P:
                line += f" | {y[2]/1e5:>9.1f} | {y[3]/1e5:>9.1f}"
            print(line)
    v = sol.y[1] * 1000
    print(f"\n  Peak velocity  : {np.max(np.abs(v)):.1f} mm/s")
    print(f"  Final position : {sol.y[0][-1]*1000:.1f} mm")
    print("  The cylinder extends while the valve is open, then holds when it")
    print("  closes (u=0). This is the workcell's first simulated motion.")
    print("=" * 62)


def make_plot(sol, p, fname="cylinder_simulation.png"):
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib/numpy unavailable; skipping plot.")
        return
    import numpy as np
    t = np.linspace(0, sol.t[-1], 600)
    Y = sol.sol(t)
    has_P = sol.y.shape[0] == 4
    nplots = 3 if has_P else 2
    fig, axes = plt.subplots(nplots, 1, figsize=(8, 3 * nplots), sharex=True)
    axes[0].plot(t, Y[0] * 1000, color="#185FA5")
    axes[0].set_ylabel("Position (mm)")
    axes[0].set_title("Workcell cylinder — extend then hold")
    axes[0].grid(True, alpha=0.3)
    axes[1].plot(t, Y[1] * 1000, color="#1D9E75")
    axes[1].set_ylabel("Velocity (mm/s)")
    axes[1].grid(True, alpha=0.3)
    if has_P:
        axes[2].plot(t, Y[2] / 1e5, label="bore Pb", color="#993C1D")
        axes[2].plot(t, Y[3] / 1e5, label="rod Pr", color="#BA7517")
        axes[2].set_ylabel("Pressure (bar)")
        axes[2].legend()
        axes[2].grid(True, alpha=0.3)
    axes[-1].set_xlabel("Time (s)")
    fig.tight_layout()
    fig.savefig(fname, dpi=120)
    print(f"Plot saved to {fname}")


if __name__ == "__main__":
    try:
        sol, p = simulate_quasistatic()
    except ImportError:
        print("scipy is required. Install with: pip install scipy")
        sys.exit(1)
    summarize(sol, p, model="quasi-static")
    if "--plot" in sys.argv:
        make_plot(sol, p)
