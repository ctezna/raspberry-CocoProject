from gpiozero import OutputDevice
from time import sleep


def feed(pin,sleep):
    motor = OutputDevice(int(pin))
    motor.on()
    sleep(int(sleep))
    motor.off()