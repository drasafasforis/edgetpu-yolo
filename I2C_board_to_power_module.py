#I2C_board_to_power_module
from periphery import I2C


try:
    while True:
        try:
            i2c = I2C("/dev/i2c-1")
            data = [0,0]
            msgs = I2C.Message(data, read=True)

            print(hex(msgs))

            
        except Exception as e:
            print(f"An error occurered: {e}")
            
except KeyboardInterrupt:
    i2c.close()
