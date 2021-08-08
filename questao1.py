"""
Lista 1 de Processamento Digital de Imagens
Questão 01
Aluno: Heitor Schulz
Matricula: 2016101758
"""

from PIL import Image
import math

def fatiamento1(imagem, limite_inferior, limite_superior):
    
    if(limite_inferior < 0 or  limite_inferior > 255):
        print("Limite inferior fora do intervalo [0-255]!!")
        return
    if(limite_superior < 0 or  limite_superior > 255):
        print("Limite superior fora do intervalo [0-255]!!")
        return
    if(limite_superior<limite_inferior):
        print("Limite superior menor que limite inferior!!")
        return


    pixels = imagem.load()
    filenameOutput = 'output/fatiamento01'

    img = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_n= img.load()

    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):
            if(pixels[i,j] >= limite_inferior and pixels[i,j] <= limite_superior):
                pixels_n[i,j]=255
            else:
                pixels_n[i,j]=pixels[i,j]

    img.save(filenameOutput+'.jpg')


def main():

    imagem = Image.open('assets/Fig10.15(a).jpg')

    limite_inferior = 145
    limite_superior = 210
    fatiamento1(imagem, limite_inferior, limite_superior)
    return


if __name__ == '__main__':
    main()
