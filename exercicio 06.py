numero = int(input("digite um numero"))
print(f"\nNúmeros ímpares de 1 ate {numero}:\n")
for i in range (1,numero + 1):
    if i % 2 !=0:
        print(i)