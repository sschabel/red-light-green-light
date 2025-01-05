from time import sleep
import random
from math import floor

class RedLightGreenLight:
    
    def __init__(self, redLight, yellowLight, greenLight, lcd, buzzer):
        self.redLight = redLight
        self.yellowLight = yellowLight
        self.greenLight = greenLight
        self.lcd = lcd
        self.buzzer = buzzer
        self.playing = False
    
    def determine_next_light(self, duration):
        light = random.randint(1, 3)
        if light == 1:
            self.buzzTime = 1
            return self.greenLight
        elif light == 2:
            self.buzzTime = 0.5
            return self.yellowLight
        else:
            self.buzzTime = 2.5
            return self.redLight
        
    def change_light(self, lastLight, nextLight):
        if lastLight != None:
            lastLight.led.off()
        self.update_lcd(nextLight.color)
        nextLight.led.on()
        self.buzzer.on(t=self.buzzTime)
        
    def update_lcd(self, color):
        lcd = self.lcd
        lcd.clear()
        lcd.backlight_on()
        length = len(color)
        remainingChars = 16 - length
        startPosition = floor(remainingChars / 2)
        lcd.move_to(startPosition, 0)
        lcd.putstr(color)
        lcd.move_to(5,1)
        lcd.putstr("Light!")

    def update_lcd_for_start(self):
        lcd = self.lcd
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(3, 0)
        lcd.putstr("Get ready to")
        lcd.move_to(4,1)
        lcd.putstr("play in...")
        sleep(1)
        lcd.clear()
        lcd.move_to(8, 0)
        lcd.putstr("3")
        self.buzzer.on(t=1)
        sleep(1)
        lcd.clear()
        lcd.move_to(8, 0)
        lcd.putstr("2")
        self.buzzer.on(t=1)
        sleep(1)
        lcd.clear()
        lcd.move_to(8, 0)
        lcd.putstr("1")
        self.buzzer.on(t=1)
        sleep(1)
        lcd.backlight_off()
    
    def start_game(self):
        self.playing = True
        lastLight = self.redLight
        self.update_lcd_for_start()
        
        while self.playing:
            duration = random.randint(3, 8)
            nextLight = self.determine_next_light(duration)
            self.change_light(lastLight, nextLight)
            sleep(duration)
            lastLight = nextLight
    
    def end_game(self):
        self.playing = False
        self.greenLight.led.off()
        self.yellowLight.led.off()
        self.redLight.led.off()
        lcd = self.lcd
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(3, 0)
        lcd.putstr("Thanks for")
        lcd.move_to(4,1)
        lcd.putstr("playing!")
        sleep(5)
        lcd.clear()
        lcd.backlight_off()
        