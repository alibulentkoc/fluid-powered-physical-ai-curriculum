"""
state_machine.py
Module 10 — Embedded Control (the machine decides and acts)

The Smart Agricultural Workcell's autonomous task logic: a finite state machine
(IDLE -> APPROACH -> GRIP -> LIFT -> MOVE -> RELEASE) with sensor-driven guards,
plus independent safety logic (pressure/position limits, watchdog) that overrides
the task to FAULT.

Run:
    python state_machine.py
"""


class WorkcellStateMachine:
    FLOW = {"IDLE": "APPROACH", "APPROACH": "GRIP", "GRIP": "LIFT",
            "LIFT": "MOVE", "MOVE": "RELEASE", "RELEASE": "IDLE"}

    def __init__(self, p_limit=118.0, x_limit=295.0, watchdog_ms=200):
        self.state = "IDLE"
        self.p_limit = p_limit
        self.x_limit = x_limit
        self.watchdog_ms = watchdog_ms

    def safety_check(self, pressure, position, ms_since_comm):
        if pressure > self.p_limit:
            return "over-pressure"
        if position > self.x_limit:
            return "over-travel"
        if ms_since_comm > self.watchdog_ms:
            return "watchdog (comm lost)"
        return None

    def step(self, sensors, guard_met):
        fault = self.safety_check(sensors["P"], sensors["x"], sensors["comm_ms"])
        if fault:
            self.state = "FAULT"
            return self.state, fault
        if guard_met and self.state in self.FLOW:
            self.state = self.FLOW[self.state]
        return self.state, None

    def recover(self):
        if self.state == "FAULT":
            self.state = "IDLE"


if __name__ == "__main__":
    print("=" * 56)
    print("THE MACHINE'S AUTONOMOUS TASK (state machine + safety)")
    print("=" * 56)
    sm = WorkcellStateMachine()
    print("\n  Normal task progression:")
    for _ in range(6):
        state, _ = sm.step({"P": 95, "x": 150, "comm_ms": 50}, guard_met=True)
        print(f"    -> {state}")

    print("\n  Safety event (pressure spike to 125 bar):")
    state, fault = sm.step({"P": 125, "x": 150, "comm_ms": 50}, guard_met=True)
    print(f"    -> {state}  ({fault})")
    sm.recover()
    print(f"    after recovery -> {sm.state}")

    print("\n  Watchdog event (comm lost 300 ms):")
    sm2 = WorkcellStateMachine()
    sm2.step({"P": 95, "x": 150, "comm_ms": 50}, guard_met=True)  # APPROACH
    state, fault = sm2.step({"P": 95, "x": 150, "comm_ms": 300}, guard_met=False)
    print(f"    -> {state}  ({fault})")
    print("=" * 56)
