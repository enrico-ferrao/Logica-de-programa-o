n = int(input("digte quantos pares você quer: "))

pares = []#iniccializou uma lista vazia
cont = 0
while cont < n :
    pares.append(2*cont)
    cont = cont + 1

print(f"pares: {pares}")
print(f"soma = {sum(pares)}")

pares = []
for v in range(2*n):
    if v % 2 == 0:
        pares.append(v)

print(f"pares: {pares}")
print(f"soma = {sum(pares)}")

pares = []
for v in range(0, 2*n, 2):
    pares.append(v)

print(f"pares: {pares}")
print(f"soma = {sum(pares)}")

pares = [v for v in range(2*n) if v%2 == 0]
print(f"pares: {pares}")
print(f"soma = {sum(pares)}")