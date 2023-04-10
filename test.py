import gpiozero
import time
"""
good pins:
2
3
20
21
26
"""

"""
drive control
m1
2
3
m2
20
21                                   
"""

"""
reserved for stepper:
5
17
23
25
"""


while True:
    pinToTest = gpiozero.DigitalOutputDevice(int(input("pin num: ")))
    pinToTest.on()
    time.sleep(1)
    pinToTest.off()
    time.sleep(1)