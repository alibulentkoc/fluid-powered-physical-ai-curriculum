"""
workcell_twin.py
Module 11 — The Integrated Digital Twin

Assembles the pump (M05), valve (M06), and cylinder (M07) models into ONE
runnable digital twin of the Smart Agricultural Workcell, with a shared state
vector. Runs in simulation mode (hypothetical inputs) or twin mode (fed real
logged inputs).

Run:
    python workcell_twin.py
"""

import math

# Machine parameters (verified across Modules 04-10)
A_BORE = math.pi * 25 ** 2
A_ROD = A_BORE - math.pi * 14 ** 2
PUMP_LPM = 10.67
SYSTEM_BAR = 100.0
CIRCUIT_DROP_BAR = 6.54

MEASURED_STATES = {"position", "bore_pressure", "rod_pressure",
                   "grip_force", "supply_flow"}
INFERRED_STATES = {"friction_coeff", "valve_deadband", "leakage_coeff"}


class WorkcellTwin:
    """The integrated digital twin: one model of the whole machine."""

    def __init__(self, friction=120.0, deadband=0.02, leakage=0.0):
        # shared state vector
        self.position = 0.0      # mm
        self.velocity = 0.0      # mm/s
        self.bore_pressure = 0.0
        self.rod_pressure = 0.0
        # inferred parameters (fitted in Lesson 04)
        self.friction = friction
        self.deadband = deadband
        self.leakage = leakage

    def step(self, valve_command, dt=0.01, load_N=800.0):
        """Advance the integrated model one timestep given a valve command."""
        u = valve_command
        p_supply = SYSTEM_BAR - CIRCUIT_DROP_BAR
        if abs(u) < self.deadband:
            u_eff = 0.0
        else:
            u_eff = u
        # valve routes flow; cylinder responds (coupled subsystems)
        if u_eff > 0:        # extend
            flow = PUMP_LPM * u_eff * (1 - self.leakage)
            self.velocity = flow * 1e6 / 60 / A_BORE
            self.bore_pressure = p_supply
            self.rod_pressure = 3.0
        elif u_eff < 0:      # retract
            flow = PUMP_LPM * abs(u_eff) * (1 - self.leakage)
            self.velocity = -(flow * 1e6 / 60 / A_ROD)
            self.bore_pressure = 3.0
            self.rod_pressure = p_supply
        else:                # hold (closed center)
            self.velocity = 0.0
            self.bore_pressure = 115.0   # relief during hold
        self.position += self.velocity * dt
        self.position = max(0.0, min(300.0, self.position))
        return self.state()

    def state(self):
        return {
            "position": round(self.position, 2),
            "velocity": round(self.velocity, 1),
            "bore_pressure": round(self.bore_pressure, 1),
            "rod_pressure": round(self.rod_pressure, 1),
        }

    def force(self):
        return (self.bore_pressure * A_BORE - self.rod_pressure * A_ROD) * 0.1


if __name__ == "__main__":
    print("=" * 56)
    print("THE INTEGRATED DIGITAL TWIN (workcell_twin.py)")
    print("=" * 56)
    print(f"\n  Measured states: {sorted(MEASURED_STATES)}")
    print(f"  Inferred states: {sorted(INFERRED_STATES)}")

    print("\n  Running the assembled twin (extend -> hold -> retract):")
    twin = WorkcellTwin()
    commands = [(1.0, 80), (0.0, 30), (-1.0, 60)]  # (command, n_steps)
    for cmd, n in commands:
        for _ in range(n):
            twin.step(cmd)
        s = twin.state()
        label = {1.0: "extend", 0.0: "hold", -1.0: "retract"}[cmd]
        print(f"    after {label:8s}: pos {s['position']:6.1f} mm, "
              f"force {twin.force()/1000:5.2f} kN")
    print("=" * 56)
