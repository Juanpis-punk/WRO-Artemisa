#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.


    
# Initialize the motors.
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
claw = Motor(Port.A)
rotar = Motor (Port.D)
# Initialize the color sensor.
line_sensor = ColorSensor(Port.S1)
line_sensor2 = ColorSensor(Port.S4)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=150)

DRIVE_SPEED = 200
PROPORTIONAL_GAIN = 1.3
ninety = 560
devolver=0

def seguir_linea():
    deviation = line_sensor.reflection() - line_sensor2.reflection()
    turn_rate = PROPORTIONAL_GAIN * deviation
    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)
    
    
def avance1():
    right_motor.run_angle(400,1000,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(400,1000,then=Stop.BRAKE, wait=True)
    
def avance2():
    right_motor.run_angle(400,1160,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(400,1160,then=Stop.BRAKE, wait=True)
    
    
def subir_garra():    
    claw.run_angle(200, -160, then=Stop.HOLD, wait=True)

def bajar_garra():
    claw.run_angle(50, 193, then=Stop.HOLD, wait=True)

def rotar_garra():
    global devolver 
    rotar.run_angle(200, 134, then=Stop.HOLD, wait=True)
    devolver = devolver+1 
    
def devolver_garra():
    # rotar.run_angle(200, -(134*devolver), then=Stop.HOLD, wait=True)
    rotar.reset_angle(0)
    
def escotilla_movible():
    avance1()
    right_motor.run_angle(500, 200, then=Stop.BRAKE, wait=True)
    left_motor.run_angle(500, , then=Stop.BRAKE, wait=True)
    avance2()
    

    
def ensayo():
    right_motor.run_angle(200,90, then=Stop.BRAKE, wait=True)
    
def artemisa():
    escotilla_movible()
    

    

    

while True:
    artemisa()
    break 
    
    
    

    
