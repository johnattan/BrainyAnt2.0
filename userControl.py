import RPi.GPIO as gpio


def move_forward(speed):
    if speed > 0:
        init()
        print('Moving FORWARD with speed = {}'.format(speed))
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(23, True)
        gpio.output(24, False)
    else:
        gpio.cleanup()


def move_left(speed):
    if speed > 0:
        init()
        print('Moving LEFT with speed = {}'.format(speed))
        gpio.output(17, False)
        gpio.output(22, True)
        gpio.output(23, True)
        gpio.output(24, False)
    else:
        gpio.cleanup()


def move_right(speed):
    if speed > 0:
        init()
        print('Moving RIGHT with speed = {}'.format(speed))
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(23, False)
        gpio.output(24, True)
    else:
        gpio.cleanup()


def move_back(speed):
    if speed > 0:
        init()
        print('Moving BACK with speed = {}'.format(speed))
        gpio.output(17, False)
        gpio.output(22, True)
        gpio.output(23, False)
        gpio.output(24, True)
    else:
        gpio.cleanup()


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
