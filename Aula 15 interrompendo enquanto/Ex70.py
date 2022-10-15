totG=0 
menor=0
cont=0
barato = ' '
mais1k=0
while True:
    nome=str(input('Digite o nome do produto: '))
    preço=float(input('Digite o preço do produto: '))
    resp = ' '
    cont+=1
    if cont ==1 or preço < menor:
        menor=preço
        barato = nome
    if preço > 1000:
        mais1k+=1
    totG+=preço
    while resp not in 'SN':
        resp=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print('Fim da execução')
        break
print(f'O total gasto foi R$ {totG:.2f}')
print(f'{mais1k} produtos acima de 1000 reais')
print(f'O produto mais barato foi {barato}, com R$ {menor}')
