# Python Interface for LyFi Compatible Devices

TBD.

## Usage

```python
import asyncio
from borneo import LyfiCoapClient

LYFI_DEVICE_ADDRESS = "coap://192.168.1.100"

async with LyfiCoapClient(LYFI_DEVICE_ADDRESS) as client:
    response = await client.get_wellknown_core()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>> Wellknown-core:")
    print(response)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>> Device information:")
    print(await client.get_info())

    print(">>>>>>>>>>>>>>>>>>>>>>>>>> Get current time zone:")
    print(await client.get_timezone())


```