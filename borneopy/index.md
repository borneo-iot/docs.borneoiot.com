(borneopy)=
# Python API & Command Line Tools

This project provides an open-source Python client API library for device communication, which can be used for debugging, testing, or integrating devices with other automation systems, such as Home Assistant.

## Installation

```bash
pip install borneoiot
```

This package also installs a globally available command-line tool, `bocli`, which provides utilities for device testing, local OTA updates, provisioning, and other development tasks. After installation you can run `bocli --help` to view available commands and usage examples.

```{toctree}
:maxdepth: 2
esptouch
lyfi
cli
```