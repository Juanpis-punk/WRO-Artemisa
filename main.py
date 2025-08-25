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

# Constants
DRIVE_SPEED = 200
PROPORTIONAL_GAIN = 1.3
ninety = 560

# State machine variables
current_state = "INIT"
devolver = 0
mission_complete = False

# States
STATE_INIT = "INIT"
STATE_MOVIBLE_HATCH = "MOVIBLE_HATCH"
STATE_FIXED_HATCH = "FIXED_HATCH"
STATE_COMPLETE = "COMPLETE"

def seguir_linea():
    """Follow line using two color sensors"""
    deviation = line_sensor.reflection() - line_sensor2.reflection()
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)

def avance1():
    """First advance movement"""
    right_motor.run_angle(400, 1150, then=Stop.BRAKE, wait=False)
    left_motor.run_angle(400, 1150, then=Stop.BRAKE, wait=True)
    
def avance2():
    """Second advance movement"""
    right_motor.run_angle(400, 1150, then=Stop.BRAKE, wait=False)
    left_motor.run_angle(400, 1150, then=Stop.BRAKE, wait=True)

def subir_garra():
    """Raise the claw"""
    claw.run_angle(200, -160, then=Stop.HOLD, wait=True)

def bajar_garra():
    """Lower the claw"""
    claw.run_angle(200, 245, then=Stop.HOLD, wait=True)

def rotar_garra():
    """Rotate the claw"""
    global devolver 
    rotar.run_angle(600, 230, then=Stop.HOLD, wait=True)
    devolver = devolver + 1 
    
def devolver_garra():
    """Reset claw rotation"""
    rotar.reset_angle(0)

def escotilla_movible():
    """Handle movible hatch sequence"""
    avance1()
    right_motor.run_angle(800, 480, then=Stop.BRAKE, wait=True)
    left_motor.run_angle(800, 445, then=Stop.BRAKE, wait=True)
    avance2()
    
def escotilla_fija():
    """Handle fixed hatch sequence"""
    right_motor.run_angle(800, 570, then=Stop.BRAKE, wait=True)
    right_motor.run_angle(400, 135, then=Stop.BRAKE, wait=False)
    left_motor.run_angle(400, 135, then=Stop.BRAKE, wait=True)
    bajar_garra()
    right_motor.run_angle(400, -170, then=Stop.BRAKE, wait=False)
    left_motor.run_angle(400, -170, then=Stop.BRAKE, wait=True)

# State machine functions
def state_init():
    """Initialize the robot and prepare for mission"""
    global current_state
    ev3.speaker.say("Initializing Artemisa")
    current_state = STATE_MOVIBLE_HATCH
    return current_state

def state_movible_hatch():
    """Execute movible hatch sequence"""
    global current_state
    ev3.speaker.say("Executing movible hatch")
    escotilla_movible()
    current_state = STATE_FIXED_HATCH
    return current_state

def state_fixed_hatch():
    """Execute fixed hatch sequence"""
    global current_state
    ev3.speaker.say("Executing fixed hatch")
    escotilla_fija()
    current_state = STATE_COMPLETE
    return current_state

def state_complete():
    """Mission complete"""
    global current_state, mission_complete
    ev3.speaker.say("Mission complete")
    mission_complete = True
    return current_state

# State machine dispatcher
def run_state_machine():
    """Main state machine dispatcher"""
    global current_state
    
    if current_state == STATE_INIT:
        return state_init()
    elif current_state == STATE_MOVIBLE_HATCH:
        return state_movible_hatch()
    elif current_state == STATE_FIXED_HATCH:
        return state_fixed_hatch()
    elif current_state == STATE_COMPLETE:
        return state_complete()
    else:
        # Handle unknown state
        ev3.speaker.say("Unknown state")
        current_state = STATE_INIT
        return current_state

# Main execution loop
while not mission_complete:
    current_state = run_state_machine()
    wait(100)  # Small delay between state transitions

ev3.speaker.say("Artemisa mission finished") 
    
    
    

    
