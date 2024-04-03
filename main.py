import random

from modules import banking_operations, user_operations

menu = """
#############################################
############ Banco Intergalático ############
#############################################

Seja Bem vindo, em que posso lhe ajudar hoje?

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

digite o número correspondente: """

balance = 0
limit_value_per_withdrawal = 500
WITHDRAWAL_LIMIT_PER_DAY = 3
withdrawals_realized = 0
statement = ""
users = []


def create_current_account():
  new_account = {}
  surprise_bonus = random.randint(10, 100)
  print(f"E para demonstrar a nossa alegrie em ter você conosco, você ganhou...\nR$ {surprise_bonus},00 !!!")
  new_account['balance'] = surprise_bonus
  pass

def fetch_users():
  pass

def account_stats():
  pass

while True:
  print(user_operations.create_user(users))

  option = input(menu)
  print("#############################################")
  if option == "1":
    output = banking_operations.deposit(balance, statement)
    balance = output['balance']
    statement = output['statement']
  elif option == "2":
    output = banking_operations.withdrawal(
      balance=balance,
      limit_value_per_withdrawal=limit_value_per_withdrawal,
      WITHDRAWAL_LIMIT_PER_DAY=WITHDRAWAL_LIMIT_PER_DAY,
      withdrawals_realized=withdrawals_realized,
      statement=statement,
      )
    balance = output['balance']
    withdrawals_realized = output['withdrawals_realized']
    statement = output['statement']
    
  elif option == "3":
    banking_operations.balance_query(balance, statement=statement)
  elif option == "0":
    print("Somos felizes por ver você crescer conosco.\nVolte sempre!!!")
    print("#############################################\n")
    break
  else :
    print("Por favor digite uma opção válida")