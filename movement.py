
import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

    global s, e, t, f
    s = gpio.PWM(7, 50)
    e = gpio.PWM(11, 50)
    t = gpio.PWM(13, 50)
    f = gpio.PWM(15, 50)

    s.start(0)
    e.start(0)
    t.start(0)
    f.start(0)


def end():
    s.stop()
    e.stop()
    t.stop()
    f.stop()


def forward(tf):
    init()
    s.ChangeDutyCycle(0)
    e.ChangeDutyCycle(97)
    t.ChangeDutyCycle(100)
    f.ChangeDutyCycle(0)
    time.sleep(tf)
    end()
    gpio.cleanup()


def reverse(tf):
    init()
    s.ChangeDutyCycle(99)
    e.ChangeDutyCycle(0)
    t.ChangeDutyCycle(0)
    f.ChangeDutyCycle(100)
    time.sleep(tf)
    end()
    gpio.cleanup()


def right(tf):
    init()
    s.ChangeDutyCycle(0)  # true
    e.ChangeDutyCycle(20)  # true
    t.ChangeDutyCycle(100)  # true
    f.ChangeDutyCycle(0)  # false
    time.sleep(tf)
    end()
    gpio.cleanup()


def left(tf):
    init()
    s.ChangeDutyCycle(0)  # false
    e.ChangeDutyCycle(100)  # true
    t.ChangeDutyCycle(20)  # false
    f.ChangeDutyCycle(0)  # false
    time.sleep(tf)
    end()
    gpio.cleanup()
