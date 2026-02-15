# Introduction

The Borneo-IoT Project is an open-source hardware and software DIY toolkit for creating DIY aquarium LED and other aquatic smart devices.

Currently, Borneo IoT Project includes the following components:

1. A mobile app serving as a universal wireless device user terminal.
2. A wireless 6-channel LED PWM embedded controller module (core board) with model ["BLC06MK1"](#blc06-hardware) and corresponding open-source firmware.
3. A 5-channel LED aluminum PCB reference design for BLC06MK1 with model ["BLB08103"](#blb08103-hardware), which includes red, green, blue, white, and ultraviolet UVA (or purple) LED channels, with a nominal power of 57W.

In the future, The Borneo-IoT Project will implement the following new hardwares and software:

- A 10-channel LED PWM embedded controller module.
- A wireless water pH and temperature monitor.
- A multi-channel doser.
- A water circulation pump.
- And more.

## Core Features

### 1. Multi-Channel LED Control
- **PWM Dimming**: Supports 6 independent PWM channels, brightness range 0-4095
- **Color Correction**: Multiple correction algorithms available
  - Logarithmic correction
  - Linear correction
  - Exponential correction (default)
  - Gamma correction
  - CIE1931 correction
- **Channel Configuration**: Each channel can be configured with name, color, and wavelength information

### 2. Intelligent Operating Modes
- **Manual Mode**: Direct control of LED color and brightness
- **Scheduled Mode**: Time-based scheduling for LED states, supporting up to 48 schedule points
- **Sunrise Simulation Mode**: Simulates natural sunrise/sunset processes

### 3. Astronomical Simulation Features
- **Sunrise/Sunset Calculation**: Precise calculation of sunrise, sunset, and solar noon times based on geographical location (latitude/longitude)
- **Daily Brightness Curve**: Generates brightness variation curves for 13 key time points throughout the day
- **Moonlight Simulation**: Calculates moon phase, illumination fraction, and moonrise/moonset times
- **Timezone Support**: Automatic handling of timezone offsets and daylight saving time

### 4. Adaptation and Optimization
- **LED Acclimation Period**: Configurable acclimation period of 5-100 days to help organisms adapt to light changes
- **Cloud Cover Simulation**: Optional cloud layer effects for added realism
- **Geolocation Integration**: Supports GPS or manual location setting

### 5. Thermal Management and Protection
- **PID Temperature Control**: Intelligent fan control to maintain target temperature
- **NTC Temperature Sensor**: Real-time monitoring of device temperature
- **Fan Modes**:
  - Manual Mode: Fixed fan power
  - PID Mode: Automatic fan speed adjustment
- **Protection Mechanisms**:
  - Overheat Protection: Automatic power reduction when exceeding set temperature
  - Overpower Protection: Prevents power overload

### 6. Remote Control and Communication
- **CoAP Protocol**: Lightweight IoT protocol based on CoAP/CBOR
- **Remote Resources**:
  - LED state control
  - Operating mode switching
  - Temperature monitoring
  - Moonlight status query
- **OTA Updates**: Over-the-air firmware upgrades for remote maintenance

### 7. User Interaction
- **Physical Button**: Local control button support
- **Status Indication**: LED status feedback
- **Preview Mode**: Temporary lighting function
- **Disco Mode**: Entertainment lighting effects

### 8. System Features
- **Time Synchronization**: NTP network time synchronization
- **Low Power Design**: Suitable for battery-powered scenarios
- **Modular Architecture**: Easy to extend and customize
- **Open Source Code**: Fully open source, community-driven development



## The directory structure of the Git repository

- `client/`: Mobile app source code
- `borneopy/`: A open-source Python API library for devices under the Borneo-IoT Project
- `fw/`: Firmware source code
    - `scripts`: Related Python scripts
    - `cmake`: CMake scripts
    - `components`: Common ESP-IDF component source code
    - `lyfi`: LED controller firmware-related source code
    - `doser`: Dosing pump firmware-related source code (under development)
- `hw/`: Circuit design source files
    - `blc06`: The core board design of Buce, the 6-channel LED controller module
    - `blb0657f`: 6-channel 57W LED lamp aluminum PCB design
    - `bld6f`: 6-channel LED driver PCB design
    - `blc05mk3`: 5-channel LED driver PCB design (*Obsoleted*)
    - `blb08103`: 5-channel 63W LED lamp aluminum PCB design (*Obsoleted*)
    - `3d-models`: STEP format 3D models
    - `datasheets`: The hardware specifications in PDF format[^3]
- `tools/`: Related scripts and tools
