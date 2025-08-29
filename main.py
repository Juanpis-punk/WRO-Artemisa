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

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=210)


def seguir_linea(DISTANCIA):
    robot.reset()

    while robot.distance() < DISTANCIA:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)

    robot.stop()


def seguir_linea2():
    robot.reset()

    while not line_sensor2.reflection() < 20:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)

    robot.stop()
    wait(200)


def seguir_linea3():
    robot.reset()

    while not 10 < line_sensor2.reflection() and line_sensor.reflection() < 20:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        
    robot.stop()
    wait(200)


""" 
 █████  ██    ██  █████  ███    ██  ██████ ███████ 
██   ██ ██    ██ ██   ██ ████   ██ ██      ██      
███████ ██    ██ ███████ ██ ██  ██ ██      █████   
██   ██  ██  ██  ██   ██ ██  ██ ██ ██      ██      
██   ██   ████   ██   ██ ██   ████  ██████ ███████ 
                                                   
                                                   """


def avance(velocidad, grados):
    right_motor.run_angle(velocidad, grados, then=Stop.BRAKE, wait=False)
    left_motor.run_angle(velocidad, grados, then=Stop.BRAKE, wait=True)

    """ 
 ██████   █████  ██████  ██████   █████  
██       ██   ██ ██   ██ ██   ██ ██   ██ 
██   ███ ███████ ██████  ██████  ███████ 
██    ██ ██   ██ ██   ██ ██   ██ ██   ██ 
 ██████  ██   ██ ██   ██ ██   ██ ██   ██ 
                                         
                                         """


def rotar_garra(TIMES):
    rotar.run_angle(600, TIMES*-150, then=Stop.HOLD, wait=True)


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
    avance(800, 850)  # AVANZA HACIA AADELANTE LUEGO DE LEER COLOR4
    # GIRO 90 GRADOS PARA QUEDAR ADYACENTE A LA ESCOTILLA
    right_motor.run_angle(800, 320, then=Stop.BRAKE, wait=False)
    # GIRO 90 GRADOS PARA QUEDAR ADYACENTE A LA ESCOTILLA
    left_motor.run_angle(800, -260, then=Stop.BRAKE, wait=True)
    avance(800, 350)  # AVANCE EN X
    # GIRO PAR AQUDAR DE FRENTE A LA ESCOTILLA
    right_motor.run_angle(800, 320, then=Stop.BRAKE, wait=False)
    # GIRO PAR AQUDAR DE FRENTE A LA ESCOTILLA
    left_motor.run_angle(800, -260, then=Stop.BRAKE, wait=True)
    bajar_garra(1200)
    avance(800, -280)  # SACAR ESCOTILLA
    subir_garra(-1200)
    avance(800, -380)  # RETROCEDER HACIA LA LINEA
    # GIRO PARA QUEDAR EN LA DIRECCION DE LA LÍNEA
    left_motor.run_angle(800, -600, then=Stop.BRAKE, wait=True)
    seguir_linea2()
    wait(500)
    seguir_linea(700)
    robot.stop()



"""
██          ██████  ██████  ██       ██████  ██████  ███████ ███████ 
██         ██      ██    ██ ██      ██    ██ ██   ██ ██      ██      
██         ██      ██    ██ ██      ██    ██ ██████  █████   ███████ 
██         ██      ██    ██ ██      ██    ██ ██   ██ ██           ██ 
███████ ██  ██████  ██████  ███████  ██████  ██   ██ ███████ ███████ 
                                                                     
                                                                     """
# Colores
colorx = None
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


def ir_color1():
    global color1
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
        ev3.speaker.beep()


def ir_color2():
    global color2
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
        ev3.speaker.beep()


def ir_color3():
    global color3
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
        ev3.speaker.beep()


def ir_color4():
    global color4
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
        ev3.speaker.beep()


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
        rotar_garra(1)
    elif colorx == Color.YELLOW:
        rotar_garra(2)
    elif colorx == Color.GREEN:
        rotar_garra(-1)

    """
    
    
░████████                                ░██                                           
░██    ░██                               ░██                                           
░██    ░██   ░██████   ░████████   ░████████  ░███████  ░██░████  ░██████    ░███████  
░████████         ░██  ░██    ░██ ░██    ░██ ░██    ░██ ░███           ░██  ░██        
░██     ░██  ░███████  ░██    ░██ ░██    ░██ ░█████████ ░██       ░███████   ░███████  
░██     ░██ ░██   ░██  ░██    ░██ ░██   ░███ ░██        ░██      ░██   ░██         ░██ 
░█████████   ░█████░██ ░██    ░██  ░█████░██  ░███████  ░██       ░█████░██  ░███████  
                                                                                       
                                                                                       
                                                                                        """


def banderas():
    avance(800, -550)
    right_motor.run_angle(800, 580, then=Stop.BRAKE, wait=True)
    avance(800, -50)
    bajar_garra(1250)
    subir_garra(1250)
    right_motor.run_angle(800, -580, then=Stop.BRAKE, wait=True)
    avance(800, 20)
    right_motor.run_angle(800, 580, then=Stop.BRAKE, wait=True)
    avance(800, 50)
    bajar_garra(900)
    avance(800, -50)
    subir_garra(900)
    right_motor.run_angle(800, 580, then=Stop.BRAKE, wait=True)
    avance(800)
    left_motor.run_angle(800, 580, then=Stop.BRAKE, wait=True)
    bajar_garra(1300)


"""
███████      ██ ███████  ██████ ██    ██  ██████ ██  ██████  ███    ██ 
██           ██ ██      ██      ██    ██ ██      ██ ██    ██ ████   ██ 
█████        ██ █████   ██      ██    ██ ██      ██ ██    ██ ██ ██  ██ 
██      ██   ██ ██      ██      ██    ██ ██      ██ ██    ██ ██  ██ ██ 
███████  █████  ███████  ██████  ██████   ██████ ██  ██████  ██   ████ 
                                                                       
                                                                       """


seguir_linea(600)
seguir_linea2()
avance(800, -260)
wait(200)
right_motor.run_angle(800, -320, then=Stop.BRAKE,
                      wait=False)  # GIRO HACIA COLORX
left_motor.run_angle(800, 260, then=Stop.BRAKE, wait=True)  # GIRO HACIA COLORX
wait(1000)
avance(800, -670)  # AVANCE HACIA COLORX

ir_colorx()  # LEER COLORX (MUESTRAS PARA LA CARGA ÚTIL)

avance(800, -25)  # AVANCE PARA EVITAR CHOQUE CON LA ESCOTILLA AMARILLA
right_motor.run_angle(800, -300, then=Stop.BRAKE, wait=True)  # GIRO HACIA COLOR1
left_motor.run_angle(800, -300, then=Stop.BRAKE, wait=True)  # GIRO HACIA COLOR1
avance(800, -409)  # AVANCE HACIA COLOR1

ir_color1()  # LEER COLOR1

avance(800, -140)  # DEZPLAZAMIENTO CORTO HACIA COLOR2

ir_color2()  # LEER COLOR2

avance(800, 483)  # AVANCE HACIA ADELANTE ANTES DE LA DIAGONAL

left_motor.run_angle(800, 277, then=Stop.BRAKE, wait=True)# PRIMER ANGULO PARA LA DIAGONAL
avance(800, -445)  # DIAGONAL
left_motor.run_angle(800, -277, then=Stop.BRAKE, wait=True)# ACOMODAMIENTO LUEGO DE LA DIAGONAL
# avance(800, -40)

ir_color3()  # LEER COLOR3

avance(800, -175)  # DEZPLAZAMIENTO CORTO PARA IR A COLOR4

ir_color4()  # LEER COLOR4

escotilla_fija()


left_motor.run_angle(800, 600, then=Stop.BRAKE, wait=True)
wait(200)
avance(800, -150)
bajar_garra(1250)
avance(800, 800)
right_motor.run_angle(800, -260, then=Stop.BRAKE, wait=False)
left_motor.run_angle(800, 260, then=Stop.BRAKE, wait=True)
avance(800, 1250)

color_rotor()
subir_garra(-1250)

#banderas()

