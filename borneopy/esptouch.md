# ESPTouch WiFi Provisioning

TBD.

## Usage

```python
import asyncio
from borneo import *

SSID = "Your WiFi name (SSID)"
PASSWORD = "Your WiFi password"
BROADCAST = True
IP = "IP of this machine"
smart_config = EspTouch(SSID, PASSWORD, BROADCAST, IP)
asyncio.run(smart_config.send_data(timeout=10)) # Running for 10 seconds
```