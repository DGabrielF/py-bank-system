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
        if withdrawal_amount <= limit_value_per_withdrawal:
          if withdrawal_amount < balance:
            balance -= withdrawal_amount
            print(f"Você sacou R$ {withdrawal_amount:.2f}, seu saldo atual é R$ {balance:.2f}")
            statement += f"saque de R$ {withdrawal_amount:.2f}\n"
            withdrawals_realized += 1
            return {'balance': balance, 'withdrawals_realized': withdrawals_realized, 'statement': statement}
        else:
          print("O valor a ser sacado não deve ser maior que o valor limite por saque")
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

