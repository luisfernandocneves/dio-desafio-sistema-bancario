

def depositar(saldo, valor, extrato, /):        

    while True:                    

        if float(valor) > 0:
            saldo = saldo + float(valor)
            extrato += f"Depósito: + R$ {valor:.2f}\n"
            break            
        else:                
            valor = input ("Valor informado para depósito não é válido! \nInforme o valor do depósito ou digite [q] para voltar ao menu anterior: ")
            if str(valor) == "q":
                break
    
    return saldo, extrato

def sacar (*, saldo, valor, limite, limiteSaques, numero_saques, extrato):
        
    while True:

        if numero_saques < limiteSaques:
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
        
    return saldo, extrato, numero_saques

def visualizarExtrato(saldo, /, *, extrato):
    if extrato == "":
        print ("Não foram realizadas movimentações")
    else:
        print ("###### EXTRATO ##########\n" + extrato + f"\nSaldo: R$ {saldo:.2f}")

def validaCpf (cpf, usuarios):
    if not cpf.isdigit():
        return False, "CPF Inválido! Digite apenas os números do CPF "
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]    
    if usuarios_filtrados:
        return False, "CPF já cadastrado! "
    else:
        return True, ""

def criarUsuario (usuarios):    
    cpf = input ("Informe o CPF do usuário: ")
    
    while True:    
        valido, mensagem = validaCpf(cpf, usuarios)
        if not valido:
            cpf = input (mensagem + " ou digite [q] para voltar ao menu anterior: ")
            if str(cpf) == "q":
                break       
        else:
            nome = input ("Informe o Nome do usuário: ")
            dataNascimento = input ("Informe a Data de Nascimento do usuário (dd-mm-aaaa): ")
            endereco = input("Informe o endereço do usuário (logradouro, nro - bairro - cidade/sigla estado): ")
            
            usuarios.append({"nome": nome, "dataNascimento": dataNascimento, "cpf": cpf, "endereco": endereco})

            print("Usuário cadastrado com sucesso!")  
            break  

def listarUsuarios(usuarios):
    for usuario in usuarios:
        print (usuario)

def listarContas(contas):
    for conta in contas:
        print (conta)

def criarConta (agencia, contas, usuarios):    
    cpf = input ("Informe o CPF do usuário: ")
    
    while True:    
        usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        if not usuario:
            cpf = input ("Usuário não encontrado, digite um CPF válido ou digite [q] para voltar ao menu anterior: ")
            if str(cpf) == "q":
                break       
        else:
            conta = {"agencia": agencia, "numeroConta": len(contas) + 1, "usuario": usuario}
            
            contas.append(conta)

            print("Conta criada com sucesso!")  
            break  

def menu():
    menu = """

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [u] Cadastrar Usuarios
        [c] Criar Conta
        [lu] Listar Usuarios        
        [lc] Listar Contas
        [q] Sair

        => """
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"
    
    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input ("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)               
            
        elif opcao == "s":
            valor = float(input ("Informe o valor do saque: "))                                        
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, limite=limite, numero_saques=numero_saques, limiteSaques=LIMITE_SAQUES, extrato=extrato)    
                  
        elif opcao == "e":        
            visualizarExtrato(saldo, extrato=extrato)    
        elif opcao == "u":
            criarUsuario(usuarios)
        elif opcao == "lu":
            listarUsuarios(usuarios)
        elif opcao == "c":
            criarConta(AGENCIA, contas, usuarios)
        elif opcao == "lc":
            listarContas(contas)
        elif opcao == "q":
            break

        else:
            print ("Operação inválida, por favor seleciona novamente a operação desejada!")
    
    return menu

menu()