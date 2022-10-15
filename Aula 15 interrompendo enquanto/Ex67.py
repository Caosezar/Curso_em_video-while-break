from re import M


n=1
while n > 0:
    n= int(input('TABUADA, DIGITE UM NÚMERO//(NÚMERO NEGATIVO PARA SAIR): '))
    if n < 0 :
        print('Programa de tabuada encerrado.')
        break  
    for c in range (1, 11):
        m = n*c
        print(f'{n} x {c} = {m}')
