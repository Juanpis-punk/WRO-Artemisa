#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Objetos
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
rotar = Motor(Port.D)

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
PROPORTIONAL_GAIN = 0.6
DISTANCIA = None

robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=185)


def seguir_linea(DISTANCIA):
    robot.reset()

    while robot.distance() < DISTANCIA:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)

    robot.stop()
    wait(500)


def seguir_linea2():
    robot.reset()

    while not line_sensor2.reflection() < 21.5:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)

    robot.stop(Stop.HOLD)
    wait(200)
    
def seguir_linea2_5():
    robot.reset()

    while not line_sensor.reflection() < 20:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)

    robot.stop(Stop.HOLD)
    wait(200)


def seguir_linea3():
    robot.reset()

    while not 30 < line_sensor2.reflection() < 40:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        
    robot.stop(Stop.HOLD)
    wait(200)
    
    
def seguir_linea4():
    robot.reset()

    while not 20 < line_sensor2.reflection() < 35 and 20 < line_sensor2.reflection() < 35:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        
    robot.stop(Stop.HOLD)
    wait(200)
    
"""    
def seguir_linea4()
    while not line_sensor.reflection() < 20 and line_sensor2.reflection() < 20:
        robot.straight()
robot.stop(Stop.HOLD)"""



""" 
 █████  ██    ██  █████  ███    ██  ██████ ███████ 
██   ██ ██    ██ ██   ██ ████   ██ ██      ██      
███████ ██    ██ ███████ ██ ██  ██ ██      █████   
██   ██  ██  ██  ██   ██ ██  ██ ██ ██      ██      
██   ██   ████   ██   ██ ██   ████  ██████ ███████ 
                                                   
                                                   """


def avance(velocidad, grados):
    right_motor.run_angle(velocidad, grados, then=Stop.HOLD, wait=False)
    left_motor.run_angle(velocidad, grados, then=Stop.HOLD, wait=True)

    """ 
 ██████   █████  ██████  ██████   █████  
██       ██   ██ ██   ██ ██   ██ ██   ██ 
██   ███ ███████ ██████  ██████  ███████ 
██    ██ ██   ██ ██   ██ ██   ██ ██   ██ 
 ██████  ██   ██ ██   ██ ██   ██ ██   ██ 
                                         
                                         """


def rotar_garra(TIMES):
    rotar.run_angle(300, TIMES*-150, then=Stop.HOLD, wait=True)


def subir_garra(GRADO):
    claw.run_angle(250, GRADO, then=Stop.HOLD, wait=True)


def bajar_garra(GRADO):
    claw.run_angle(250, GRADO, then=Stop.HOLD, wait=True)


    



"""
██          ██████  ██████  ██       ██████  ██████  ███████ ███████ 
██         ██      ██    ██ ██      ██    ██ ██   ██ ██      ██      
██         ██      ██    ██ ██      ██    ██ ██████  █████   ███████ 
██         ██      ██    ██ ██      ██    ██ ██   ██ ██           ██ 
███████ ██  ██████  ██████  ███████  ██████  ██   ██ ███████ ███████ 
                                                                     
                                                                     """
# Colores

colorx = Color.GREEN
color1 = None
color2 = None
color3 = None
color4 = None
valid_colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]


def ir_colorx():
    global colorx
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
        ev3.speaker.beep()


        
  
"""
███████ ███████  ██████    ███████ ██      ██  █████  
██      ██      ██         ██      ██      ██ ██   ██ 
█████   ███████ ██         █████   ██      ██ ███████ 
██           ██ ██         ██      ██ ██   ██ ██   ██ 
███████ ███████  ██████ ██ ██      ██  █████  ██   ██ 
                                                      
"""
def escotilla_fija():
    avance(800, 400)
    left_motor.run_angle(800,-260, then=Stop.BRAKE, wait=False)
    right_motor.run_angle(800,260, then=Stop.BRAKE, wait=True)
    avance(800,630)
    right_motor.run_angle(800,580, then=Stop.BRAKE, wait=True)
    avance(800,360)
    bajar_garra(410)
    avance(800,-300)
    subir_garra(-415)      

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
    elif colorx == Color.RED:
        rotar_garra(-1)
    elif colorx == Color.YELLOW:
        rotar_garra(2)
    elif colorx == Color.GREEN:
        rotar_garra(1)

    """
    
    
░████████                                ░██                                           
░██    ░██                               ░██                                           
░██    ░██   ░██████   ░████████   ░████████  ░███████  ░██░████  ░██████    ░███████  
░████████         ░██  ░██    ░██ ░██    ░██ ░██    ░██ ░███           ░██  ░██        
░██     ░██  ░███████  ░██    ░██ ░██    ░██ ░█████████ ░██       ░███████   ░███████  
░██     ░██ ░██   ░██  ░██    ░██ ░██   ░███ ░██        ░██      ░██   ░██         ░██ 
░█████████   ░█████░██ ░██    ░██  ░█████░██  ░███████  ░██       ░█████░██  ░███████  
                                                                                       
                                                                                       
                                                                                        """

def bandera():
    avance(800,-820)
    right_motor.run_angle(600,580, then=Stop.HOLD, wait=True)
    avance(800,-116.5)
    bajar_garra(385)
    subir_garra(-385)
    left_motor.run_angle(600,580, then=Stop.HOLD, wait=True)
    right_motor.run_angle(600,580, then=Stop.HOLD , wait=True)
    avance(800,-137)
    bajar_garra(310)
    avance(600,-130)
    subir_garra(-310)
    


"""
███████      ██ ███████  ██████ ██    ██  ██████ ██  ██████  ███    ██ 
██           ██ ██      ██      ██    ██ ██      ██ ██    ██ ████   ██ 
█████        ██ █████   ██      ██    ██ ██      ██ ██    ██ ██ ██  ██ 
██      ██   ██ ██      ██      ██    ██ ██      ██ ██    ██ ██  ██ ██ 
███████  █████  ███████  ██████  ██████   ██████ ██  ██████  ██   ████ 
                                                                       
                                                                       """
def artemisa():
    seguir_linea(600)
    seguir_linea2()
    wait(100)
    robot.stop()
    avance(800, -157)
    wait(200)
    right_motor.run_angle(800, -315, then=Stop.BRAKE,wait=False)  # GIRO HACIA COLORX
    left_motor.run_angle(800, 265, then=Stop.BRAKE, wait=True)  # GIRO HACIA COLORX
    wait(500)
    avance(800, -656.5)  # REVERSA HACIA COLORX

    ir_colorx()  # LEER COLORX (MUESTRAS PARA LA CARGA ÚTIL)

    escotilla_fija()

    avance(800, -510)# RETROCEDER HACIA LA LINEA 
    robot.turn(-92) #Giro para quedar al sentido de la linea
    robot.stop()
    wait(500)


    seguir_linea(830)
    seguir_linea3() #Parar en la franja azul
    robot.straight(205) #acomodarse en el cuadrito de inicio
    robot.stop()
    right_motor.run_angle(800, -320, then=Stop.BRAKE,wait=False)  # GIRO HACIA COLORX
    left_motor.run_angle(800, 260, then=Stop.BRAKE, wait=True)  # GIRO HACIA COLORX
    avance(800, 150) #avance para mejor agarre
    bajar_garra(388)
    avance(800, 645) #Avance vertical para ir a dejar la carga
    left_motor.run_angle(800, 585)
    avance(800, 900) #Avance rumbo al punto de carga útil
    color_rotor()       
    subir_garra(-415)
    avance(800, 100)
    

    bandera()
    avance(800, -120)
    right_motor.run_angle(800, 585)
    avance(800, 165)
    seguir_linea2_5()
    robot.stop()
    avance(800, 135)
    robot.turn(88)
    robot.stop()
    avance(800,210)
    bajar_garra(415)
    
while True:
    pressed = ev3.buttons.pressed()
    if Button.DOWN in pressed:
        artemisa()