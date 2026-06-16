# Platform-Power-Configuration-Simulator
This project simulates a platform-level power configuration system for embedded devices. It determines behavior for display, lid service, PSU boot policy, and LED control based on device configuration.

The simulator focuses on handling platform variations such as display-less systems, lidless devices, and different power supply capabilities.
-------------------------------
## Problem Statement
Embedded systems often support multiple hardware configurations (e.g., laptops, desktops, or display-less platforms). If firmware blindly executes hardware-dependent operations without validating configuration, it can lead to system hangs, incorrect behavior, or inefficient power handling.

## Examples:
- Attempting display initialization on a display-less system
- Enabling lid services on a lidless platform
- Booting under insufficient power conditions
- Incorrect LED behavior across system states
--------------------------------------
## Solution:
This project introduces a configuration-driven simulation engine that:
- Skips display initialization when no display is present
- Disables lid service when the device has no lid sensor
- Applies power supply-based boot policies
- Controls LED behavior across system lifecycle states
- Prevents invalid hardware interactions through validation checks

## Key Features
### Display-less Configuration Handling
- Detects absence of display hardware
- Skips display initialization to prevent system hang scenarios
### Lidless Device Support
- Disables lid-related logic when no lid sensor is present
### Power Supply Policy Handling
- Evaluates connected PSU wattage
- Routes system into normal or weak power paths based on policy rules
### Power LED Behavior Simulation- Simulates LED behavior for system states:
- Runtime
- Shutdown complete 
- Hibernate complete
### Configuration-Driven Architecture
- Entire system behavior is controlled through YAML configuration files
- Easily extendable to support new platform types
