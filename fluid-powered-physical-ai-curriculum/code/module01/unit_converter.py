"""
unit_converter.py
Module 01 — Foundations of Fluid Power and Physical AI

Hydraulic engineering unit conversions and a HydraulicSystem helper class.
Used throughout the curriculum. Standard library only — no dependencies.

Run directly for a self-test:
    python unit_converter.py
"""

import math
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Pressure
# ---------------------------------------------------------------------------
def bar_to_pa(bar: float) -> float:
    """Bar to Pascals. 1 bar = 100,000 Pa."""
    return bar * 1e5


def pa_to_bar(pa: float) -> float:
    """Pascals to bar."""
    return pa / 1e5


def bar_to_psi(bar: float) -> float:
    """Bar to PSI. 1 bar = 14.5038 PSI."""
    return bar * 14.5038


def psi_to_bar(psi: float) -> float:
    """PSI to bar."""
    return psi / 14.5038


# ---------------------------------------------------------------------------
# Flow rate
# ---------------------------------------------------------------------------
def lpm_to_m3s(lpm: float) -> float:
    """Litres per minute to cubic metres per second."""
    return lpm / 60_000


def m3s_to_lpm(m3s: float) -> float:
    """Cubic metres per second to litres per minute."""
    return m3s * 60_000


def gpm_to_lpm(gpm: float) -> float:
    """US gallons per minute to litres per minute. 1 GPM = 3.78541 LPM."""
    return gpm * 3.78541


def lpm_to_gpm(lpm: float) -> float:
    """Litres per minute to US gallons per minute."""
    return lpm / 3.78541


# ---------------------------------------------------------------------------
# Power
# ---------------------------------------------------------------------------
def hp_to_kw(hp: float) -> float:
    """Mechanical horsepower to kilowatts. 1 HP = 0.745700 kW."""
    return hp * 0.745700


def kw_to_hp(kw: float) -> float:
    """Kilowatts to mechanical horsepower."""
    return kw / 0.745700


# ---------------------------------------------------------------------------
# Geometry
# ---------------------------------------------------------------------------
def mm2_to_m2(mm2: float) -> float:
    """Square millimetres to square metres."""
    return mm2 / 1e6


def bore_area_mm2(diameter_mm: float) -> float:
    """Circular bore area from diameter, in square millimetres."""
    return math.pi * (diameter_mm / 2) ** 2


def annulus_area_mm2(bore_mm: float, rod_mm: float) -> float:
    """Rod-side (annular) area of a double-acting cylinder, in mm²."""
    return bore_area_mm2(bore_mm) - bore_area_mm2(rod_mm)


# ---------------------------------------------------------------------------
# HydraulicSystem helper
# ---------------------------------------------------------------------------
@dataclass
class HydraulicSystem:
    """
    A minimal hydraulic system description for first-pass workcell calculations.

    Attributes:
        pressure_bar: System pressure in bar.
        flow_lpm: Pump flow rate in litres per minute.
        bore_mm: Cylinder bore diameter in millimetres.
        rod_mm: Rod diameter in millimetres (default 0 for single-acting).
    """
    pressure_bar: float
    flow_lpm: float
    bore_mm: float
    rod_mm: float = 0.0

    def extend_force_kN(self) -> float:
        """Extend force (full bore side) in kilonewtons. F = P * A."""
        area = bore_area_mm2(self.bore_mm)              # mm²
        force_n = self.pressure_bar * 0.1 * area        # bar*0.1 = N/mm²
        return force_n / 1000

    def retract_force_kN(self) -> float:
        """Retract force (rod side) in kilonewtons."""
        area = annulus_area_mm2(self.bore_mm, self.rod_mm)
        force_n = self.pressure_bar * 0.1 * area
        return force_n / 1000

    def extend_velocity_mms(self) -> float:
        """Extend velocity in mm/s. v = Q / A."""
        flow_mm3s = self.flow_lpm * 1e6 / 60
        return flow_mm3s / bore_area_mm2(self.bore_mm)

    def retract_velocity_mms(self) -> float:
        """Retract velocity in mm/s (rod side, faster than extend)."""
        flow_mm3s = self.flow_lpm * 1e6 / 60
        return flow_mm3s / annulus_area_mm2(self.bore_mm, self.rod_mm)

    def power_kw(self) -> float:
        """Hydraulic power in kW. P = p*Q / 600 (bar, LPM)."""
        return (self.pressure_bar * self.flow_lpm) / 600

    def motor_power_kw(self, pump_efficiency: float = 0.85) -> float:
        """Required motor power, accounting for pump efficiency."""
        return self.power_kw() / pump_efficiency

    def summary(self) -> None:
        """Print a formatted summary."""
        print("=" * 46)
        print("HYDRAULIC SYSTEM SUMMARY")
        print("=" * 46)
        print(f"  Pressure        : {self.pressure_bar:.1f} bar "
              f"({bar_to_psi(self.pressure_bar):.0f} PSI)")
        print(f"  Flow rate       : {self.flow_lpm:.1f} LPM "
              f"({lpm_to_gpm(self.flow_lpm):.1f} GPM)")
        print(f"  Bore / rod      : {self.bore_mm:.0f} / {self.rod_mm:.0f} mm")
        print(f"  Extend force    : {self.extend_force_kN():.2f} kN")
        if self.rod_mm > 0:
            print(f"  Retract force   : {self.retract_force_kN():.2f} kN")
        print(f"  Extend velocity : {self.extend_velocity_mms():.1f} mm/s")
        if self.rod_mm > 0:
            print(f"  Retract velocity: {self.retract_velocity_mms():.1f} mm/s")
        print(f"  Hydraulic power : {self.power_kw():.2f} kW")
        print(f"  Motor power     : {self.motor_power_kw():.2f} kW "
              f"(at 85% pump eff.)")
        print("=" * 46)


# ---------------------------------------------------------------------------
# Self-test — the baseline Smart Agricultural Workcell operating point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    workcell = HydraulicSystem(
        pressure_bar=100.0,
        flow_lpm=10.0,
        bore_mm=50.0,
        rod_mm=25.0,
    )
    workcell.summary()

    print()
    print("Conversion spot-checks:")
    print(f"  3000 PSI = {psi_to_bar(3000):.1f} bar")
    print(f"  15 GPM   = {gpm_to_lpm(15):.1f} LPM")
    print(f"  5 HP     = {hp_to_kw(5):.2f} kW")
