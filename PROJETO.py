import random

lista = []

for i in range(30):
    numero = random.randint(0, 100)
    lista.append(numero)

print(lista)

posicao = random.randint(1, 28)

numero = lista[posicao]
esquerda = lista[posicao - 1]
direita = lista[posicao + 1]

print("Número escolhido:", numero)
print("Esquerda:", esquerda)
print("Direita:", direita)

if esquerda > direita and esquerda > numero:
    print("O maior do lado é:", esquerda)

elif direita > esquerda and direita > numero:
    print("O maior do lado é:", direita)

elif numero > esquerda and numero > direita:
    print("O número escolhido já é o maior:", numero)

else:
    print("Há empate entre os valores.")

print("O maior número da lista é:", max(lista))
