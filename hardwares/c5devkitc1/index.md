(c5devkitc1-hardware)=
# Espressif ESP32-C5-DevKitC-1 Board

## Introduction

To make it easier for users who want to quickly test our firmware and the [mobile app](mobile-app), we provide a firmware profile that supports the [Espressif `ESP32-C5-DevKitC-1` development board](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c5/esp32-c5-devkitc-1). You can flash the firmware over the module's USB-to-UART interface and control it with our mobile app.

Note that because the `ESP32-C5-DevKitC-1` lacks the external peripherals present on our dedicated controller, supported hardware features are limited to the following:

1. **6 independent LED PWM channels**: 6 separate LED PWM dimming channels. Your LED driver circuit should include pull-down resistors to avoid large inrush currents at power-up.
2. **Fan PWM output**: A PWM output for fan. Because the NTC thermistor support circuit is not present, you can only set the fan PWM duty manually in the app; the PID closed-loop automatic fan-speed control provided by our dedicated controller is not available.
3. **User button**: A user button for temporary light-on (short press) and Wi‑Fi reset (long press). This reuses the `ESP32-C5-DevKitC-1`'s built-in "Boot" button, or you can wire an external button from the module's `GPIO28` pin to `GND` to use it outside the board.

## Pinout

| `ESP32-C5-DevKitC-1` pin | BorneoIoT function | Notes |
|:-------------|:---------------------|:----------------------------------------------------|
| `GPIO7`      | LED PWM Channel 0    |        |
| `GPIO8`      | LED PWM Channel 1    |        |
| `GPIO9`      | LED PWM Channel 2    |        |
| `GPIO10`     | LED PWM Channel 3    |        |
| `GPIO26`     | LED PWM Channel 4    |        |
| `GPIO25`     | LED PWM Channel 5    |        |
| `GPIO23`     | Fan PWM output       | Fan PWM output, uses standard 25 kHz PWM  |
| `GPIO28`     | User button          | This IO is shared with the board's "Boot" button.   |


## Build and flash firmware

You can either build and flash the firmware locally using ESP-IDF, or use our web-based, open-source flasher.

### Build and flash yourself

Connect the board with a USB cable, open an ESP-IDF terminal, and run:

```bash
cd fw/lyfi # change to LyFi firmware directory
idf.py build -DPRODUCT_ID=bst/c5devkitc1 # build firmware
idf.py flash # flash firmware
idf.py monitor # view firmware logs
```

After flashing you can connect the module with our mobile app.

### Use the web-based flasher (recommended for quick tests)

If you don't want to set up the ESP-IDF toolchain locally, you can use our WebSerial-based open-source flasher at [flasher.borneoiot.com](https://flasher.borneoiot.com). It runs in your browser and communicates with the `ESP32-C5-DevKitC-1` over USB.

The web flasher is ideal for quick testing and for users who prefer not to install the full ESP-IDF toolchain.