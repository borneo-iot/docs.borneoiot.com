# Hardware

The hardware design uses the open-source [Horizon EDA](https://horizon-eda.org). After installation, open the corresponding `.hprj` project file in the directory.

Note that the core board of this project requires a 1.27mm pitch 6-Pin programming clip, or you can also use an general ESP32-C3 development board.

:::{note}
Using a development board is only for initial firmware running experience. Apart from WiFi network connection, output dimming PWM signals, and fan PWM signals, all other functionalities require support from the peripheral circuits of the custom PCB in this project.
:::


```{figure} ./images/programming-clip.jpg
:name: programming-clip
:alt: Programming clip
:align: center
:width: 50%
A typical programming clip for reference
```