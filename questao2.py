"""
Lista 1 de Processamento Digital de Imagens
Questão 02
Aluno: Heitor Schulz
Matricula: 2016101758
"""

from PIL import Image
import numpy as np
import math


# Corrige os valores do array para o intervalo de [0,255] por deslocamento e normalização
# Desloca o array pelo menor valor, dessa forma o valor mínimo vai para 0.
# E por fim normaliza pelo maior valor, dessa forma o valor máximo vai para 255.
def corrige_valores_por_shift_e_normalizacao(array):
    valor_minimo = np.amin(array)
   
    if valor_minimo < 0:
        array = array - valor_minimo

    valor_maximo = np.amax(array)
    if valor_maximo > 255:
        array = array * 255/valor_maximo

    return array

# Corrige os valores do array por meio de corte
# Valores negativos vão para 0
# Valores maiores que 255 vão para 255
def corrige_valores_por_corte(array):
    return np.clip(array,0,255)

# Rotaciona o filtro em 180 para fazer a convolução depois
def rotaciona_array_180_graus(array_entrada, m, n, array_saida):
    for i in range(m):
        for j in range(n):
            array_saida[i][(n-1)-j]=array_entrada[(m-1)-i][j]

#Realiza a convolução NxN
def convolucaonxn(imagem, filtro, constante, nome, tamanho_filtro, correcao):

    pixels = np.asarray(imagem,dtype='float64')

    ##Rotaciona 180 Graus o filtro
    filtro_out = filtro
    rotaciona_array_180_graus(filtro,tamanho_filtro,tamanho_filtro,filtro_out)
    filtro = filtro_out
    ##Realiza a convulação
    filenameConv = 'output/'
    img = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_n = np.asarray(img,dtype='float64')

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
            
            pixels_n[i,j]=resultado*constante
    
    if(correcao):
        pixels_n = corrige_valores_por_shift_e_normalizacao(pixels_n)
    else:
        pixels_n = corrige_valores_por_corte(pixels_n)    

    img = Image.fromarray(np.uint8(pixels_n))
    img.save(filenameConv+nome+'.jpg')

#Aplica a mascara de nitidez
def mascara_de_nitidez(imagem, nome):

    pixels_o = np.asarray(imagem,dtype='float64')

    #Passo 1: Borrar imagem original
    #Filtro: Passa-Baixa 3x3
    Constante_Passa_Baixa_3x3 = 1/9
    Filtro_Passa_Baixa_3x3 = [[1, 1, 1],
                              [1, 1, 1],
                              [1, 1, 1]]
    convolucaonxn(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"tmp_convolucao_Borrado_3x3",3,False)
    borrado = Image.open('output/tmp_convolucao_Borrado_3x3.jpg')
    pixels_b = np.asarray(borrado,dtype='float64')

    #Passo 2: Subtrair a imagem borrada da imagem original, obtendo a máscara
    mascara = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_m = np.asarray(mascara,dtype='float64')
    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):
            pixels_m[i,j]=pixels_o[i,j]-pixels_b[i,j]
    
    mascara = Image.fromarray(np.uint8(corrige_valores_por_corte(pixels_m)))
    mascara.save('output/tmp_mascara_nitidez'+'.jpg')
    
    #Passo 3: Adicionar uma porção ponderada da máscara à imagem original
    img_out = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_out = np.asarray(img_out,dtype='float64')

    constante = 1
    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):
            pixels_out[i,j]=pixels_o[i,j] + (constante * pixels_m[i,j])
    
    pixels_out = corrige_valores_por_corte(pixels_out)
    img_out = Image.fromarray(np.uint8(pixels_out))
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

    convolucaonxn(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"2A-Passa-baixas",3,False)
    convolucaonxn(imagem,Filtro_Laplaciano_3x3,Constante_Laplaciano_3x3,"2B.1-Laplaciano_sem_correcao",3,False)
    convolucaonxn(imagem,Filtro_Laplaciano_3x3_45g,Constante_Laplaciano_3x3_45g,"2B.2-Laplaciano-45G_sem_correcao",3,False)
    convolucaonxn(imagem,Filtro_Laplaciano_3x3,Constante_Laplaciano_3x3,"2B.3-Laplaciano",3,True)
    convolucaonxn(imagem,Filtro_Laplaciano_3x3_45g,Constante_Laplaciano_3x3_45g,"2B.4-Laplaciano-45G",3,True)
    mascara_de_nitidez(imagem, "2C-Mascara-de-Nitidez")
    return

if __name__ == '__main__':
    main()
