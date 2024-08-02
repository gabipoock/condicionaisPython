#Desenvolva um programa que verifica se uma palavra é um palíndromo (uma
#palavra que se lê da mesma forma de trás para frente) usando a estrutura if.

palavra = input("Oiee! Digite uma palavra para saber se ela é um palíndromo: ").strip()

if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")