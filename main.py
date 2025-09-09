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
    while not 20 < line_sensor2.reflection() < 30:
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
    
def seguir_linea_minus_4(velocidad):
    robot.reset()
        #seguir hasta ver negro pero pa tras
    while not line_sensor.reflection() < 17:
        left_motor.run(velocidad)   # velocidad en grados por segundo
        right_motor.run(velocidad)
        
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
    
    
def avance_mm(velocidad, milimetros):
      right_motor.run_angle(velocidad, (milimetros*100)/46.9, then=Stop.HOLD, wait=False)
      left_motor.run_angle(velocidad, (milimetros*100)/46.9, then=Stop.HOLD, wait=True) 
       
    

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
    avance(800,631) #Avance en X
    right_motor.run_angle(800,580, then=Stop.BRAKE, wait=True) #Giro
    avance(800,270)#Avance recto hacia escotilla roja
    bajar_garra(390)
    avance(800,-250) #Retroceso para halar
    subir_garra(-390)
    wait(500)
    rotar_garra(1) #reacomodar garra
     


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
    avance(400,-50)
    wait(200)
    avance(400, -100)
    left_motor.run_angle(400,-580,then=Stop.BRAKE, wait=True)
    avance(800,1190)
    left_motor.run_angle(400,890 ,then=Stop.BRAKE, wait=True)
    avance(800,-90)
    subir_garra(-407)
    avance(600,-200)  
    bajar_garra(406)   
    avance(400, -50)   
    right_motor.run_angle(400,550,then=Stop.BRAKE, wait=True)
    avance(800,-140)  
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
        
def arreglar_garra():
    if colorx == Color.GREEN:
        rotar_garra(1)
    if colorx == Color.RED:
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
    avance(800,-890) #Salida de carga útil
    right_motor.run_angle(600,580, then=Stop.HOLD, wait=True) #Giro para quedar de frente a bandera 1
    avance(800,-70)
    bajar_garra(390) #Bajar banderita
    subir_garra(-390)
    left_motor.run_angle(600,580, then=Stop.HOLD, wait=True)#Giro para quedar en X
    right_motor.run_angle(600,580, then=Stop.HOLD , wait=True)#Quedar frente a banderita 2
    avance(800,-60) #Retroceso para precisión
    bajar_garra(330)
    avance(600,-220) # Hala palanquita
    subir_garra(-330)
    


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
        bajar_garra(394) #Cargautil
        color_rotor() 
        avance(600, 550) #avance para llegar a la línea
        seguir_linea4() #Chocar con la línea
        robot.stop()
        wait(300)
        robot.turn(89.2)#Giro para quedar en x
        robot.stop()
        subir_garra2(-394)
        avance(500, 1280)
        wait(200)
        bandera()
        seguir_linea_minus_4(-550) #Retroceder a línea y chocar
        robot.stop()
        avance(800, 90) #acomodarse pa el seguir linea
        robot.turn(90)#GIro al sentido oriente de linea
        robot.stop()
        seguir_linea2() #Chocar adyacente
        robot.stop()
        avance(800, 350) #X hacia escotilla roja
        robot.turn(-90) #Giro a escotilla roja
        robot.stop()
        bajar_garra(390)
        avance(800,500) #Y a escotilla roja
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""
            
            
            
            
            
       

while True:
    pressed = ev3.buttons.pressed()
    if Button.DOWN in pressed:
        wait(1000)
        seguir_linea(600)
        seguir_linea2()
        wait(100)
        robot.stop()
        avance(800, -149) #Retroceso para ir a colorx
        
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
        
        bajar_garra(394) #Cargautil
        color_rotor() 
        avance(600, 550) #avance para llegar a la línea
        seguir_linea4()#Chocar con la línea
        robot.stop()
        avance(800, 40)
        wait(300)
        robot.turn(89.2)#Giro para quedar en x
        robot.stop()
        subir_garra2(-394)
        avance(500, 1280)
        wait(200)
        bandera()

        seguir_linea_minus_4(-550) #Retroceder a línea y chocar
        robot.stop()
        avance(800,350) #Vertical a escotilla amarilla Y
        robot.turn(-85) #Giro a escotilla para quedar en X
        robot.stop()
        avance(400, -775) #Empujar escotilla
        left_motor.run_angle(800, -300, then=Stop.HOLD, wait=True)
        left_motor.run_angle(800, 300, then=Stop.HOLD, wait=True)
        seguir_linea_minus_4(-400) #Chocar con adyacente negra
        robot.stop()
        left_motor.run_angle(600, -580, then=Stop.BRAKE, wait=True) #Giro hacia linea principal
        seguir_linea4() #Chocar con linea principal
        robot.stop()
        avance(800, 115) #Acomodacion para el angulo
        robot.turn(-78) #Angulo para quedar en sentido de linea a morros
        robot.stop()
        DRIVE_SPEED = 200
        seguir_linea2() #Chocar con segunda adyacente
        robot.stop()    
        seguir_linea(160)#Avance a morros
        arreglar_garra()
        morros()
        avance(800, -390) #Retroceso a misión especial
        left_motor.run_angle(800, -300, then=Stop.HOLD, wait = True)#Giro para buscar línea
        
        seguir_linea_minus_4() #Choque con linea
        robot.stop()
        
        robot.turn(90)#Giro a la izquierda para alinearse con linea principal
        robot.stop()
        
        seguir_linea2()#Seguimos linea y chocamos con adyacente
        robot.turn(-90)#Giro para alinearse con adyacente
        robot.stop()
        
        seguir_linea(363) #Seguimos adyacente
        robot.stop(Stop.HOLD)  
        robot.turn(90)#Giro a la izquierda para quedar frente a bloque de marcado
        robot.stop()
        
        avance(800, -80)#retroceso para precisión
        bajar_garra(410)  
        avance(800,500)  #Retroceso mayor para Ir a dejar el bloquesito 
        robot.turn(-90) #giro a la derecha para quedar frente a zona de destino
        robot.stop()
        
        avance(800,500) #Avanzamos a zona de destino
        subir_garra(415) #Soltamos bloquesito
      
avance_mm(800,300)      
robot.stop(Stop.HOLD)  



while True:
    
    ev3.speaker.play_notes(["A4/4","A4/4","A4/4","C/4", "C4/4", "G4/8", "G4/8", "D4/4", ""] tempo=130)
    left_motor.run_angle(800, -12000, then=Stop.HOLD, wait=False)
    right_motor.run_angle(800, 12000, then=Stop.HOLD, wait=True)
"""


