num =0
cont=0
soma=0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma+=num
    cont+=1
print('Acabou.')
print(f'Você digitou {cont-1} números e a soma entre eles foi {soma-999}. ')
