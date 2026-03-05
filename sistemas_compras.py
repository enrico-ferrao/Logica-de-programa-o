#valor de compras.
# input forma de pagamento.
# avista sendo variavel 1 ( pix c/10% de desconto).
# variavel 2 (boleto c/5% de desconto).
# essas 2 variaveis sao em if dentro do primero if
# aprazo + numero de parcelas (2 vezes e o valor final), (3 vezes + 5% de acrescimo + valor final), (+ que 3 é invalido)
# caso nao seja avista ou aprazo TEM QUE DAR INVALIDO


valor_compra = float(input("Qual valor da compra? ").replace(",", "."))
forma_de_pagamento = int(input("Qual forma de pagamento ? (avista = 1, aprazo = 2) "))


if forma_de_pagamento == 1:
    avista = int(input("Avista no pix ou no boleto? (pix = 1, boleto = 2) "))
    if avista == 1:
        desconto = valor_compra * 0.1
        valor_final = valor_compra - desconto
        print (f"Sua compra deu: R${valor_final} e seu desconto foi de R${desconto} ")
    elif avista == 2:
        desconto = valor_compra * 0.05
        valor_final = valor_compra - desconto
        print ("Sua compra deu: R$ %.2f e seu desconto foi de R$ %.2f "  %(valor_final,desconto))
    else:
        print("Opção invalida!")


elif forma_de_pagamento == 2:
    aprazo = int(input("Aprazo, em quantas parcelas: (2 vez = 2, 3 vezes = 3) "))
    valor_parcela = valor_compra / aprazo
    if aprazo == 2:
        print (f"Sua compra deu: R${valor_compra}, o valor da parcela é de: R${valor_parcela} e a compra foi divida em: {aprazo} vezes s/ juros ")
    
    elif aprazo == 3:
        acrescimo = valor_compra * 0.05
        valor_final = valor_compra + acrescimo
        print (f"Sua compra deu: R${valor_final}, o valor da parcela é de: R${valor_parcela} e a compra foi divida em: {aprazo} vezes com 5% juros ")

    else:
        print ("Opção invalida!")

else:
    print("Opção invalida!")