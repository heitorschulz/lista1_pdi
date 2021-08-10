"""
Lista 1 de Processamento Digital de Imagens
Questão 02
Aluno: Heitor Schulz
Matricula: 2016101758
"""

from PIL import Image
import math

def rotaciona_array_180_graus(array_entrada, m, n, array_saida):
    for i in range(m):
        for j in range(n):
            array_saida[i][(n-1)-j]=array_entrada[(m-1)-i][j]

def convolucaonxn(imagem, filtro, constante, nome, tamanho_filtro):

    pixels = imagem.load()

    ##Rotaciona 180 Graus o filtro
    filtro_out = filtro
    rotaciona_array_180_graus(filtro,tamanho_filtro,tamanho_filtro,filtro_out)
    filtro = filtro_out
    ##Realiza a convulação
    filenameConv = 'output/'
    img = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_n= img.load()

    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):

            resultado=0
            initCounter = - int(tamanho_filtro/2)
            linha = initCounter
            coluna = initCounter
            
            for ii in filtro:
                for jj in ii:

                    pos_y=i+linha
                    pos_x=j+coluna
                    ##Trata Bordas aqui
                    if(pos_y<0):
                        while(pos_y<0):
                            pos_y+=1
                    if(pos_x<0):
                        while(pos_x<0):
                            pos_x+=1
                    if(pos_y>=imagem.size[0]):
                        while(pos_y>=imagem.size[0]):
                            pos_y-=1
                    if(pos_x>=imagem.size[1]):
                        while(pos_x>=imagem.size[1]):
                            pos_x-=1
                    resultado+=pixels[pos_y, pos_x]*jj

                    coluna+=1
                
                coluna = initCounter
                linha+=1
            
            # if(resultado>255):
            #     resultado=255
            # if(resultado<0):
            #     resultado=0
            ##print(resultado*constante)

            pixels_n[i,j]=int(resultado*constante)

    img.save(filenameConv+nome+'.jpg')

def mascara_de_nitidez(imagem, nome):

    pixels_o = imagem.load()

    #Passo 1: Borrar imagem original
    #Filtro: Passa-Baixa 3x3
    Constante_Passa_Baixa_3x3 = 1/9
    Filtro_Passa_Baixa_3x3 = [[1, 1, 1],
                              [1, 1, 1],
                              [1, 1, 1]]
    convolucaonxn(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"tmp_convolucao_Borrado_3x3",3)
    borrado = Image.open('output/tmp_convolucao_Borrado_3x3.jpg')
    pixels_b= borrado.load()

    #Passo 2: Subtrair a imagem borrada da imagem original, obtendo a máscara
    mascara = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_m = mascara.load()
    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):
            pixels_m[i,j]=pixels_o[i,j]-pixels_b[i,j]
    mascara.save('output/tmp_mascara_nitidez'+'.jpg')
    
    #Passo 3: Adicionar uma porção ponderada da máscara à imagem original
    img_out = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_out = img_out.load()

    constante = 1
    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):
            pixels_out[i,j]=pixels_o[i,j] + int(constante * pixels_m[i,j])
    img_out.save('output/'+nome+'.jpg')



def main():
    #Filtro: Passa-Baixa 3x3
    Constante_Passa_Baixa_3x3 = 1/9
    Filtro_Passa_Baixa_3x3 = [[1, 1, 1],
                              [1, 1, 1],
                              [1, 1, 1]]

    #Filtro: Gaussiano 3x3
    Constante_Gaussiano_3x3 = 1/16
    Filtro_Gaussiano_3x3 = [[1, 2, 1],
                            [2, 4, 2],
                            [1, 2, 1]]

    #Filtro: Laplaciano 3x3
    Constante_Laplaciano_3x3 = 1
    Filtro_Laplaciano_3x3 = [[0,  1, 0],
                             [1, -4, 1],
                             [0,  1, 0]]           

    #Filtro: Laplaciano 45Graus 3x3
    Constante_Laplaciano_3x3_45g = 1
    Filtro_Laplaciano_3x3_45g = [[-1, -1, -1],
                                 [-1,  8, -1],
                                 [-1, -1, -1]] 

    imagem = Image.open('assets/lena.tif')

    convolucaonxn(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"2A-Passa-baixas",3)
    convolucaonxn(imagem,Filtro_Laplaciano_3x3,Constante_Laplaciano_3x3,"2B-Laplaciano",3)
    mascara_de_nitidez(imagem, "2C-Mascara-de-Nitidez")
    return

if __name__ == '__main__':
    main()
