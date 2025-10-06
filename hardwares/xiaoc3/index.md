(xiaoc3-hardware)=
# Seeed XIAO-ESP32-C3

## Introduction

To make it easier for users who want to quickly test our firmware and the [mobile app](mobile-app), we provide a firmware build that supports the [Seeed XIAO-ESP32C3 module](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started). You can flash the firmware over the module's USB-OTG interface and control it with our mobile app. Note that because the XIAO-ESP32C3 lacks the external peripherals present on our dedicated controller, supported hardware features are limited to the following:

1. **6 independent LED PWM channels**: 6 separate LED PWM dimming channels. Your LED driver circuit should include pull-down resistors to avoid large inrush currents at power-up.
2. **Fan PWM output**: A PWM output for fan. Because the NTC thermistor support circuit is not present, you can only set the fan PWM duty manually in the app; the PID closed-loop automatic fan-speed control provided by our dedicated controller is not available.
3. **User button**: A user button for temporary light-on (short press) and Wi‑Fi reset (long press). This reuses the XIAO-ESP32C3's built-in "Boot" button, or you can wire an external button from the module's D9 pin to GND to use it outside the board.

## Pinout

| XIAO-ESP32C3 pin | BorneoIoT function | Notes |
|:-------------------|:--------------|:--------------|
| D1     | LED PWM Channel 0    |        |
| D2     | LED PWM Channel 1    |        |
| D3     | LED PWM Channel 2    |        |
| D4     | LED PWM Channel 3    |        |
| D5     | LED PWM Channel 4    |        |
| D6     | LED PWM Channel 5    |        |
| D7     | Fan PWM output    | Fan PWM output, uses standard 25 kHz PWM  |
| D9     | User button    | This IO is shared with the XIAO-ESP32C3 "Boot" button.   |


## Build and flash firmware

Connect the XIAO-ESP32C3 with a USB cable, open an ESP-IDF terminal, and run:

```bash
cd fw/lyfi # change to LyFi firmware directory
idf.py build -DPRODUCT_ID=bst/xiaoc3 # build firmware
idf.py flash # flash firmware
idf.py monitor # view firmware logs
```

After these steps you can connect the module with our mobile app.