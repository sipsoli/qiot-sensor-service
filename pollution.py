#!/usr/bin/env python3
from pms5003 import PMS5003

pms5003 = PMS5003(
    device='/dev/ttyAMA0',
    baudrate=9600,
    pin_enable=22,
    pin_reset=27
)


def get_all_particulates():
    pms5003data = pms5003.read()
    readings = pms5003data.data
    return {
        'pm1_0': readings[0],
        'pm2_5': readings[1],
        'pm10': readings[2],
        'pm1_0_atm': readings[3],
        'pm2_5_atm': readings[4],
        'pm10_atm': readings[5],
        'gt0_3um': readings[6],
        'gt0_5um': readings[7],
        'gt1_0um': readings[8],
        'gt2_5um': readings[9],
        'gt5_0um': readings[10],
        'gt10um': readings[11]
    }
