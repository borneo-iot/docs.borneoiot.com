# Add a New Device

Adding and registering a new device using the Borneo-IoT App is easy.

First, ensure that your phone is connected to your local WiFi router and that your WiFi router has the 2.4GHz WiFi network enabled. It does not matter whether your phone is connected to a 2.4GHz or 5GHz network, as long as they are connected. However, connecting your phone to the 2.4GHz WiFi network and placing it close to the Borneo-IoT device can improve the reliability and speed of the new device's network configuration (provisioning).

:::{note}
Currently, all Borneo-IoT devices only support 2.4GHz WiFi networks and cannot connect to 5GHz WiFi networks.
:::

Switch to the "Devices" page using the navigation at the bottom, and click the plus button in the upper right corner:

```{figure} ./images/add-0.jpg
:align: center
:height: 480px
```

In the pop-up menu, select "Add New Devices" to enter the device addition page:

```{figure} ./images/add-1.jpg
:align: center
:height: 480px
```

Enter your WiFi router's name in the "WiFi Name" text box and the corresponding WiFi password in the "WiFi Password" text box. After confirming the information is correct, click the "Start" button to proceed with the device network configuration and discovery.

:::{note}
If you enter an incorrect WiFi name and/or password, the device will not be able to connect to the WiFi network and will not be detected by your phone. Therefore, you will need to use the device's network reset function to make the device forget the incorrect WiFi information. Refer to the operation manual of your specific Borneo-IoT hardware for detailed instructions.
:::

After a few seconds (depending on the congestion of your WiFi signal), the devices discovered by the mobile app will be displayed below. Through this operation, you can configure the WiFi network for multiple devices at once.

```{figure} ./images/add-2.jpg
:align: center
:height: 480px
```

Once all your desired devices are found, click "Stop" again to stop the network configuration and device discovery.


At this point, the plus button in the device list will be available. Clicking it will pop-up the device group selection, indicating which device group your device will join. After selecting the device group, the app will prompt that the device has been successfully added.

```{figure} ./images/add-device-group-select.jpg
:align: center
:height: 480px
```

Click the back button to return to the device management list to see the newly added device.


```{figure} ./images/add-device-done.jpg
:align: center
:height: 480px
```
