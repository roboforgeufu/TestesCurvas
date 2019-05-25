#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor
#importacao da biblioteca de motores
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveTank,SpeedPercent
import time
# declaracao dos sensores
sensor1 = ColorSensor(INPUT_1)  #sensor da esquerda
sensor2 = ColorSensor(INPUT_2)  #sensor da direita

#declaracao dos motores
tank = MoveTank(OUTPUT_A,OUTPUT_B)
motorA = LargeMotor(OUTPUT_A)   #motor da esquerda
motorB = LargeMotor(OUTPUT_B)   #motor da direita
motorC = LargeMotor(OUTPUT_C)

#Variaveis
vel_tank = 400
curv2_90 = 400

#90* p/  com 1 motor // x é a quantidade de rotacoes do motorB
def esq90(x):
    motorA.stop()
    motorB.on_for_rotations(SpeedPercent(100), x)
    motorB.stop()

#90* p/ direita com 1 motor // x é a quantidade de rotacoes do motorA
def dir90(x):
    motorB.stop()
    motorA.on_for_rotations(SpeedPercent(100), x)
    motorA.stop()


#90* p/ esquerda com 2 motores // x é a posicao final intencionada do motorA
def esq2(x):
    #x = variavel que representa o "tamanho da curva", atraves das rotacoes do motor A
    motorA.reset()
    motorB.reset()
    while motorA.position < x:
        motorA.run_forever(speed_sp = 900)
        motorB.run_forever(speed_sp = -900)
    motorA.stop()
    motorB.stop()

#90* p/ direita com 2 motores // x é a posicao final intencionada do motorB
def dir2(x):
    #x = variavel que representa o "tamanho da curva", atraves das rotacoes do motor B
    motorA.reset()
    motorB.reset()
    while motorB.position < x:
        motorA.run_forever(speed_sp = -900)
        motorB.run_forever(speed_sp = 900)
    motorA.stop()
    motorB.stop()

#ajuste na linha
def ajuste(cor, direcao):
    while sensor1.color != cor:
        motorA.run_forever(speed_sp = 100 * direcao)
    motorA.stop()
    while sensor2.color != cor:
        motorB.run_forever(speed_sp = 100 * direcao)
    motorB.stop()

#EXECUCAO

while sensor1.color == 6 and sensor2.color == 6:
    motorA.run_forever(speed_sp = vel_tank)
    motorB.run_forever(speed_sp = vel_tank)
motorA.reset()
motorB.reset()
while motorA.position > 600:
    motorA.run_forever(speed_sp = -vel_tank)
    motorB.run_forever(speed_sp = -vel_tank)
motorA.stop()
motorB.stop()

ajuste(5, 1)

motorA.reset()
motorB.reset()
while motorA.position < 600:
    motorA.run_forever(speed_sp = vel_tank)
    motorB.run_forever(speed_sp = vel_tank)
motorA.stop()
motorB.stop()

dir2(curv2_90)
while sensor1.color != 6 and sensor2.color != 6:
    motorA.run_forever(speed_sp = vel_tank)
    motorB.run_forever(speed_sp = vel_tank)
motorA.reset()
motorB.reset()
while motorA.position > 600:
    motorA.run_forever(speed_sp = -vel_tank)
    motorB.run_forever(speed_sp = -vel_tank)
motorA.stop()
motorB.stop()

ajuste(6, 1)

while motorA.position < 600:
    motorA.run_forever(speed_sp = vel_tank)
    motorB.run_forever(speed_sp = vel_tank)
motorA.stop()
motorB.stop()

ajuste(5, -1)
