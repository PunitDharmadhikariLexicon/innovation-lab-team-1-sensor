import sqlite3
from datetime import datetime

table_name = "sensor_data"

def insert_sensor_data(co2, temperature, humidity):
	try:
		sqliteConnection = sqlite3.connect("../db/sensor_data.db")
		cursor = sqliteConnection.cursor()
		print("Successfully connected to SQLite")
		now = datetime.now()
		sqlite_insert_query = """INSERT INTO """ + table_name + """(datetime, co2, temperature, humidity)
					VALUES 
					(?, ?,?,?);"""
		data_tuple = (now, co2, temperature, humidity)
		count = cursor.execute(sqlite_insert_query, data_tuple)
		sqliteConnection.commit()
		print("Record successfully inserted record into \'" + table_name + "\' table: (", cursor.rowcount, ")")
		cursor.close()
	except sqlite3.Error as error:
		print("Failed to insert data into \'" + table_name + "\'", error)
	finally:
		if sqliteConnection:
			sqliteConnection.close()
			print("The SQLite connection is now closed")
