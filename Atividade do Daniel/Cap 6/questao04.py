#Faça um programa que preencha um vetor com quinze elementos inteiros e 
#verifique a existência de elementos iguais a 30, 
#mostrando as posições em que apareceram.

mostNum30 : int
cont30 : int
numeros = []
cont30 = 0

for n in range (0, 2):
    numeros.append(str("Insira o número: "))

    if numeros[n] == 30:
        cont30 += 1
        mostNum30.append(numeros[n])
        print("Entrou")

    print(F"A quabtidade de vezes em que o 30 aparece são de {cont30} vezes!")


