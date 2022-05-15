import smbus
import time

sensor = 0x23

turnoff = 0x00
turnon = 0x01
reset = 0x07 

received_address = 0x23
bus = smbus.SMBus(1)

time.sleep(1)

def light():
    address = bus.read_i2c_block_data(sensor,received_address)
    val = light_intensity(address)
    return val

def light_intensity(address):
    val = (address[1] + (256 * address[0])) / 1.2
    return val

def message():
    while 1:
        intensity = light()
        print("Value: " ,end = "")
        print(light())
        if(intensity  > 1300):
            print("very bright")
        elif(intensity > 600 and intesity < 1000):
            print("bright")
        elif(intensity > 200 and intensity < 600):
            print("dim")
        elif(intensity > 50 and intensity <150):
            print("dark")
        elif(intensity< 50):
            print("too dark")
            
        time.sleep(0.50)
        print
        
message()  
