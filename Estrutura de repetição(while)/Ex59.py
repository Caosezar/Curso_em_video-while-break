#Crie um programa que leia dois valores e mostre um menu na  tela, 1 para somar 2 multiplicar 3 maior 4 novos números 5 sair do programa
#O programa deve realizar o que lhe for solicitado
from time import sleep  as sp

from pyautogui import sleep
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digit eo segundo valor: '))
op = 0 
while op != 5:
    print(''' Qual operação deseja realizar?
[1] SOMA
[2] MULTIPLICAÇÃO
[3] MAIOR
[4] SELECIONAR NUMEROS NOVAMENTE
[5] SAIR DO PROGRAMA ''')
    op= int(input('Digite o sua opção: '))
    print('Processando . . .')
    sleep(0.80)
    if op==1:
        soma = n1+n2
        print(f'{n1} + {n2} = {soma}')
    elif op==2:
        mult = n1*n2
        print(f'{n1} x {n2} = {mult}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'{maior} é o maior entre {n1} e {n2}. ')
    elif op==4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print("Finalizando ...")
        sleep(1.25)
        print('Fim da execução. ')