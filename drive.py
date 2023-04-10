import gpiozero
from time import sleep
class DriveMotors():
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        self.p1 = [gpiozero.DigitalOutputDevice(m1[0]),gpiozero.DigitalOutputDevice(m1[1])]
        self.p2 = [gpiozero.DigitalOutputDevice(m2[0]),gpiozero.DigitalOutputDevice(m2[1])]
    def writeMotors(self,d1,d2):
        print(max(0+d1,0),max(0-d1,0),max(0+d2,0),max(0-d2,0))
        self.p1[0].value = max(0+d1,0)
        self.p1[1].value = max(0-d1,0)
        self.p2[0].value = max(0+d2,0)
        self.p2[1].value = max(0-d2,0)
    
        

motors = DriveMotors((2,3),(20,21))


while True:
    motors.writeMotors(0,0)
    sleep(1)
    motors.writeMotors(1,-1)
    sleep(1)
    motors.writeMotors(-1,1)
    sleep(1) 

