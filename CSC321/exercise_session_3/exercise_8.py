from machine import Pin, PWM
from time import sleep

led_pin = 19
push_btn_pin = 22
buz_pin = Pin(27)

buzzer = PWM(buz_pin)
led = Pin(led_pin, Pin.OUT)


C6 = 1047
CS6 = 1109
D6 = 1175
DS6 = 1245
E6 = 1319
F6 = 1397
FS6 = 1480
G6 = 1568
GS6 = 1661
A6 = 1760
AS6 = 1865
B6 = 1976
C7 = 2093
CS7 =2217
D7 = 2349
DS7 = 2489
E7 = 2637
F7 = 2794
FS7 = 2960
G7 = 3136
GS7 = 3322
A7 = 3520
AS7 = 3729
B7 = 3951

def play(notes, delay, active_duty=50):
    for note in notes:
        if note == 0:
            buzzer.duty(0)
        else:
            buzzer.freq(note)
            buzzer.duty(active_duty)
        sleep(delay)
    buzzer.duty(0)
    buzzer.deinit()
    
song = [
    C6, C6, 0, 0, G6, 0, G6, 0, G6, 0, G6, 0, G6, G6, 0, 0, 0,
     E6, 0, F6, 0, E6, 0, D6, 0, C6, 0, A6, A6, 0, 0, 0,
     G6, G6, 0, C6, C6, 0, B6, B6, 0, D6, D6, 0, C6, C6, 0, 0, 0, 0,
     C6, C6, 0, 0, G6, 0, G6, 0, G6, 0, G6, 0, G6, G6, 0, 0, 0,
     E6, 0, F6, 0, E6, 0, D6, 0, C6, 0, A6, A6, 0, 0, 0,0,
     G6, G6, 0, C6, C6, 0, B6, B6, 0, D6, D6, 0, C6, C6, 0,
     C7, 0, C7, 0, 0, G6, 0, A6, 0, G6, 0, 0, E6, 0, G6, G6, 0, 0, 0,
     F6, 0, E6, 0, F6, 0, 0, E6, 0, F6, 0, 0, E6, E6, 0, D6, D6, D6, 0, C6, C6, 0, A7, 0,
     G6, G6, 0, C6, C6, 0, B6, B6, 0, D6, D6, 0, C6, C6, 0, 0, 0, 0]

play(song, 0.19)