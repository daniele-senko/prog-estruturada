precos = [100, 200, 300, 400, 500]

#filtrar os precos menores que 300 e exibir em uma nova lista
precos_baixos = list(filter(lambda x: x < 300, precos))

print(precos_baixos)