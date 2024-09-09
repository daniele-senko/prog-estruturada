frutas = ["Abacaxi", "Banana", "Caju", "Damasco", "Figo", "Graviola"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
dados = ["Carlos", 19, True, "Pedro", "Ana", 1.78, 2001]

#declaração de maneira explicita

a = list(range(10))
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = list()
# a = []

empresas = list(["Toyota", "Volkswagen", "Ford"])
# empresas = ["Toyota", "Volkswagen", "Ford"]

unemat = list("UNEMAT")
# unemat = ["U", "N", "E", "M", "A", "T"]

#-------#

# Acessando elementos de uma lista

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]	
print(letras[0]) # A

# i-ésimo elemento

print(letras[8-1]) # H

#podem ser acessadas de forma negativa

print (letras[-8]) # A
print(letras[-1]) # H

#-------#

#TAMANHO DA LISTA


frutas = ["Abacaxi", "Banana", "Caju", "Damasco", "Figo", "Graviola"]
numeros = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]

print(len(frutas)) # 6
print(len(numeros)) # 11
print(len(letras)) # 8

#-------#

#SELECIONANDO INTERVALOS DA LISTA

lista[start:stop:step]

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Selecionando do segundo até o quarto elemento
print(letras[1:4]) # ['B', 'C', 'D'] 

# Selecionando os três primeiros elementos
print(letras[:3]) # ['A', 'B', 'C']

# Selecionando os quatros ultimos elementos
print(letras[-4:]) # ['E', 'F', 'G', 'H']

# Elementos pares da lista
print(letras[::2]) # ['A', 'C', 'E', 'G']

# Obtendo os elementos em ordem inversa
print(letras[::-1]) # ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
