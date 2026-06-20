"""
twin_dashboard.py
Module 11 — The Integrated Digital Twin

A monitoring dashboard for the Smart Agricultural Workcell twin. Text-based
summary here; with --plot, renders the operator panels (position tracking,
pressure, residuals, fault flags). Runs in replay on logged data.

Run:
    python twin_dashboard.py
    python twin_dashboard.py --plot
"""

import sys
import math
from workcell_twin import WorkcellTwin


def run_dashboard_data(dt=0.01, n=300, inject_fault=False):
    """Generate dashboard data: command, measured, predicted, residual, flags."""
    real = WorkcellTwin(friction=125.0)
    twin = WorkcellTwin(friction=124.0)   # well-fitted
    data = {"t": [], "cmd": [], "measured": [], "predicted": [],
            "residual": [], "flag": []}
    for k in range(n):
        t = k * dt
        cmd = 1.0 if t < 1.2 else (0.0 if t < 2.0 else -1.0)
        real.step(cmd, dt)
        twin.step(cmd, dt)
        meas = real.position
        if inject_fault and t > 1.5:
            meas += 4.0 * (t - 1.5)        # sensor drift, 4 mm/s ramp
        resid = meas - twin.position
        flag = abs(resid) > 3 * 0.5
        for key, val in [("t", t), ("cmd", cmd), ("measured", meas),
                         ("predicted", twin.position), ("residual", resid),
                         ("flag", flag)]:
            data[key].append(val)
    return data


def text_summary(data):
    rms = math.sqrt(sum(r*r for r in data["residual"]) / len(data["residual"]))
    flags = sum(data["flag"])
    print(f"  samples: {len(data['t'])}, duration {data['t'][-1]:.1f} s")
    print(f"  position RMS residual: {rms:.2f} mm")
    print(f"  fault flags raised: {flags}")
    print(f"  status: {'FAULT DETECTED' if flags > 5 else 'HEALTHY'}")


def make_plots(data):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib unavailable; skipping plots."); return
    fig, ax = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    t = data["t"]
    ax[0].plot(t, data["measured"], label="measured", color="#185FA5")
    ax[0].plot(t, data["predicted"], "--", label="twin", color="#C0392B")
    ax[0].set_ylabel("position (mm)"); ax[0].legend(); ax[0].set_title("Position tracking")
    ax[1].plot(t, data["residual"], color="#8E44AD")
    ax[1].axhline(1.5, ls=":", color="gray"); ax[1].axhline(-1.5, ls=":", color="gray")
    ax[1].set_ylabel("residual (mm)"); ax[1].set_title("Residual (with thresholds)")
    ax[2].plot(t, [1 if f else 0 for f in data["flag"]], color="#C0392B")
    ax[2].set_ylabel("fault flag"); ax[2].set_xlabel("time (s)")
    ax[2].set_title("Fault flags")
    fig.tight_layout(); fig.savefig("twin_dashboard.png", dpi=120)
    print("Dashboard saved to twin_dashboard.png")


if __name__ == "__main__":
    print("=" * 56)
    print("THE TWIN'S MONITORING DASHBOARD")
    print("=" * 56)
    print("\n  Healthy machine:")
    text_summary(run_dashboard_data(inject_fault=False))
    print("\n  With injected sensor drift:")
    data = run_dashboard_data(inject_fault=True)
    text_summary(data)
    if "--plot" in sys.argv:
        make_plots(data)
    print("=" * 56)
