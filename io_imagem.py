from PIL import Image, PngImagePlugin

# Ref: https://gist.github.com/vlantonov/e5de46679379faad1bf24adc7d65c890

def read(filename: str):
  im = Image.open(filename)
  im.load()
  return im.info

def write(in_filename: str, out_filename: str, data: dict[str,str]):
  info = PngImagePlugin.PngInfo()

  for key, value in data.items():
    info.add(key, value)

  im = Image.open(in_filename)
  im.save(out_filename, 'PNG', pnginfo=info)

if __name__=='__main__':
  print(read('tst.png').keys())