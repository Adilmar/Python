from random import randint
print ('Bem vindo!')
sorteado = randint(1, 100)
chute = 0
while chute != sorteado:
    chute = int(input ('Chute: '))
    if chute == sorteado:
        print ('Voc� venceu!')
    else:
        if chute > sorteado:
            print ('Seu n�mero � maior')
        else:
            print ('Seu n�mero � Menor')
print ('Fim do jogo!')
