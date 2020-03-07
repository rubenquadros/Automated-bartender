# Created by ruben.quadros on 26/02/20.

import json
import RPi.GPIO as GPIO
import time


# noinspection PyMethodMayBeStatic
class Bartender:
    def __init__(self):
        self.pump_configuration = json.load(open('pump_config.json'))
        GPIO.setmode(GPIO.BCM)
        for pump in self.pump_configuration.keys():
            GPIO.setup(self.pump_configuration[pump]["pin"], GPIO.OUT, initial=GPIO.HIGH)
        print("Done initializing")

    def get_pins(self, ingredients):
        pins = []
        for ingredient in ingredients.keys():
            for pump in self.pump_configuration.keys():
                if self.pump_configuration[pump]["value"] == ingredient:
                    pins.append(self.pump_configuration[pump]["pin"])
        return pins

    def get_quantity(self, ingredients):
        quantities = []
        for ingredient in ingredients.values():
            quantities.append(ingredient)
        return quantities

    def pour_drink(self, pins, quantity):
        wait_time = 2
        for i in range(len(pins)):
            # calculate flow rate based on quantity
            GPIO.output(pins[i], GPIO.LOW)
            time.sleep(wait_time)
            GPIO.output(pins[i], GPIO.HIGH)
