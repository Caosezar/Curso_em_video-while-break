from ast import Num


maior = 0
menor = 0
média = 0
soma = 0
cont = 0
atual=0
res = ('S')
while res in "Ss":
    n1 = int(input('Digite um número: '))
    soma+=n1
    cont += 1
    if n1>atual:
        maior = n1
    if n1 < atual:
        menor = n1
    atual = n1
    res=str(input('Quer continuar? [S/N]').upper().strip()[0])
média = soma/cont
print(f'Você digitou {cont} números, maior número foi {maior}, e o menor número foi {menor} e a média foi {média}.')