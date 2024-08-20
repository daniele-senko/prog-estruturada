val1 = int(input("Digite um valor: "))
val2 = int(input("Digite um segundo valor: "))

while val2 == 0:
    print("Valor invalido")
    val2 = int(input("Digite um segundo valor: "))

div = val1/val2
print(f'Resultado: {div}')