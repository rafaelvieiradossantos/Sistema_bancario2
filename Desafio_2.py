# Este é um sistema bancario.
import textwrap

def menu():
    menu = """
    ------------------
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar contas
    [nu] Novo Usuario
    [q] Sair
    ------------------
    """
    return input(textwrap.dedent(menu))

def deposito(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n=== Operação falhou! ===")

    return saldo,extrato

def saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    exceder_saldo = valor > saldo
    exceder_limite =  valor > limite
    exceder_saques = numero_saques > limite_saques
    if excedeu_saldo:
        print("Operação falhou !!! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou !!! Você execedeu o saque limite.")

    elif excedeu_saques:
        print("Operação falhou !!! Numero máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:  R$ {valor:.2}\n"
        numero_saques+=1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou !!! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("======= EXTRATO =======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (CEP): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta,usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            Conta corrente: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
    """
    print("="* 20)
    print(textwrap.dedent(linha))

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do Deposito: "))

            saldo, extrato = deposito(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação invalida, informe uma opção válida.")


main()
