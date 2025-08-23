from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFil

claw = Motor(Port.A)

# Abrir la garra (mover -90 grados)
claw.run_angle(200, -90, then=Stop.HOLD, wait=True)

# Cerrar la garra (mover +90 grados)
claw.run_angle(200, 90, then=Stop.HOLD, wait=True)