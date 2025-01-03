# Firmware

## Build from source

### Environment Setup

The firmware is developed using Espressif's ESP-IDF framework. Please refer to the official documentation to set up the development environment and compile the official "hello_world" example to ensure proper configuration.

### Building

Once the environment is ready, open ESP-IDF 5.x PowerShell or CMD, navigate to the `fw/lyfi` directory, and execute:
```bash
idf.py build
```
to start the firmware build process.

## Flashing firmware

Connect the device and execute the following command:
```bash
idf.py flash -p <SERIAL_PORT_NAME>
```
to flash the firmware to the module's MCU. You can omit the `-p` parameter to let the `idf.py` tool automatically detect the serial port.

