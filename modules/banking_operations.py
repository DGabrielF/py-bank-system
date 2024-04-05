from modules import validations


def deposit(balance, statement):
    print("Você selecionou a opção de Depósito")
    deposit_amount = input("Quanto você deseja depositar? ")
    if validations.number(deposit_amount):
      deposit_amount = float(deposit_amount)
      if deposit_amount > 0:
        balance += deposit_amount
        print(f"Você depositou R$ {deposit_amount:.2f}, seu saldo atual é R$ {balance:.2f}")
        statement += f"depósito de R$ {deposit_amount:.2f}\n"
        return {'balance': balance, 'statement': statement}
      else:
        print("O valor a ser depositado deve ser maior que zero")
    else:
      print("Por favor digite uma quantia válida")
    print("_" * 45, "\n")

def withdrawal(*, balance, limit_value_per_withdrawal, WITHDRAWAL_LIMIT_PER_DAY, withdrawals_realized, statement):
    print("Você selecionou a opção de Saque")
    withdrawal_amount = input("Quanto você deseja sacar? ")
    if withdrawals_realized < WITHDRAWAL_LIMIT_PER_DAY:
      if validations.number(withdrawal_amount):
        withdrawal_amount = float(withdrawal_amount)
        if withdrawal_amount < balance:
          if withdrawal_amount <= limit_value_per_withdrawal:
            balance -= withdrawal_amount
            print(f"Você sacou R$ {withdrawal_amount:.2f}, seu saldo atual é R$ {balance:.2f}")
            statement += f"saque de R$ {withdrawal_amount:.2f}\n"
            withdrawals_realized += 1
            return {'balance': balance, 'withdrawals_realized': withdrawals_realized, 'statement': statement}
          else:
            print("O valor a ser sacado não deve ser maior que o valor limite por saque")
        else:
          print("O valor a ser sacado não pode ser maior que o saldo")
      else:
        print("Por favor digite uma quantia válida")
    else:
      print("A quantidade de saques diários já chegou ao limite\nTente novamente amanhã ou entre em contato com a gerência")
    print("_" * 45, "\n")


def balance_query(balance, /, *, statement):
    print("Você selecionou a opção de Saque")
    print("\n################## EXTRATO ##################")
    print("Nenhuma movimentação realizada neste período." if not statement else statement)
    print(f"Saldo atual: R$ {balance:.2f}")
    print("#" * 45, "\n")
    print("_" * 45, "\n")

def start_operations(selected_account, *, operation_menu):
  while True:
    operation_option = input(operation_menu)
    print("#" * 45, "\n")
    # Depositar
    if operation_option == "1":
      output = deposit(selected_account['balance'], selected_account['statement'])
      if output:
        selected_account['balance'] = output['balance']
        selected_account['statement'] = output['statement']
    # Sacar
    elif operation_option == "2":
      output = withdrawal(balance=selected_account['balance'], limit_value_per_withdrawal=selected_account['account_type']['limit_value_per_withdrawal'], WITHDRAWAL_LIMIT_PER_DAY=selected_account['account_type']['withdrawal_limit_per_day'],
        withdrawals_realized=selected_account['withdrawals_realized'], statement=selected_account['statement'])
      if output:
        selected_account['balance'] = output['balance']
        selected_account['withdrawals_realized'] = output['withdrawals_realized']
        selected_account['statement'] = output['statement']
    # Extrato
    elif operation_option == "3":
      balance_query(selected_account['balance'], statement=selected_account['statement'])
    # Sair
    elif operation_option == "0":
      print("Somos felizes por ver você crescer conosco.\nVolte sempre!!!")
      print("#" * 45, "\n")
      break
    else :
      print("Por favor digite uma opção válida")
  return True
