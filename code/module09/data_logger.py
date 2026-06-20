"""
data_logger.py
Module 09 — Sensing (the machine perceives)

The Smart Agricultural Workcell's data pipeline: log a task cycle and compare
measured signals to the digital twin's prediction (the residual). Closes the
loop between the physical machine and its digital model.

Run:
    python data_logger.py
"""

import math
import random
import csv
import io


def twin_position(t):
    """Twin-predicted position over a task cycle (mm)."""
    if t < 1.66:
        return 90.6 * t
    elif t < 2.66:
        return 150.0
    elif t < 3.8:
        return max(0.0, 150.0 - 131.9 * (t - 2.66))
    return 0.0


def log_cycle(n=400, dt=0.01, seed=2):
    """Generate a logged cycle: time, measured position, twin position."""
    random.seed(seed)
    rows = []
    for k in range(n):
        t = k * dt
        twin = max(0.0, min(150.0, twin_position(t)))
        measured = twin + random.uniform(-1.5, 1.5)
        rows.append((round(t, 3), round(measured, 2), round(twin, 2)))
    return rows


def to_csv(rows):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["t_s", "position_measured_mm", "position_twin_mm"])
    w.writerows(rows)
    return buf.getvalue()


def rms_residual(rows):
    res = [m - tw for _, m, tw in rows]
    return math.sqrt(sum(r * r for r in res) / len(res))


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S DATA PIPELINE (sensor -> twin)")
    print("=" * 56)
    rows = log_cycle()
    csv_text = to_csv(rows)
    print(f"\n  Logged {len(rows)} samples over {rows[-1][0]:.1f} s")
    print("  CSV head:")
    for line in csv_text.splitlines()[:4]:
        print(f"    {line}")
    rms = rms_residual(rows)
    print(f"\n  Position RMS residual vs twin: {rms:.2f} mm "
          f"over 150 mm ({rms/150*100:.1f}%)")
    print(f"  Twin verdict: "
          f"{'EXCELLENT (faithful mirror)' if rms/150 < 0.02 else 'needs refinement'}")
    print("=" * 56)
