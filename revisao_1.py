# Uma confeiteira vende bolos e quer gerar rótulos automaticamente. 
# Leia o nome do produto, o peso  gramas e o preço. Exiba um rótulo formatado com o preço por kg calculado.

#entrada
nomeProduto = input("Digite o nome do produto: ")
pesoProduto = int(input("Digite o peso do produto: "))
precoProduto =float(input("Digite o preço por kg: "))

#processamento
precoFinal = pesoProduto * (precoProduto / 1000)

#saida
print(f"Produto: {nomeProduto} | Peso: {pesoProduto}g | Preço: R${precoFinal}")
print(f"{nomeProduto} - {pesoProduto}g - R${precoFinal} (R${precoProduto}) ")