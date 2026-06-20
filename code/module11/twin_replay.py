"""
twin_replay.py
Module 11 — The Integrated Digital Twin

Runs the workcell twin in REPLAY mode against a logged task cycle: aligns time
axes, resamples mismatched rates, feeds logged inputs, and compares predicted
vs. measured outputs.

Run:
    python twin_replay.py
"""

import math
from workcell_twin import WorkcellTwin


def resample(log_times, log_values, target_times):
    """Linear-interpolate logged data onto the twin's time grid."""
    out = []
    for t in target_times:
        if t <= log_times[0]:
            out.append(log_values[0]); continue
        if t >= log_times[-1]:
            out.append(log_values[-1]); continue
        for i in range(len(log_times) - 1):
            if log_times[i] <= t <= log_times[i + 1]:
                frac = (t - log_times[i]) / (log_times[i + 1] - log_times[i])
                out.append(log_values[i] + frac * (log_values[i + 1] - log_values[i]))
                break
    return out


def generate_log(dt=0.01, n=400):
    """A synthetic logged task cycle (command + measured position)."""
    twin = WorkcellTwin(friction=125.0)   # 'real machine' slightly diff friction
    times, commands, measured = [], [], []
    for k in range(n):
        t = k * dt
        if t < 0.8: cmd = 1.0       # extend
        elif t < 1.8: cmd = 0.0     # hold
        elif t < 2.4: cmd = -1.0    # retract
        else: cmd = 0.0
        twin.step(cmd, dt)
        times.append(t); commands.append(cmd)
        # add small measurement noise
        measured.append(twin.position + (0.5 * math.sin(k)))
    return times, commands, measured


def replay(times, commands, measured, dt=0.01):
    """Feed logged commands to a fresh twin; compare predicted vs measured."""
    twin = WorkcellTwin(friction=120.0)   # twin's (slightly off) friction
    residuals = []
    for t, cmd, meas in zip(times, commands, measured):
        twin.step(cmd, dt)
        residuals.append(meas - twin.position)
    rms = math.sqrt(sum(r * r for r in residuals) / len(residuals))
    return rms, residuals


if __name__ == "__main__":
    print("=" * 56)
    print("TWIN REPLAY (synchronized comparison)")
    print("=" * 56)
    times, commands, measured = generate_log()
    rms, residuals = replay(times, commands, measured)
    print(f"\n  Replayed {len(times)} samples over {times[-1]:.1f} s")
    print(f"  Position RMS residual: {rms:.2f} mm over 150 mm "
          f"({rms/150*100:.1f}%)")
    verdict = "synchronized (faithful mirror)" if rms/150 < 0.03 else "needs refinement"
    print(f"  Twin verdict: {verdict}")
    print("\n  Resampling demo (50 Hz log -> 100 Hz twin grid):")
    aligned = resample([0, 0.02, 0.04], [0, 1.8, 3.6],
                       [0, 0.01, 0.02, 0.03, 0.04])
    print(f"    {[round(a,2) for a in aligned]}")
    print("=" * 56)
