menu = """
#############################################
############ Banco Intergalático ############
#############################################
Seja Bem vindo, em que posso lhe ajudar hoje?

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

balance = 0
limit_value_per_withdrawal = 500
WITHDRAWAL_LIMIT_PER_DAY = 3
withdrawals_realized = 0
statement = ""

def number_validation(input):
  try:
    float(input)
    return True
  except ValueError:
    return False

while True:
  option = input(menu)
  print("#############################################")
  if option == "1":
    print("Você selecionou a opção de Depósito")
    deposit_amount = input("Quanto você deseja depositar? ")
    if number_validation(deposit_amount):
      deposit_amount = float(deposit_amount)
      if deposit_amount > 0:
        balance += deposit_amount
        print(f"Você depositou R$ {deposit_amount:.2f}, seu saldo atual é R$ {balance:.2f}")
        statement += f"depósito de R$ {deposit_amount:.2f}\n"
      else:
        print("O valor a ser depositado deve ser maior que zero")
    else:
      print("Por favor digite uma quantia válida")
    print("#############################################\n")

  elif option == "2":
    print("Você selecionou a opção de Saque")
    withdrawal_amount = input("Quanto você deseja sacar? ")
    if withdrawals_realized < WITHDRAWAL_LIMIT_PER_DAY:
      if number_validation(withdrawal_amount):
        withdrawal_amount = float(withdrawal_amount)
        if withdrawal_amount <= limit_value_per_withdrawal:
          if withdrawal_amount < balance:
            balance -= withdrawal_amount
            print(f"Você sacou R$ {withdrawal_amount:.2f}, seu saldo atual é R$ {balance:.2f}")
            statement += f"saque de R$ {withdrawal_amount:.2f}\n"
            withdrawals_realized += 1
        else:
          print("O valor a ser sacado não deve ser maior que o valor limite por saque")
      else:
        print("Por favor digite uma quantia válida")
    else:
      print("A quantidade de saques diários já chegou ao limite, tente novamente amanhã ou entre em contato com a gerência")
    print("#############################################\n")
    
  elif option == "3":
    print("Você selecionou a opção de Saque")
    print("\n################## EXTRATO ##################")
    print("Nenhuma movimentação realizada neste período." if not statement else statement)
    print(f"Saldo atual: R$ {balance:.2f}")
    print("\n#############################################")
  elif option == "0":
    print("Somos felizes por você crescer conosco.\nVolte sempre!!!")
    print("#############################################\n")
    break
  else :
    print("Por favor digite uma opção válida")