"""
task_sequencer.py
Module 08 — Integrating the Machine's Hydraulic Circuit

The Smart Agricultural Workcell's pick-and-place task sequence: ordered steps
with completion conditions, single-actuator-at-a-time flow allocation, and
cycle-time / throughput computation. Skeleton of the Module 10 state machine.

Run:
    python task_sequencer.py
"""

import math

A_BORE = math.pi * 25 ** 2
A_ROD = A_BORE - math.pi * 14 ** 2
PUMP_LPM = 10.67


def stroke_time_s(distance_mm, area_mm2):
    """Time for the active actuator to travel a distance at full pump flow."""
    v_mm_s = PUMP_LPM * 1e6 / 60 / area_mm2
    return distance_mm / v_mm_s


def pick_and_place(position_mm=150, move_mm=150, grip_s=0.5,
                   release_s=0.5, transition_s=0.2):
    """Define and time the machine's pick-and-place sequence."""
    steps = [
        ("position", "primary cylinder", stroke_time_s(position_mm, A_BORE)),
        ("grip",     "end-effector",     grip_s),
        ("move",     "primary cylinder", stroke_time_s(move_mm, A_ROD)),
        ("release",  "end-effector",     release_s),
    ]
    t = 0.0
    timeline = []
    for name, actuator, dur in steps:
        timeline.append((t, name, actuator, dur))
        t += dur + transition_s
    return timeline, t


if __name__ == "__main__":
    print("=" * 60)
    print("THE MACHINE'S PICK-AND-PLACE SEQUENCE")
    print("=" * 60)
    timeline, total = pick_and_place()
    for start, name, actuator, dur in timeline:
        print(f"  [{start:4.1f}s] {name:9s}: {actuator:16s} ({dur:.2f}s)")
    print(f"\n  Total cycle: {total:.1f} s  ->  {60/total:.0f} cycles/min")
    print("  (one actuator at a time, each at full pump flow)")
    print("=" * 60)
