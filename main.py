"""
Lista 1 de Processamento Digital de Imagens
Aluno: Heitor Schulz
Matricula: 2016101758
"""


from PIL import Image

print("Hello")

imagem = Image.open('assets/lena.tif')
pixels = imagem.load()
print(imagem.size)
print(pixels[0,0])
pixels[0,0]=0
imagem.save('teste.jpg')