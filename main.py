import sys
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)

print("I2C devices found: ", [hex(i) for i in i2c.scan()])

bme688 = 0x61

if not bme688 in i2c.scan():
	print("Could not find device")
	sys.exit()

def get_bme688_id():
	i2c.writeto(bme688, bytes([0xd0]), stop=False)
	result = bytearray(1)
	i2c.readfrom_into(bme688, result)
	print("Value ID:", int.from_bytes(result, "big"))



def setup_db():
	pass



if __name__ == "__main__":
	get_bme688_id()
