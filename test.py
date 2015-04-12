#!/usr/bin/env python

__author__ = 'lusio'

import mraa

led = mraa.Gpio(4)
led.dir(mraa.DIR_OUT)

#fan = mraa.Aio(8)
fan = mraa.Pwm(3)
# fan.dir(mraa.DIR_OUT)


def set_fan(b):
    fan.write(b)


def set_led(b):
    led.write(b)