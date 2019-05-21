#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor
#importacao da biblioteca de motores
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveTank,SpeedPercent
# declaracao dos sensores
sensor1 = ColorSensor(INPUT_1)  #sensor da esquerda
sensor2 = ColorSensor(INPUT_2)  #sensor da direita

#declaracao dos motores
tank = MoveTank(OUTPUT_A,OUTPUT_B)
motorA = LargeMotor(OUTPUT_A)   #motor da esquerda
motorB = LargeMotor(OUTPUT_B)   #motor da direita
motorC = MediumMotor(OUTPUT_C)

#90* p/ direita
def dir90():
    motorC.on_for_degrees(SpeedPercent(50), 25, block = True)
    motorB.run_forever(speed_sp = 10)
    motorA.on_for_rotations(SpeedPercent(100), 2.8)
    motorA.stop()
    motorB.stop()
    motorC.on_for_degrees(SpeedPercent(-30), 25)
#90* p/ esquerda
def esq90():
    motorC.on_for_degrees(SpeedPercent(-50), 25, block = True)
    motorB.on_for_rotations(SpeedPercent(100), 2.3)
    motorB.stop()
    motorC.on_for_degrees(SpeedPercent(30), 25)
#ajuste na linha - nao funcionou()
def ajuste():
    motorC.on_for_degrees(SpeedPercent(-50), 25, block = True)
    while sensor1.color != 6:
        motorB.run_forever(speed_sp = -100)
    motorB.stop()
    motorC.on_for_degrees(SpeedPercent(50), 50, block = True)
    while sensor2.color != 6:
        motorA.run_forever(speed_sp = -100)
    motorA.stop()
    motorC.on_for_degrees(SpeedPercent(-50), 25, block = True)

def tentar_direcao(n):
    if n == 0:
        dir90()
    elif n == 2:
        esq90()
    tank.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 700)
    while sensor1.color == 6 and sensor2.color == 6:
        print(sensor1.color,'====', sensor2.color)
        tank.run_forever(speed_sp = 400)
    tank.stop()
    cor = sensor1.color
    return cor

#Execucao
#declaracao de uma lista vazia para receber as cores ja lidas
cores = []

while sensor1.color == 6 and sensor2.color == 6:
    print(sensor1.color,'====', sensor2.color)
    tank.run_forever(speed_sp = 400)
tank.stop()

while sensor1.color != 6 and sensor2.color != 6:
    tank.run_forever(speed_sp = -200)
tank.on_for_degrees(SpeedPercent(30), SpeedPercent(30), 40)
tank.stop()

cor  = tentar_direcao(2)
while True:
    print(cor)
