from textwrap import dedent

def menu():
    print ("\n","MENU".center(40, "="))
    menu = ("""
    O que gostaria de fazer hoje?
    =============================

    [d] - Depósito
    [s] - Saque
    [e] - Extrato
    [nu] - Novo Usuário
    [nc] - Nova Conta
    [lc] - Listar Contas
    [q] - Sair

    =============================
    Escolha a operação: """) 

    return input(dedent(menu))


def deposito(saldo, valor, extrato, /):
    if (valor > 0):
        saldo += valor
        extrato += f"Você depositou: R${deposito:,.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_de_saques, limite_saque):
    if (numero_de_saques >= limite_saque):
        print ("\n","Saque".center(40, "="))

        print ("\n@@@ Limite de saques foi excedido @@@")

    else:
        print ("\n","Saque".center(40, "="))
        valor = float(input("\nDigite o valor a ser sacado: "))

        if (valor > saldo):
            print ("\n@@@ Saldo insuficiente para saque! @@@")
                
        elif (valor > limite):
            print ("\n@@@ Valor de saque excedeu o limite@@@")

        else:
            numero_de_saques += 1
            extrato += f"Saque feito de: R${saque:,.2f}\n"
            print ("\n === Saque efetuado com sucesso! ===")
            saldo = saldo - valor
    
    return saldo, extrato
   

def exibir_extrato(saldo, /, *, extrato):
    print ("\n","Extrato".center(40, "="))
    print ("Não houve movimentações na conta" if not extrato else extrato) 
    print ("--------------------------------------")
    print (f"Seu saldo atual é de: {saldo:,.2f}") 
    print ("======================================")


def criar_usuario(usuarios):
    print ("\n","Criação de Usuário".center(40, "="))

    cpf = input("\nDigite seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Digite o seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (logradouro, nro - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        
    print ("=== Usuário criado com sucesso! ===")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    print ("\n","Criação de Conta".center(40, "="))

    cpf = input("\nDigite o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while (True):

        opcao = menu()
    
        if (opcao == "d"):
            print ("\n","Depósito".center(40, "="))

            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif (opcao == "s"):    
            print ("\n","Saque".center(40, "="))

            valor = float(input("Digite o valor a ser depositado: "))
            saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_de_saques = numero_saques,
                limite_saque = LIMITE_SAQUES
            )

        elif (opcao == "e"):
            exibir_extrato(saldo, extrato = extrato)

        elif (opcao == "nu"):
            criar_usuario(usuarios)

        elif (opcao == "nc"):
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif (opcao == "lc"):
            listar_contas(contas)

        elif (opcao == "q"):
            print ("\nAtendimento finalizado")
            break

        else:
            print ("\n@@@ Operação inválida, por favor coloque uma opção válida")


main()
