# Add your Python code here. E.g.
from microbit import *
import neopixel

strip = neopixel.create(DigitalPin.P0, 60, NeoPixelMode.RGB)
count = 0

class Wave():
    def strength(self, index):
        return 0

    def hue_shift(self,index):
        return 0

    def move_wave(self):
        pass

from typing import List, int

class Wave1(Wave):
    def __init__(self):
        i:int = 0
        self.strengths = [0,0,0,0]
        for i in range(0,60):
            self.strengths[i] = wave_1_strength(i)
    def strength(self,index):
        return self.strengths[index]
    def move_wave(self):
        rotate_led_strengths(self.strengths)

class Wave2(Wave):
    def __init__(self):
        self.hue_shifts = [0,0]
        for i in range(0,60):
            self.hue_shifts[i] = wave_2_strength(i)
    def hue_shift(self,index):
        return self.hue_shifts[index]
    def move_wave(self):
        rotate_led_strengths(self.hue_shifts)

def wave_1_strength(index):
    scale = 8
    if index <=10:
        return index * scale
    elif index < 30:
        return (15 - (index/2)) * scale
    else:
        return 0

def wave_2_strength(index):
    scale=4
    if index <20:
        return index *scale/2
    elif index < 40:
        return (20 - (index/2)) * scale
    else:
        return 0

def rotate_led_strengths(strengths):
    temp = strengths[0]
    for index in range(60):
        strengths[index] = strengths[index+1]
    strengths[59] = temp

def show_leds(wave_array):
    for index in range(60):
        strength = 0
        for wave in waves:
            if wave.strength(index) > strength:
                strength = wave.strength(index)
        hue_shift = 0
        for wave in waves:
            hue_shift = hue_shift + wave.hue_shift(index)
        strip.set_pixel_color(index, neopixel.hsl(240-hue_shift*2,255, strength))

waves:List[Wave] = [Wave1(), Wave2()]

def move_waves(waves:List[Wave]):
    for wave in waves:
        wave.move_wave()

while True:
    global count
    global waves
    basic.pause(100)
    move_waves(waves)
    waves[0].move_wave()
    show_leds(waves)
    strip.show()
