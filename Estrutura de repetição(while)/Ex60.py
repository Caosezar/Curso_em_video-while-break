#escreva um programa qualquer que leia um número e mostre seu fatorial.

n = int(input('Digite um número: '))
c = n
res = 1
while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else '=', end='')
    res*=c
    c-=1
print(f'{res}')
'''numero = int(input("Fatorial de: ") )
resultado=1
count=1

while count <= numero:
    resultado = resultado*count
    count += 1

print(resultado)'''