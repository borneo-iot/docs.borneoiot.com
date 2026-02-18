# ESPTouch WiFi Provisioning

> ⚠️ **Deprecated** — EspTouch provisioning is deprecated for new Borneo‑IoT devices. We now use **Bluetooth (BLE) provisioning** for onboarding new hardware; EspTouch is retained only for legacy / older devices that do not support BLE.
>
> For new devices and mobile‑app workflows prefer the BLE provisioning method. If you need BLE provisioning documentation added here or elsewhere, tell me and I will add it.

Overview

The `EspTouch` helper implements smart-config style provisioning (ESP-Touch) used by many Espressif-based devices to receive Wi‑Fi credentials over the local network. Use it from scripts or interactive tools when you need to provision devices without a web UI.

Quick start

- Create an `EspTouch` instance with SSID and password.
- Call `send_data(timeout=...)` to broadcast the credentials for a limited time.

Usage (Python)

```python
import asyncio
from borneo import EspTouch

SSID = "Your WiFi name (SSID)"
PASSWORD = "Your WiFi password"
BROADCAST = True
IP = "IP of this machine"

smart_config = EspTouch(SSID, PASSWORD, BROADCAST, IP)
# broadcast credentials for 10 seconds
asyncio.run(smart_config.send_data(timeout=10))
```

Parameters
- SSID (str): Wi‑Fi network name
- PASSWORD (str): Wi‑Fi password (passphrase)
- BROADCAST (bool): whether to use broadcast packets
- IP (str | None): local interface IP to use for sending packets
- timeout (int | float): seconds to transmit the provisioning packets

Behavior & notes
- The operation is time‑limited — set an appropriate `timeout` (5–15s is typical).
- Running as a normal user is usually sufficient, but some platforms may require elevated privileges to send raw/broadcast packets.
- The provisioning process is best performed near the target device (Wi‑Fi range).

See also
- `bocli mdns` to discover devices after provisioning
- `borneopy` Python API for higher‑level device onboarding workflows
