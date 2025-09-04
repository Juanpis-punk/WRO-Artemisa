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
░███     ░███               ░██                                              
░████   ░████               ░██                                              
░██░██ ░██░██  ░███████  ░████████  ░███████  ░██░████  ░███████   ░███████  
░██ ░████ ░██ ░██    ░██    ░██    ░██    ░██ ░███     ░██    ░██ ░██        
░██  ░██  ░██ ░██    ░██    ░██    ░██    ░██ ░██      ░█████████  ░███████  
░██       ░██ ░██    ░██    ░██    ░██    ░██ ░██      ░██               ░██ 
░██       ░██  ░███████      ░████  ░███████  ░██       ░███████   ░███████  
                                                                             
                                                                             
                                                                             
"""

right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
claw = Motor(Port.A)
rotar = Motor(Port.D)

"""
  ░██████                                                                              
 ░██   ░██                                                                             
░██          ░███████  ░████████   ░███████   ░███████  ░██░████  ░███████   ░███████  
 ░████████  ░██    ░██ ░██    ░██ ░██        ░██    ░██ ░███     ░██    ░██ ░██        
        ░██ ░█████████ ░██    ░██  ░███████  ░██    ░██ ░██      ░█████████  ░███████  
 ░██   ░██  ░██        ░██    ░██        ░██ ░██    ░██ ░██      ░██               ░██ 
  ░██████    ░███████  ░██    ░██  ░███████   ░███████  ░██       ░███████   ░███████  
                                                                                       
                                                                                       
                                                                                       
"""
line_sensor = ColorSensor(Port.S1) #Derecho
line_sensor2 = ColorSensor(Port.S4)
colorsensor_left = ColorSensor(Port.S3)
colorsensor_right = ColorSensor(Port.S2)

"""
  ░██████       ░██ ░██                                 
 ░██   ░██      ░██                                     
░██             ░██ ░██░████████   ░███████   ░██████   
 ░████████      ░██ ░██░██    ░██ ░██    ░██       ░██  
        ░██     ░██ ░██░██    ░██ ░█████████  ░███████  
 ░██   ░██      ░██ ░██░██    ░██ ░██        ░██   ░██  
  ░██████   ░██ ░██ ░██░██    ░██  ░███████   ░█████░██ 
                                                        
                                                        
                                                    
"""
DRIVE_SPEED = 300
PROPORTIONAL_GAIN = 0.6
DISTANCIA = None

robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=185)
robot.settings(straight_speed=250)


def seguir_linea(DISTANCIA):
    robot.reset()
    #La de toda la vida
    while robot.distance() < DISTANCIA:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)

    robot.stop()
    wait(500)


def seguir_linea2():
    robot.reset()
    #para parar cuando hay una transversal
    while not line_sensor2.reflection() < 21.5:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)

    robot.stop(Stop.HOLD)
    wait(200)
    
def seguir_linea2_5():
    robot.reset()
    #para parar con una transversal pero con el sensor dereho
    while not line_sensor.reflection() < 21.5:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)

    robot.stop(Stop.HOLD)
    wait(200)


def seguir_linea3():
    robot.reset()
    #para parar con la franja azul
    while not 30 < line_sensor2.reflection() < 40:
        deviation = line_sensor2.reflection() - line_sensor.reflection()
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        
    robot.stop(Stop.HOLD)
    wait(200)
    
    
def seguir_linea4():
    robot.reset()
    #seguir hasta ver negro
    while not line_sensor.reflection() < 17:
        left_motor.run(400)   # velocidad en grados por segundo
        right_motor.run(400)
        
    robot.stop(Stop.HOLD)
    wait(200)
    
def seguir_linea_minus_4():
    robot.reset()
    #seguir hasta ver negro pero pa tras
    while not line_sensor.reflection() < 17:
        left_motor.run(-700)   # velocidad en grados por segundo
        right_motor.run(-700)
        
    robot.stop(Stop.BRAKE)
    wait(200)

    
def seguir_linea5():
    robot.reset()
    #seguir hasta ver nblanco pero con sensor derecho
    while not line_sensor2.reflection() > 90:
        left_motor.run(500)   # velocidad en grados por segundo
        right_motor.run(500)
        
    robot.stop(Stop.HOLD)
    wait(200)
    
    
def seguir_linea5_5():
    robot.reset()
    #seguir hasta ver blanco pa tras con el sensor derecho
    while not line_sensor.reflection() > 90:
        left_motor.run(-500)   # velocidad en grados por segundo
        right_motor.run(-500)
        
    robot.stop(Stop.HOLD)
    wait(200)
    
    
def seguir_linea6():
    robot.reset()
    def seguir_linea6():
        robot.reset()
        start_time = None   # Aquí guardaremos el momento en que superamos 90

        while True:
            deviation = line_sensor2.reflection() - line_sensor.reflection()
            turn_rate = PROPORTIONAL_GAIN * deviation
            robot.drive(DRIVE_SPEED, turn_rate)

        
            if line_sensor2.reflection() > 90:
                if start_time is None:
                    start_time = time.time()
                
                elif time.time() - start_time >= 0.8:
                    break
            else:
                start_time = None

        # Detener robot
        robot.stop(Stop.HOLD)
        wait(200)

    

""" 

   ░███                                                           
  ░██░██                                                          
 ░██  ░██  ░██    ░██  ░██████   ░████████   ░███████   ░███████  
░█████████ ░██    ░██       ░██  ░██    ░██ ░██    ░██ ░██    ░██ 
░██    ░██  ░██  ░██   ░███████  ░██    ░██ ░██        ░█████████ 
░██    ░██   ░██░██   ░██   ░██  ░██    ░██ ░██    ░██ ░██        
░██    ░██    ░███     ░█████░██ ░██    ░██  ░███████   ░███████  
                                                                  
                                                                  
                                                                  
"""


def avance(velocidad, grados):
    right_motor.run_angle(velocidad, grados, then=Stop.HOLD, wait=False)
    left_motor.run_angle(velocidad, grados, then=Stop.HOLD, wait=True)

""" 
    ░██████                                          
 ░██   ░██                                         
░██         ░██████   ░██░████ ░██░████  ░██████   
░██  █████       ░██  ░███     ░███           ░██  
░██     ██  ░███████  ░██      ░██       ░███████  
 ░██  ░███ ░██   ░██  ░██      ░██      ░██   ░██  
  ░█████░█  ░█████░██ ░██      ░██       ░█████░██ 
                                                   
                                                   
                                                     
"""


def rotar_garra(TIMES):
    rotar.run_angle(300, TIMES*-150, then=Stop.HOLD, wait=True)
    
def rotar_garra_x(TIMES):
    rotar.run_angle(300, TIMES*-170, then=Stop.HOLD, wait=True)
    


def subir_garra(GRADO):
    claw.run_angle(400, GRADO, then=Stop.HOLD, wait=True)


def bajar_garra(GRADO):
    claw.run_angle(400, GRADO, then=Stop.HOLD, wait=True)

def subir_garra2(GRADO):
    claw.run_angle(160, GRADO, then=Stop.HOLD, wait=True)
    



"""
░██                                   ░██                                           
░██                                   ░██                                           
░██              ░███████   ░███████  ░██  ░███████  ░██░████  ░███████   ░███████  
░██             ░██    ░██ ░██    ░██ ░██ ░██    ░██ ░███     ░██    ░██ ░██        
░██             ░██        ░██    ░██ ░██ ░██    ░██ ░██      ░█████████  ░███████  
░██             ░██    ░██ ░██    ░██ ░██ ░██    ░██ ░██      ░██               ░██ 
░██████████ ░██  ░███████   ░███████  ░██  ░███████  ░██       ░███████   ░███████  
                                                                                    
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
            ev3.speaker.play_notes(
                ["C4/32", "D4/32", "E4/32"], tempo=120)
        if colorx == Color.BLUE:
            ev3.speaker.play_notes(
                ["C4/32", "D4/32", "E4/32"], tempo=120)
        if colorx == Color.GREEN:
            ev3.speaker.play_notes(
                ["C4/32", "D4/32", "E4/32"], tempo=120)
        if colorx == Color.YELLOW:
            ev3.speaker.play_notes(
                ["C4/32", "D4/32", "E4/32"], tempo=120)

    else:
        ev3.speaker.beep()
    


        
  
"""
░██████████                                          ░████ ░██  ░██            
░██                                                 ░██                        
░██          ░███████   ░███████   ░███████      ░████████ ░██  ░██  ░██████   
░█████████  ░██        ░██    ░██ ░██    ░██        ░██    ░██  ░██       ░██  
░██          ░███████  ░██        ░██    ░██        ░██    ░██  ░██  ░███████  
░██                ░██ ░██    ░██ ░██    ░██        ░██    ░██  ░██ ░██   ░██  
░██████████  ░███████   ░███████   ░███████  ░██    ░██    ░██  ░██  ░█████░██ 
                                                                ░██            
                                                              ░███             
                                                                               
"""
def escotilla_fija():
    avance(800, 403) #Avance hacia adelante luego de leer colorx
    left_motor.run_angle(800,-260, then=Stop.BRAKE, wait=False)#GIro a la derecha
    right_motor.run_angle(800,317, then=Stop.BRAKE, wait=True)
    avance(800,630) #Avance en X
    right_motor.run_angle(800,580, then=Stop.BRAKE, wait=True) #Giro
    avance(800,270)#Avance recto hacia escotilla roja
    bajar_garra(390)
    avance(800,-250) #Retroceso para halar
    subir_garra(-390)
    rotar_garra_x(1) #reacomodar garra
     


"""

░███     ░███                                                    
░████   ░████                                                    
░██░██ ░██░██  ░███████  ░██░████ ░██░████  ░███████   ░███████  
░██ ░████ ░██ ░██    ░██ ░███     ░███     ░██    ░██ ░██        
░██  ░██  ░██ ░██    ░██ ░██      ░██      ░██    ░██  ░███████  
░██       ░██ ░██    ░██ ░██      ░██      ░██    ░██        ░██ 
░██       ░██  ░███████  ░██      ░██       ░███████   ░███████  
                                                            
"""
def morros():
    bajar_garra(407)
    avance(400,40)
    wait(200)
    avance(400, -100)
    left_motor.run_angle(400,-580,then=Stop.BRAKE, wait=True)
    avance(800,1190)
    left_motor.run_angle(400,890 ,then=Stop.BRAKE, wait=True)
    avance(800,-70)
    subir_garra(-407)
    avance(600,-200)  
    bajar_garra(406)   
    avance(400, -50)   
    right_motor.run_angle(400,550,then=Stop.BRAKE, wait=True)
    avance(800,-115)  
    subir_garra2(-407)

"""
  ░██████             ░██                        ░█████████                ░██                        
 ░██   ░██            ░██                        ░██     ░██               ░██                        
░██         ░███████  ░██  ░███████  ░██░████    ░██     ░██  ░███████  ░████████  ░███████  ░██░████ 
░██        ░██    ░██ ░██ ░██    ░██ ░███        ░█████████  ░██    ░██    ░██    ░██    ░██ ░███     
░██        ░██    ░██ ░██ ░██    ░██ ░██         ░██   ░██   ░██    ░██    ░██    ░██    ░██ ░██      
 ░██   ░██ ░██    ░██ ░██ ░██    ░██ ░██         ░██    ░██  ░██    ░██    ░██    ░██    ░██ ░██      
  ░██████   ░███████  ░██  ░███████  ░██         ░██     ░██  ░███████      ░████  ░███████  ░██      
                                                                                                      
                                                                                                      
                                                                                                                                                                                                                                                                                                                                                      
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
    avance(800,-740) #Salida de carga útil
    right_motor.run_angle(600,590, then=Stop.HOLD, wait=True) #Giro para quedar de frente a bandera 1
    avance(800,-73)
    bajar_garra(385) #Bajar banderita
    subir_garra(-385)
    left_motor.run_angle(600,580, then=Stop.HOLD, wait=True)#Giro para quedar en X
    right_motor.run_angle(600,580, then=Stop.HOLD , wait=True)#Quedar frente a banderita 2
    avance(800,-85) #Retroceso para precisión
    bajar_garra(310)
    avance(600,-220) # Hala palanquita
    subir_garra(-310)
    


"""
░██████████   ░██                                             ░██                      
░██                                                                                    
░██           ░██  ░███████   ░███████  ░██    ░██  ░███████  ░██ ░███████  ░████████  
░█████████    ░██ ░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██ ░██░██    ░██ ░██    ░██ 
░██           ░██ ░█████████ ░██        ░██    ░██ ░██        ░██░██    ░██ ░██    ░██ 
░██           ░██ ░██        ░██    ░██ ░██   ░███ ░██    ░██ ░██░██    ░██ ░██    ░██ 
░██████████   ░██  ░███████   ░███████   ░█████░██  ░███████  ░██ ░███████  ░██    ░██ 
              ░██                                                                      
            ░███                                                                     """
            
            
 
while True:
    pressed = ev3.buttons.pressed()
    if Button.DOWN in pressed:
        wait(1000)
        seguir_linea(600)
        seguir_linea2()
        wait(100)
        robot.stop()
        avance(800, -150) #Retroceso para ir a colorx
        
        wait(200)
        
        right_motor.run_angle(800, -315, then=Stop.BRAKE,wait=False)  # GIRO HACIA COLORX
        left_motor.run_angle(800, 265, then=Stop.BRAKE, wait=True)  # GIRO HACIA COLORX
        wait(500)
        avance(800, -660)  # REVERSA HACIA COLORX
        left_motor.run_angle(800,-50, then=Stop.BRAKE, wait=True)
        ir_colorx()  # LEER COLORX (MUESTRAS PARA LA CARGA ÚTIL)
        left_motor.run_angle(800,50, then=Stop.BRAKE, wait=True)
        
        escotilla_fija()

        avance(800, -490)# RETROCEDER HACIA LA LINEA 
        robot.turn(-88) #Giro para quedar al sentido de la linea
        robot.stop()
        wait(500)

        seguir_linea(630)
        seguir_linea3() #Parar en la franja azul
        robot.straight(190) #acomodarse en el cuadrito de inicio
        robot.stop()
        #CARGA-UTIL
        right_motor.run_angle(800, -320, then=Stop.BRAKE,wait=False)  #Giro hacia Carga útil
        left_motor.run_angle(800, 260, then=Stop.BRAKE, wait=True)  
        avance(800, 150) #avance para mejor agarre
        
        bajar_garra(395)
        color_rotor() 
        avance(600, 550) #avance para llegar a la línea
        seguir_linea4()#Chocar con la línea
        wait(300)
        robot.turn(90)#Giro para quedar en x
        robot.stop()
        avance(800, -400) #Choque a la pared
        avance(400, 1300) #Ir a dejar carga util
        wait(100)
        subir_garra2(-395)
        wait(200)
        bandera()
        
        seguir_linea_minus_4() #Retroceder a línea
        avance(800, -250)
        robot.stop()
        avance(800, 406) #Verticl a escotilla amarilla
        robot.turn(-85) #Giro a escotilla
        robot.stop()
        avance(800, -300)
        left_motor.run_angle(800, -80, then=Stop.HOLD, wait=True)
        left_motor.run_angle(800, 80, then=Stop.HOLD, wait=True)
        seguir_linea_minus_4() #Chocar con adyacente negra
        robot.stop()
        left_motor.run_angle(800, -580, then=Stop.BRAKE, wait=True) #Giro hacia linea principal
        seguir_linea4() #Chocar con linea principal
        robot.stop()
        avance(800, 115) #Acomodacion para el angulo
        robot.turn(-80) #Angulo para quedar en sentido de linea a morros
        robot.stop()
        seguir_linea2() #CHocar con segunda adyacente
        robot.stop()    
    
        avance(800, 400)#Avance a morros
        ev3.speaker.say("Hopa")
        morros()
 

