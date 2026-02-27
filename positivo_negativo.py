#ler um número e dizer se ele positivo, negativo ou neutro

#entrada
numero = int(input("Digite um numero: "))

#teste lógico 

if numero > 0:
    print (f"{numero} é positivo")
elif numero == 0:
    print (f"{numero} é neutro")
else: 
    print (f"{numero} é negativo")

