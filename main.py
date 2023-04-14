from approxeng.input.selectbinder import ControllerResource
from time import sleep
import turtle
import pygame
import gpiozero
import threading
import sys
# pin1 = gpiozero.DigitalOutputDevice(17)
# pin2 = gpiozero.DigitalOutputDevice(23)
# pin3= gpiozero.DigitalOutputDevice(25)
# pin4 = gpiozero.DigitalOutputDevice(5)

class StepperMotor():
    step_delay=5/1000
    step_steps=10
    def __init__(self,p1,p2,p3,p4):
        self.pin1=gpiozero.DigitalOutputDevice(p1)
        self.pin2=gpiozero.DigitalOutputDevice(p2)
        self.pin3=gpiozero.DigitalOutputDevice(p3)
        self.pin4=gpiozero.DigitalOutputDevice(p4)
    def setStep(self,w1, w2, w3, w4):
        self.pin1.value = w1
        self.pin2.value = w2
        self.pin3.value = w3
        self.pin4.value = w4
    def forward(self):

        i = 0
        while i in range(0, StepperMotor.step_steps):
            self.setStep(1, 0, 1, 0)
            sleep(StepperMotor.step_delay)
            self.setStep(0, 1, 1, 0)
            sleep(StepperMotor.step_delay)
            self.setStep(0, 1, 0, 1)
            sleep(StepperMotor.step_delay)
            self.setStep(1, 0, 0, 1)
            sleep(StepperMotor.step_delay)
            i += 1
    def backward(self):
        i = 0
        while i in range(0, StepperMotor.step_steps):
            self.setStep(1, 0, 0, 1)
            sleep(StepperMotor.step_delay)
            self.setStep(0, 1, 0, 1)
            sleep(StepperMotor.step_delay)
            self.setStep(0, 1, 1, 0)
            sleep(StepperMotor.step_delay)
            self.setStep(1, 0, 1, 0)
            sleep(StepperMotor.step_delay)
            i += 1
class DriveMotors():
    def __init__(self,m1,m2,pwm1,pwm2):
        self.m1 = m1
        self.m2 = m2
        self.pwm1 = gpiozero.PWMOutputDevice(pwm1)
        self.pwm2 = gpiozero.PWMOutputDevice(pwm2)
        self.p1 = [gpiozero.DigitalOutputDevice(m1[0]),gpiozero.DigitalOutputDevice(m1[1])]
        self.p2 = [gpiozero.DigitalOutputDevice(m2[0]),gpiozero.DigitalOutputDevice(m2[1])]
    def writeMotors(self,d1,d2,s1,s2):
        # print(max(0+d1,0),max(0-d1,0),max(0+d2,0),max(0-d2,0))
        self.pwm1.value = s1
        self.pwm2.value = s2
        self.p1[0].value = max(0+d1,0)
        self.p1[1].value = max(0-d1,0)
        self.p2[0].value = max(0+d2,0)
        self.p2[1].value = max(0-d2,0)
    
        

running = True

def handleStepper(joystick=None):
    print(joystick)
    stepper = StepperMotor(17,23,25,5)
    while running:
        if joystick['rx']  >= 0.9:
            stepper.forward()
        if joystick['rx'] <=  -0.9:
            stepper.backward()
        sleep(1/30)
def handleDrive(joystick = None):
    motors = DriveMotors((2,3),(20,21),18,13)
    while running:
        print((vel/max_v)*30)
        motors.writeMotors(1,1,min(1,1+joystick["lx"])*(vel/max_v)*30,min(1,1-joystick["lx"])*(vel/max_v)*30)
pygame.mixer.init()
sound = pygame.mixer.Sound('screaming.wav')
acc = .6
rev_acc = 10
max_v = 200
vel = 0

while True:
    try:
        with ControllerResource() as joystick:
            print('Found a joystick and connected')
            stepper_thread = threading.Thread(target=handleStepper,kwargs={"joystick":joystick},name="joystick_thread")
            stepper_thread.start()
            drive_thread = threading.Thread(target=handleDrive,kwargs={"joystick":joystick},name="drive_thread")
            drive_thread.start()
            while joystick.connected:
                # Do stuff with your joystick here!
                
                if joystick.r2 is not None and joystick.l2 is None:
                    vel=min(vel+acc,max_v)
                if joystick.l2 is not None and joystick.r2 is None:
                    vel=max(vel-rev_acc,0)
                if joystick.cross is not None:
                    turtle.clear()
                if joystick.dup is not None:
                    sound.play()
                if joystick.ddown is not None:
                    running = False
                    stepper_thread.join()
                    drive_thread.join()
                    sys.exit("Program ended")
                turtle.forward(vel)
                vel*=0.9
                turtle.right(joystick['lx']*15)
                # ....
        # Joystick disconnected...
        print('Connection to joystick lost')
    except IOError:
        # No joystick found, wait for a bit before trying again
        print('Unable to find any joysticks')
        sleep(1.0)
