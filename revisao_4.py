# Uma loja online cobra frete assim: grátis para compras acima de R$200; R$15 para até 5kg; R$25 para 5–20kg; R$50 acima de 20kg — mas há 20% de desconto no frete para clientes premium.
# Leia o valor da compra, o peso e se o cliente é premium (s/n). Exiba o frete final e o total do pedido.

#entrada
valorCompra = float(input("Digite o valor da compra: ").replace(",","."))
pesoCompra = float(input("Digite o peso: (em KG) ").replace(",","."))
tipoCliente = input("O cliente é premium? (s/n) ".replace("S","s"))


#processamento
print (f"Compra: {valorCompra} | Peso: {pesoCompra}Kg | Premium: {tipoCliente}")
if valorCompra >= 200:
    frete = "Gratis"
    print (f"Frete: {frete} | Total: R${valorCompra}")
else:
    if pesoCompra <= 5:
        frete = 15
    elif pesoCompra > 5 and pesoCompra <= 20:
        frete = 25
    else:
        frete = 50
    if tipoCliente == "s" and valorCompra < 200:
        frete = frete - (frete * 0.2)
    valorTotal = valorCompra + frete
    print (f"Frete: {frete} | Total: R${valorTotal}")




#saida

