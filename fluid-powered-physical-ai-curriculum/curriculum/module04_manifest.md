# Module 04 — Fluid Mechanics for Intelligent Machines

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 04 of 12  
**Estimated Duration:** 2.5 weeks  
**Capstone Subsystems:** 2 (Fluid Transport), 4 (Actuation), 6 (Digital Twin)  
**Pipeline Stages:** ACTUATE, VALIDATE

> **Machine mission for this module:** Teaching the Machine to Predict Its Own Behavior
>
> **Machine Capability Added:** Predict hydraulic behavior before building.
>
> **Benchmark task advanced:** Precision Positioning

---

## Module Purpose

This is the mathematical core of the curriculum's first half.

Modules 01–03 built vocabulary and physical intuition. Module 04 builds the equations that will power every simulation in the curriculum — including the digital twin. Students who complete this module can write differential equations that predict how their workcell behaves and begin to understand why measured behavior sometimes diverges from expectation.

The framing is deliberate: these are not fluid mechanics equations in the abstract. They are the models we will put inside the digital twin.

**Workcell contribution:** Students write and simulate the first dynamic model of their workcell — a pressure-flow simulation of the supply line and primary cylinder.

---

## Learning Objectives

- LO-04.1: Apply Bernoulli's equation to predict pressure and velocity changes through restrictions and fittings
- LO-04.2: Apply the orifice flow equation to model flow through a valve opening
- LO-04.3: Derive and explain the continuity equation for a hydraulic cylinder (flow in = area × velocity)
- LO-04.4: Write a force balance equation for a hydraulic cylinder including pressure forces, friction, and load
- LO-04.5: Write the first-order ODE governing cylinder pressure dynamics
- LO-04.6: Solve simple hydraulic ODEs numerically using SciPy `solve_ivp`
- LO-04.7: Explain bulk modulus and its role in hydraulic stiffness and response speed
- LO-04.8: Connect the cylinder dynamics model to the digital twin pipeline

---

## Prerequisite Knowledge

- Modules 01–03 complete
- Basic calculus: derivatives, the idea of an ODE
- Python: NumPy, Matplotlib (introductory level is sufficient)

---

## Key Topics

### Topic 1 — Bernoulli and the Energy Equation
Bernoulli's equation for steady, incompressible flow. Pressure head, velocity head, elevation head. Where it applies and where it breaks down (viscous flows, unsteady conditions).

**Workcell connection:** Using Bernoulli to estimate velocity at the pump outlet and pressure recovery downstream.

### Topic 2 — Orifice Flow and the Valve Model
The orifice equation: Q = Cd·A·√(2ΔP/ρ). Flow coefficient (Cv, Kv). Cavitation. The orifice equation is the mathematical model of every valve in the workcell.

**Workcell connection:** Students write the valve flow model that will appear in their digital twin. This is the first digital twin component.

### Topic 3 — Cylinder Dynamics: The Force Balance
Forces on a moving cylinder rod: pressure force, rod-side back-pressure, friction (Stribeck model, simplified), external load, inertia. Newton's second law for the cylinder.

$$m\ddot{x} = A_b P_b - A_r P_r - F_{friction} - F_{load}$$

**Workcell connection:** Setting up the equations for the workcell's primary cylinder. Identifying the load (the end effector + workpiece weight).

### Topic 4 — Pressure Dynamics and Bulk Modulus
Why hydraulic systems are not perfectly rigid. Bulk modulus: B = -V(dP/dV). Effective bulk modulus (including hose compliance). Pressure rise rate equation.

$$\frac{dP}{dt} = \frac{B_e}{V}(Q_{in} - A\dot{x})$$

This equation governs how fast the system responds to a valve opening. It is central to the digital twin.

**Workcell connection:** Estimating the pressure rise rate in the workcell cylinder. Why the system has a finite response speed.

### Topic 5 — Simulation: First ODE in Python
Combining the force balance and pressure dynamics into a coupled ODE system. Solving with `scipy.integrate.solve_ivp`. Plotting cylinder position, velocity, and pressure vs. time.

**Workcell connection:** First simulation of the workcell's primary cylinder responding to a valve command.

---

## Capstone Connection

**Deliverable this module:** First simulation notebook — `code/module04/cylinder_simulation.ipynb`. Simulates the primary cylinder of the workcell responding to a step valve opening. Plots position, velocity, and bore pressure vs. time.

**Digital twin contribution (major):**
- Orifice flow model (Subsystem 3 — Motion Control)
- Cylinder dynamics ODE (Subsystem 4 — Actuation)
- Pressure dynamics equation (Subsystem 2 — Fluid Transport)

These three components form the mechanical core of the digital twin. Every later module adds to this foundation.

---

## Labs

**Lab 04 — Step Response Observation**  
Apply a step valve command to a simple hydraulic circuit (bench demo or low-pressure pneumatic substitute). Record cylinder position vs. time. Compare to the simulation from Topic 5. Identify sources of discrepancy (friction, bulk modulus approximation, measurement noise).

---

## Code

`code/module04/orifice_flow.py` — Orifice equation implementation. Plot flow vs. pressure drop for a range of valve openings.

`code/module04/cylinder_dynamics.py` — Coupled ODE for cylinder force balance + pressure dynamics. Standalone script version.

`code/module04/cylinder_simulation.ipynb` — Jupyter notebook: set up workcell cylinder parameters, run simulation, compare to ideal (frictionless) case.

---

## Assessment

- Derive the pressure dynamics equation from scratch (closed-book)
- Simulation parameter study: how does bulk modulus affect response speed?
- Lab report: measured vs. simulated step response. Explain the difference.

---

## Connections Forward

- Module 05 uses the pump model to set the input boundary condition for this simulation
- Module 06 replaces the ideal step valve with the orifice model from Topic 2
- Module 07 refines the cylinder model with real cylinder parameters
- Module 11 integrates all of these into the full digital twin

---

*Module 04 Manifest — Version 0.1*
