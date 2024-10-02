import datetime

def sistema():
    
    saldo = 0
    extrato = []
    limite_saque = 500  # Limite máximo por saque
    numero_saques = 0  # Número de saques realizados no dia
    numero_deposito = 0
    max_operacao = 10 
    
    print("Escolha uma opção: ")
    
    opcao = -1
    
    while opcao != 0:
        
        opcao = int(input("\n [1] Depositar \n [2] Sacar \n [3] Ver extrato \n [0] Sair \n\n"))
        
        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
        
            if numero_deposito >= max_operacao: 
                print("Número máximo de operações atingido para hoje.")
    
            elif valor <= 0:  # Verifica se o valor é negativo ou zero
                print("Depósito inválido! O valor deve ser maior que R$ 0,00.")
            else:
                saldo += valor
                now = datetime.datetime.now()  # Define a variável now
                extrato.append(f"Deposito de R$ { valor:.2f} em {now.strftime('%d-%m-%y %H:%M')}")
                numero_deposito += 1
                print(f"Valor depositado: R$ {valor:.2f}")#.2f representa duas casas decimais depois da virgula
        
        elif opcao == 2:
            if numero_saques >= max_operacao:
                print("Número máximo de operações atingido para hoje.")
            else:
                saque = float(input("Digite o valor a ser sacado: "))
                if saque > saldo:
                    print("Saldo insuficiente!")
                elif saque > limite_saque:
                    print(f"Valor máximo para saque é R$ {limite_saque:.2f}.")
                else:
                    saldo -= saque
                    now = datetime.datetime.now()  # Define a variável now
                    extrato.append(f"Saque de R$ {saque:.2f} em {now.strftime('%d-%m-%y %H:%M')}")
                    numero_saques += 1 
                    print(f"Valor sacado: R$ {saque:.2f}")
                    
            
        elif opcao == 3:
            print("\n --- Extrato ---")
            if not extrato:
                print("Nenhuma transação realizada.")
            else:  
                for transacao in extrato:
                    print(transacao)
            print(f"Saldo atual: R$ {saldo:.2f}")
            
        elif opcao == 0:
            print("Saindo...")
        else:
            print("Opção inválida! Tente novamente.")
            
            
sistema()

