import random
import getpass
import requests
from modules import validations

def login_user(users):
  while True: 
    print("Caso queira cancelar a operação digite 'sair' a qualquer momento")
    cpf = input("Digite o seu CPF: ")
    if cpf.lower() == "sair":
      break
    if not validations.cpf(cpf):
      print("O CPF indicado não é válido")
      print("Tente novamente")
    for user in users:
      if user['cpf'] == cpf:
        user_found = user
        break
      else:
        user_found = None
        print("Infelizmente não encontramos esse CPF em nosso banco de dados")
        print("Tente novamente")
    if user_found:
      break

  while True:
    password = getpass.getpass("Digite a senha: ")
    if password.lower() == "sair":
      return None
    if password == user_found['password']:
      return user_found
    else:
      print("Senha incorreta")

CEP_API_BASE_URL = "https://viacep.com.br/ws"

def get_cep_data(cep):
  response = requests.get(f"{CEP_API_BASE_URL}/{cep}/json")
  if not response.ok:
    raise Exception(f"Erro ao obter dados. Código de status: {response.status_code}")
  return response.json()

def create_user(users):
  print("Caso queira cancelar a operação digite 'sair' a qualquer momento")
  new_user = {}
  new_user['name'] = input("Digite seu primeiro e seu último nome: ")
  if new_user['name'].lower() == "sair":
    return None
  if not add_cpf(users, new_user):
    return None
  if not add_address(new_user):
    return None
  if not add_password(new_user):
    return None
  return new_user

def add_cpf(users, new_user):
  while True:
    cpf = input("Digite seu Cadastro de Pessoa Física (CPF): ")
    if cpf.lower() == 'sair':
      return None
    if validations.cpf(cpf):
      cpf_found = any(obj['cpf'] == cpf for obj in users)
      if not cpf_found:
        new_user['cpf'] = cpf
        break
      else:
        print("Acredito que você já possui uma conta intergalática")
        print("Esqueceu sua senha?")
        reset_password = input("Digite [s] para Sim ou [n] para Não: ")
        if reset_password[0].lower() == "s":
          print("Vamos iniciar a recuperação")
          redefine_password()
        else:
          return None
    else:
      print("Desculpe, mas o CPF informado não é válido")
  return True

def add_password(user):
  password_min_lenght = 5
  password_max_lenght = 10
  while True:
    password = getpass.getpass(f"Digite sua senha\n(deve conter entre {password_min_lenght} e {password_max_lenght} caracteres): ")
    if password.lower() == 'sair':
      return None
    if not validations.range_length_interval(password, max=password_max_lenght, min=password_min_lenght):
      print("Essa senha não atende aos requisitos de tamanho")
    else:
      break
  while True:
    confim_password = getpass.getpass("Repita a sua senha: ")
    if confim_password.lower() == 'sair':
      return None
    if password == confim_password:
      user['password'] = password
      print("Parabéns sua conta foi criada com sucesso")
      return True
    else:
      print("essa senha não corresponde a senha anterior, tente novamente")

def add_address(user):
  while True:
    cep = input("Digite o seu CEP: ")
    if cep.lower() == 'sair':
      return None
    try:
      cep_data = get_cep_data(cep)
      if len(cep_data) > 1:
        print("_" * 45, "\n")
        print("confirme se as informações estão corretas:")
        print('cep', cep_data['cep'],'\nlogradouro', cep_data['logradouro'])
        print('bairro', cep_data['bairro'],'\nlocalidade', cep_data['localidade'])
        print('uf', cep_data['uf'])
        print("_" * 45, "\n")
        confirm_address = input("Digite [s] para Sim ou [n] para Não: ")
        if confirm_address[0].lower() == "s":
          address_number = input("Digite o número da sua residência,\nse ela não possuir um número deixe o campo em vazio: ")
          print("Obrigado, estamos armazenando seus dados de endereço")
          user['full_CEP_info'] = cep_data 
          user['address'] = f"{cep_data['logradouro']}, {address_number if address_number else "S/N"} - {cep_data['bairro']} - {cep_data['localidade']}/{cep_data['uf']}"
          print("Endereço armazenado com sucesso!\nAgora podemos continuar o cadastro")
          print("_" * 45, "\n")
          return True
        elif confirm_address[0].lower() == "n":
          print("Vamos tentar novamente")
      else:
        print("Não foi possível encontrar esse CEP")
        print("Em caso de dúvidas pesquise o CEP pelo seu endereço no site dos correios:\nhttps://buscacepinter.correios.com.br/app/localidade_logradouro/index.php")
    except Exception as e:
      print(e)

def redefine_password(users):
  print("Caso queira cancelar a operação digite 'sair' a qualquer momento")
  while True:
    cpf = input("Digite seu Cadastro de Pessoa Física (CPF): ")
    if cpf.lower() == 'sair':
      break
    if validations.cpf(cpf):
      cpf_found = any(obj.cpf == cpf for obj in users)
      for user in users:
        if user['cpf'] == cpf_found:
          user_found = user
          test_question = random.randint(1,3)
          if test_question == 1:
            uf = input("Digite o estado do seu endereço carastrado: ")
            answer = True if uf.lower() == user_found['full_CEP_info']['uf'].lower() else False
          elif test_question == 2:
            localidade = input("Digite a cidade ou distrito do seu endereço carastrado: ")
            answer = True if localidade.lower() == user_found['full_CEP_info']['localidade'].lower() else False
          elif test_question == 3:
            cep = input("Digite a cidade ou distrito do seu endereço carastrado: ")
            answer = True if cep.lower() == user_found['full_CEP_info']['localidade'].lower() else False
          if answer:
            if add_password(user_found):
              break
        else:
          user_found = None
          print("Infelizmente não encontramos esse CPF em nosso banco de dados")
          print("Tente novamente")
      if user_found:
        break
    else:
      print("O CPF indicado não é válido")
      print("Tente novamente")
