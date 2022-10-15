win =1

from random import randrange
while win ==1:
    cont=0
    player=int(input('Digite um valor: '))
    regra=int(input('''Par ou ímpar?  
    1)PAR
    2)ÍMPAR
    → '''))
    pc=randrange(1,10)
    gg = player + pc
    if regra ==1:
        if gg%2==0:
            cont=cont+1
            win=1
            print(f'Eu digitei {pc} e você digitou {player} .Você venceu!')
        else:
            win=2
            print(f'Eu digitei {pc} e você digitou {player} .Você perdeu!')
    if regra ==2:
        if gg%2==1:
            cont=cont+1
            win=1
            print(f'Eu digitei {pc} e você digitou {player} .Você venceu!')
        else:
            win=2
            print(f'Eu digitei {pc} e você digitou {player} .Você perdeu!')
    if cont > 1:
        print(f'Você ganhou {cont} vezes!')      


