from modules import validations
import getpass
import requests

CEP_API_BASE_URL = "https://viacep.com.br/ws"

def get_cep_data(cep):
  response = requests.get(f"{CEP_API_BASE_URL}/{cep}/json")
  if not response.ok:
    raise Exception(f"Erro ao obter dados. Código de status: {response.status_code}")
  return response.json()

def create_user(users):
  new_user = {}
  new_user['name'] = input("Digite seu primeiro e seu último nome: ")
  add_cpf(users, new_user)

  add_address(new_user)

  add_password(new_user)

  return new_user

def add_cpf(users, new_user):
    while True:
      cpf = input("Digite seu Cadastro de Pessoa Física (CPF): ")
      if validations.cpf(cpf):
        cpf_found = any(obj.cpf == cpf for obj in users)
        if not cpf_found:
          new_user['cpf'] = cpf
          break
        else:
          print("Acredito que você já possui uma conta intergalática")
          print("Esqueceu sua senha?")
          reset_password = input("Digite [s] para Sim ou [n] para Não: ")
          if reset_password[0].lower() == "s":
            print("Vamos iniciar a recuperação")

          else:
            break
      else:
        print("Desculpe, mas o CPF informado não é válido")

def add_password(user):
    while True:
      password_min_lenght = 4
      password_max_lenght = 10
      password = getpass.getpass(f"Digite sua senha\n(deve conter entre {password_min_lenght} e {password_max_lenght} caracteres): ")
      if not validations.range_length_interval(password, max=password_max_lenght, min=password_min_lenght):
        print("Essa senha não atende aos requisitos de tamanho")
      else:
        break
    while True:
      confim_password = getpass.getpass("Repita a sua senha: ")
      if password == confim_password:
        user['password'] = password
        print("Parabéns sua conta foi criada com sucesso")
        break
      else:
        print("essa senha não corresponde a senha anterior, tente novamente")

def add_address(user):
    while True:
      cep = input("Digite o seu CEP ou 'sair' para encerrar: ")
      if cep.lower() == 'sair':
        break
      try:
        cep_data = get_cep_data(cep)
        if len(cep_data) > 1:
          print("_" * 46, "\n")
          print("confirme se as informações estão corretas")
          print('cep', cep_data['cep'])
          print('logradouro', cep_data['logradouro'])
          print('bairro', cep_data['bairro'])
          print('localidade', cep_data['localidade'])
          print('uf', cep_data['uf'])
          print("_" * 46, "\n")
          confirm_address = input("Digite [s] para Sim ou [n] para Não: ")
          if confirm_address[0].lower() == "s":
            address_number = input("Digite o número da sua residência,\nse ela não possuir um número deixe o campo em vazio: ")
            print("Obrigado, estamos armazenando seus dados de endereço")
            user['full_CEP_info'] = cep_data 
            user['address'] = f"{cep_data['logradouro']}, {address_number} - {cep_data['bairro']} - {cep_data['localidade']}/{cep_data['uf']}"
            print("Endereço armazenado com sucesso!\nAgorapodemos continuar o cadastro")
            print("_" * 46, "\n")
            break
          elif confirm_address[0].lower() == "n":
            print("Vamos tentar novamente")
        else:
          print("Não foi possível encontrar esse CEP")
          print("Em caso de dúvidas pesquise o CEP pelo seu endereço no site dos correios:\nhttps://buscacepinter.correios.com.br/app/localidade_logradouro/index.php")
      except Exception as e:
        print(e)