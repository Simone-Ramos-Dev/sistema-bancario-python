import datetime

# Inicializa as variáveis do sistema
saldo = 0.0
extrato = []

def deposito(valor):
    """Realiza um depósito se o valor for positivo."""
    global saldo
    if valor > 0:
        saldo += valor
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato.append({"tipo": "deposito", "valor": valor, "data": data_hora})
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def saque(valor):
    """Realiza um saque se as condições de saldo e limite forem atendidas."""
    global saldo
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > 0:
        saldo -= valor
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato.append({"tipo": "saque", "valor": valor, "data": data_hora})
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    """Exibe o histórico de transações de depósito e o saldo atual."""
    print("\n================ EXTRATO ================")
    
    depositos_encontrados = False
    for operacao in extrato:
        if operacao["tipo"] == "deposito":
            print(f"Depósito: R$ {operacao['valor']:.2f}")
            depositos_encontrados = True
    
    if not depositos_encontrados:
        print("Não foram realizados depósitos.")
    
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def menu():
    """Exibe o menu de opções e processa a escolha do usuário."""
    menu_string = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

    while True:
        opcao = input(menu_string).lower().strip()
        
        try:
            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                deposito(valor)
            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                saque(valor)
            elif opcao == "e":
                exibir_extrato()
            elif opcao == "q":
                print("Obrigado por usar nosso sistema bancário. Até mais!")
                break
            else:
                print("Operação inválida, por favor selecione a operação desejada.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Inicia o programa
if __name__ == "__main__":
    menu()