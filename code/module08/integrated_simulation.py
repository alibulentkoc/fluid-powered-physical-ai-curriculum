"""
integrated_simulation.py
Module 08 — Integrating the Machine's Hydraulic Circuit

THE CLIMAX: combines the pump model (Module 05), valve model (Module 06), and
cylinder model (Module 07) into a single time-domain simulation of a complete
task cycle: startup -> extend -> hold -> retract -> stop.

Plots (with --plot): pressure, flow, position, and force vs. time.

This is the digital twin executing a full task for the first time -- the
physical machine, simulated end to end.

Run:
    python integrated_simulation.py
    python integrated_simulation.py --plot
"""

import sys
import math

# ---- Machine parameters (from Modules 05-07, all verified) ----
PUMP_LPM = 10.67            # actual flow (Module 05)
RELIEF_BAR = 115.0          # relief setting (Module 05/06)
BORE_MM, ROD_MM = 50.0, 28.0
A_BORE = math.pi * (BORE_MM/2)**2          # mm^2
A_ROD = A_BORE - math.pi * (ROD_MM/2)**2
STROKE_MM = 300.0
SYSTEM_BAR = 100.0
CIRCUIT_DROP_BAR = 6.54     # line+filter+valve (Module 08 L01)

# Friction (Module 07)
F_STATIC, F_COULOMB = 120.0, 70.0
V_STRIBECK, VISC_B = 10.0, 200.0

LOAD_N = 800.0              # workpiece + mechanism load


def pump_flow(t, startup_time=0.3):
    """Pump flow ramps up during startup (Module 05)."""
    if t < startup_time:
        return PUMP_LPM * (t / startup_time)
    return PUMP_LPM


def friction(v_mm_s):
    """Stribeck friction (Module 07)."""
    if abs(v_mm_s) < 1e-6:
        return F_STATIC
    s = 1 if v_mm_s > 0 else -1
    return s*(F_COULOMB + (F_STATIC-F_COULOMB)*math.exp(-(v_mm_s/V_STRIBECK)**2)) \
        + VISC_B*(v_mm_s/1000)


def simulate(dt=0.002):
    """Simulate a full task cycle. Returns time-series dict."""
    # Phases: startup+extend to 150mm, hold 1.0s, retract to 0, stop
    target_extend = 150.0
    hold_duration = 1.0

    t = 0.0
    pos = 0.0          # mm
    vel = 0.0          # mm/s
    phase = "extend"
    hold_start = None

    ts, pos_s, vel_s, pres_s, flow_s, force_s = [], [], [], [], [], []

    while True:
        q = pump_flow(t)                         # LPM available
        # Pressure available at cylinder after circuit drops
        p_supply = SYSTEM_BAR - CIRCUIT_DROP_BAR

        if phase == "extend":
            # flow drives the bore; velocity from flow/area
            vel = q * 1e6/60 / A_BORE            # mm/s
            # force balance (informational): hydraulic - load - friction
            F_hyd = p_supply * 0.1 * A_BORE
            force = F_hyd - LOAD_N - friction(vel)
            pressure = p_supply
            flow = q
            pos += vel * dt
            if pos >= target_extend:
                pos = target_extend
                phase = "hold"
                hold_start = t
        elif phase == "hold":
            vel = 0.0
            # closed-center: pump flow spills over relief, pressure at relief
            pressure = RELIEF_BAR
            flow = 0.0                            # no flow to cylinder
            force = LOAD_N                         # holding the load
            if t - hold_start >= hold_duration:
                phase = "retract"
        elif phase == "retract":
            vel = -(q * 1e6/60 / A_ROD)          # mm/s (rod side, faster)
            F_hyd = p_supply * 0.1 * A_ROD
            force = F_hyd + LOAD_N - friction(vel)  # load assists retract here
            pressure = p_supply
            flow = q
            pos += vel * dt
            if pos <= 0.0:
                pos = 0.0
                phase = "stop"
        elif phase == "stop":
            vel = 0.0
            pressure = SYSTEM_BAR - CIRCUIT_DROP_BAR
            flow = 0.0
            force = 0.0

        ts.append(t); pos_s.append(pos); vel_s.append(vel)
        pres_s.append(pressure); flow_s.append(flow); force_s.append(force/1000)

        if phase == "stop":
            # record a little tail then break
            if t > ts[0] + 0.2 and pos == 0.0:
                # add 0.3s of stop
                if ts[-1] - (hold_start or 0) > hold_duration + 0.3:
                    break
        t += dt
        if t > 20:   # safety
            break

    return {
        "t": ts, "position": pos_s, "velocity": vel_s,
        "pressure": pres_s, "flow": flow_s, "force": force_s,
    }


def summarize(data):
    print("=" * 60)
    print("INTEGRATED TASK SIMULATION — full cycle")
    print("  startup -> extend -> hold -> retract -> stop")
    print("=" * 60)
    t = data["t"]
    print(f"  Total simulated time : {t[-1]:.2f} s")
    print(f"  Peak position        : {max(data['position']):.1f} mm")
    print(f"  Peak pressure        : {max(data['pressure']):.1f} bar (hold/relief)")
    print(f"  Extend velocity      : {max(data['velocity']):.1f} mm/s")
    print(f"  Retract velocity     : {min(data['velocity']):.1f} mm/s")
    print(f"  Max force            : {max(data['force']):.2f} kN")
    # phase boundaries
    print("\n  The simulation combines:")
    print("    - pump model (Module 05): flow ramp + relief at hold")
    print("    - valve model (Module 06): closed-center hold")
    print("    - cylinder model (Module 07): force, friction, area asymmetry")
    print("=" * 60)


def make_plots(data):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib unavailable; skipping plots.")
        return
    fig, ax = plt.subplots(2, 2, figsize=(13, 8))
    t = data["t"]
    ax[0,0].plot(t, data["position"], color="#185FA5"); ax[0,0].set_title("Position (mm)")
    ax[0,1].plot(t, data["pressure"], color="#C0392B"); ax[0,1].set_title("Pressure (bar)")
    ax[1,0].plot(t, data["flow"], color="#27AE60"); ax[1,0].set_title("Flow to cylinder (LPM)")
    ax[1,1].plot(t, data["force"], color="#8E44AD"); ax[1,1].set_title("Force (kN)")
    for a in ax.flat:
        a.set_xlabel("time (s)"); a.grid(alpha=0.3)
    fig.suptitle("Smart Agricultural Workcell — full task cycle", fontsize=13)
    fig.tight_layout()
    fig.savefig("integrated_simulation.png", dpi=120)
    print("Plot saved to integrated_simulation.png")


if __name__ == "__main__":
    data = simulate()
    summarize(data)
    if "--plot" in sys.argv:
        make_plots(data)
