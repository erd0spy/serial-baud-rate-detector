# Serial Baud Rate Detector

Serial Baud Rate Detector is a Python script that detects the baud rate of a device connected to a serial port using an FT232RL or FT232H USB-to-serial adapter. It may also work with other adapters, but this has not been tested.

The script is developed for hardware hacking and security research, and is useful when you need to communicate with a device over a serial connection, but you don't know the baud rate. With this script, you can quickly and easily determine the baud rate of the target device, which can help you in reverse engineering, debugging, and testing.

## Requirements

This script requires the following:
- Python 3.x
- pyserial 3.4 (Python package for accessing serial ports)

## Installation

To install the required Python packages, run the following command:

```bash
$ git clone https://github.com/erd0spy/serial-baud-rate-detector
$ cd serial-baud-rate-detector
$ pip3 install -r requirements.txt
```

## Usage

To use the script, run the following command:

```bash
$ python3 baud-rate-detector.py [serial port] [options]
```

Replace `[serial port]` with the name of the serial port to scan (e.g., `/dev/ttyUSB0` on Linux or `COM3` on Windows). The following options are available:
-    `-t`, `--timeout`: The timeout for serial communication in seconds (default: 3).
-    `-a`, `--all`: If set, scan all possible UART baud rates (may take longer).
-    `-d`, `--data`: The data to send to the device in ASCII format (default: "AT\r\n").
-    `-p`, `--print`: If set, print the response received from the device.
-    `--print-all`: If set, print the response for all tested baud rates.

## License

This script is released under the MIT License. Feel free to use, modify, and distribute it as you see fit. However, please note that the script is provided as-is, and the author assumes no liability for any issues that may arise from its use.
