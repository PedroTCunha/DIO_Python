SENHA = "0000"
saldo = float(2000)
processo = ""
saque = 0
saques_feitos = 0
LIMITES_SAQUE = 3
extrato = ""
deposito = 0


senha_digi = input("Digite sua senha: ")

while (processo != "q"):
    if (SENHA == senha_digi):
        print ("\nSeja bem vindo ao Banco Teófilo".center(20))

        print (f"""\n
        O que gostaria de fazer hoje?
        =============================

        [d] - Depósito
        [s] - Saque
        [e] - Extrato
        [q] - Sair

        =============================
        """)
    
        processo = input("Escolha o processo: ")
    

        if (processo == "d"):
            print ("\n","Depósito".center(40, "="))

            deposito = float(input("\nDigite o valor a ser depositado: "))

            extrato += f"Você depositou: R${deposito:,.2f}\n"
            saldo = saldo + deposito
            processo = ""
        

        elif (processo == "s"):
                
            if (saques_feitos >= LIMITES_SAQUE):
                print ("\n","Saque".center(40, "="))

                print ("""\n
                =====================================
                Você não pode fazer mais saques hoje!
                =====================================
                       """)
                processo = ""
            else:
                print ("\n","Saque".center(40, "="))
                saque = float(input("\nDigite o valor a ser sacado: "))
                valor_saque = saque

                if (valor_saque > saldo):
                    print ("\nSaldo insuficiente para saque!")
                    processo = ""
                
                elif (valor_saque > 500):
                    print ("\nValor alto para saque")
                    processo = ""

                else:
                    saques_feitos += 1
                    extrato += f"Saque feito de: R${saque:,.2f}\n"
                    saldo = saldo - saque
                    processo = ""


        elif (processo == "e"):
            print ("\n","Extrato".center(40, "="))
            print ("Não houve movimentações na conta" if not extrato else extrato) 
            print ("--------------------------------------")
            print (f"Seu saldo atual é de: {saldo:,.2f}") 
            print ("======================================")
            processo = ""

    else:
        print ("\nSenha incorreta! Atendimento finalizado")
        break

else:
    print("\nAtendimento finalizado!\n")