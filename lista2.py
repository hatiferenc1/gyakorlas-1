import random
lista = []
for i in range(10):
    a = random.randint(1,10)
    lista.append(a)
print(lista)

összeg = 0
for szam in lista:
    összeg = összeg + szam
print(összeg)  