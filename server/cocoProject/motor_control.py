from gpiozero import OutputDevice
from time import sleep
import sys

class MotorControl():

    pin = 0

    def __init__(self, pin):
        self.pin = pin

    def feed(self, delay=1):
        motor = OutputDevice(self.pin)
        motor.on()
        sleep(delay)
        motor.off()







if __name__ == "__main__":
    pin = int(sys.argv[1])
    motor = MotorControl(pin)
    motor.feed()


