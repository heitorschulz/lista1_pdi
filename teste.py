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

    # print('PSNR'+ nome + '.jpg / Ruidosa.tif:')
    # calculoPSNR(img,imagem)
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

    # print('PSNR'+ nome + '.jpg / Ruidosa.tif:')
    # calculoPSNR(img,imagem)
    #img_original = Image.open('assets/original.tif')
    #print('\nPSNR original.tif /'+ nome + '.jpg:')
    #calculoPSNR(img_original,img)


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


def gerar_array(tamanho):


    arrayA = []
    for i in range(tamanho):
        arrayA.append(1)

    arrayB = []
    for j in range(tamanho):
        arrayB.append(arrayA)

    return arrayB

def main():

    #Filtro: media 3x3
    Constante_media_50 = 1/(50**2)
    Filtro_media_50 = gerar_array(50)

    imagem = Image.open('assets/lena2.tif')

    convolucaonxn(imagem,Filtro_media_50,Constante_media_50,"teste50x50",50)

    return

if __name__ == '__main__':
    main()
