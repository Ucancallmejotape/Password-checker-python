def verificar_senha(senha):
  """Verficando se a senha é válida.

  Essa função verifica as seguintes condições
  C1: possui tamanho igual a 4;
  C2: inclui pelo menos um dígito (0-9);
  C3: inclui pelo menos uma letra maiúscula (A-Z);
  C4: inclui pelo menos um dos seguintes caracteres especiais: "!", "@", "#", "$", "#", "%", "^", "&", 
   """
Caracteresespeciais=["!", "@", "#", "$", "#", "%", "^", "&"]
return_val=True

senha = input('Digite a nova senha:  ')

repeticao = input('Repita a senha, por favor: ')

if senha == repeticao:
    
    print('Aqui vamos testar as condições C1 até C4...')
    
else:
    print('Calma, jovem, a senha repetida não confere.')

#Verifica se a senha atende a condição de tamanho C1
if len(senha) != 4:
    print('Sua senha não possui 4 caracteres = C1 NÃO OK')
    return_val=False

#Verifica se a senha possui pelo menos um dos números exigidos na condição C2
if not any(char.isdigit() for char in senha):
    print('Sua senha deve conter pelo menos um número = C2 NÃO OK')
    return_val=False

#Verifica se a senha possui pelo menos uma letra maiúscula exigida na condição C3
if not any(char.isupper() for char in senha):
    print('Sua senha deve conter pelo menos uma letra maiúscula = C3 NÃO OK')
    return_val=False

#Verifica se a senha possui pelo menos um dos simbolos especiais exigidos na condição C4
if not any(char in Caracteresespeciais  for char in senha):
    print('Sua senha deve conter pelo menos um dos caracteres especiais !@#$#%^&*e = C4 NÃO OK')
    return_val=False

# Verificando se a senha atende de C1-C4   
if return_val:
    print('Sua senha atende a todas condições, logo é válida')
else:
  print('Sua senha não atende uma ou mais condições, logo é inválida')


