#!/usr/bin/env python3

import argparse
import serial
import time
import string

DEFAULT_TIMEOUT = 3  # seconds
BAUDRATES = (110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 128000, 230400, 256000, 460800, 576000, 921600)

def detect_baud_rate(port, data=None, timeout=DEFAULT_TIMEOUT, scan_all=False, print_response=False, print_all=False):
    baudrates = BAUDRATES if scan_all else (9600, 19200, 38400, 57600, 115200, 14400)
    detected_baud_rate = None
    for baudrate in baudrates:
        with serial.Serial(port, timeout=timeout) as ser:
            ser.baudrate = baudrate
            if data is not None:
                ser.write(data)
                time.sleep(timeout)
            response = ser.read(ser.in_waiting)
            if validate_response(response):
                if print_response or print_all:
                    print(f"Response at {baudrate} baud rate: {response}")
                detected_baud_rate = baudrate
                if not print_all:
                    break
    if detected_baud_rate is not None:
        print(f"Detected baud rate: {detected_baud_rate}")
    else:
        print("Could not detect baud rate.")

def validate_response(response):
    try:
        response_str = response.decode()
        return any(c in string.printable for c in response_str)
    except UnicodeDecodeError:
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Detect the baud rate of a device connected to an USB-to-serial adapter')
    parser.add_argument('port', type=str, help='The name of the serial port to scan')
    parser.add_argument('-t', '--timeout', type=float, default=DEFAULT_TIMEOUT, help='The timeout for serial communication in seconds (default: 3)')
    parser.add_argument('-a', '--all', action='store_true', help='If set, scan all possible UART baud rates (may take longer)')
    parser.add_argument('-d', '--data', type=str, help='The data to send to the device in ASCII format (default: "AT\\r\\n")')
    parser.add_argument('-p', '--print', action='store_true', help='If set, print the response received from the device')
    parser.add_argument('--print-all', action='store_true', help='If set, print the response for all tested baud rates')
    args = parser.parse_args()

    data = args.data.encode() if args.data is not None else b'AT\r\n'
    detect_baud_rate(args.port, data=data, timeout=args.timeout, scan_all=args.all, print_response=args.print, print_all=args.print_all)
