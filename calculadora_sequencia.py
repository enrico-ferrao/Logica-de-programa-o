num = int(input("Digite um numero: "))

valor = 0
# c/ for
for n in range (1, num+1,1):
    valor = valor + n
print (valor)
    

#c/ while
valor = 0
n = 1
while n <= num:
    valor = valor + n
    n = n + 1
print (valor)