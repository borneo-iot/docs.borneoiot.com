# Command Line Tools

### `bocli` — command-line tool 🔧

`bocli` is the console script provided by this package (see `pyproject.toml`).
Install the package to get the `bocli` command (`pip install -e .`) or run via `uv run bocli`.

Usage:

```text
bocli [global options] <command> [command options]
```

Global options
- `-h, --host`  Device base URL for CoAP commands (e.g. `coap://192.168.1.10`)
- `-v, --verbose`  Increase verbosity (repeatable)
- `-c, --compatible`  Compatibility string (default: `bst,borneo-lyfi`)
- `--version`  Print version and exit

Available commands
- `lota` — perform local OTA over CoAP
  - usage: `bocli -h coap://192.168.1.100 lota firmware.bin [--block-size 512] [--status-only]`
  - note: `fw_path` is required; `--status-only` will only query OTA status and exit
- `mdns` — discover devices via mDNS (e.g. `bocli mdns -t 5` or `bocli mdns --find`)
- `get` — call `get_<what>` on `LyfiCoapClient` and print JSON
  - usage: `bocli -h coap://192.168.1.100 get color`
  - list targets: `bocli -h coap://192.168.1.100 get --list`
- `capabilities` — list available `get_...` methods (supports `--json`)
- `on` / `off` — turn device on / off (e.g. `bocli -h coap://192.168.1.100 on`)
- `factory-reset` — perform factory reset (use `-y` to bypass confirmation)

Examples
```bash
# discover devices with mDNS for 3 seconds
bocli mdns -t 3

# list `get_...` targets supported by the device
bocli -h coap://192.168.1.100 get --list

# get a resource (prints JSON)
bocli -h coap://192.168.1.100 get color

# turn device on
bocli -h coap://192.168.1.100 on

# perform OTA (upload firmware)
bocli -h coap://192.168.1.100 lota firmware.bin
# check OTA status only (fw_path is still required by the CLI)
bocli -h coap://192.168.1.100 lota firmware.bin --status-only
```

See `borneo/cli.py` for full command descriptions and options.