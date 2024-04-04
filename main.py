from modules import banking_operations, user_operations

bank_logo = """
#############################################
############ Banco Intergalático ############
#############################################
"""
login_menu = f"""
{bank_logo}

Seja Bem vindo

[1] Entrar
[2] Cadastrar
[3] Recuperar senha
[0] Sair

digite o número correspondente: """




balance = 0
account_type = [
  {"name": "silver", "limit_value_per_withdrawal": 500, "withdrawal_limit_per_day": 3, },
  {"name": "gold", "limit_value_per_withdrawal": 1000, "withdrawal_limit_per_day": 5},
  {"name": "platinum", "limit_value_per_withdrawal": 2500, "withdrawal_limit_per_day": 8},
  {"name": "black", "limit_value_per_withdrawal": 3500, "withdrawal_limit_per_day": 12},
]
limit_value_per_withdrawal = 500
WITHDRAWAL_LIMIT_PER_DAY = 3
withdrawals_realized = 0
statement = ""
users = []
current_accounts = []


def start_operations(user):
  operation_menu = f"""
  {bank_logo}

  Certo, o que você deseja fazer?

  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair

  digite o número correspondente: """

  while True:
    operation_option = input(operation_menu)
    print("#" * 45, "\n")
    if operation_option == "1":
      output = banking_operations.deposit(user['balance'], user['statement'])
      user.balance = output['balance']
      user.statement = output['statement']
    elif operation_option == "2":
      output = banking_operations.withdrawal(balance=user['balance'], limit_value_per_withdrawal=user['limit_value_per_withdrawal'], WITHDRAWAL_LIMIT_PER_DAY=WITHDRAWAL_LIMIT_PER_DAY,
        withdrawals_realized=withdrawals_realized, statement=statement)
      balance = output['balance']
      withdrawals_realized = output['withdrawals_realized']
      statement = output['statement']
      
    elif operation_option == "3":
      banking_operations.balance_query(balance, statement=statement)
    elif operation_option == "0":
      print("Somos felizes por ver você crescer conosco.\nVolte sempre!!!")
      print("#" * 45, "\n")
      break
    else :
      print("Por favor digite uma opção válida")
  return True


while True:
  login_option = input(login_menu)
  if login_option == "1":
    user_operations.login_user(users, bank_logo=bank_logo)
  elif login_option == "2":
    users.append(user_operations.create_user(users))
  elif login_option == "3":
    pass
  elif login_option == "0":
    print("Somos felizes por ver você crescer conosco.\nVolte sempre!!!")
    print("#" * 45, "\n")
    break
  else :
    print("Por favor digite uma opção válida")
