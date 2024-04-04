
import random


def create_current_account():
  new_account = {}
  # a conta será umas string com 10 dígitos
  # que se inicia em 0000000001
  # a agência será sempre "0001"
  # sorteio de tipo de conta
  # sorteio de bônus com peso do tipo de conta
  surprise_bonus = random.randint(10, 100)
  print(f"E para demonstrar a nossa alegrie em ter você conosco, você ganhou...\nR$ {surprise_bonus},00 !!!")
  new_account['balance'] = surprise_bonus
  pass

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
        break
      else:
        acc = user_accounts[int(select_account)-1]
    else:
      print("Você ainda não possui uma conta, que tal criarmos uma agora?")
      create_current_account()
  return True
