# Python Interface for LyFi Compatible Devices

TBD.

## Usage

### Example of getting status and information from a LyFi device

```python
import asyncio
from pprint import pprint
from borneo import LyfiCoapClient

LYFI_DEVICE_ADDRESS = "coap://192.168.1.100"

def main():
    async with LyfiCoapClient(LYFI_DEVICE_ADDRESS) as client:
        response = await client.get_wellknown_core()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>> Wellknown-core:")
        pprint(response, indent=4)

        print(">>>>>>>>>>>>>>>>>>>>>>>>>> Device information:")
        device_info = await client.get_info()
        pprint(device_info, indent=4)

        print(">>>>>>>>>>>>>>>>>>>>>>>>>> Get current time zone:")
        tz = await client.get_timezone()
        print(tz)

        print(">>>>>>>>>>>>>>>>>>>>>>>>>> LyFi device information:")
        lyfi_info = await client.get_lyfi_info()
        pprint(lyfi_info, indent=4)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>> Current general status:")
        status = await client.get_status()
        pprint(status, indent=4)

        print(">>>>>>>>>>>>>>>>>>>>>>>>>> Current LyFi status:")
        status = await client.get_lyfi_status()
        pprint(status, indent=4)

        # Make sure the device is powered on
        print(">>>>>>>>>>>>>>>>>>>>>>>>>> LED Powered on:")
        powered_on = await client.get_on_off()
        pprint(powered_on, indent=4)

        if not powered_on:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>> Turning the power on...")
            await client.set_on_off(True)


asyncio.get_event_loop().run_until_complete(main())

```