from cryptography.fernet import Fernet


def gen_save_key(filename='chave'):
  key = Fernet.generate_key()
  with open('chave', 'wb+') as f:
    f.write(key)
  return key

if __name__=='__main__':
  print(gen_save_key())