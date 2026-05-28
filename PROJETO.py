import random

lista = []

for numsort in range(30):
    lista.append(random.randint(0, 100))

print(lista)
    
indice = random.randint(1, len(lista) - 2)
escolhido = lista[indice]

esquerda = lista[indice - 1]
direita = lista[indice + 1]

print("Número escolhido:", escolhido)
print("Esquerda:", esquerda)
print("Direita:", direita)

if esquerda > direita and esquerda > escolhido:
    print("O maior do lado é:", esquerda)
elif direita > esquerda and direita > escolhido:
    print("O maior do lado é:", direita)
elif escolhido > esquerda and escolhido > direita:
    print("O número escolhido já é o maior:", escolhido)
elif max(lista) != escolhido:
    print("O escolhido não é o ótimo global, então ficou em ótimo local.")
else:
    print("Há empate entre os valores.")

print("O maior número da lista é o:", max(lista))
