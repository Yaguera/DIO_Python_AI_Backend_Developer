from datetime import datetime
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
depositos = 0
saques = 0
limite_saque = 500
SAQUES_POR_DIA = 3

while True:
  opcao = input(menu).lower()
  
  if opcao == "d":
    valor_deposito = float(input("Digite o valor do deposito: "))
    if valor_deposito > 0:
        data_e_hora_atuais = datetime.now()
        data_atual = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        depositos += 1
        saldo += valor_deposito
        extrato += f"Deposido no valor de R${valor_deposito:.2f} realizado no dia {data_atual}\n"
        print(f"Deposito de R${valor_deposito:.2f} realizado com sucesso")
    else:
        print("Falha na operação. Digite um valor válido.")

  if opcao == "s":
    if saques < SAQUES_POR_DIA:
        if saldo > 0:
          valor_saque = float(input("Digite o valor do saque: "))
          if valor_saque <= saldo:
            data_e_hora_atuais = datetime.now()
            data_atual = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
            saques += 1
            saldo -= valor_saque
            extrato += f"Saque no valor de R${valor_saque:.2f} realizado no dia {data_atual}\n"
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso. {saques}")
          else: print(f"Saldo insuficiente. Você possui R${saldo:.2f}")
        else:
          print("Saldo zerado.")
    else:
        print("LIMITE DE SAQUE DIÁRIO ATINGIDO.")
  
  if opcao == "e":
    print(f'============= EXTRATO =============')
    print(f"Saldo atual: {saldo}")
    print("============Atividades=============")
    print(f"Você realizou {depositos} deposito(s) e {saques} saque(s).")
    print("Não foram realizadas movimentações." if not extrato else extrato)

  if opcao == "q":
    break
