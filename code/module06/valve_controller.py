"""
valve_controller.py
Module 06 — Controlling the Machine's Motion

The Smart Agricultural Workcell's first embedded control logic: commanding the
directional valve electronically (on/off), and the proportional-valve upgrade.
This is the bridge from the digital twin's valve model to commanded motion.

Run:
    python valve_controller.py
"""

import math
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "module04"))

try:
    from orifice_flow import valve_flow
except Exception:
    # Fallback if module04 path not available
    def valve_flow(u, dp_pa, cd=0.62, area_max_m2=2.5e-6, rho=870):
        if u <= 0 or dp_pa <= 0:
            return 0.0
        return cd * area_max_m2 * max(0.0, min(1.0, u)) * math.sqrt(2 * dp_pa / rho)

BORE_MM = 50.0
ROD_MM = 28.0
A_BORE = math.pi * (BORE_MM / 2) ** 2
A_ROD = A_BORE - math.pi * (ROD_MM / 2) ** 2
FLOW_LPM = 10.67


def _vel(flow_lpm, area_mm2):
    return flow_lpm * 1e6 / 60 / area_mm2


class OnOffDCVController:
    """The machine's first embedded controller: on/off 4/3 closed-center DCV."""

    def __init__(self):
        self.solenoid_A = False
        self.solenoid_B = False

    def command(self, cmd):
        if cmd == "extend":
            self.solenoid_A, self.solenoid_B = True, False
            return f"extend at {_vel(FLOW_LPM, A_BORE):.1f} mm/s (P->A)"
        elif cmd == "retract":
            self.solenoid_A, self.solenoid_B = False, True
            return f"retract at {_vel(FLOW_LPM, A_ROD):.1f} mm/s (P->B)"
        elif cmd == "hold":
            self.solenoid_A, self.solenoid_B = False, False
            return "hold: cylinder locked (closed center)"
        return "unknown command"


class ProportionalValveController:
    """Smooth variable control: command in [-1,1] -> flow via orifice model."""

    def __init__(self, supply_bar=100.0, area_max_m2=2.5e-6):
        self.supply_pa = supply_bar * 1e5
        self.area_max = area_max_m2

    def flow_lpm(self, u, cylinder_pressure_bar=30.0):
        dp = max(0.0, self.supply_pa - cylinder_pressure_bar * 1e5)
        q = valve_flow(abs(u), dp, area_max_m2=self.area_max)
        return q * 60000 * (1 if u >= 0 else -1)

    def smooth_approach(self, distance_to_target_mm, slow_zone_mm=20.0):
        """Ramp command down as the cylinder nears the target (preview of M10)."""
        if distance_to_target_mm >= slow_zone_mm:
            return 1.0
        return max(0.15, distance_to_target_mm / slow_zone_mm)


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S FIRST EMBEDDED CONTROL")
    print("=" * 56)
    print("\nOn/off DCV command sequence:")
    ctrl = OnOffDCVController()
    for cmd in ["extend", "hold", "retract", "hold"]:
        print(f"  '{cmd:8s}' -> {ctrl.command(cmd)}")

    print("\nProportional valve — smooth approach (command vs. distance):")
    prop = ProportionalValveController()
    for d in [50, 20, 15, 10, 5, 2]:
        u = prop.smooth_approach(d)
        print(f"  {d:2d} mm to target -> command {u:.2f} "
              f"({prop.flow_lpm(u):.2f} LPM)")
    print("=" * 56)
