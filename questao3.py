"""
Lista 1 de Processamento Digital de Imagens
Questão 03
Aluno: Heitor Schulz
Matricula: 2016101758
"""

from PIL import Image
import math

# Reduz a imagem eliminando-se alternativamente
# as linhas e colunas.
def reducao_imagem(imagem,nome):
    pixels_o = imagem.load()

    comprimento= math.floor(imagem.size[0]/2)
    altura=math.ceil(imagem.size[1]/2)

    img = Image.new(imagem.mode,(comprimento, altura) , color = 'black')
    pixels_n= img.load()

    for i in range(comprimento):
        for j in range(altura):
            pixels_n[i,j]=pixels_o[(2*i),(2*j+1)]

    img.save('output/'+nome+'.jpg')

# Proposta de solução: Borrar a imagem primeiro
# e depois reduzir a imagem, reduzindo o efeito de Aliasing
def proposta_solucao(imagem,nome):
    from questao2 import convolucaonxn

    Constante_media_5x5 = 1/25
    Filtro_media_3x3 = [[1, 1, 1,1,1],
                        [1, 1, 1,1,1],
                        [1, 1, 1,1,1],
                        [1, 1, 1,1,1],
                        [1, 1, 1,1,1],]

    convolucaonxn(imagem,Filtro_media_3x3,Constante_media_5x5,"tmp_"+nome,5,False)

    img_tmp = Image.open('output/tmp_'+nome+'.jpg')
    reducao_imagem(img_tmp,nome)
    proposta_solucao

def main():

    imagem = Image.open('assets/frexp_1.png')
    reducao_imagem(imagem,"03-A")
    proposta_solucao(imagem,"03-B")

    return


if __name__ == '__main__':
    main()