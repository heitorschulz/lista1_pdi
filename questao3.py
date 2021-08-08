"""
Lista 1 de Processamento Digital de Imagens
Questão 03
Aluno: Heitor Schulz
Matricula: 2016101758
"""

from PIL import Image
import math


def exercicio3(imagem,nome):
    pixels_o = imagem.load()

    comprimento= math.floor(imagem.size[0]/2)
    altura=math.ceil(imagem.size[1]/2)

    img = Image.new(imagem.mode,(comprimento, altura) , color = 'black')
    pixels_n= img.load()

    for i in range(comprimento):
        for j in range(altura):

            pixels_n[i,j]=pixels_o[(2*i),(2*j+1)]

    img.save('output/'+nome+'.jpg')


def main():

    imagem = Image.open('assets/frexp_1.png')
    exercicio3(imagem,"Exercicio03-A")


    return


if __name__ == '__main__':
    main()
