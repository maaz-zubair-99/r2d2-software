from approxeng.input.selectbinder import ControllerResource
from time import sleep
import turtle
acc = 1
rev_acc = 3
max_v = 200
vel = 0
while True:
    try:
        with ControllerResource() as joystick:
            print('Found a joystick and connected')
            while joystick.connected:
                # Do stuff with your joystick here!
                if joystick.r2 is not None and joystick.l2 is None:
                    vel=min(vel+acc,max_v)
                if joystick.l2 is not None and joystick.r2 is None:
                    vel=max(vel-rev_acc,0)
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
