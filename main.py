#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
                                         
                                                           
#Objetos
ev3 = EV3Brick()

"""
███    ███  ██████  ████████  ██████  ██████  ███████ ███████ 
████  ████ ██    ██    ██    ██    ██ ██   ██ ██      ██      
██ ████ ██ ██    ██    ██    ██    ██ ██████  █████   ███████ 
██  ██  ██ ██    ██    ██    ██    ██ ██   ██ ██           ██ 
██      ██  ██████     ██     ██████  ██   ██ ███████ ███████ 
                                                    """
                                                
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
claw = Motor(Port.A)
rotar = Motor (Port.D)

"""
███████ ███████ ███    ██ ███████  ██████  ██████  ███████ ███████ 
██      ██      ████   ██ ██      ██    ██ ██   ██ ██      ██      
███████ █████   ██ ██  ██ ███████ ██    ██ ██████  █████   ███████ 
     ██ ██      ██  ██ ██      ██ ██    ██ ██   ██ ██           ██ 
███████ ███████ ██   ████ ███████  ██████  ██   ██ ███████ ███████ 
                                                                   
                                                        """
line_sensor = ColorSensor(Port.S1)
line_sensor2 = ColorSensor(Port.S4)
colorsensor_left = ColorSensor(Port.S3)
colorsensor_right = ColorSensor(Port.S2)

"""
███████         ██      ██ ███    ██ ███████  █████  
██              ██      ██ ████   ██ ██      ██   ██ 
███████  ████   ██      ██ ██ ██  ██ █████   ███████ 
     ██         ██      ██ ██  ██ ██ ██      ██   ██ 
███████         ███████ ██ ██   ████ ███████ ██   ██ 

"""
DRIVE_SPEED = 200
PROPORTIONAL_GAIN = 0.5
DISTANCIA = None

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=150)

def seguir_linea(DISTANCIA):
    robot.reset()
    
    while robot.distance() < DISTANCIA:
        deviation = line_sensor.reflection() - line_sensor2.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        
    robot.stop()

""" 
 █████  ██    ██  █████  ███    ██  ██████ ███████ 
██   ██ ██    ██ ██   ██ ████   ██ ██      ██      
███████ ██    ██ ███████ ██ ██  ██ ██      █████   
██   ██  ██  ██  ██   ██ ██  ██ ██ ██      ██      
██   ██   ████   ██   ██ ██   ████  ██████ ███████ 
                                                   
                                                   """
def avance(velocidad, grados):
    right_motor.run_angle(velocidad,grados,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(velocidad,grados,then=Stop.BRAKE, wait=True)
    
    """ 
 ██████   █████  ██████  ██████   █████  
██       ██   ██ ██   ██ ██   ██ ██   ██ 
██   ███ ███████ ██████  ██████  ███████ 
██    ██ ██   ██ ██   ██ ██   ██ ██   ██ 
 ██████  ██   ██ ██   ██ ██   ██ ██   ██ 
                                         
                                         """
def rotar_garra():
    rotar.run_angle(600, -150, then=Stop.HOLD, wait=True)
    
def subir_garra():    
    claw.run_angle(600, -1000, then=Stop.BRAKE, wait=True)

def bajar_garra():
    claw.run_angle(600, 1250, then=Stop.HOLD, wait=True)
    

"""
██          ██████  ██████  ██       ██████  ██████  ███████ ███████ 
██         ██      ██    ██ ██      ██    ██ ██   ██ ██      ██      
██         ██      ██    ██ ██      ██    ██ ██████  █████   ███████ 
██         ██      ██    ██ ██      ██    ██ ██   ██ ██           ██ 
███████ ██  ██████  ██████  ███████  ██████  ██   ██ ███████ ███████ 
                                                                     
                                                                     """
#Colores
color1 = None
color2 = None
color3 = None 
color4 = None
valid_colors = [ Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]


def Colorcapture():
    avance(800, 1000)
    right_motor.run_angle(800, -160, then=Stop.BRAKE, wait=True)
    left_motor.run_angle(800, 160, then=Stop.BRAKE, wait=True)
    avance(800, -800)
    wait(500)
    
    detected_color = colorsensor_right.color()
    
    if detected_color in valid_colors:
        color1 = detected_color
        if color1 != None:
            avance1()
            right_motor.run_angle(800, 465, then=Stop.BRAKE, wait=True)
            left_motor.run_angle(800, 465, then=Stop.BRAKE, wait=True)
            avance2()
        
    else:
        claw.run_angle(180, 245, then=Stop.BRAKE, wait=True)
        
    

    """
███████      ██ ███████  ██████ ██    ██  ██████ ██  ██████  ███    ██ 
██           ██ ██      ██      ██    ██ ██      ██ ██    ██ ████   ██ 
█████        ██ █████   ██      ██    ██ ██      ██ ██    ██ ██ ██  ██ 
██      ██   ██ ██      ██      ██    ██ ██      ██ ██    ██ ██  ██ ██ 
███████  █████  ███████  ██████  ██████   ██████ ██  ██████  ██   ████ 
                                                                       
                                                                       """
             
seguir_linea(1000)                                                         


    
    
    


    
    
    
     
   
    
    
    
    
 