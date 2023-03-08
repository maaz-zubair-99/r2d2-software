import gpiozero
import time
"""
good pins:

5
26
25
23
"""
pin1 = gpiozero.DigitalOutputDevice(17)
pin2 = gpiozero.DigitalOutputDevice(23)
pin3= gpiozero.DigitalOutputDevice(25)
pin4 = gpiozero.DigitalOutputDevice(5)
def writePins(a,b,c,d):
    pin1.value=a
    pin2.value=b
    pin3.value=c
    pin4.value=d
while True:
    writePins(1,1,1,1)
    time.sleep(1)
    writePins(0,0,0,0)
    time.sleep(1)