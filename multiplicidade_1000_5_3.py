soma = 0
for n in range(0,1001,1):
    if n % 5 == 0 or n % 3 == 0:
        soma = soma + n
print (f"valor: {soma}")