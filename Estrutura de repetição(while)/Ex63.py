#fazer uma sequência fibonancci
from calendar import c


def teste():
    res=int(input('''Deseja fazer novamente? 
    1) SIM
    2) NÃO
    → '''))
    if res == 1:
        fibonacci()
    elif res == 2:
            print('Fim da execução!')
    else:
        print('ERRor')


def fibonacci():
    n1=int(input('Que termo deseja encontra? '))
    ult=1
    penult=1
    if (n1==1) or (n1==2):
        print('1')
    else:
        cont = 3
    while cont <=n1:
        termo = ult + penult
        penult = ult
        ult = termo
        cont+=1
        print(f'{termo} → ', end='')
    teste()

fibonacci()
