from modules import account_operations, user_operations

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

menu = f"""
{bank_logo}
Muito bem, em que posso lhe ajudar hoje?

[1] Acessar uma conta
[2] Criar uma conta
[0] Sair

digite o número correspondente: """

operation_menu = f"""
{bank_logo}

Certo, o que você deseja fazer?

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

digite o número correspondente: """

account_types = [
  {"name": "silver", "limit_value_per_withdrawal": 500, "withdrawal_limit_per_day": 3},
  {"name": "gold", "limit_value_per_withdrawal": 1000, "withdrawal_limit_per_day": 5},
  {"name": "platinum", "limit_value_per_withdrawal": 2500, "withdrawal_limit_per_day": 8},
  {"name": "black", "limit_value_per_withdrawal": 3500, "withdrawal_limit_per_day": 12},
]
users = []
current_accounts = []

while True:
  login_option = input(login_menu)
  # Fazer login
  if login_option == "1":
    user = user_operations.login_user(users)
    if user:
      account_operations.start_operations(menu, operation_menu, account_types, current_accounts, user)
  # Fazer cadastro
  elif login_option == "2":
    new_user = user_operations.create_user(users)
    if new_user:
      users.append(new_user)
      account_operations.start_operations(menu, operation_menu, account_types, current_accounts, new_user)
  # Resetar senha
  elif login_option == "3":
    user_operations.redefine_password(users)
    pass
  elif login_option == "0":
    print("Somos felizes por ver você crescer conosco.\nVolte sempre!!!")
    print("#" * 45, "\n")
    break
  else :
    print("Por favor digite uma opção válida")
