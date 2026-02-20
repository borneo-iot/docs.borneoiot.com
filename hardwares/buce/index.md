(buce-hardware)=
# Buce: 6-Channel LED PWM Dimmer (BLC06MK1)

```{figure} ./images/blc06mk1.jpg
:name: blc06mk1-appearance
:alt: Buce Module Appearance
:align: center
:width: 50%

The Appearance of Buce Module
```

## Overview

Buce (Model BLC06MK1) is an innovative 6-channel All-in-One WiFi LED PWM Controller designed for enthusiasts who love DIY lighting projects, particularly in aquariums and photography. This versatile controller provides six independent PWM channels, allowing users to customize and control lighting effects wirelessly through our [open-source mobile app](mobile-app).

With multi-segment dimming capabilities, Buce can simulate natural daylight transitions, such as sunrise and sunset, enhancing the visual experience in various settings.

### What will people use it for?

* Aquarium Lighting: Aquarium hobbyists can use Buce to simulate natural lighting environments, promoting the health and growth of aquatic plants or corals.
* Photography Lighting: Photographers can set up dynamic lighting scenes to capture stunning images with precise control over brightness and color, perfect for studio or outdoor shoots.
* Home Lighting: DIY enthusiasts can integrate Buce into their smart home systems to create personalized lighting ambiances for different rooms and occasions, with smooth transitions throughout the day.

## Block Diagram

```{figure} ./images/block-diagram.svg
:name: buce-block-diagram
:alt: Module Block Diagram
:align: center
:width: 80%
Module Block Diagram
```

## Features

* Dimming:
  * The firmware and mobile app support advanced programmable multi-stage dimming.
  * Supports linear, logarithmic, gamma, exponential and CIE-1931 dimming algorithms.
  * Supports scheduling mode, manual mode, and temporary appreciation mode.
  * 6 independent PWM dimming channels.
  * High dimming frequency (default 19kHz), ensuring no flickering is visible to the naked eye or detected by recording devices,
    while completely eliminating noise from the circuit.
  * Supports phase shifting for PWM signal, significantly reducing the peak current of the LED driver when not running at full power.
  * 4096 dimming levels.
  * Fully automated solar illumination intensity simulation based on astronomical algorithms.
  * Soft start and soft shutdown features to avoid startling aquatic life.
* Built-in Thermal Management:
  * Integrated NTC temperature sensing circuit that can directly connect to a 3950 10kΩ NTC.
  * Integrated fan driver circuit, capable of directly connecting to 12V two-wire fans and PWM-controlled fans. Two-wire fans can set speed through voltage adjustment.
  * Fan cooling control via PID algorithm (default set to maintain 45°C, configurable via software). Automatic emergency shutdown occurs if the NTC temperature exceeds 65°C.
* Highly Integrated (All-in-One):
  * Compact size of only 22×30mm.
  * Built-in buck converter circuit, allowing direct input of 5~36V voltage.
  * Built-in power voltage measurement circuit, with the option to connect an INA139 for current and power measurement.
  * Capable of outputting 3.3V voltage to power external devices.
  * Supports external buttons for functions like WiFi provisioning (network setup).
* Other Features:
  * Automatic SNTP time synchronization.
  * 0.1" (2.54mm) header interface, convenient for DIY projects.
  * Communicate using CBOR over CoAP/UDP, and provide Python communication examples.

Please checkout the following datasheets for more information about the hardware.

* Buce (Model BLC06MK1) Datasheet: [`blc06mk1.pdf`](https://github.com/borneo-iot/borneo/blob/master/hw/datasheets/blc06mk1.pdf)

## Usage

### Pinout

```{figure} ./images/gds.png
:name: buce-gds
:alt: Buce Pinout Diagram
:align: center
:width: 80%
Pinout Diagram
```

### Typical Peripheral Circuit

```{figure} ./images/peripherals.svg
:name: buce-peripheral-circuit-diagram
:alt: Typical Peripheral Circuit Diagram
:align: center
:width: 90%
Typical Peripheral Circuit Diagram
```

## Resources

### Datasheet

<embed src="/_static/files/buce/blc06mk1.pdf" class="pdf-embed" type="application/pdf">
