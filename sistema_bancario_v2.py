from datetime import datetime
import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo,valor_deposito,depositos,extrato, /):
    if valor_deposito > 0:
        data_e_hora_atuais = datetime.now()
        data_atual = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        saldo += valor_deposito
        depositos += 1
        extrato += f"Deposido no valor de R${valor_deposito:.2f} realizado no dia {data_atual}\n"
        print(f"Deposito no valor de R${valor_deposito:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, depositos

def sacar(*, saldo, valor_saque, limite_saque, saques_por_dia, saques, extrato):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite_saque
    excedeu_saques = saques >= saques_por_dia
    data_e_hora_atuais = datetime.now()
    data_atual = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

    if excedeu_saldo:
      print("Você não possui saldo suficiente")
    elif excedeu_limite:
      print("Valor limite de saque atingido.")
    elif excedeu_saques:
      print("Número de saques diários atingido.")
    elif saldo > 0:
      saldo -= valor_saque
      saques += 1
      extrato += f"Saque no valor de R${valor_saque:.2f} realizado no dia {data_atual}\n"
      print(f"Saque no valor de R${valor_saque:.2f} realizado com sucesso. {saques}") 
    else:
      print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, saques

def exibir_extrato(saldo,depositos,saques, /, *,extrato):
    print(f'============= EXTRATO =============')
    print(f"Saldo atual: {saldo}")
    print("============Atividades=============")
    print(f"Você realizou {depositos} deposito(s) e {saques} saque(s).")
    print("Não foram realizadas movimentações." if not extrato else extrato)

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("CPF já cadastrado.")
        return

    nome = input("Informe seu nome completo")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f"Usuario {nome} criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        numero_conta = len(contas) + 1
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario não encontrado!")

def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
        return
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
  SAQUES_POR_DIA = 3
  AGENCIA = "0001"
  
  saldo = 0
  extrato = ""
  depositos = 0
  saques = 0
  limite_saque = 500
  contas = []
  usuarios = []
  
  while True:
    opcao = menu()
    
    if opcao == "d":
      valor_deposito = float(input("Informe o valor do deposito: "))
      saldo,extrato,depositos = depositar(saldo, valor_deposito, depositos, extrato)
  
    elif opcao == "s":
      valor_saque = float(input("Informe o valor que deseja sacar: "))
      saldo, extrato, saques = sacar(
        saldo=saldo,
        valor_saque=valor_saque,
        limite_saque=limite_saque,
        saques_por_dia=SAQUES_POR_DIA,
        saques=saques,
        extrato=extrato
      )
        
    
    elif opcao == "e":
      exibir_extrato(saldo,depositos,saques,extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        nova_conta = criar_conta(AGENCIA, contas, usuarios)
        contas.append(nova_conta)

    elif opcao == "lc":
        listar_contas(contas)
    
    elif opcao == "q":
      break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
main()
