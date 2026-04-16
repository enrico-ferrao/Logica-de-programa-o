n = int(input("Digite a quantidade de notas: "))
notas = []
i = 1
while i < n+1:
    notas.append(float(input(f"Digite a {i} nota: ")))
    i += 1
