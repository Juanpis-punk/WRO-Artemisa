from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

left_motor = Motor(Port.C)
right_motor = Motor(Port.B)

left_motor.run_angle(200, 360, then=Stop.BRAKE, wait=False)
right_motor.run_angle(200, 360, then=Stop.BRAKE, wait=True