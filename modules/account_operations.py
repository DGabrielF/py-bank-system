
import random

from modules import banking_operations

def fetch_accounts(user, current_accounts):
  while True:
    user_accounts = []
    for acc in current_accounts:
      if acc['user_cpf'] == user['cpf']:
        user_accounts.append(acc)
    if len(user_accounts)>0:
      print("Aqui estão todas as suas contas:")
      dynamic_account_menu = ""
      for index, acc in enumerate(user_accounts):
        dynamic_account_menu += f"[{index+1}] conta {acc['number']} agência {acc['agency']}\n"
        dynamic_account_menu += "[0] Sair"
      select_account = input(dynamic_account_menu)
      if select_account == "0":
        return None
      else:
        acc = user_accounts[int(select_account)-1]
        return acc
    else:
      print("Você ainda não possui uma conta, que tal criarmos uma agora?")
      return create_current_account()

def create_current_account(user, current_accounts, account_types):
  new_account = {
    "account_holder": user['cpf'],
    "agency": "0001",
    'withdrawals_realized': 0
  }

  aux = len(current_accounts)+1
  new_account["account_number"] = f"{aux:010d}"

  print("Estamos realizando uma promoção para democratizar as nossas contas")
  print("Funciona da seguinte forma,\nvocê vai ganhar uma conta especial, com todos os benefícios\ne melhor sem nenhum encargo a mais do que a conta mais básica!!!")
  new_account['account_type'] = random.choice(account_types)
  acc_type = new_account["account_type"]["name"].capitalize()

  print(f"E a sua conta será... {acc_type}")
  surprise_bonus = random.randint(1, 10) * new_account["account_type"]["limit_value_per_withdrawal"]
  print(f"E para demonstrar a nossa alegria em ter você conosco, você ganhou...\nR$ {surprise_bonus},00 !!!")
  new_account['balance'] = surprise_bonus
  new_account['statement'] = f"Prêmio de R$ {surprise_bonus:.2f}\n"

  return new_account

def start_operations(menu, operation_menu, account_types, current_accounts, user):
  while True:
    menu_option = input(menu)
      # Acessar conta
    if menu_option == "1":
      selected_account = fetch_accounts(user, current_accounts)
      if selected_account:
        banking_operations.start_operations(selected_account, operation_menu=operation_menu)
      # Criar conta
    elif menu_option == "2":
      new_account = create_current_account(user, current_accounts, account_types)
      print("linha 75, apresentar new_account", new_account)
      if new_account:
        current_accounts.append(new_account)
        banking_operations.start_operations(new_account, operation_menu=operation_menu)
      else:
        print("Pareque que algo deu errado, tente novamente mais tarde")
    elif menu_option == "0":
      print("Somos felizes por ver você crescer conosco.\nVolte sempre!!!")
      print("#" * 45, "\n")
      break
    else :
      print("Por favor digite uma opção válida")
  return True