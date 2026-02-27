#saber se o numero é par ou impar

#entrada
numero = int(input("Digite um numero: "))

#processamento
numero_resto = numero % 2

#teste logico
if numero_resto == 0:
    print ("Numero é par")
else:
    print ("Numero é impar")