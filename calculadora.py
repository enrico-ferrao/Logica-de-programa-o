#faça uma calculadora de segundo grau

import math

print ("Bem vindo a calculadora de equação de segundo grau")

def se():
    a = float(input("Qual o termo A: "))
    if a == 0:
        print ("Essa função não é de segundo grau")
        return se()
    else:
        b = float(input("Qual o termo B: "))
        c = float(input("Qual o termo C: "))
        delta = (b ** 2) - 4 * a * c
        if delta < 0:
            print ("Não tem raiz real ")
        if delta < 0:
            print ("Não tem raiz real ")
        elif delta == 0:
            x = -b +math.sqrt(delta) / 2 * a
            print (f"O x é {x}")
        else:
            x1 = -b +math.sqrt(delta) / 2 * a
            x2 = -b -math.sqrt(delta) / 2 * a
            print (f"O x1 é {x1} e o x2 é {x2}")

se()
