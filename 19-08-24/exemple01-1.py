# deepseek
#1) Para que a divisão entre 2 números possa ser realizada, o divisor não pode ser nulo (zero). Escreva um programa para ler 2 valores e imprimir o resultado da divisão do primeiro pelo segundo. OBS: O programa deve validar a leitura do segundo valor (que não deve ser nulo). Enquanto for fornecido um valor nulo a leitura deve ser repetida. Utilize a estrutura while na construção da repetição de validação.
#2) Altere a solução do exercício anterior para que seja impressa a mensagem "Valor inválido!" caso o segundo valorinformado seja zero.

val1 = int(input("Digite um valor: "))
val2 = int(input("Digite um segundo valor: "))

while val2 == 0:
    print("Valor invalido")
    val2 = int(input("Digite um segundo valor: "))

div = val1/val2
print(f'Resultado: {div}')