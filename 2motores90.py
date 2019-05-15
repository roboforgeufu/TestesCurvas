#!/usr/bin/env python3
#importacao da biblioteca de motores
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveTank,SpeedPercent
#importacao da biblioteca tempo p/contagem de segundos
import time

#definicoes
tank = MoveTank(OUTPUT_A,OUTPUT_B)
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
motorC = MediumMotor(OUTPUT_C)

#testes p/ conseguir uma curva de 90* utilizando dois motores(A e B)ao mesmo tempo
#p/ esquerda:
def esq90_2(n):
    #n = variavel que representa o "tamanho da curva"
    motorA.reset()
    motorB.reset()
    motorC.on_for_degrees(SpeedPercent(50), 25, block = True) #coloca o eixo das rotas traseiras na posicao correta
    while motorA.position < n:
        motorA.run_forever(speed_sp = 900)
        motorB.run_forever(speed_sp = -400)
    motorA.stop()
    motorB.stop()
    motorC.on_for_degrees(SpeedPercent(-50), 25) # traz o eixo das rodas traseiras para a posicao central
#p/direita:
def dir90_2(n):
    #n = variavel que representa o "tamanho da curva"
    motorA.reset()
    motorB.reset()
    motorC.on_for_degrees(SpeedPercent(-50), 25, block = True) #coloca o eixo das rotas traseiras na posicao correta
    while motorB.position < n:
        motorA.run_forever(speed_sp = -400)
        motorB.run_forever(speed_sp = 900)
    motorA.stop()
    motorB.stop()
    motorC.on_for_degrees(SpeedPercent(50), 25) # traz o eixo das rodas traseiras para a posicao central

#Execucao
esq90_2(1300)
tank.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 5) #segue reto por cinco rotacoes dos motores A e B
dir90_2(1300)
