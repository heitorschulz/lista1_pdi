"""
Lista 1 de Processamento Digital de Imagens
Questão 06
Aluno: Heitor Schulz
Matricula: 2016101758
"""

from PIL import Image
import math

def rotaciona_array_180_graus(array_entrada, m, n, array_saida):
    for i in range(m):
        for j in range(n):
            array_saida[i][(n-1)-j]=array_entrada[(m-1)-i][j]

def convolucaonxn(imagem,filtro,constante,nome, tamanho_filtro):

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

            pixels_n[i,j]=int(resultado*constante)

    img.save(filenameConv+nome+'.jpg')

    img_original = Image.open('assets/original.tif')
    print('\nPSNR original.tif /'+ nome + '.jpg:')
    calculoPSNR(img_original,img)


def filtro_mediana(imagem,tamanho_filtro,nome):
    pixels_o = imagem.load()

    img = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_n= img.load()

    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):

            array=[]
            initCounter = - int(tamanho_filtro/2)
            linha = initCounter
            coluna = initCounter
            
            for ii in range(tamanho_filtro):
                for jj in range(tamanho_filtro):

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
                    array.append(pixels_o[pos_y, pos_x])
                    coluna+=1
                coluna = initCounter
                linha+=1
            
            array.sort()
            pixels_n[i,j]=array[int((tamanho_filtro**2)/2)]

    img.save('output/'+nome+'.jpg')

    img_original = Image.open('assets/original.tif')
    print('\nPSNR original.tif /'+ nome + '.jpg:')
    calculoPSNR(img_original,img)


def calculoPSNR(img_original, img_ruidosa):

    pixels_o = img_original.load()
    pixels_r= img_ruidosa.load()

    somatorio=0

    for i in range(img_original.size[0]):
        for j in range(img_original.size[1]):
            somatorio+=(pixels_o[i,j]-pixels_r[i,j])**2

    MSE=somatorio/(img_original.size[0]*img_original.size[1])
    MAX=255
    PSNR=20*math.log10((MAX/math.sqrt(MSE)))
    print(str(PSNR))

def main():

    #Filtro: media 3x3
    Constante_media_3x3 = 1/9
    Filtro_media_3x3 = [[1, 1, 1],
                              [1, 1, 1],
                              [1, 1, 1]]

    #Filtro: media 11x11
    Constante_media_11x11 = 1/121
    Filtro_media_11x11 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                ]

    img_original = Image.open('assets/original.tif')
    imagem = Image.open('assets/ruidosa1.tif')
    print('\nPSNR original.tif / Ruidosa1.tif:')
    calculoPSNR(img_original,imagem)

    convolucaonxn(imagem,Filtro_media_3x3,Constante_media_3x3,"6A.1-ruidosa1_media_3x3",3)
    convolucaonxn(imagem,Filtro_media_11x11,Constante_media_11x11,"6A.2-ruidosa1_media_11x11",11)
    filtro_mediana(imagem, 3, '6A.3-ruidosa1_mediana_3x3')
    filtro_mediana(imagem, 11, '6A.4-ruidosa1_mediana_11x11')


    imagem = Image.open('assets/ruidosa2.tif')
    print('\nPSNR original.tif / Ruidosa2.tif:')
    calculoPSNR(img_original,imagem)
    convolucaonxn(imagem,Filtro_media_3x3,Constante_media_3x3,"6B.1-ruidosa2_media_3x3",3)
    convolucaonxn(imagem,Filtro_media_11x11,Constante_media_11x11,"6B.2-ruidosa2_media_11x11",11)
    filtro_mediana(imagem, 3, '6B.3-ruidosa2_mediana_3x3')
    filtro_mediana(imagem, 11, '6B.4-ruidosa2_mediana_11x11')

    return

if __name__ == '__main__':
    main()
