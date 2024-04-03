def number(input):
  try:
    float(input)
    return True
  except ValueError:
    return False

def cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False

    return True

def min_length(string, min):
   return True if len(string)>= min else False

def max_length(string, max):
   return True if len(string)<= max else False

def range_length_interval(string, /, *, max, min):
   return min_length(string, min) and max_length(string, max)