#Crie um programa que calcula a soma de todos os números em uma lista usando a estrutura for.

print('//SOMA DE UMA LISTA DE NÚMEROS//')
lista = []

for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    lista.append(num)

soma = 0

for numero in lista:
    soma += numero

print(f"A soma dos 5 números que você escolheu é: {soma} :)")