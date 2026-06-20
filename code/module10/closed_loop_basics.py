"""
closed_loop_basics.py
Module 10 — Embedded Control (the machine decides and acts)

Open-loop vs. proportional closed-loop positioning for the Smart Agricultural
Workcell: why open-loop is inconsistent and how feedback corrects.

Run:
    python closed_loop_basics.py
"""


def open_loop(target, friction):
    """Open-loop: command a time, get an inconsistent result under friction."""
    nominal_gain = 1.0
    # friction reduces the achieved distance unpredictably
    return target * nominal_gain - friction * 3.3


def proportional(target, kp=0.02, friction=0.0, steps=500, dt=0.01,
                 vel_gain=90.0, deadband=0.02):
    pos = 0.0
    for _ in range(steps):
        u = max(-1.0, min(1.0, kp * (target - pos)))
        if abs(u) < deadband:
            u = 0.0
        vel = vel_gain * u
        if vel > 0:
            vel = max(0.0, vel - friction)
        pos += vel * dt
    return pos


def steady_state_error(u_hold, kp):
    """Proportional control's steady-state error to hold a load."""
    return u_hold / kp


if __name__ == "__main__":
    print("=" * 56)
    print("OPEN-LOOP vs CLOSED-LOOP POSITIONING (target 200 mm)")
    print("=" * 56)
    print("\n  Open-loop (cannot correct):")
    for f, label in [(0, "nominal"), (3, "cold fluid")]:
        print(f"    {label:12s}: {open_loop(200, f):.1f} mm "
              f"(error {200-open_loop(200,f):.1f} mm, uncorrectable)")

    print("\n  Proportional closed-loop (adapts):")
    for f, label in [(0, "nominal"), (3, "cold fluid")]:
        p = proportional(200, friction=f)
        print(f"    {label:12s}: {p:.1f} mm (error {200-p:.1f} mm)")

    print(f"\n  Proportional steady-state error to hold (u=0.06, kp=0.02): "
          f"{steady_state_error(0.06, 0.02):.1f} mm")
    print("  -> the integral term (PID) eliminates this")
    print("=" * 56)
