from datetime import date

# Função para verificar se um ano é bissexto
def is_bissexto(ano):
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

# Função para calcular o número de dias em um mês, levando em conta anos bissextos
def dias_no_mes(mes, ano):
    if mes == 2:  # Fevereiro
        return 29 if is_bissexto(ano) else 28
    elif mes in [4, 6, 9, 11]:  # Abril, Junho, Setembro, Novembro
        return 30
    else:  # Todos os outros meses
        return 31

# Função para calcular o número de dias entre duas datas
def dias_entre_datas(d1, m1, a1, d2, m2, a2):
    data_inicio = date(a1, m1, d1)
    data_fim = date(a2, m2, d2)
    return (data_fim - data_inicio).days

# Função principal que lê e processa as entradas
def main():
    while True:
        # Lendo as duas datas
        entrada = input("Digite as duas datas (dia1 mês1 ano1 dia2 mês2 ano2): ")
        dia1, mes1, ano1, dia2, mes2, ano2 = map(int, entrada.split())
        
        # Se o dia for negativo, interrompe o loop
        if dia1 < 0:
            break
        
        # Calculando o número de dias entre as duas datas
        dias_decorridos = dias_entre_datas(dia1, mes1, ano1, dia2, mes2, ano2)
        
        # Imprimindo o resultado
        print(f"Número de dias decorridos: {dias_decorridos}")

# Executando o programa
main()
