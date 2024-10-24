def menu ():
    menu = """\n
    ---------------------- MENU ----------------------

    [1] \tDepositar
    [2] \tSacar
    [3] \tExtrato
    [4] \tNova Conta
    [5] \tListar Contas
    [6] \tNovo Usuário
    [7] \tSair

    -------------------------------------------------
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
      if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n **** Depósito realizado com sucesso! ****")
      else:
        print("XXXX Operação falhou! O valor informado é inválido. XXXX")

      return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_valor_saque, numero_saques, LIMITE_SAQUES):
 
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_valor_saque
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
            print("XXXX Operação falhou! Você não tem saldo suficiente XXXX.")

    elif excedeu_limite:
            print("XXXX Operação falhou! O valor do saque excede o limite. XXXX")

    elif excedeu_saques:
            print("XXXX Operação falhou! Número máximo de saques excedido. XXXX")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n**** Saque realizado! ****")

    else:
            print("XXXX Operação falhou! O valor informado é inválido. XXXX")

    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
     
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def criar_usuario(usuarios):
    cpf= input(" Informe os 11 digitos do CPF (apenas números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("\n XXXX CPF já cadastrado! XXXX")
         return
     
    nome = input("\n informe seu nome completo: ")
    data_nascimento = input("\n informe sua data de nascimento (DD/MM/AAAA):")
    Endereço = input(" informe seu endereço completo (logradouro - N° - Bairro - Cidade/Estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "Endereço": Endereço})
    print(" **** Usuário cadastrado com sucesso! ****")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("informe o CPF do usuario:")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n**** conta criada com sucesso! ****")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print("\nXXXX Usuário não encontrado! XXXX")

def listar_contas(contas):
     for conta in contas:
            linha = f"""\
                Agência: \t{conta['agencia']}
                C/C: \t\t{conta['numero_conta']}
                Titular: \t{conta ['usuario']['nome']}
                """
            print("=" * 100)
            print(linha.strip(""))

def main():


    saldo = 0
    limite_valor_saque = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato =depositar(saldo, valor, extrato)
   
        elif opcao == "2":
        
         valor = float(input("Informe o valor do saque: "))

         saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_valor_saque=limite_valor_saque,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == "3":
        
         exibir_extrato (saldo, extrato=extrato)
        
        elif opcao == "4":
         
         numero_conta = len(contas) + 1
         conta = criar_conta(agencia, numero_conta, usuarios)

         if conta:
            contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)


        elif opcao == "6":
         criar_usuario(usuarios)
        

        elif opcao == "7":
         break

        else:
         print("Operação inválida, por favor selecione novamente a operação desejada.")

main()