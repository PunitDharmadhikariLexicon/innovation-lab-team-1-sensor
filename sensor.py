import board
import adafruit_scd30
import busio
import time
from datetime import datetime
import sqlite3
from db import insert_sensor_data

i2c = busio.I2C(board.SCL, board.SDA)
scd = adafruit_scd30.SCD30(board.I2C())

while True:
	if scd.data_available:
		print("Data Available?", "True" if scd.data_available else "False")
		now = datetime.now()
		print("Date/Time:", now)
		print("CO2:", scd.CO2, "PPM")
		print("Temperature:", scd.temperature, "degrees C")
		print("Humidity:", scd.relative_humidity, "%%rH")
		insert_sensor_data(scd.CO2, scd.temperature, scd.relative_humidity)
		print("-"*15)
	time.sleep(10)


