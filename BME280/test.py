from mq import *
import sys, time
	while True:
		temperature,pressure,humidity = readBME280All()
  		print "Temperature : ", temperature, "C"
  		print "Pressure : ", pressure, "hPa"
  		print "Humidity : ", humidity, "%"
		time.sleep(0.1)