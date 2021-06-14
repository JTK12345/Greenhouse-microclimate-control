from sgp30 import SGP30
import time

sgp30 = SGP30()

while True:
    result = sgp30.get_air_quality()
    print(result)
    time.sleep(1.0)
