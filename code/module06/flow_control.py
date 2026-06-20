"""
flow_control.py
Module 06 — Controlling the Machine's Motion

Models meter-out flow control for the Smart Agricultural Workcell: the speed
control that gives the machine a controlled approach, and why meter-out (not
meter-in) is used for loads that may run away.

Run:
    python flow_control.py
"""

import math

BORE_MM = 50.0
ROD_MM = 28.0
A_BORE = math.pi * (BORE_MM / 2) ** 2
A_ROD = A_BORE - math.pi * (ROD_MM / 2) ** 2
PUMP_LPM = 10.67


def meter_out_flow_lpm(velocity_mm_s, extending=True):
    """Flow the meter-out valve passes for a target extend/retract velocity."""
    # meter-out throttles the EXIT chamber: rod side on extend, bore side on retract
    area = A_ROD if extending else A_BORE
    return velocity_mm_s * area * 60 / 1e6


def bore_fill_lpm(velocity_mm_s, extending=True):
    """Flow into the driven chamber for a target velocity."""
    area = A_BORE if extending else A_ROD
    return velocity_mm_s * area * 60 / 1e6


def spill_over_relief_lpm(velocity_mm_s, extending=True):
    """Excess pump flow spilled over the relief during slow motion."""
    return max(0.0, PUMP_LPM - bore_fill_lpm(velocity_mm_s, extending))


def metering_choice(load_type):
    """The machine's meter-in vs meter-out decision."""
    if load_type == "resisting":
        return "meter-in OR meter-out both work (load opposes motion)"
    elif load_type == "running":
        return ("meter-OUT required: load assists motion; meter-in would let "
                "the cylinder run away and cavitate")
    return "unknown load type"


if __name__ == "__main__":
    print("=" * 60)
    print("THE MACHINE'S SPEED CONTROL (meter-out flow control)")
    print("=" * 60)
    print(f"\nMeter-out flow for each extend approach speed:")
    print(f"  {'v (mm/s)':>9} | {'meter-out LPM':>13} | {'spill to relief':>15}")
    for v in (90, 50, 30, 20, 15, 10):
        mo = meter_out_flow_lpm(v)
        spill = spill_over_relief_lpm(v)
        print(f"  {v:>9} | {mo:>13.2f} | {spill:>13.1f} LPM")

    print("\nMeter-in vs meter-out decision:")
    for lt in ("resisting", "running"):
        print(f"  {lt:10s}: {metering_choice(lt)}")
    print("\n  The machine uses METER-OUT: it controls both resisting and")
    print("  running loads, so the machine can lower loads without dropping them.")
    print("=" * 60)
