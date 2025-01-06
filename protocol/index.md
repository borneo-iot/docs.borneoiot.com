# Protocol


All Borneo-IoT devices utilize ESPTouch for WiFi provisioning, mDNS/Zeroconf for device discovery, and CoAP as the primary application layer communication protocol.

All CoAP-enabled devices share several common interfaces, such as retrieving device information, with additional interfaces provided by different devices for their unique functions.

```{toctree}
:maxdepth: 2
provisioning
mdns
coap
lyfi
```