import random

sorteado = random.randint(1,10)
chute = int(input("digite um numero de 1 a 10: "))

while chute != sorteado:
    print ("Errou")
    chute = int(input("tente novamente: "))
print ("parabens")