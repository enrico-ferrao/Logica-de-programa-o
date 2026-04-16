#entrada
char = input ("Digite o caracter: ")
largura = int(input("Digite a largura: "))
altura = int (input ("Digite a altura: "))

#processamento
for i in range (0,altura):
    if i == 0 or i == altura -1:
        print (char*largura)
    else:
        print (char + " " *(largura - 2) + char)
