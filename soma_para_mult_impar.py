#entrada de dados
inicio = int(input("digite o valor inicial do intervalo: "))
fim = int(input("digite o valor final do intervalo: "))

#validar a entrada
if inicio > fim:
    aux = inicio
    inicio = fim
    fim = aux

fim = fim + 1 
#inicializar os acumuladores
soma = 0
multiplicacao = 1

# o laço

for n in range (inicio,fim,1):
    if n % 2 == 0:
        soma = soma + n
    else:
        multiplicacao = multiplicacao * n
print (f"soma = {soma}\nmuliplicação = {multiplicacao}")