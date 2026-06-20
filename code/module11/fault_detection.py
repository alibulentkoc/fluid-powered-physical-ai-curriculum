"""
fault_detection.py
Module 11 — The Integrated Digital Twin

Residual-based fault detection and classification for the Smart Agricultural
Workcell twin: threshold detection, trend detection, and classifying faults
from their residual signatures.

Run:
    python fault_detection.py
"""


def detect_threshold(residual, sigma, k=3):
    """Flag if the instantaneous residual exceeds k-sigma."""
    return abs(residual) > k * sigma


def detect_trend(residual_history, slope_threshold=0.05):
    """Flag a slow fault from a significant residual slope (least squares)."""
    n = len(residual_history)
    if n < 3:
        return False, 0.0
    xs = list(range(n))
    mx = sum(xs) / n
    my = sum(residual_history) / n
    num = sum((xs[i] - mx) * (residual_history[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    slope = num / den if den else 0.0
    return abs(slope) > slope_threshold, slope


def classify_fault(pos_slope, pressure_slope, extend_resid, retract_resid,
                   noise=0.5):
    """Identify a fault from its residual signature."""
    flags = []
    if abs(pressure_slope) > 0.1:
        flags.append("SEAL LEAK (pressure residual ramping)")
    if abs(pos_slope) > 0.05 and abs(pressure_slope) < 0.1:
        flags.append("SENSOR DRIFT (position residual ramps, pressure normal)")
    if abs(abs(extend_resid) - abs(retract_resid)) > 3 * noise:
        flags.append("VALVE HYSTERESIS (asymmetric residual)")
    return flags if flags else ["HEALTHY"]


if __name__ == "__main__":
    print("=" * 60)
    print("THE TWIN'S FAULT DETECTION (residual signatures)")
    print("=" * 60)

    print("\n  Trend detection (sensor drift, +0.2 mm/cycle):")
    drift = [0.2 * i for i in range(10)]
    flagged, slope = detect_trend(drift)
    print(f"    slope {slope:.2f} mm/cycle -> "
          f"{'FAULT FLAGGED' if flagged else 'ok'}")

    print("\n  Fault classification from signatures:")
    cases = [
        ("healthy",         0.0,  0.0,  0.3, 0.3),
        ("sensor drift",    0.2,  0.0,  0.3, 0.3),
        ("seal leak",       0.0, -0.3,  0.3, 0.3),
        ("valve hysteresis",0.0,  0.0,  0.5, 3.0),
    ]
    for name, ps, prs, ext, ret in cases:
        result = classify_fault(ps, prs, ext, ret)
        print(f"    {name:16s} -> {result[0]}")
    print("=" * 60)
