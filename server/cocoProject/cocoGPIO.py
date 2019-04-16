from gpiozero import OutputDevice
from time import sleep


def feed(pin):
    motor = OutputDevice(int(pin))
    motor.on()
    sleep(3)
    motor.off()