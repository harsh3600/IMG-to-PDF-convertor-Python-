from PIL import Image
img=Image.open('IMG.PNG')
im=img.convert('RGB')
im.save('IMG.pdf')

