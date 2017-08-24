from random import randint
print ('Bem vindo!')
sorteado = randint(1, 100)
chute = 0
while chute != sorteado:
    chute = int(input ('Chute: '))
    if chute == sorteado:
        print ('Você venceu!')
    else:
        if chute > sorteado:
            print ('Seu número é maior')
        else:
            print ('Seu número é Menor')
print ('Fim do jogo!')
