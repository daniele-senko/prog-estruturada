''' Escreva um programa para ler as notas da 1ª e 2ª avaliações de um aluno, calcular e
imprimir a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota
válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.
Deve ser impressa a mensagem "Nota inválida" caso a nota informada não pertença ao
intervalo [0,10]. '''

def ler_nota():
    while True: 
        nota = float(input("Digite a nota da avaliação (de 0 a 10): "))
        if 0 <= nota <= 10: 
            return nota
        else: 
            print("Nota inválida. Por favor, a nota deve ser de 0 a 10.")

#ler notas
nota1 = ler_nota()
nota2 = ler_nota()

#calcular média 
media = (nota1 + nota2)/2
print("A média semestral é: ", media)
        