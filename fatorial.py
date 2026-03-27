#entrada
num = int(input("digite um inteiro positivo: "))

#iniciar a multiplicação

fatorial = 1

for n in range (1,num + 1, 1):
    fatorial = fatorial * n

print (f"fatorial de {num} = {fatorial}")
       
#laço com while
fatorial = 1
n = 1 

while n <= num:
    fatorial = fatorial * n
    n = n + 1
print (f"fatorial de {num} = {fatorial}")
