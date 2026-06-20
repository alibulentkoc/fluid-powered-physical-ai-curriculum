"""
cleanliness_calculator.py
Module 03 — Hydraulic Fluids and Energy Transmission

Maps hydraulic components to their ISO 4406 cleanliness targets, recommends a
minimum filter Beta ratio, and shows filter efficiency and particles-passed.

Run:
    python cleanliness_calculator.py
"""

# Typical ISO 4406 cleanliness targets by component sensitivity
COMPONENT_TARGETS = {
    "gear_pump":         "20/18/15",
    "solenoid_valve":    "18/16/13",
    "proportional_valve":"17/15/12",
    "servo_valve":       "16/14/11",
}

# Minimum recommended filter Beta_10 to achieve/hold each target
TARGET_MIN_BETA10 = {
    "20/18/15": 25,
    "18/16/13": 100,
    "17/15/12": 200,
    "16/14/11": 1000,
}


def efficiency(beta: float) -> float:
    """Filter capture efficiency (%) at the rated micron size."""
    return (1 - 1 / beta) * 100


def particles_passed(beta: float, particles_in: int) -> float:
    """Number of particles passing the filter, given particles upstream."""
    return particles_in / beta


def recommend_for_component(component: str) -> dict:
    """Return target code and minimum Beta_10 for a component."""
    target = COMPONENT_TARGETS[component]
    return {
        "component": component,
        "iso_target": target,
        "min_beta10": TARGET_MIN_BETA10[target],
    }


def system_target(components: list[str]) -> dict:
    """The most sensitive component sets the system target."""
    # order from least to most sensitive
    order = ["gear_pump", "solenoid_valve", "proportional_valve", "servo_valve"]
    most_sensitive = max(components, key=lambda c: order.index(c))
    return recommend_for_component(most_sensitive)


if __name__ == "__main__":
    print("=" * 56)
    print("ISO 4406 CLEANLINESS CALCULATOR")
    print("=" * 56)
    print("\nComponent targets:")
    for comp, target in COMPONENT_TARGETS.items():
        beta = TARGET_MIN_BETA10[target]
        print(f"  {comp:20s} -> {target}  (min Beta_10 = {beta})")

    print("\nFilter efficiency and particles passed (of 1,000,000 >10um):")
    print(f"  {'Beta_10':>8} | {'Efficiency':>11} | {'Passed':>10}")
    print(f"  {'-'*8}-+-{'-'*11}-+-{'-'*10}")
    for beta in (25, 75, 100, 200, 1000):
        print(f"  {beta:>8} | {efficiency(beta):>9.2f}% | "
              f"{particles_passed(beta, 1_000_000):>10,.0f}")

    print("\nWorkcell (solenoid DCV is most sensitive component):")
    rec = system_target(["gear_pump", "solenoid_valve"])
    print(f"  System target: {rec['iso_target']}")
    print(f"  Minimum filter: Beta_10 >= {rec['min_beta10']}")
    print("=" * 56)
