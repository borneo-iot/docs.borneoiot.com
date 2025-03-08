# Firmware

## Building from Source Code

### Environment Setup

The framework of this project is developed using the official ESP-IDF framework from Espressif. If you do not have the ESP-IDF build environment, you need to download and configure the ESP-IDF SDK from Espressif's official website.

After completing the installation and configuration, try building the `hello_world` example provided by ESP-IDF to ensure that you have set up the environment correctly.

#### Windows

##### ESP-IDF SDK Download and Installation

First, go to Espressif's [official website](https://dl.espressif.com/dl/esp-idf/) to download the ESP-IDF SDK installer, which includes the ESP-IDF framework, GCC compiler, and all other tools you need.

It is recommended to download the Offline Installer without Espressif-IDE since we don't use it.

#### Linux

TBD

### Building

Once the environment is ready, open ESP-IDF 5.x PowerShell or CMD, navigate to the `fw/lyfi` directory, and execute:

```bash
idf.py build
```

to start the firmware build process.

![](./videos/fw-build.mp4)


## Flashing Firmware

Connect the device and execute the following command:

```bash
idf.py flash -p <SERIAL_PORT_NAME> -DBORNEO_BOARD=<BOARD_NAME>
```

to flash the firmware to the module's MCU. You can omit the `-p` parameter to let the `idf.py` tool automatically detect the serial port.

The parameter `-DBORNEO_BOARD=` is optional. `<BOARD_DIR_NAME>` is the name of the subdirectory in the `boards/` directory, used to specify the board definition when building the firmware.


![](./videos/fw-flashing.mp4)