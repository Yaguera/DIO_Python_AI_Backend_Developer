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
  
    if opcao == "s":
      valor_saque = float(input("Informe o valor que deseja sacar: "))
      saldo, extrato, saques = sacar(
        saldo=saldo,
        valor_saque=valor_saque,
        limite_saque=limite_saque,
        saques_por_dia=SAQUES_POR_DIA,
        saques=saques,
        extrato=extrato
      )
        
    
    if opcao == "e":
      print(f'============= EXTRATO =============')
      print(f"Saldo atual: {saldo}")
      print("============Atividades=============")
      print(f"Você realizou {depositos} deposito(s) e {saques} saque(s).")
      print("Não foram realizadas movimentações." if not extrato else extrato)
  
    if opcao == "q":
      break
main()
