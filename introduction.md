# Introduction

The Borneo-IoT Project is an open-source hardware and software DIY toolkit for creating DIY aquarium LED and other aquatic smart devices.

Currently, Borneo IoT Project includes the following components:

1. A mobile app serving as a universal wireless device user terminal.
2. A wireless 5-channel LED PWM embedded controller module (core board) with model ["BLC05MK3"](#blc05-hardware) and corresponding open-source firmware.
3. A 5-channel LED aluminum PCB reference design for BLC05MK3 with model ["BLB08103"](#blb08103-hardware), which includes red, green, blue, white, and ultraviolet UVA (or purple) LED channels, with a nominal power of 63W.

In the future, The Borneo-IoT Project will implement the following new hardwares and software:

- A 10-channel LED PWM embedded controller module.
- A wireless water pH and temperature monitor.
- A multi-channel doser.
- A water circulation pump.
- And more.

## The directory structure of the Git repository

- `client/`: Mobile app source code
- `fw/`: Firmware source code
    - `scripts`: Related Python scripts, including the device Python client library
    - `cmake`: CMake scripts
    - `components`: Common ESP-IDF component source code
    - `lyfi`: LED controller firmware-related source code
    - `doser`: Dosing pump firmware-related source code (under development)
- `hw/`: Circuit design source files
    - `blc05mk3`: 5-channel LED controller core board design
    - `blc05mk3-horizontal`: 5-channel LED controller core board with horizontal pin headers
    - `blb08103`: 5-channel 63W LED lamp aluminum substrate design
    - `3d-models`: Exported STEP format 3D models of the core board
    - `datasheets`: The hardware specifications in PDF format
- `tools/`: Related scripts and tools