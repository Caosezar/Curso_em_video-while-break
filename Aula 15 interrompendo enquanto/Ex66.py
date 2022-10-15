s=n = cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números é de : {s}')