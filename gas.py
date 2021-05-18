#!/usr/bin/env python3
from enviroplus import gas

gas.enable_adc()
gas.set_adc_gain(4.096)


def get_gas_data():
    return {
        'adc': gas.read_adc(),
        'nh3': gas.read_nh3(),
        'oxidising': gas.read_oxidising(),
        'reducing': gas.read_reducing()
    }
