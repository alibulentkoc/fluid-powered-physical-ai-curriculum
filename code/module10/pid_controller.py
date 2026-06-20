"""
pid_controller.py
Module 10 — Embedded Control (the machine decides and acts)

The Smart Agricultural Workcell's PID position controller: discrete-time, with
anti-windup, derivative filtering, and output clamping. Tuned in simulation to
meet <5% overshoot, <2 mm steady-state error.

Run:
    python pid_controller.py
"""


class PID:
    """Discrete PID with anti-windup and output clamping."""

    def __init__(self, kp, ki, kd, u_min=-1.0, u_max=1.0, d_filter=0.5):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.u_min, self.u_max = u_min, u_max
        self.d_filter = d_filter
        self.integral = 0.0
        self.prev_error = 0.0
        self.prev_deriv = 0.0

    def step(self, error, dt):
        raw_deriv = (error - self.prev_error) / dt
        deriv = self.d_filter * raw_deriv + (1 - self.d_filter) * self.prev_deriv
        u_unclamped = self.kp * error + self.ki * self.integral + self.kd * deriv
        u = max(self.u_min, min(self.u_max, u_unclamped))
        if u == u_unclamped:          # anti-windup: integrate only if not saturated
            self.integral += error * dt
        self.prev_error = error
        self.prev_deriv = deriv
        return u


def simulate_step(pid, target=200.0, steps=800, dt=0.01, vel_gain=90.0,
                  deadband=0.02):
    """Simulate the closed-loop step response; return metrics."""
    pos, peak = 0.0, 0.0
    settle_time = None
    for k in range(steps):
        u = pid.step(target - pos, dt)
        if abs(u) < deadband:
            u = 0.0
        pos += vel_gain * u * dt
        peak = max(peak, pos)
        if settle_time is None and abs(target - pos) < 0.02 * target:
            settle_time = k * dt
    overshoot = max(0.0, (peak - target) / target * 100)
    sse = target - pos
    return {"final_mm": round(pos, 1), "overshoot_pct": round(overshoot, 1),
            "steady_state_error_mm": round(sse, 2),
            "settle_time_s": settle_time}


if __name__ == "__main__":
    print("=" * 60)
    print("THE MACHINE'S PID POSITION CONTROLLER (200 mm step)")
    print("=" * 60)
    tunings = [
        ("P only", PID(0.02, 0.0, 0.0)),
        ("P+I", PID(0.02, 0.01, 0.0)),
        ("P+I+D (tuned)", PID(0.02, 0.002, 0.04)),
    ]
    for name, pid in tunings:
        m = simulate_step(pid)
        print(f"\n  {name}:")
        print(f"    settles {m['final_mm']} mm, overshoot {m['overshoot_pct']}%, "
              f"SSE {m['steady_state_error_mm']} mm")

    print("\n  Target: <5% overshoot, <2 mm steady-state error")
    m = simulate_step(PID(0.02, 0.002, 0.04))
    ok = m["overshoot_pct"] < 5 and abs(m["steady_state_error_mm"]) < 2
    print(f"  Tuned controller meets spec: {ok}")
    print("=" * 60)
