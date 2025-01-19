# FAQ

## Hardware and Firmware

### Where can I change the I/O's so the code works with my particular board?

First, make a copy of the directory `fw\lyfi\boards\blc05emk1`, let's say `fw\lyfi\boards\myboard`.

Then, open the `fw\lyfi\boards\myboard\sdkconfig` file using a text editor. Make sure to modify the first line, change `CONFIG_BORNEO_BOARD_ID=` to `CONFIG_BORNEO_BOARD_ID="myboard"`.

On line 31, change `CONFIG_BORNEO_NTC_ENABLED=y` to `=n`, if you don't have an NTC thermistor.

Starting from line 43, `CONFIG_LYFI_LED_CH0_GPIO=3` refers to the first PWM channel using GPIO3 on the ESP32-C3.

For any unused channels, you can set `CONFIG_LYFI_LED_CH*_ENABLED=n` to disable it.

Finally, use `idf.py build -DBORNEO_BOARD=myboard` to execute the build, and `idf.py flash` to perform the flashing.
