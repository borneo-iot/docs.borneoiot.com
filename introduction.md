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

## The directory structure of the Git repository

- `client/`: Mobile app source code
- `borneopy/`: A open-source Python client library for devices under the Borneo-IoT Project
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
