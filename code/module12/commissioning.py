"""
commissioning.py
Module 12 — The Complete Autonomous Workcell (CAPSTONE)

Commissions the Smart Agricultural Workcell in dependency order, confirming each
subsystem on a foundation of confirmed ones, and isolating any fault to its
subsystem.

Run:
    python commissioning.py
"""

# Commissioning order: each subsystem depends on the ones before it
ORDER = [
    ("hydraulic_power", "pressure to 100 bar, no leak, relief at 115 bar"),
    ("fluid_transport", "fluid reaches valves, returns through filter, no leak"),
    ("motion_control",  "cylinder extends/holds/retracts open-loop"),
    ("actuation",       "both actuators full stroke, force as expected"),
    ("sensing",         "all sensors calibrated, logging at >=10 Hz"),
    ("control_and_twin","position step meets spec; twin connected + validated"),
]


def commission(confirmed):
    """Bring up subsystems in order; halt and isolate the first failure."""
    log = []
    for sub, test in ORDER:
        ok = confirmed.get(sub, False)
        log.append((sub, test, ok))
        if not ok:
            return False, sub, log
    return True, None, log


def print_run(title, confirmed):
    print(f"\n  {title}")
    done, fault, log = commission(confirmed)
    for sub, test, ok in log:
        mark = "PASS" if ok else "HALT"
        print(f"    [{mark}] {sub:18s} -- {test}")
        if not ok:
            break
    if done:
        print("    => ALL SUBSYSTEMS CONFIRMED — machine commissioned")
    else:
        print(f"    => fault ISOLATED to '{fault}' "
              f"(all prior subsystems confirmed)")


if __name__ == "__main__":
    print("=" * 64)
    print("WORKCELL COMMISSIONING (dependency-ordered bring-up)")
    print("=" * 64)

    all_ok = {sub: True for sub, _ in ORDER}
    print_run("Fully working machine:", all_ok)

    faulty = dict(all_ok); faulty["sensing"] = False
    print_run("Machine with a sensing fault:", faulty)
    print("\n" + "=" * 64)
