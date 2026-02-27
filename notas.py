#Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

#entrada
nome = input("digite o nome do aluno: ")
n1 = float(input("digite a nota do primeiro semestre: ").replace(",","."))
n2 = float(input("digite a nota do segundo semestre: ").replace(",","."))
n3 = float(input("digite a nota do terceiro semestre: ").replace(",","."))

#processamento
media = (n1 + n2 + n3) / 3
frase = (f"o aluno, {nome}, está com a media: {media} ")

#saida
if media >= 7:
    print (frase + "e foi aprovado" )

elif media <= 5 and media < 7:
    print (frase + "e esta de recuperação")

else:
    print(frase + "e ficou reprovado")

