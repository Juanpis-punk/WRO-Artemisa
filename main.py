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
ev3.speaker.set_volume(100)

                                                                                                            
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
DRIVE_SPEED = 300
PROPORTIONAL_GAIN = 0.5
DISTANCIA = None

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=210)

def seguir_linea(DISTANCIA):
    robot.reset()
    
    while robot.distance() < DISTANCIA:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
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
def rotar_garra(TIMES):
    rotar.run_angle(600, TIMES*(-150), then=Stop.HOLD, wait=True)
    
def subir_garra(GRADO):    
    claw.run_angle(600, GRADO, then=Stop.BRAKE, wait=True)

def bajar_garra(GRADO):
    claw.run_angle(600, GRADO, then=Stop.BRAKE, wait=True)
    
"""
███████ ███████  ██████    ███████ ██      ██  █████  
██      ██      ██         ██      ██      ██ ██   ██ 
█████   ███████ ██         █████   ██      ██ ███████ 
██           ██ ██         ██      ██ ██   ██ ██   ██ 
███████ ███████  ██████ ██ ██      ██  █████  ██   ██ 
                                                      
"""
    
def escotilla_fija():
    avance(800, 850)
    right_motor.run_angle(800,320,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(800,-260,then=Stop.BRAKE, wait=True)
    avance(800, 350)
    right_motor.run_angle(800,320,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(800,-260,then=Stop.BRAKE, wait=True)
    bajar_garra(1200)
    avance(800, -280)
    subir_garra(-1200)
    avance(800, -400)
    right_motor.run_angle(800,320,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(800,-260,then=Stop.BRAKE, wait=True)
    seguir_linea(1300)
    robot.stop()

"""
██          ██████  ██████  ██       ██████  ██████  ███████ ███████ 
██         ██      ██    ██ ██      ██    ██ ██   ██ ██      ██      
██         ██      ██    ██ ██      ██    ██ ██████  █████   ███████ 
██         ██      ██    ██ ██      ██    ██ ██   ██ ██           ██ 
███████ ██  ██████  ██████  ███████  ██████  ██   ██ ███████ ███████ 
                                                                     
                                                                     """
#Colores
colorx = None
color1 = None
color2 = None 
color3 = None
color4 = None
valid_colors = [ Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]

def ir_colorx():
    if colorsensor_right.color() in valid_colors:
        wait(500)
        colorx = colorsensor_right.color()
        
        if colorx == Color.RED: 
            ev3.speaker.say("Red")
        if colorx == Color.BLUE: 
            ev3.speaker.say("Blue")
        if colorx == Color.GREEN: 
            ev3.speaker.say("Green")
        if colorx == Color.YELLOW: 
            ev3.speaker.say("Yellow")
        
    else:
        rotar_garra(1)
        
def ir_color1():
    if colorsensor_right.color() in valid_colors:
        wait(500)
        color1 = colorsensor_right.color()
        
        if color1 == Color.RED: 
            ev3.speaker.say("Red")
        if color1 == Color.BLUE: 
            ev3.speaker.say("Blue")
        if color1 == Color.GREEN: 
            ev3.speaker.say("Green")
        if color1 == Color.YELLOW: 
            ev3.speaker.say("Yellow") 
    else:
        rotar_garra(1)
    
def ir_color2():
    if colorsensor_right.color() in valid_colors and colorsensor_right.color() != color1:
        wait(500)
        color2 = colorsensor_right.color()
        
        if color2 == Color.RED: 
            ev3.speaker.say("Red")
        if color2 == Color.BLUE: 
            ev3.speaker.say("Blue")
        if color2 == Color.GREEN: 
            ev3.speaker.say("Green")
        if color2 == Color.YELLOW: 
            ev3.speaker.say("Yellow")
    else:
        rotar_garra(1)
        
        
def ir_color3():
    if colorsensor_left.color() in valid_colors and colorsensor_left.color() != (color1, color2):
        wait(500)
        color3 = colorsensor_left.color()
        
        if color3 == Color.RED: 
            ev3.speaker.say("Red")
        if color3 == Color.BLUE: 
            ev3.speaker.say("Blue")
        if color3 == Color.GREEN: 
            ev3.speaker.say("Green")
        if color3 == Color.YELLOW: 
            ev3.speaker.say("Yellow")
    else:
        rotar_garra(1)
        
def ir_color4():
    if colorsensor_left.color() in valid_colors and colorsensor_left.color() != (color1, color2, color3):
        wait(500)
        color4 = colorsensor_left.color()
        
        if color4 == Color.RED: 
            ev3.speaker.say("Red")
        if color4 == Color.BLUE: 
            ev3.speaker.say("Blue")
        if color4 == Color.GREEN: 
            ev3.speaker.say("Green")
        if color4 == Color.YELLOW: 
            ev3.speaker.say("Yellow")
    else:
        rotar_garra(1)
        
        
        
"""

██████   ██████  ████████  ██████  ██████      ██████  ███████      ██████  ██████  ██       ██████  ██████  ███████ ███████ 
██   ██ ██    ██    ██    ██    ██ ██   ██     ██   ██ ██          ██      ██    ██ ██      ██    ██ ██   ██ ██      ██      
██████  ██    ██    ██    ██    ██ ██████      ██   ██ █████       ██      ██    ██ ██      ██    ██ ██████  █████   ███████ 
██   ██ ██    ██    ██    ██    ██ ██   ██     ██   ██ ██          ██      ██    ██ ██      ██    ██ ██   ██ ██           ██ 
██   ██  ██████     ██     ██████  ██   ██     ██████  ███████      ██████  ██████  ███████  ██████  ██   ██ ███████ ███████ 
                                                                                                                             
                                                                                                                             
"""
def color_rotor():
    if colorx == Color.BLUE:
        rotar_garra(0)
    if colorx == Color.RED:
        rotar_garra(1)
    if colorx == Color.YELLOW:
        rotar_garra(2)
    if colorx == Color.GREEN:
        rotar_garra(-1)
        
   
   
    

    """
███████      ██ ███████  ██████ ██    ██  ██████ ██  ██████  ███    ██ 
██           ██ ██      ██      ██    ██ ██      ██ ██    ██ ████   ██ 
█████        ██ █████   ██      ██    ██ ██      ██ ██    ██ ██ ██  ██ 
██      ██   ██ ██      ██      ██    ██ ██      ██ ██    ██ ██  ██ ██ 
███████  █████  ███████  ██████  ██████   ██████ ██  ██████  ██   ████ 
                                                                       
                                                                       """


seguir_linea(873)
wait(200)
right_motor.run_angle(800, -320, then=Stop.BRAKE, wait=False)
left_motor.run_angle(800, 260, then=Stop.BRAKE, wait=True)
wait(1000)
avance(800, -566)

ir_colorx()

avance(800, -25)
right_motor.run_angle(800, -300, then=Stop.BRAKE, wait=True)
left_motor.run_angle(800, -300, then=Stop.BRAKE, wait=True)
avance(800, -416)

ir_color1()

avance(800, -150)

ir_color2()

avance(800, 483)
left_motor.run_angle(800, 272, then=Stop.BRAKE, wait=True)
avance(800, -405)
left_motor.run_angle(800, -272, then=Stop.BRAKE, wait=True)
#avance(800, -20)

ir_color3()

avance(800, -175)

ir_color4()

escotilla_fija()

right_motor.run_angle(800, -390, then=Stop.BRAKE, wait=False)
left_motor.run_angle(800, 456, then=Stop.BRAKE, wait=True)
avance(800, 400)

bajar_garra(1250)
"""
avance(800, 500)

right_motor.run_angle(800, -390, then=Stop.BRAKE, wait=False)
left_motor.run_angle(800, 465, then=Stop.BRAKE, wait=True)

avance(800, 600)

color_rotor()

subir_garra(1250)
    """


