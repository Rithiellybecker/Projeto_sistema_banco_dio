import datetime 
import textwrap
import time

def menu():
    menu = """\n
    [1] Depositar 
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Listar Contas
    [6] Novo usuário
    [0] Sair 
    --> """ 
    return input(menu)

def depositar(saldo, valor, extrato, LIMITE_OPERACOES, numero_saque, numero_deposito):
    if numero_deposito >= LIMITE_OPERACOES:
        print("Limite de operações de depósito atingido.")
        return saldo, extrato, numero_deposito, numero_saque
    
    if valor > 0:
        saldo += valor
        now = datetime.datetime.now()
        extrato.append(f"Depósito de R$ {valor:.2f} em {now.strftime('%d-%m-%Y %H:%M')} \n")
        numero_deposito += 1
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_deposito, numero_saque

def sacar(numero_saque, LIMITE_OPERACOES, saldo, extrato, numero_deposito, valor):
    if numero_saque >= LIMITE_OPERACOES:
        print("Limite de operações de saque atingido.")
        return saldo, extrato, numero_deposito, numero_saque
    
    if valor > 0 and valor <= saldo:
        saldo -= valor
        now = datetime.datetime.now()
        extrato.append(f"Saque de R$ {valor:.2f} em {now.strftime('%d-%m-%Y %H:%M')} \n") 
        numero_saque += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Verifique o saldo e o valor do saque. @@@")
    
    return saldo, extrato, numero_deposito, numero_saque 

def exibir_extrato(saldo, extrato):
    if not extrato:
        print("\nNão foram realizadas movimentações.\n")
    else:
        print("\nExtrato:")
        print(extrato)
        print(f"\nSaldo atual: R${saldo:.2f}\n")
        
def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:  # Verifica se o usuário foi encontrado
        nova_conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
        print("\n=== Conta criada com sucesso! ===")
        return nova_conta  # Retorna a nova conta

    print("CPF não encontrado")  # Mensagem se o CPF não for encontrado
    return None  # Retorna None se a conta não for criada

def listar_contas(contas):
    if contas:
        print("\nContas cadastradas:")
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Número da conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
    else:
        print("\nNenhuma conta cadastrada.")
    
def main():
    LIMITE_OPERACOES = 10
    AGENCIA = "0001"
    numero_conta = 1  # Inicia o número da conta
    numero_saque = 0
    numero_deposito = 0
    saldo = 0.0
    extrato = []
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
    
        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato, numero_deposito, numero_saque = depositar(saldo, valor, extrato, LIMITE_OPERACOES, numero_saque, numero_deposito)
            except ValueError:
                print("Por favor, insira um valor numérico.")
            
        elif opcao == "2":
            try:
                valor = float(input("Informe o valor que deseja sacar: "))
                saldo, extrato, numero_deposito, numero_saque = sacar(numero_saque, LIMITE_OPERACOES, saldo, extrato, numero_deposito, valor)
            except ValueError:
                print("Por favor, insira um valor numérico.")
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
            
        elif opcao == "4":
            nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)  # Chama a função para criar conta
            if nova_conta:  # Verifica se a conta foi criada
                contas.append(nova_conta)  # Adiciona a nova conta à lista de contas
                numero_conta += 1  # Incrementa o número da conta
                
        elif opcao == "5":
            listar_contas(contas)
            
        elif opcao == "6":
            novo_usuario(usuarios)
            
        elif opcao == "0":
            print("Saindo...")
            time.sleep(1)  # Atraso para melhor visualização da mensagem
            break
            
        else: 
            print("Opção inválida. Tente novamente.")

main()
