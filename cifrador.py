from cryptography.fernet import Fernet
import io_imagem
import os

IGNORE = ['Raw profile type exif', 'icc_profile', 'XML:com.adobe.xmp', 'dpi']

def read_png(pngfile: str, keyfile: str):
  key = open(keyfile, 'rb').read()
  fer = Fernet(key)
  encrypted_data = io_imagem.read(pngfile)
  data = {}
  for k, v in encrypted_data.items():
    if k in IGNORE: continue
    data[fer.decrypt(k)] = fer.decrypt(v)
  return data


def write_png(pngfile: str, keyfile: str, data: dict[bytes, bytes]):
  key = open(keyfile, 'rb').read()
  fer = Fernet(key)
  encripted_data = {}
  for k, v in data.items():
    encripted_data[fer.encrypt(k)] = fer.encrypt(v)
  io_imagem.write(pngfile, pngfile, encripted_data)
  return io_imagem.read(pngfile)


if __name__=='__main__':
  row = input('[r]ead or [w]rite: ')
  conf = input('config file: ')
  [png, keyfile] = open(conf, 'r').readlines()
  png = png.strip('\n')
  keyfile = keyfile.strip('\n')
  if row=='w':
    num = int(input('quantity: '))
    data = read_png(png, keyfile)
    for i in range(num):
      print(f'---secred {i}---')
      title = input('name: ').encode()
      content = input('content: ').encode()
      data[title] = content
    write_png(png, keyfile, data)
  print(read_png(png, keyfile))
  input('...')
  os.system('cls')
  os.system('clear')