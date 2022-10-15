#Melhore o jogo do desafio 28, onde o computador  vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites fora necessarios até acertar.
cont = 1
from random import randrange as rr
player = int(input('Digite um número de 1 a 10 e tente acertar em qual número eu estou pensando. '))
pc = rr(1,10)
while player != pc:
    cont += 1
    player = int(input(f'Não! não pensei em {player} pensei em {pc}, TENTE NOVAMENTE!'))
    pc = rr(1,10)
print(f'Parabéns, você acertou! pensei exatamente em {pc}')
if cont < 5:
    print(f'Foram {cont} tentativas.')    
elif cont >= 10:
    print(f'minha nossa você precisou de {cont} tentativas para acertar? Muito azarado credo!')
elif cont == 1:
    print('Nossa!! de primeira!! PARABÉNS!! ESTAMOS EM SINTONIA<3')
print('FIM DO JOGO')
