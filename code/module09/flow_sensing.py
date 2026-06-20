"""
flow_sensing.py
Module 09 — Sensing (the machine perceives)

Flow sensing and residual-based self-diagnosis for the Smart Agricultural
Workcell: turbine meter, leakage residual, detection threshold, trend prediction.

Run:
    python flow_sensing.py
"""


def flow_from_frequency(freq_hz, K=0.5):
    """Turbine flow meter: flow = K * frequency."""
    return K * freq_hz


def leak_residual(measured_lpm, expected_lpm=10.67):
    leak = expected_lpm - measured_lpm
    return leak, leak / expected_lpm * 100


def fault_status(leak_lpm, noise_floor=0.1, k_sigma=3):
    threshold = k_sigma * noise_floor
    if leak_lpm < threshold:
        return "OK"
    elif leak_lpm < 1.0:
        return "WATCH"
    return "FAULT"


def weeks_to_failure(current_leak, rate_per_week, criterion=2.0):
    if rate_per_week <= 0:
        return float("inf")
    return (criterion - current_leak) / rate_per_week


if __name__ == "__main__":
    print("=" * 60)
    print("THE MACHINE'S SELF-DIAGNOSIS (flow residual)")
    print("=" * 60)
    print(f"  {'week':>4} | {'freq':>5} | {'flow':>7} | {'leak':>6} | "
          f"{'%':>5} | status")
    data = [(1, 21.3), (4, 20.8), (8, 19.6), (12, 18.0)]
    for week, freq in data:
        q = flow_from_frequency(freq)
        leak, pct = leak_residual(q)
        print(f"  {week:>4} | {freq:>5.1f} | {q:>5.2f} L | {leak:>5.2f} L | "
              f"{pct:>4.1f}% | {fault_status(leak)}")

    rate = (1.67 - 0.02) / 11      # LPM/week over weeks 1-12
    wtf = weeks_to_failure(1.67, rate)
    print(f"\n  Leak growing ~{rate:.2f} LPM/week")
    print(f"  Predicted weeks to 2.0 LPM failure criterion: {wtf:.1f}")
    print("  -> schedule pump maintenance before then")
    print("=" * 60)
