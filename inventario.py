from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

 #AVANCES
def avance1():
    right_motor.run_angle(500,950,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(500, 950, then=Stop.BRAKE, wait=True)
    
def avance2():
    right_motor.run_angle(500,800,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(500,800,then=Stop.BRAKE, wait=True)
    
def avance3():
    right_motor.run_angle(500,600,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(500,600,then=Stop.BRAKE, wait=True)
    
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

#SEGUIMIENTO DE LINEA#
DRIVE_SPEED = 200
PROPORTIONAL_GAIN = 0.8
devolver=0

def seguir_linea():
    deviation = line_sensor.reflection() - line_sensor2.reflection()
    turn_rate = PROPORTIONAL_GAIN * deviation
    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)
    
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

#MOVIMIENTOS DE GARRA#

def subir_garra():    
    claw.run_angle(200, -190, then=Stop.BRAKE, wait=True)

def bajar_garra():
    claw.run_angle(180, 245, then=Stop.BRAKE, wait=True)

def rotar_garra():
    global devolver 
    rotar.run_angle(600, 230, then=Stop.HOLD, wait=True)
    devolver = devolver+1 
    
def devolver_garra():
    # rotar.run_angle(200, -(134*devolver), then=Stop.HOLD, wait=True)
    rotar.reset_angle(0)
    
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

#ESCOTILLA FIJA#

def escotilla_fija():
        right_motor.run_angle(800, 550, then=Stop.BRAKE, wait=True)
        right_motor.run_angle(400,160,then=Stop.BRAKE, wait=False)
        left_motor.run_angle(400,160,then=Stop.BRAKE, wait=True)
        bajar_garra()
        right_motor.run_angle(400,-170,then=Stop.BRAKE, wait=False)
        left_motor.run_angle(400,-170,then=Stop.BRAKE, wait=True)
        subir_garra()
    
    
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
    
#LECTURA DE COLORES
#Colores
color1 = None
color2 = None
color3 = None 
color4 = None
valid_colors = [ Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
    
    
def escotilla_movible():

    right_motor.run_angle(800, 260, then=Stop.BRAKE, wait=True)
    left_motor.run_angle(800, 260, then=Stop.BRAKE, wait=True)
    right_motor.run_angle(800, -100, then=Stop.BRAKE, wait=True)
    left_motor.run_angle(800, -100, then=Stop.BRAKE, wait=True)
    wait(500)
    
    detected_color = colorsensor_left.color()
    
    if detected_color in valid_colors:
        color1 = detected_color
        if color1 != None:
            avance1()
            right_motor.run_angle(800, 465, then=Stop.BRAKE, wait=True)
            left_motor.run_angle(800, 465, then=Stop.BRAKE, wait=True)
            avance2()
        
    else:
        claw.run_angle(180, 245, then=Stop.BRAKE, wait=True)
                
                    
escotilla_movible()

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

#GIROCARGA#

def giro_carga():
    left_motor.run_angle(600, -267, then=Stop.BRAKE, wait=True)
    right_motor.run_angle(600, 300, then=Stop.BRAKE, wait=False)
    
    #Ejecucion de la GiroCarga
giro_carga()
bajar_garra()
#while line_sensor.reflection() < 50 and line_sensor2.reflection() < 50:
 #   right_motor.run_angle(400, -260, then=Stop.BRAKE, wait=False)
  #  left_motor.run(400)
   # right_motor.run(400)
    #break
avance3()
left_motor.run_angle(600, 267, then=Stop.BRAKE, wait=False)
right_motor.run_angle(600, -310, then=Stop.BRAKE, wait=True)

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

#Seguimiento de Líneas de los chavales
def seguir_linea():
    deviation = line_sensor.reflection() - line_sensor2.reflection()
    turn_rate = PROPORTIONAL_GAIN * deviation
    right_motor.run_angle(DRIVE_SPEED, turn_rate wait=False)
    left_motor.run_angle(DRIVE_SPEED, turn_rate wait=True)
    cont=+1
    return cont
    
    
if(seguir_linea()>=2S):
    right_motor.break()
    left_motor.break()
