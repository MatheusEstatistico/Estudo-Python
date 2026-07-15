import random

jogador_vence = 0
pc_vence = 0
opcoes = ['pedra', 'papel', 'tesoura']

while True: 
    jogador_input = input('Escreva Pedra/Papel/Tesoura ou Q para saír: ').lower()
    if jogador_input == 'q':
        break
    
    if jogador_input not in opcoes:
        continue

    numero = random.randint(0, 2)
    # pedra: 0, papel: 1, tesoura: 2
    pc_escolhe = opcoes[numero]
    print('O computador escolheu:', pc_escolhe + '.')

    if jogador_input == 'pedra' and pc_escolhe == 'tesoura':
        print('Você venceu!')
        jogador_vence += 1
        print(f'''
        Jogador | Computador
           {jogador_vence}    |    {pc_vence}\n
        ''')
    elif jogador_input == 'papel' and pc_escolhe == 'pedra':
        print('Você venceu!')
        jogador_vence += 1
        print(f'''
        Jogador | Computador
           {jogador_vence}    |    {pc_vence}\n
        ''')
    elif jogador_input == 'tesoura' and pc_escolhe == 'papel':
        print('Você venceu!')
        jogador_vence += 1
        print(f'''
        Jogador | Computador
           {jogador_vence}    |    {pc_vence}\n
        ''')
    elif jogador_input == pc_escolhe:
        print('Empate')
        print(f'''
        Jogador | Computador
           {jogador_vence}    |    {pc_vence}\n
        ''')
    else:
        print('Você perdeu!')
        pc_vence += 1
        print(f'''
        Jogador | Computador
           {jogador_vence}    |    {pc_vence}\n
        ''')

print(f'''O placar final é: 
    Jogador | Computador
       {jogador_vence}    |    {pc_vence}
''')
print('Até logo!\n')
