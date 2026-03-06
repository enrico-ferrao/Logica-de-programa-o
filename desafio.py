#ler 2 numeros, exibir o maior
#ler 2 numeros, exibir o maior ou se são iguais
#ler 3 numeros, exibir o maior

modelo = int(input("Qual modelo quer ir: "))
valor1 = int(input("Digite o primeiro numeros: "))
valor2 = int(input("Digite o segundo numeros: "))


if modelo == 1:
    if valor1 > valor2:
        print (f"o maior numeros é {valor1} ")

    else:
        print (f"o maior numeros é {valor2} ")
        
elif modelo == 2:
    if valor1 > valor2:
        print (f"o maior numeros é {valor1} ")
    elif valor2 > valor1:
        print (f"o maior numeros é {valor2} ")
    else:
        print (f"os numeros são iguais ")

else:
    valor3 = int(input("Digite o terceiro numeros: "))
    if valor1 > valor2 and valor1 > valor3:
        print (f"o maior numeros é {valor1} ")
    elif valor2 > valor1 and valor2 > valor3:
        print (f"o maior numeros é {valor2} ")
    else:
        print (f"o maior numeros é {valor3} ")
