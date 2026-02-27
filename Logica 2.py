a = 10
a+a

nome = "Enrico"
sobrenome = "Ferrão"
f"{nome} {sobrenome}"

b = 3
potencia = a ** b
print ("%d elevado a %d = %d" %(a,b,potencia))

#ler a altura e o peso de um usuário, calcular e exibir seu imc.

#entradas
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

#processamento
imc = peso / altura ** 2

#saida
print ("Seu imc é de %.2f " %(imc))

#quando usamos .2f, ele exibira 2 casas decimais

#ler a  altura e a base de um triangullo e calcular sua area ( base * altura) / 2

#entradas
altura = float(input("Digite a altura: "))
base = float(input("Digite a base: "))

#processamento
area = (base * altura) / 2

#saida
print ("A area do triangulo é %.2f" %(area))

#A velocidade 100km/h corresponde a 62 milhas/h. Ler uma velocidade em km

#entradas
velocidadekm = float(input("Digite sua velocidade: "))

#processamento
velocidademh = velocidadekm * 0.62

#saida
print (f"A velocidade em milhas é: {velocidademh}")


# Transforme 17043 segundos em minutos e horas

#entrada
segundos = 17043

#processamento
horas = segundos // 3600
minutos = (segundos % 3600)/60
segundos_resto = segundos % 3600 % 60

#saida
print (f"{segundos} em horas minutos fica: %d h %d m %d s " %(horas,minutos,segundos_resto))

# a % é o resto da conta, depois do numero inteiro


#Caixa eletronico possui notas de: 100, 50 , 20 , 10
#entrada
saque = 790

#processamento
cem = saque // 100
resto_cem = saque % 100
cinquenta = resto_cem // 50
resto_cinquenta =  cinquenta % 50
vinte = resto_cinquenta // 20
resto_vinte = vinte % 20
dez = resto_vinte // 10

#saida
print (f"{cem} de 100, {cinquenta} de 50, {vinte} de 20, {dez} de 10")

#Transforme celsus em Fahrenheit
#entrada
celsus = float(input("Digite a temperatura em \u00B0C: "))

#processamento
fahrenheit = (celsus * 1.8) + 32

#saida
print (f"{fahrenheit} \u00B0F ")

#Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4.90, escreva um algoritmo para ler: a marcação do odômetro (Km) no início do dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia
#entrada
odometro_dia = float(input("digite o odometro no inicio: "))
odometro_noite = float(input("digite o odometro no final: "))
dinheiro = float(input("digite o dinheiro ao final: R$ "))
litros = float(input("digite quantos litros usou: "))
gasolina = 4.90

#processamento
kmrodados = odometro_noite - odometro_2dia
kml = kmrodados / litros
consumo = litros * gasolina
lucro = dinheiro - consumo

#saida
print (f"Você rodou {kml} Km/L e o lucro foi de: R${lucro}")

