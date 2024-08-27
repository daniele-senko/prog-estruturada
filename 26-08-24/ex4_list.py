'''. Reescreva o programa anterior para que no final seja impressa a mensagem: "Novo cálculo
(1.sim 2.não)" solicitando ao usuário que informe um código (1 ou 2) indicando se ele
deseja ou não executar o programa novamente. Se for informado o código 1 deve ser
repetida a execução de todo o programa para permitir um novo cálculo, caso contrário ele
deve ser encerrado.'''

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

# perguntar se deseja calcular novamente
while True: 
    escolha = int(input("Novo cálculo (1. Sim, 2.Não): "))
    if escolha == 2:
        print ("Programa encerrado.")
        break
    elif escolha != 1:
        print("Opção inválida. Por favor, digite 1 ou 2.")