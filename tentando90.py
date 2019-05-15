#!/usr/bin/env python3
#Codigo que faz uma curva p/ direita, segue reto, e faz uma curva p/ esquerda
#importacao da biblioteca de motores
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveTank,SpeedPercent

#definicoes
tank = MoveTank(OUTPUT_A,OUTPUT_B)
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
motorC = MediumMotor(OUTPUT_C)

#testes p/ conseguir uma corva de 90* com 1motor + motor C
#90* p/ direita
def dir90():
    motorC.on_for_degrees(SpeedPercent(50), 25, block = True)
    motorA.on_for_rotations(SpeedPercent(100), 3.8)
    motorA.stop()
    motorC.on_for_degrees(SpeedPercent(-30), 25)
#90* p/ esquerda
def esq90():
    motorC.on_for_degrees(SpeedPercent(-50), 25, block = True)
    motorB.on_for_rotations(SpeedPercent(100), 3.8)
    motorB.stop()
    motorC.on_for_degrees(SpeedPercent(30), 25)

#Execucao:
dir90() #curva p/direita
tank.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 5) #segue reto por cinco rotacoes dos motores A e B
esq90() #curva p/ esquerda
