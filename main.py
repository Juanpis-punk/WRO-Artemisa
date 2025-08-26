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


#Motores 
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
claw = Motor(Port.A)
rotar = Motor (Port.D)

#Sensores
line_sensor = ColorSensor(Port.S1)
line_sensor2 = ColorSensor(Port.S4)
colorsensor_left = ColorSensor(Port.S3)
colorsensor_right = ColorSensor(Port.S2)

 #Funciones de avance
def avance1():
    right_motor.run_angle(500,950,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(500, 950, then=Stop.BRAKE, wait=True)
    
def avance2():
    right_motor.run_angle(500,800,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(500,800,then=Stop.BRAKE, wait=True)
    
def avance3():
    right_motor.run_angle(500,800,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(500,800,then=Stop.BRAKE, wait=True)
    
def avance4():
    right_motor.run_angle(500,1100,then=Stop.BRAKE, wait=False)
    left_motor.run_angle(500,1100,then=Stop.BRAKE, wait=True)
    
#Funciones de garra

def rotar_garra():
    rotar.run_angle(600, -150, then=Stop.HOLD, wait=True)
    
def subir_garra():    
    claw.run_angle(200, -190, then=Stop.BRAKE, wait=True)

def bajar_garra():
    claw.run_angle(600, 240, then=Stop.HOLD, wait=True)
    
    
#Funciones principales

def giro_carga():
    left_motor.run_angle(600, -267, then=Stop.BRAKE, wait=True)
    right_motor.run_angle(600, 300, then=Stop.BRAKE, wait=False)
    
def giro_carga2():
    left_motor.run_angle(600, 267, then=Stop.BRAKE, wait=False)
    right_motor.run_angle(600, -320, then=Stop.BRAKE, wait=True)
    
   
#Ejecucion
giro_carga()
bajar_garra()
#while line_sensor.reflection() < 50 and line_sensor2.reflection() < 50:
 #   right_motor.run_angle(400, -260, then=Stop.BRAKE, wait=False)
  #  left_motor.run(400)
   # right_motor.run(400)
    #break
avance3()
giro_carga2()
avance4()
subir_garra()



    
    
    


    

        
    
        



     
   
    
    
    
    
 