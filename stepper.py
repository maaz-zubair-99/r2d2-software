import gpiozero
import time
pin1 = gpiozero.DigitalOutputDevice(5)
pin2 = gpiozero.DigitalOutputDevice(6)
pin3= gpiozero.DigitalOutputDevice(12)
pin4 = gpiozero.DigitalOutputDevice(26)

steps = 0
direction = True
def loop():
    for i in range(4096):
        stepper(1)
        time.sleep(0.8)
    direction = not direction
def writePins(a,b,c,d):
    pin1.value=a
    pin2.value=b
    pin3.value=c
    pin4.value=d

def stepper(xw):
    for i in range(xw):
        if(steps == 0):
            writePins(0,0,0,1)
        elif(steps == 1):
            writePins(0,0,1,1)
        elif(steps == 2):
            writePins(0,0,1,0)
        elif(steps == 3):
            writePins(0,1,1,0)
        elif(steps == 4):
            writePins(0,1,0,0)
        elif(steps == 5):
            writePins(1,1,0,0)
        elif(steps == 6):
            writePins(1,0,0,0)
        elif(steps == 7):
            writePins(1,0,0,1)
        else:
            writePins(0,0,0,0)
        setDirection()
def setDirection():
    global steps, direction
    if(direction):
        steps+=1
    if(not direction):
        steps-=1
    if(steps > 7):
        steps=0
    if(steps < 0):
        steps=7

while True:
    loop()