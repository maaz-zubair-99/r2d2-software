import time
import gpiozero
import math
pin1 = gpiozero.DigitalOutputDevice(17)
pin2 = gpiozero.DigitalOutputDevice(23)
pin3= gpiozero.DigitalOutputDevice(25)
pin4 = gpiozero.DigitalOutputDevice(5)






def forward(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        i += 1

def backwards(delay, steps):
    i = 0
    while i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        i += 1

def setStep(w1, w2, w3, w4):
    pin1.value = w1
    pin2.value = w2
    pin3.value = w3
    pin4.value = w4

while True:
    user_delay = input("Delay between steps (milliseconds)?")
    user_steps = input("How many steps forward? ")
    forward(int(user_delay) / 1000.0, int(user_steps))
    user_steps = input("How many steps backwards? ")
    backwards(int(user_delay) / 1000.0,int(user_steps))