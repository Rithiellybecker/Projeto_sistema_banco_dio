def sistema():
    
    saldo = 0
    extrato = []
    
    print("Escolha uma opção: ")
    
    opcao = -1
    
    while opcao != 0:
        
        opcao = int(input("\n [1] Depositar \n [2] Sacar \n [3] Ver extrato \n [0] Sair \n\n"))
        
        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            saldo += valor
            extrato.append(f"Deposito de: R$ {valor:.2f}") #.append modifica o valor do extrato
            print(f"Valor depositado: R$ {valor:.2f}") #.2f representa duas casas decimais depois da virgula
                    
        elif opcao == 2:
            saque = float(input("Digite o valor a ser sacado: "))
            if saque > saldo: #faz a verificação se a operação e verdadeira
                print("Saldo insuficiente!")
            else:
                saldo -= saque
                extrato.append(f"Saque: R$ {saque:.2f}")
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
            

3
sistema()

