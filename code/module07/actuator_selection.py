"""
actuator_selection.py
Module 07 — Producing the Machine's Force and Motion

The cylinder-vs-motor decision logic and hydraulic motor sizing for the
Smart Agricultural Workcell. Matches actuator type to each task's requirements.

Run:
    python actuator_selection.py
"""

import math


def choose_actuator(motion, continuous=False, needs_position_hold=False):
    """Select actuator type from task motion requirements."""
    if motion == "linear":
        return "CYLINDER (linear force, position hold, finite stroke)"
    if motion == "rotary":
        if continuous:
            return "MOTOR (continuous rotation, speed control)"
        if needs_position_hold:
            return "MOTOR + brake (rotary position hold)"
        return "MOTOR (large-angle rotation)"
    return "unknown"


def motor_pressure_bar(torque_Nm, displacement_cc, mech_eff=0.9):
    """Pressure to produce a torque from a hydraulic motor."""
    Dm = displacement_cc * 1e-6
    dP = 2*math.pi*torque_Nm / (Dm * mech_eff)
    return dP / 1e5


def motor_flow_lpm(speed_rpm, displacement_cc, vol_eff=0.92):
    """Flow to spin a motor at a given speed."""
    return speed_rpm * displacement_cc / 1000 / vol_eff


if __name__ == "__main__":
    print("=" * 60)
    print("THE MACHINE'S ACTUATOR SELECTION (per task)")
    print("=" * 60)
    tasks = [
        ("primary positioning", "linear", False, True),
        ("gripping", "linear", False, True),
        ("continuous spin", "rotary", True, False),
        ("part rotation", "rotary", False, False),
    ]
    for name, motion, cont, hold in tasks:
        print(f"  {name:20s} -> {choose_actuator(motion, cont, hold)}")

    print("\n  Motor sizing example (rotary task):")
    for T, Dm in [(5, 4), (8, 6)]:
        p = motor_pressure_bar(T, Dm)
        print(f"    {T} N*m, {Dm} cc/rev -> {p:.0f} bar "
              f"({'OK' if p <= 100 else 'EXCEEDS 100 bar'})")
    print(f"    60 RPM, 6 cc/rev -> {motor_flow_lpm(60, 6):.2f} LPM "
          f"(pump has 10.67 LPM - ample)")
    print("=" * 60)
