#!/usr/bin/env python3
import subprocess


def get_serial_number():
    result = subprocess.run("cat /sys/firmware/devicetree/base/serial-number", check=True,
                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rpi3_serial = {
        'id': result.stdout.decode("utf-8").rstrip("\x00")
    }
    return rpi3_serial
