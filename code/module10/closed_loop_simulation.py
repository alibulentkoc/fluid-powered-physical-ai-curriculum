"""
closed_loop_simulation.py
Module 10 — Embedded Control (the machine decides and acts)

Adds the PID controller (Lesson 02) to the integrated machine model (Module 08),
simulating the full CLOSED-LOOP position step response. This is how the machine
predicts its control behavior BEFORE hardware tuning -- the digital twin as a
safe tuning environment.

Plots (with --plot): position, command, error vs. time.

Run:
    python closed_loop_simulation.py
    python closed_loop_simulation.py --plot
"""

import sys
import os
import math

sys.path.insert(0, os.path.dirname(__file__))
from pid_controller import PID

# Machine model parameters (from Modules 04-08, verified)
VEL_GAIN = 90.0          # mm/s per unit command at nominal load
DEADBAND = 0.02          # valve dead-band
F_STATIC = 120.0         # N (Module 07)


def closed_loop_step(pid, target=200.0, dt=0.01, steps=800,
                     load_friction=0.0, hold_load=0.02):
    """Simulate the machine's closed-loop position step response.

    hold_load: a constant command needed to hold position against gravity/load.
    This gives the integral term something to balance, as on the real machine.
    """
    pos, vel, peak = 0.0, 0.0, 0.0
    ts, pos_s, cmd_s, err_s = [], [], [], []
    settle_time = None
    for k in range(steps):
        t = k * dt
        error = target - pos
        u = pid.step(error, dt)
        # net command must overcome the hold load before producing motion
        u_net = u - hold_load
        u_eff = u_net if abs(u_net) > DEADBAND else 0.0
        vel = VEL_GAIN * u_eff
        if vel > 0:
            vel = max(0.0, vel - load_friction)
        elif vel < 0:
            vel = min(0.0, vel + load_friction)
        pos += vel * dt
        peak = max(peak, pos)
        if settle_time is None and abs(error) < 0.02 * target:
            settle_time = t
        ts.append(t); pos_s.append(pos); cmd_s.append(u); err_s.append(error)
    overshoot = max(0.0, (peak - target) / target * 100)
    return {
        "t": ts, "position": pos_s, "command": cmd_s, "error": err_s,
        "overshoot_pct": round(overshoot, 1),
        "final_mm": round(pos, 1),
        "steady_state_error_mm": round(target - pos, 2),
        "settle_time_s": settle_time,
    }


def summarize(data, target=200):
    print("=" * 60)
    print("CLOSED-LOOP STEP RESPONSE (PID + machine model)")
    print(f"  target {target} mm")
    print("=" * 60)
    print(f"  Final position    : {data['final_mm']} mm")
    print(f"  Overshoot         : {data['overshoot_pct']} %")
    print(f"  Steady-state error: {data['steady_state_error_mm']} mm")
    print(f"  Settling time     : {data['settle_time_s']} s")
    meets = data["overshoot_pct"] < 5 and abs(data["steady_state_error_mm"]) < 2
    print(f"\n  Meets spec (<5% overshoot, <2 mm error): {meets}")
    print("\n  This prediction is made in the twin BEFORE hardware tuning.")
    print("  Compare to actual hardware run to validate the twin (Lesson 04).")
    print("=" * 60)


def make_plots(data):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib unavailable; skipping plots.")
        return
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))
    t = data["t"]
    ax[0].plot(t, data["position"], color="#185FA5")
    ax[0].axhline(200, ls="--", color="gray"); ax[0].set_title("Position (mm)")
    ax[1].plot(t, data["command"], color="#27AE60"); ax[1].set_title("Valve command")
    ax[2].plot(t, data["error"], color="#C0392B"); ax[2].set_title("Error (mm)")
    for a in ax:
        a.set_xlabel("time (s)"); a.grid(alpha=0.3)
    fig.suptitle("Workcell closed-loop step response (predicted)", fontsize=13)
    fig.tight_layout()
    fig.savefig("closed_loop_simulation.png", dpi=120)
    print("Plot saved to closed_loop_simulation.png")


if __name__ == "__main__":
    pid = PID(0.02, 0.002, 0.04)
    data = closed_loop_step(pid)
    summarize(data)
    if "--plot" in sys.argv:
        make_plots(data)
