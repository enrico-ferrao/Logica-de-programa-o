numero = int( input ("digite seus valores, 0 encerra: "))
soma = 0

while numero != 0:
    soma = soma + numero
    print (f"soma parcial = {soma}\n")
    numero =  int ( input ("digite o proximo, 0 encerra: "))

print (f"soma = {soma}")