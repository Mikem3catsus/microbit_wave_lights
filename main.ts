let strip = neopixel.create(DigitalPin.P0, 60, NeoPixelMode.RGB)
let wave_1 = [0, 0]
let wave_2 = [0, 0]
let count = 0
function wave_1_strength(index: number): number {
    let scale = 8
    if (index <= 10) {
        return index * scale
    } else if (index < 30) {
        return (15 - index / 2) * scale
    } else {
        return 0
    }
    
}

function wave_2_strength(index: number): number {
    let scale = 4
    if (index < 20) {
        return index * scale / 2
    } else if (index < 40) {
        return (20 - index / 2) * scale
    } else {
        return 0
    }
    
}

function rotate_led_strengths(strengths: number[]) {
    let temp = strengths[0]
    for (let index = 0; index < 60; index++) {
        strengths[index] = strengths[index + 1]
    }
    strengths[59] = temp
}

function show_leds() {
    let l: number;
    for (let index = 0; index < 60; index++) {
        l = wave_1[index]
        if (wave_2[index] > l) {
            l = wave_2[index]
        }
        
        strip.setPixelColor(index, neopixel.hsl(240 - wave_2[index] * 2, 255, l))
    }
}

for (let index = 0; index < 60; index++) {
    wave_1[index] = wave_1_strength(index) + 5
    wave_2[index] = wave_2_strength(index) + 5
}
count = 1
basic.forever(function on_forever() {
    let count: number;
    basic.pause(100)
    rotate_led_strengths(wave_1)
    if (count == 1) {
        rotate_led_strengths(wave_2)
        count = 0
    } else {
        count = 1
    }
    
    show_leds()
    strip.show()
})
