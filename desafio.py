menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":       

        valor = float(input ("Informe o valor do depósito: "))

        while True:                    

            if float(valor) > 0:
                saldo = saldo + float(valor)
                extrato += f"Depósito: + R$ {valor:.2f}\n"
                break            
            else:                
                 valor = input ("Valor informado para depósito não é válido! \nInforme o valor do depósito ou digite [q] para voltar ao menu anterior: ")
                 if str(valor) == "q":
                    break

    elif opcao == "s":
         
        valor = float(input ("Informe o valor do saque: "))                                        

        while True:

            if numero_saques < LIMITE_SAQUES:
                if float(valor) <= limite:
                    if float(valor) <= saldo and float(valor) > 0:
                        saldo -= float(valor)
                        numero_saques += 1
                        extrato += f"Saque: - R$ {float(valor):.2f}\n"
                        break
                    else:
                        valor = input ("Valor informado não é válido ou saldo insuficiente! \nInforme o valor do saque ou digite [q] para voltar ao menu anterior: ")
                        if str(valor) == "q":
                            break     
                else:
                    valor = input ("Valor informado para saque excede o limite! \nInforme o valor do saque ou digite [q] para voltar ao menu anterior: ")
                    if str(valor) == "q":
                        break     
            else:
                print ("Limite de saques diários excedido. Tente novamente amanhã!")
                break
    
    elif opcao == "e":        
        if extrato == "":
            print ("Não foram realizadas movimentações")
        else:
            print ("###### EXTRATO ##########\n" + extrato + f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print ("Operação inválida, por favor seleciona novamente a operação desejada!")
    