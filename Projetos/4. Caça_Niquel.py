import random

MAX_LINHAS = 3
MIN_APOSTA = 1
MAX_APOSTA = 100

ROWS = 3
COLS = 3

simbolos_cont = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

simbolo_valor = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def verificar_vitorias(colunas, linhas, aposta, valores):
    vencidas = 0
    vencidas_linhas = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            simbolo_verificar = coluna[linha]
            if simbolo != simbolo_verificar:
                break
        else:
            vencidas += valores[simbolo] * aposta
            vencidas_linhas.append(linha + 1)
    return vencidas, vencidas_linhas

def get_caca_niquel_spin(rows, cols, simbolos):
    todos_simbolos = []
    for simbolo, simbolos_cont in simbolos.items():
        for _ in range(simbolos_cont):
            todos_simbolos.append(simbolo)
    colunas = []
    for _ in range(cols):
        coluna = []
        atuais_simbolos = todos_simbolos[:]
        for _ in range(rows):
            valor = random.choice(atuais_simbolos)
            atuais_simbolos.remove(valor)
            coluna.append(valor)
        colunas.append(coluna)
    return colunas

def print_caca_niquel(colunas):
    for row in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) - 1:
                print(coluna[row], end=" | ")
            else:
                print(coluna[row], end="")
        print()

def deposito():
    while True:
        quantia = input('Faça um novo depósito: ')
        if quantia.isdigit():
            quantia = int(quantia)
            if quantia > 0:
                break
            else:
                print('O depósito tem que ser maior que 0.')
        else:
            print('Por favor digite um número.')
    return quantia

def get_linhas():
    while True:
        linhas = input('Insira o número de linhas em que deseja apostar (1-' + str(MAX_LINHAS) + ') ')
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                break
            else:
                print('Digite um número válido de linhas.')
        else:
            print('Por favor digite um número.')
    return linhas

def get_aposta():
    while True:
        quantia = input('Quanto quer apostar em cada linha? ')
        if quantia.isdigit():
            quantia = int(quantia)
            if MIN_APOSTA <= quantia <= MAX_APOSTA:
                break
            else:
                print(f'A aposta deve estar entre R${MIN_APOSTA} e R${MAX_APOSTA}')
        else:
            print('Por favor digite um número.')
    return quantia

def girar(carteira):
    linhas = get_linhas()
    while True:
        aposta = get_aposta()
        aposta_total = aposta * linhas
        if aposta_total > carteira:
            print(f'Você não tem esse valor para apostar. Sua carteira possui R${carteira}')
        else:
            break
    print(f'Você está apostando R${aposta} em {linhas} linhas.\nO total da aposta é R${aposta_total}')

    slots = get_caca_niquel_spin(ROWS, COLS, simbolos_cont)
    print_caca_niquel(slots)
    vencidas, vencidas_linhas = verificar_vitorias(slots, linhas, aposta, simbolo_valor)
    if vencidas > 0:
        print(f'Você ganhou R${vencidas}.')
        print(f'Você ganhou na linha:', *vencidas_linhas)
    else:
        print('Você perdeu :(')
    if vencidas <= 0:
        sobra = vencidas - aposta_total
    else:
        sobra = vencidas
    return sobra

def main():
    carteira = deposito()
    while True:
        print(f'Seu saldo atual é R${carteira}')
        resposta = input('Aperte enter para jogar ou q para sair.')
        if resposta == 'q':
            break
        carteira += girar(carteira)
    print(f'Você ainda tem R${carteira}\n')
        
main()
