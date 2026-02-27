# Ler o sexo (masculino ou feminino) e a altura de uma pessoa em metros. Calcular o peso ideal :
# masculino: p1 = 72.7 x altura - 58
# feminino: p1 = 62.1 x altura - 44.7
# != é quando é diferente

#entrada

def sex():
    sexo = input("Digite seu sexo (M/F): ").replace("m","M").replace("f","F")
    if sexo != "M" and sexo != "F":
        print ("É aceito apenas M ou F")
        return sex()
    else:
        altura = float(input("Digite sua altura (em metros): ").replace(",","."))
        if sexo == "M":
            p1 = 72.7 * altura - 58
            print ("Seu peso ideal é %.2f" %p1)
        else:
            p1 = 62.1 * altura - 44.7
            print ("Seu peso ideal é %.2f" %p1)

sex()


               









