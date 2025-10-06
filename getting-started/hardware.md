# Hardware

The hardware design is created with the open-source Horizon EDA ([horizon-eda.org](https://horizon-eda.org)). After installing Horizon EDA, open the corresponding `.hprj` project file in this directory.

The Buce module in this project requires a 0.5" (1.27 mm) pitch 6-pin programming clip. Alternatively, you can use a general ESP32-C3 development board.

:::{note}
Using a third-party development board such as the [XIAO-ESP32C3](xiaoc3-hardware) is intended only for initial firmware testing. Except for Wi‑Fi connectivity, LED dimming PWM outputs, and the fan PWM output, other features depend on the peripheral circuits on the custom PCB used in this project.
:::


```{figure} ./images/programming-clip.jpg
:name: programming-clip
:alt: Programming clip
:align: center
:width: 50%
A typical programming clip for reference
```