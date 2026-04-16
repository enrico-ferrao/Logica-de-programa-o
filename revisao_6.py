contador  = 0
somador = 0
min = None
max = None
while True:
    iqa = int(input("Digite a leitura: "))

    if iqa == -1:
        break

    contador = contador + 1
    somador = somador + iqa
    if min is None or iqa < min:
        min = iqa
    if max is None or iqa > max:
        max = iqa

media = somador / contador 
print (f"Leituras: {contador} | Media: {media:.2f} | Min: {min} | Max: {max}")
if media <= 50:
    print ("Classificação do dia: Boa")
elif media > 50 and media <= 100:
    print ("Classificação do dia: Moderada")
elif media > 100 and media <= 150:
    print ("Classificação do dia: Ruim para grupos sensíveis")
elif media > 150 and media <= 200:
    print ("Classificação do dia: Ruim")
else:
    print ("Classificação do dia: Muito ruim")