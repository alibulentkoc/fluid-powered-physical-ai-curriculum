"""
pump_performance_model.py
Module 05 — Powering the Smart Agricultural Workcell

The pump model for the Smart Agricultural Workcell's digital twin. Calculates
flow, hydraulic power, efficiencies, and motor requirements; generates pump
performance curves; and produces the Hydraulic Power Unit (HPU) Design artifact.

This is the power source the Module 04 cylinder simulation feeds from. Imported
by the integrated digital twin (Module 11).

Run:
    python pump_performance_model.py            # prints HPU design + tables
    python pump_performance_model.py --plot     # also saves performance curves
"""

import sys
from dataclasses import dataclass


@dataclass
class PumpSpec:
    """The workcell's gear pump and its drive."""
    displacement_cc: float = 8.0
    speed_rpm: float = 1450.0
    vol_eff_nominal: float = 0.92      # at nominal pressure
    mech_eff: float = 0.90
    rated_pressure_bar: float = 150.0


# ---- Flow ----------------------------------------------------------------

def theoretical_flow_lpm(spec: PumpSpec, speed_rpm: float = None) -> float:
    """Q_t = D * n  (LPM)."""
    n = spec.speed_rpm if speed_rpm is None else speed_rpm
    return spec.displacement_cc * n / 1000.0


def volumetric_efficiency(spec: PumpSpec, pressure_bar: float) -> float:
    """
    Volumetric efficiency droops with pressure (internal leakage grows).
    Simple linear model anchored at the nominal value, ~100 bar.
    """
    droop_per_bar = 0.0004   # ~4% loss per 100 bar
    eta = spec.vol_eff_nominal - droop_per_bar * (pressure_bar - 100.0)
    return max(0.5, min(0.98, eta))


def actual_flow_lpm(spec: PumpSpec, pressure_bar: float = 100.0,
                    speed_rpm: float = None) -> float:
    """Q_a = Q_t * eta_v(pressure)."""
    return theoretical_flow_lpm(spec, speed_rpm) * \
        volumetric_efficiency(spec, pressure_bar)


# ---- Power ---------------------------------------------------------------

def hydraulic_power_kw(pressure_bar: float, flow_lpm: float) -> float:
    """P_hyd = p * Q / 600  (kW, with bar and LPM)."""
    return pressure_bar * flow_lpm / 600.0


def overall_efficiency(spec: PumpSpec, pressure_bar: float) -> float:
    return volumetric_efficiency(spec, pressure_bar) * spec.mech_eff


def shaft_power_kw(spec: PumpSpec, pressure_bar: float) -> float:
    """Motor shaft power required = hydraulic power / overall efficiency."""
    qa = actual_flow_lpm(spec, pressure_bar)
    p_hyd = hydraulic_power_kw(pressure_bar, qa)
    return p_hyd / overall_efficiency(spec, pressure_bar)


def cylinder_velocity_mm_s(spec: PumpSpec, bore_mm: float = 50.0,
                           pressure_bar: float = 100.0,
                           speed_rpm: float = None) -> float:
    """The machine's motion speed from pump output (continuity)."""
    import math
    qa_mm3s = actual_flow_lpm(spec, pressure_bar, speed_rpm) * 1e6 / 60.0
    area = math.pi * (bore_mm / 2) ** 2
    return qa_mm3s / area


# ---- HPU design (the artifact) -------------------------------------------

def design_hpu(spec: PumpSpec, operating_bar: float = 100.0,
               k_reservoir: float = 4.0, service_factor: float = 1.15) -> dict:
    """Produce the Hydraulic Power Unit Design artifact.

    Motor sizing uses the standard service-factor approach: a motor's
    nameplate rating P times its service factor SF gives the continuous
    capability. We require P * SF >= shaft power, i.e. P >= P_shaft / SF,
    then round up to the next standard size. This matches how bench HPU
    motors are specified in practice (and keeps the workcell on the 2.2 kW
    frame established in Modules 01-02 rather than over-provisioning)."""
    qa = actual_flow_lpm(spec, operating_bar)
    p_hyd = hydraulic_power_kw(operating_bar, qa)
    eta_o = overall_efficiency(spec, operating_bar)
    p_shaft = p_hyd / eta_o
    p_motor = standard_motor_size(p_shaft / service_factor)
    return {
        "pump_type": "Gear, fixed displacement",
        "displacement_cc_rev": spec.displacement_cc,
        "motor_speed_rpm": spec.speed_rpm,
        "actual_flow_lpm": round(qa, 2),
        "operating_pressure_bar": operating_bar,
        "hydraulic_power_kw": round(p_hyd, 2),
        "overall_efficiency": round(eta_o, 3),
        "shaft_power_kw": round(p_shaft, 2),
        "motor_power_kw": p_motor,
        "motor_with_service_factor_kw": round(p_motor * service_factor, 2),
        "reservoir_litres": round(k_reservoir * qa),
        "relief_setting_bar": round(operating_bar * 1.15),
        "heat_load_kw": round(p_shaft * (1 - eta_o), 2),
    }


def standard_motor_size(required_kw: float) -> float:
    """Round up to the next standard IEC motor size."""
    standard = [0.75, 1.1, 1.5, 2.2, 3.0, 4.0, 5.5, 7.5]
    for s in standard:
        if s >= required_kw:
            return s
    return required_kw


# ---- Reporting -----------------------------------------------------------

def print_report(spec: PumpSpec):
    print("=" * 60)
    print("HYDRAULIC POWER UNIT DESIGN — Smart Agricultural Workcell")
    print("=" * 60)
    design = design_hpu(spec)
    for k, v in design.items():
        print(f"  {k:24s}: {v}")

    print("\n--- Flow vs. motor speed (machine's speed control) ---")
    print(f"  {'RPM':>6} | {'flow LPM':>9} | {'cyl mm/s':>9}")
    for rpm in (480, 750, 1000, 1450, 2000):
        qa = actual_flow_lpm(spec, 100, rpm)
        v = cylinder_velocity_mm_s(spec, 50, 100, rpm)
        print(f"  {rpm:>6} | {qa:>9.2f} | {v:>9.1f}")

    print("\n--- Efficiency & power vs. pressure ---")
    print(f"  {'bar':>5} | {'eta_v':>6} | {'eta_o':>6} | "
          f"{'P_hyd kW':>9} | {'P_motor kW':>10}")
    for p in (50, 80, 100, 120, 150):
        ev = volumetric_efficiency(spec, p)
        eo = overall_efficiency(spec, p)
        qa = actual_flow_lpm(spec, p)
        ph = hydraulic_power_kw(p, qa)
        ps = shaft_power_kw(spec, p)
        print(f"  {p:>5} | {ev:>6.3f} | {eo:>6.3f} | {ph:>9.2f} | {ps:>10.2f}")
    print("=" * 60)


def make_plots(spec: PumpSpec):
    try:
        import numpy as np
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib/numpy unavailable; skipping plots.")
        return
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    rpm = np.linspace(300, 2500, 200)
    axes[0].plot(rpm, [actual_flow_lpm(spec, 100, r) for r in rpm], color="#185FA5")
    axes[0].axhline(10.0, ls="--", color="gray", label="10 LPM target")
    axes[0].set_xlabel("Motor speed (RPM)"); axes[0].set_ylabel("Actual flow (LPM)")
    axes[0].set_title("Flow vs. speed"); axes[0].legend(); axes[0].grid(alpha=0.3)

    p = np.linspace(20, 150, 200)
    axes[1].plot(p, [volumetric_efficiency(spec, pp) for pp in p], label="volumetric")
    axes[1].plot(p, [overall_efficiency(spec, pp) for pp in p], label="overall")
    axes[1].set_xlabel("Pressure (bar)"); axes[1].set_ylabel("Efficiency")
    axes[1].set_title("Efficiency vs. pressure"); axes[1].legend(); axes[1].grid(alpha=0.3)

    axes[2].plot(p, [hydraulic_power_kw(pp, actual_flow_lpm(spec, pp)) for pp in p],
                 label="hydraulic out")
    axes[2].plot(p, [shaft_power_kw(spec, pp) for pp in p], label="motor in")
    axes[2].set_xlabel("Pressure (bar)"); axes[2].set_ylabel("Power (kW)")
    axes[2].set_title("Power vs. pressure"); axes[2].legend(); axes[2].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig("pump_performance.png", dpi=120)
    print("Plots saved to pump_performance.png")


if __name__ == "__main__":
    spec = PumpSpec()
    print_report(spec)
    if "--plot" in sys.argv:
        make_plots(spec)
