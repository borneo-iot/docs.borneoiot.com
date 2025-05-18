# FAQ

## Hardware and Firmware

### Where the hell are your open-source BoM, Gerbers, and schematics?

The project's PCB design uses [Horizon EDA](https://horizon-eda.org).

After installation, you can open the `.hprj` file and export the BoM and Gerber files yourself.

---

### Where can I change the I/O's so the code works with my particular board?

First, make a copy of the directory `fw/lyfi/boards/bst/blc06mk1`, let's say `fw/lyfi/boards/me/myboard`.

Then, open the `fw/lyfi/boards/me/myboard/sdkconfig.board` file using a text editor. Make sure to modify the first line, change `CONFIG_BORNEO_BOARD_ID=` to `CONFIG_BORNEO_BOARD_ID="myboard"`.

On line 31, change `CONFIG_BORNEO_NTC_ENABLED=y` to `=n`, if you don't have an NTC thermistor.

Starting from line 43, `CONFIG_LYFI_LED_CH0_GPIO=3` refers to the first PWM channel using GPIO3 on the ESP32-C3.

For any unused channels, you can set `CONFIG_LYFI_LED_CH*_ENABLED=n` to disable it.

Finally, use `idf.py build -DPRODUCT_ID=my/myprod` to execute the build, and `idf.py flash` to perform the flashing.