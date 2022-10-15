#faça um programa  que leia o sexo de uma pessoa, mas só aceite valores "M" ou "f" caso esteja errado peça a digitação novamente até ter um valor correto
masc = 0
fem = 0
sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Digite novamente, desta vez usando (M) ou (F)). ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso. ')
