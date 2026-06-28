# Fusion Diagnostic Camera System (FDCS): Conceptual Design of a Radiation-Hardened Multispectral Diagnostic System for Fusion Plasma-Facing Components

## Overview

FDCS is a conceptual design study for a multispectral imaging diagnostic system intended for monitoring **plasma-facing components (PFCs)** in magnetically confined fusion devices such as tokamaks.

The goal of this project is to explore the end-to-end design considerations of a robust optical diagnostic system capable of operating in extreme fusion environments characterized by high heat flux, intense radiation fields, strong magnetic fields, and limited physical access.

This project is not tied to a specific experimental implementation, but is intended as a physics-informed systems design exercise bridging experimental condensed matter physics, detector instrumentation, and fusion diagnostics.

---

## Motivation

Plasma-facing components in fusion devices experience extreme operational conditions including:

- transient and steady-state heat loads
- erosion and material redeposition
- impurity transport and emission
- arcing and localized damage events
- surface modification from plasma-material interactions

Reliable, real-time diagnostics of these processes are essential for:

- improving plasma confinement performance
- extending component lifetime
- validating plasma-material interaction models
- enabling safe long-pulse operation in future fusion reactors

FDCS explores a diagnostic architecture inspired by modern scientific imaging systems, adapted to the constraints of fusion environments.

---

## System Concept

FDCS is a modular imaging system composed of four main subsystems:

1. **Optical Collection System**
   - Sapphire or fused silica viewport
   - Lens system optimized for wide-angle collection
   - Spectral filtering for visible and near-infrared emission

2. **Radiation and Magnetic Shielding Layer**
   - Shielding against neutron and gamma radiation
   - Electromagnetic protection for sensitive electronics
   - Thermal isolation from high heat flux environment

3. **Multispectral Sensor Module**
   - CMOS-based visible imaging sensor
   - Infrared thermography channel for surface temperature estimation
   - Calibration sources for gain and drift correction

4. **Edge Processing and Data System**
   - Real-time frame acquisition and compression
   - Event detection (arcs, hot spots, impurity bursts)
   - Time-synchronized shot-based data storage
   - Integration with downstream analysis pipelines

---

## Physics Modeling Approach

The system design is informed by simplified physics models including:

- blackbody radiation from plasma-facing surfaces
- radiative heat flux estimates for tungsten, graphite, molybdenum and lithium-based materials
- photon transport through optical viewport systems
- signal-to-noise considerations under radiation-induced sensor noise
- basic thermal response modeling of surface components

These models are implemented in Python to provide order-of-magnitude design constraints and to guide subsystem tradeoffs.

![Heat balance during plasma pulse](/figures/heat_balance_during_plasma_pulse.png)

---

## Key Design Considerations

FDCS is designed under the following constraints typical of fusion environments:

- **Radiation hardness:** sensor and electronics survivability under neutron/gamma flux
- **Magnetic field compatibility:** operation in strong static magnetic fields
- **Thermal resilience:** protection from conductive and radiative heat loads
- **Limited access:** minimal maintenance due to reactor operational constraints
- **Real-time performance:** capability to support pulse-based experimental operation

---

## Example Use Cases

- Monitoring divertor surface temperature evolution during plasma shots
- Detecting arcing events and localized surface damage
- Tracking impurity emission and deposition patterns
- Supporting validation of plasma-material interaction models
- Providing real-time feedback for operational optimization

---


---

## Current Status

This is an evolving conceptual design study. Current work focuses on:

- physics-based constraint modeling
- subsystem architecture definition
- optical signal chain estimation
- synthetic event simulation for validation of detection concepts

Future extensions may include:
- full optical ray-tracing simulation
- radiation transport modeling
- machine learning-based event detection
- integration with experimental fusion diagnostics datasets

---

## Relevance to Fusion Diagnostics

FDCS is motivated by diagnostic systems used in modern tokamaks, where optical and infrared imaging systems play a critical role in:

- plasma-facing component monitoring
- edge plasma diagnostics
- disruption and transient event detection
- machine protection systems

The design emphasizes modularity and robustness, reflecting the operational constraints of long-pulse and reactor-scale fusion devices.

---

## Author Background

This project is developed from a background in experimental condensed matter and astroparticle physics, with experience in:

- detector instrumentation and optical sensor systems
- vacuum and low-temperature experimental environments
- large-scale scientific data acquisition and analysis
- Python-based scientific computing and modeling
- participation in international physics collaborations

The objective is to explore fusion diagnostic system design from a cross-disciplinary experimental physics perspective.

---

## Disclaimer

This project is a conceptual design study intended for educational and research exploration purposes. It does not represent a deployed or operational fusion diagnostic system.


