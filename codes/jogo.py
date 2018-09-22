#!/usr/bin/python
# -*- encoding: utf-8 -*-

from random import randint
print ('Bem vindo!')
sorteado = randint(1, 10)
chute = 0
tentativas = 0
while chute != sorteado:
    chute = int(input ('Chute: '))
    if chute == sorteado:
        print ('Você venceu!')
    else:
        if chute > sorteado:
            print ('Seu número é maior')
            tentativas+=1
        else:
            print ('Seu número é Menor')
            tentativas+=1
print ('Fim do jogo! em '),tentativas," tentativas"
