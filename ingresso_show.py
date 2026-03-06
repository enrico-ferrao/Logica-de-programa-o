ingresso = int (input ("Qual o ingresso: (pista = 1, arquibancada = 2) "))
quantidade = int ( input ("Quantos ingressos: ") )

if ingresso == 1:
    tipo = int (input ("Qual tipo de pista: (premium = 1, comum = 2)"))
    if tipo == 1:
        print (f"Na pista premium, você gastará R$ {quantidade  * 500}")

    else:
        print (f"Na pista comum, você gastará R${quantidade * 200 }")

else:
    tipo = int (input (f"Qual tipo de aquibancada: (inferior = 1, superior = 2)"))
    if tipo == 1:
        print (f"Na arquibancada inferior, você gastará R${quantidade * 400}")

    else:
        print (f"Na arquibancada superior, você gastará R${quantidade * 350}")
    
