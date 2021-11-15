#!/usr/bin/python3
# Adapted from https://pypi.org/project/scd30-i2c/
# Gregory Berardi 09/06/2021


from scd30_i2c import SCD30
import time
from datetime import datetime

scd30 = SCD30()

scd30.set_measurement_interval(2)
scd30.start_periodic_measurement()

while True:
    if scd30.get_data_ready():
        m = scd30.read_measurement()
        if m is not None:
            now = datetime.now()
            current_time = now.strftime("%D %H:%M:%S")
#            with open('co2.dat', 'w') as f:
            print(f"{current_time},{m[0]:.2f},{m[1]*1.8+32:.2f},{m[2]:.2f}")
#            print(f"{current_time} - CO2: {m[0]:.2f}ppm, temp: {m[1]*1.8+32:.2f}°F, rh: {m[2]:.2f}%")
        time.sleep(2)
    else:
        time.sleep(0.2)
