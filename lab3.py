import smbus
import time

class PCF8591:

  def __init__(self, address):
    self.bus = smbus.SMBus(1)
    self.address = address
  
  def read(self, chn):
    try:
        if chn == 0:
            self.bus.write_byte(self.address,0x40)
        if chn == 1:
            self.bus.write_byte(self.address,0x41)
        if chn == 2:
            self.bus.write_byte(self.address,0x42)
        if chn == 3:
            self.bus.write_byte(self.address,0x43)
        self.bus.read_byte(self.address)
    except Exception as e:
        print ("Address: %s" % self.address)
        print (e)
    return self.bus.read_byte(self.address)
  
  def write(self, val):
    try:
        self.bus.write_byte_data(self.address, 0x40, int(val))
    except Exception as e:
        print ("Error: Device address: 0x%2X" % self.address)
        print (e)
  
class Joystick:
  
  def __init__(self):
    self.adc = PCF8591(0x48)

  def getX(self):
    return self.adc.read(0)
  
  def getY(self):
    return self.adc.read(1)

if __name__ == "__main__":
  joystick = Joystick()
  try:
    while True:
      print(str(joystick.getX()) + "\t" + str*joystick.getY())
      time.sleep(0.1)
  except KeyboardInterrupt:
    print("\nExiting")
  except Exception as e:
    print("\ne")
  