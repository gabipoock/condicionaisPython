#Crie um programa que exibe a tabuada de um número escolhido pelo usuário utilizando
#a estrutura for.

print('//CALCULADORA DE TABUADA//')
numero = int(input("Oioii! Digite um número para ver a sua tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print('Essa é a tabuada do número', numero)