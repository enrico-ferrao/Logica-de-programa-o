#Leia o valor total da conta, o percentual de gorjeta desejado e o número de pessoas.
#Exiba o valor da gorjeta, o total com gorjeta e quanto cada pessoa paga.

#entrada
valorConta = float(input("Digite o valor da conta: ").replace(",","."))
percentualGorjeta = int(input("Digite o percentual de gorjeta: "))
qntDePessoa = float(input("Digite a quantidade de pessoas: "))

#processamento
gorjetaPagar = valorConta * (percentualGorjeta / 100)
totalPagar = gorjetaPagar + valorConta
valorPorPessoa = totalPagar / qntDePessoa

#saida
print (f"Conta: R${valorConta} | Gorjeta: {percentualGorjeta}% | Pessoas: {qntDePessoa}")
print(f"Gorjeta: R${gorjetaPagar:.2f} | Total: R${totalPagar:.2f} | Por pessoa: R${valorPorPessoa:.2f}")