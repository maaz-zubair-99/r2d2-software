from approxeng.input.selectbinder import ControllerResource
from time import sleep
import turtle
import pygame
import gpiozero
import threading
pin1 = gpiozero.DigitalOutputDevice(17)
pin2 = gpiozero.DigitalOutputDevice(23)
pin3= gpiozero.DigitalOutputDevice(25)
pin4 = gpiozero.DigitalOutputDevice(5)
step_delay=5/1000
step_steps=5
def forward():
    global fd_started
    i = 0
    while i in range(0, step_steps):
        setStep(1, 0, 1, 0)
        sleep(step_delay)
        setStep(0, 1, 1, 0)
        sleep(step_delay)
        setStep(0, 1, 0, 1)
        sleep(step_delay)
        setStep(1, 0, 0, 1)
        sleep(step_delay)
        i += 1
    fd_started =False
def backward():
    i = 0
    while i in range(0, step_steps):
        setStep(1, 0, 0, 1)
        sleep(step_delay)
        setStep(0, 1, 0, 1)
        sleep(step_delay)
        setStep(0, 1, 1, 0)
        sleep(step_delay)
        setStep(1, 0, 1, 0)
        sleep(step_delay)
        i += 1

def setStep(w1, w2, w3, w4):
    pin1.value = w1
    pin2.value = w2
    pin3.value = w3
    pin4.value = w4

running = True

def handleStepper(joystick=None):
    print(joystick)
    while running:
        if joystick['rx']  >= 0.9:
            forward()
        if joystick['rx'] <=  -0.9:
            backward()
        sleep(1/30)

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
