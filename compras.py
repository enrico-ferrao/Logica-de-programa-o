#ler: nome do produto, valor unitário e quantidade comprada
#calcular o total da compra
#se a quantidade for maior que 100, definir um desconto de 100%

#entrada
nome_produto = input("Nome do produto: ")
valor_produto = float(input("Valor do produto: "))
quantidade_produto = int(input("quantidade produto: "))

#processamento
total_compra = valor_produto * quantidade_produto

#logica
if quantidade_produto > 100:
    desconto = total_compra * 0.1
    valor_final = total_compra - desconto
    print (f"Sua compra deu {valor_final:.2f }, houve um desconto de {desconto:.2f}, {quantidade_produto} de {nome_produto}")

else:
    print (f"Sua compra deu R${total_compra:.2f }, {quantidade_produto} de {nome_produto}")
