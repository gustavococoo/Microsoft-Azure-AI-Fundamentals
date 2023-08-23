print(' BEM VINDO AO BANCO PYTHON ')

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ''
qtd_saques = 0
limite_saques = 3

while True:
    opção = int(input(f'Digite a opção: {menu}'))
    if opção == 1:
        valor = float(input('\nValor a ser depositado: R$'))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print('Valor informado inválido!')

    elif opção == 2:
        valor = float(input('\nInforme o valor a ser sacado: R$ '))
        passou_saldo = valor > saldo
        passou_limite = valor > limite
        passou_saques = qtd_saques >= limite_saques

        if passou_saldo:
            print('Saldo insuficiente!')
        elif passou_limite:
            print('O valor do saque excede o limite')
        elif passou_saques:
            print('Número de saques excedidos')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            qtd_saques += 1
        else:
            print('Operação inválida')
        
    elif opção == 3:
        print(' -=-=-=-=-=-=-= EXTRATO -=-=-=-=-=-=-=')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('-='*20)

    elif opção == 4:
        break

    else:
        print('Operação inválida, tente novamente!')

