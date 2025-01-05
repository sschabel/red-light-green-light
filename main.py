from time import sleep

import machine
from machine import I2C, Pin
from picozero import LED
from picozero import Buzzer

from light import Light
from pico_i2c_lcd import I2cLcd
from red_light_green_light import RedLightGreenLight

SDA_PIN = 0
SCL_PIN = 1

i2c = I2C(0, sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)

I2C_ADDRESS = i2c.scan()[0]
I2C_NUM_ROWS = 2 # This depends on how many rows your I2C screen has
I2C_NUM_COLS = 16 # This depends on how many columns your I2C screen has

# These will change depending on which GPIO Pin is used for your LEDs
GREEN_LED_GPIO = 13
YELLOW_LED_GPIO = 8
RED_LED_GPIO = 6
BUZZER_GPIO = 28

lcd = I2cLcd(i2c, I2C_ADDRESS, I2C_NUM_ROWS, I2C_NUM_COLS)

button = machine.Pin(18, Pin.IN, Pin.PULL_UP) # button to turn game on & off
greenLed = LED(GREEN_LED_GPIO)
yellowLed = LED(YELLOW_LED_GPIO)
redLed = LED(RED_LED_GPIO)
buzzer = Buzzer(BUZZER_GPIO)

greenLight = Light("Green", greenLed)
yellowLight = Light("Yellow", yellowLed)
redLight = Light("Red", redLed)

lcd.backlight_off()

game = RedLightGreenLight(redLight, yellowLight, greenLight, lcd, buzzer)

def handle_interrupt(pin):
    game.end_game()
    button.irq(None, Pin.IRQ_RISING)

while True:
    if button.value() == 0:
        print("You pressed the button!")
        sleep(0.5)
        button.irq(handler=handle_interrupt, trigger=Pin.IRQ_RISING)
        game.start_game()