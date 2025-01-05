from time import sleep, sleep_ms
import random
from math import floor

class RedLightGreenLight:
    
    def __init__(self, red_light, yellow_light, green_light, lcd, buzzer):
        self.red_light = red_light
        self.yellow_light = yellow_light
        self.green_light = green_light
        self.lcd = lcd
        self.buzzer = buzzer
        self.playing = False
    
    def determine_next_light(self, last_light):
        if last_light == self.red_light:
            light = random.choice([1, 2])
        elif last_light == self.yellow_light:
            light = random.choice([1, 3])
        else:
            light = random.choice([2, 3])

        if light == 1:
            return self.green_light
        elif light == 2:
            return self.yellow_light
        else:
            return self.red_light
        
    def change_light(self, last_light, next_light):
        if last_light is not None:
            last_light.led.off()
        self.update_lcd(next_light.color)
        next_light.led.on()
        self.activate_buzzer(next_light)

    def activate_buzzer(self, next_light):
        if next_light == self.green_light:
            self.buzzer.on(t=0.15)
            sleep_ms(250)
            self.buzzer.on(t=0.15)
            sleep_ms(250)
            self.buzzer.on(t=0.15)
        elif next_light == self.yellow_light:
            self.buzzer.on(t=0.15)
            sleep_ms(250)
            self.buzzer.on(t=0.15)
        else:
            self.buzzer.on(t=1.5)
        
    def update_lcd(self, color):
        lcd = self.lcd
        lcd.clear()
        lcd.backlight_on()
        length = len(color)
        remaining_chars = 16 - length
        start_position = floor(remaining_chars / 2)
        lcd.move_to(start_position, 0)
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
        last_light = self.red_light
        self.update_lcd_for_start()
        
        while self.playing:
            duration = random.randint(3, 8)
            next_light = self.determine_next_light(last_light)
            self.change_light(last_light, next_light)
            sleep(duration)
            last_light = next_light
    
    def end_game(self):
        self.playing = False
        self.green_light.led.off()
        self.yellow_light.led.off()
        self.red_light.led.off()
        self.buzzer.off()
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
        