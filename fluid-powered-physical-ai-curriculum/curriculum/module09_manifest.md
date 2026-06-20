# Module 09 — Sensors and Instrumentation

**Curriculum:** Fluid-Powered Physical AI  
**Module Number:** 09 of 12  
**Estimated Duration:** 2 weeks  
**Capstone Subsystems:** 5 (Sensing and Intelligence)  
**Pipeline Stages:** SENSE, UNDERSTAND (signal conditioning)

---

## Module Purpose

This module begins the intelligence arc.

Students have designed and can simulate a complete hydraulic system. Now they must make it *perceive*. Sensors transform the physical state of the workcell — pressure, position, flow, force, temperature, visual — into electrical signals that an embedded controller can read, reason about, and act on.

The module covers the full chain: transducer physics → signal conditioning → wiring → analog-to-digital conversion → calibration → data logging. By the end, students have instrumented the workcell and are reading real sensor data in Python.

**Workcell contribution:** Fully wired sensor layer for the Smart Agricultural Workcell. Each sensor calibrated, tested, and data-logged.

---

## Learning Objectives

- LO-09.1: Describe the operating principle of the primary sensor types used in the workcell: pressure transducer, linear position sensor, flow sensor, load cell, temperature sensor
- LO-09.2: Explain common output signal formats: 0–5V, 0–10V, 4–20mA, PWM, digital (I2C, SPI)
- LO-09.3: Design a basic signal conditioning circuit for a 4–20mA pressure transducer (shunt resistor, voltage divider)
- LO-09.4: Wire sensors to an Arduino and write code to read and convert raw ADC values to physical units
- LO-09.5: Calibrate a sensor using a two-point calibration (zero and span)
- LO-09.6: Explain noise sources in sensor measurements and implement a simple moving-average filter in code
- LO-09.7: Log sensor data to a CSV file from the Raspberry Pi and visualize it in Python
- LO-09.8: Identify what each workcell sensor contributes to the digital twin's SENSE pipeline stage

---

## Prerequisite Knowledge

- Modules 01–08 complete
- Basic electronics: voltage, current, resistance (Ohm's law), analog vs. digital signals
- Arduino basics: `analogRead()`, `Serial.print()`

---

## Key Topics

### Topic 1 — Pressure Sensing
Strain gauge pressure transducer physics. Wheatstone bridge. 4–20mA output: why current signals are preferred in industrial environments (noise immunity, wire resistance independence). Shunt resistor circuit for Arduino. Pressure transducer placement in the workcell circuit.

**Workcell connection:** Two pressure transducers: bore-side and rod-side of the primary cylinder. Calculating cylinder force from differential pressure.

### Topic 2 — Position Sensing
Linear potentiometer (resistive divider, simple and cheap). Magnetostrictive transducer (high accuracy, longer stroke). Reed switch / Hall effect limit sensors. Which to use for the workcell and why.

**Workcell connection:** Position transducer on the primary cylinder rod. Velocity estimation from position derivative (and why naive differentiation is noisy).

### Topic 3 — Flow Sensing
Turbine flow meter principle. Frequency output interpretation. Gear flow meter (higher viscosity tolerance). Where to place the flow sensor in the workcell circuit. Why flow measurement enables leakage detection.

**Workcell connection:** Flow sensor on the supply line. Using measured vs. expected flow to detect valve wear or internal leakage.

### Topic 4 — Force and Load Sensing
Load cell operating principle (strain gauge bridge). Amplifier (HX711 or INA125). Taring and calibration. End-effector force sensing: why it matters for grip control and workpiece protection.

**Workcell connection:** Load cell on the end effector jaw. Using force feedback to detect contact and limit grip force.

### Topic 5 — Signal Conditioning and Filtering
Noise sources: electromagnetic interference, ground loops, ADC quantization. Moving average filter. Exponential smoothing filter. Why filter parameters affect control loop performance.

**Workcell connection:** Implementing filters in Arduino. Effect of filter lag on position control loop response.

### Topic 6 — Data Logging and Visualization
Arduino → serial → Raspberry Pi. Python `pyserial` to read data. Logging to CSV. Matplotlib time-series plots. Real-time monitoring dashboard (simple version).

**Workcell connection:** Complete sensor data log from a workcell task cycle. Feeding this data to the digital twin for comparison.

---

## Capstone Connection

**Deliverable this module:** Sensor wiring diagram for the Smart Agricultural Workcell (all sensors, connections, signal conditioning, Arduino I/O pin assignments) + working data logger that records all sensor channels during a task cycle.

**Digital twin contribution:** Sensor noise model — adding Gaussian noise to digital twin outputs to simulate real measurement conditions. Calibration parameters stored in the twin's configuration.

---

## Labs

**Lab 09A — Pressure Transducer Calibration**  
Wire a pressure transducer to an Arduino. Apply known pressures (deadweight tester, pneumatic gauge, or calibrated reference). Record ADC values. Fit calibration curve. Test accuracy.

**Lab 09B — Position Sensor Integration**  
Mount a linear potentiometer on a cylinder (or slide). Move the cylinder through its stroke while logging position. Calculate velocity. Apply moving-average filter and observe the effect on velocity signal.

**Lab 09C — Full Sensor Suite**  
Integrate all workcell sensors onto the Arduino. Run a task cycle. Log all channels simultaneously. Visualize in Python.

---

## Code

`code/module09/sensor_reader/sensor_reader.ino` — Arduino sketch: reads pressure, position, flow, and load cell channels; outputs calibrated values via serial.

`code/module09/data_logger.py` — Python: reads serial from Arduino, logs to CSV with timestamp.

`code/module09/sensor_viz.ipynb` — Jupyter notebook: load CSV, plot all sensor channels, apply filters, compare filtered vs. raw.

---

## Assessment

- Design the signal conditioning circuit for a 4–20mA pressure transducer feeding an Arduino 5V ADC
- Write the calibration equation for a position sensor given two reference measurements
- Lab report: sensor data from a task cycle, annotated to identify each phase of motion

---

*Module 09 Manifest — Version 0.1*
