continuar=('S')
tot18=0
totH=0
totM20=0
while continuar == ('S'):
    print('========CADASTRO DE PESSOAS========')
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo= str(input('Sexo? [M/F]: ')).strip().upper()[0]
        if idade >=18:
            tot18+=1
        if sexo == ('M'):
            totH+=1
        if sexo == 'F' and idade <20:
            totM20+=1
    continuar= ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == ('N'):
        print('Fim do Cadastro.')
        break
print(f'O Total de pessoas com mais de 18 anos é: {tot18}.')
print(f'Ao Todo são {totH} homens.')  
print(f'O Total de mulheres com menos de 20 anos é {totM20}.')

