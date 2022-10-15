#Refaça o exercício 51 com while.
def teste():
    res = int(input('''Deseja continuar?
    1)SIM
    2)NÃO
    →'''))
    while res == 1:
        progressao()
        if res != 1:
            print('Finalizando...')
def progressao():
    n1 = int(input('Digite o primeiro termo: '))
    razao = int(input('Digite a razão: '))
    termo = 0
    cont = 1
    while cont <= 10:
        print(f'{termo}', end='→')
        termo += razao
        cont+=1
    print('Fim')
    teste()
progressao()


