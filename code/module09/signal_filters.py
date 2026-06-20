"""
signal_filters.py
Module 09 — Sensing (the machine perceives)

Signal conditioning for the Smart Agricultural Workcell: moving-average and
exponential filters, the noise-vs-lag tradeoff, and filtered velocity estimation.

Run:
    python signal_filters.py
"""

import random
import statistics


def moving_average(signal, N):
    out = []
    for k in range(len(signal)):
        window = signal[max(0, k - N + 1):k + 1]
        out.append(sum(window) / len(window))
    return out


def exponential(signal, alpha):
    out = [signal[0]]
    for x in signal[1:]:
        out.append(alpha * x + (1 - alpha) * out[-1])
    return out


def ma_lag_ms(N, dt_ms):
    return (N - 1) / 2 * dt_ms


def ma_noise_factor(N):
    return 1 / N ** 0.5


def velocity_estimate(positions, dt, filt_alpha=0.4):
    """Filter THEN differentiate (the right order)."""
    filt = exponential(positions, filt_alpha)
    vel = [0.0]
    for k in range(1, len(filt)):
        vel.append((filt[k] - filt[k - 1]) / dt)
    return vel


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S SIGNAL CONDITIONING")
    print("=" * 56)
    print("\n  Noise-vs-lag tradeoff (10 ms sampling):")
    print(f"    {'filter':>10} | {'noise x':>8} | {'lag ms':>7}")
    for N in (4, 9, 25):
        print(f"    {'MA('+str(N)+')':>10} | {ma_noise_factor(N):>8.2f} | "
              f"{ma_lag_ms(N, 10):>7.0f}")

    random.seed(1)
    raw = [150 + random.uniform(-0.5, 0.5) for _ in range(50)]
    print(f"\n  Held-still position (true 150 mm):")
    print(f"    raw noise std:    {statistics.pstdev(raw):.3f} mm")
    print(f"    MA(4) noise std:  {statistics.pstdev(moving_average(raw,4)):.3f} mm")
    print(f"    exp(0.4) std:     {statistics.pstdev(exponential(raw,0.4)):.3f} mm")
    print("=" * 56)
