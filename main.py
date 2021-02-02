strip = neopixel.create(DigitalPin.P0, 60, NeoPixelMode.RGB)
wave_1 = [0,0]
wave_2 = [0,0]
count = 0

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

def show_leds():
    for index in range(60):
        l = wave_1[index]
        if wave_2[index] > l :
             l = wave_2[index]
        strip.set_pixel_color(index, neopixel.hsl(240-(wave_2[index]*2),255, l))

for index in range(60):
    wave_1[index] = (wave_1_strength(index)+5)
    wave_2[index]  = (wave_2_strength(index)+5)

def on_forever():
    global count
    basic.pause(100)
    rotate_led_strengths(wave_1)
    led.plot(count,1)
    if count == 0:
        led.plot(count,count)
        rotate_led_strengths(wave_2)
        count = 1
    else:
        led.plot(count,count)
        count = 0
    show_leds()
    strip.show()

basic.forever(on_forever)