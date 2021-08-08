"""
Lista 1 de Processamento Digital de Imagens
Aluno: Heitor Schulz
Matricula: 2016101758
"""


from PIL import Image
import math


def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return True
    else:
        return False

def rotaciona_array_180_graus(array_entrada, m, n, array_saida):
    for i in range(m):
        for j in range(n):
            array_saida[i][(n-1)-j]=array_entrada[(m-1)-i][j]

    print(array_saida)
    print(array_entrada)

def fatiamento(imagem):

    pixels = imagem.load()
    filenameOutput = 'output/fatiamento1_'
    ## Fatiamento usando 8 intervalos/fatias 
    ## Fatiamento estilo 1 
    fatias=8
    valor_maior_nivel=255
    range_fatias=(valor_maior_nivel+1)/fatias

    for f in range(fatias):
        img = Image.new(imagem.mode, imagem.size, color = 'black')
        pixels_n= img.load()

        for i in range(imagem.size[0]):
            for j in range(imagem.size[1]):
                if(pixels[i,j] >= range_fatias*f and pixels[i,j] <= (range_fatias*(f+1)-1)):
                    pixels_n[i,j]=pixels[i,j]

        img.save(filenameOutput+format(f, '02d')+'.jpg')


    filenameOutput = 'output/fatiamento2_'
    ## Fatiamento usando 8 intervalos/fatias 
    ## Fatiamento estilo 2
    fatias=8
    valor_maior_nivel=255
    range_fatias=(valor_maior_nivel+1)/fatias

    for f in range(fatias):
        img = Image.new(imagem.mode, imagem.size, color = 'black')
        pixels_n= img.load()

        for i in range(imagem.size[0]):
            for j in range(imagem.size[1]):
                if(pixels[i,j] >= range_fatias*f and pixels[i,j] <= (range_fatias*(f+1)-1)):
                    pixels_n[i,j]=255

        img.save(filenameOutput+format(f, '02d')+'.jpg')

    filenameOutput = 'output/fatiamento3_'
    ## Fatiamento usando 8 intervalos/fatias 
    ## Fatiamento estilo 3
    fatias=8
    valor_maior_nivel=255
    range_fatias=(valor_maior_nivel+1)/fatias

    for f in range(fatias):
        img = Image.new(imagem.mode, imagem.size, color = 'black')
        pixels_n= img.load()

        for i in range(imagem.size[0]):
            for j in range(imagem.size[1]):
                if(isKthBitSet(pixels[i,j], (f+1))):
                    pixels_n[i,j]=pixels[i,j]

        img.save(filenameOutput+format(f, '02d')+'.jpg')

    filenameOutput = 'output/fatiamento4_'
    ## Fatiamento usando 8 intervalos/fatias 
    ## Fatiamento estilo 4
    fatias=8
    valor_maior_nivel=255
    range_fatias=(valor_maior_nivel+1)/fatias

    for f in range(fatias):
        img = Image.new(imagem.mode, imagem.size, color = 'black')
        pixels_n= img.load()

        for i in range(imagem.size[0]):
            for j in range(imagem.size[1]):
                if(isKthBitSet(pixels[i,j], (f+1))):
                    pixels_n[i,j]=255

        img.save(filenameOutput+format(f, '02d')+'.jpg')

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
                pixels_n[i,j]=0

    img.save(filenameOutput+'.jpg')

def fatiamento2(imagem, limite_inferior, limite_superior):
    
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
    filenameOutput = 'output/fatiamento02'

    img = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_n= img.load()

    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):
            if(pixels[i,j] >= limite_inferior and pixels[i,j] <= limite_superior):
                pixels_n[i,j]=pixels[i,j] ##255
            else:
                pixels_n[i,j]=0

    img.save(filenameOutput+'.jpg')


##
def convolucao3x3(imagem,filtro,constante,nome):

    pixels = imagem.load()

    ##Rotaciona 180 Graus o filtro

    ##Realiza a convulação
    filenameConv = 'output/convolucao_'
    img = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_n= img.load()

    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):

            resultado=0
            initCounter = - int(len(filtro)/2)
            linha = initCounter
            coluna = initCounter
            
            for ii in filtro:
                #print(ii)
                for jj in ii:

                    pos_y=i+linha
                    pos_x=j+coluna
                    ##Tratar Bordas aqui?
                    if(i+linha<0):
                        pos_y+=1
                    if(j+coluna<0):
                        pos_x+=1
                    if(i+linha>=imagem.size[0]):
                        pos_y-=1
                    if(j+coluna>=imagem.size[1]):
                        pos_x-=1
                    resultado+=pixels[pos_y, pos_x]*jj

                    coluna+=1
                
                coluna = initCounter
                linha+=1
                
            pixels_n[i,j]=int(resultado*constante)

    img.save(filenameConv+nome+'.jpg')

def convolucaonxn(imagem,filtro,constante,nome, tamanho_filtro):

    pixels = imagem.load()

    ##Rotaciona 180 Graus o filtro
    filtro_out = filtro
    rotaciona_array_180_graus(filtro,tamanho_filtro,tamanho_filtro,filtro_out)
    filtro = filtro_out
    ##Realiza a convulação
    filenameConv = 'output/convolucao_'
    img = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_n= img.load()

    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):

            resultado=0
            initCounter = - int(tamanho_filtro/2)
            linha = initCounter
            coluna = initCounter
            
            for ii in filtro:
                #print(ii)
                for jj in ii:

                    pos_y=i+linha
                    pos_x=j+coluna
                    ##Tratar Bordas aqui?
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

def mascara_de_nitidez(imagem):

    pixels_o = imagem.load()

    #Passo 1: Borrar imagem original
    #Filtro: Passa-Baixa 3x3
    Constante_Passa_Baixa_3x3 = 1/9
    Filtro_Passa_Baixa_3x3 = [[1, 1, 1],
                              [1, 1, 1],
                              [1, 1, 1]]
    convolucao3x3(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"Borrado_3x3")
    borrado = Image.open('output/convolucao_Borrado_3x3.jpg')
    pixels_b= borrado.load()

    #Passo 2: Subtrair a imagem borrada da imagem original, obtendo a máscara
    mascara = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_m = mascara.load()
    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):
            pixels_m[i,j]=pixels_o[i,j]-pixels_b[i,j]
    mascara.save('output/mascara_nitidez'+'.jpg')
    
    #Passo 3: Adicionar uma porção ponderada da máscara à imagem original
    img_out = Image.new(imagem.mode, imagem.size, color = 'black')
    pixels_out = img_out.load()

    constante = 1.5
    for i in range(imagem.size[0]):
        for j in range(imagem.size[1]):
            pixels_out[i,j]=pixels_o[i,j] + int(constante * pixels_m[i,j])
    img_out.save('output/original+mascara_nitidez1.5'+'.jpg')


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
                #print(ii)
                for jj in range(tamanho_filtro):

                    pos_y=i+linha
                    pos_x=j+coluna
                    ##Tratar Bordas aqui?
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

    img.save(nome+'_filtro_mediana'+str(tamanho_filtro)+'x'+str(tamanho_filtro)+'.jpg')

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

    print("Iniciando programa")
    #imagem = Image.open('assets/Fig10.15(a).jpg')

    imagem = Image.open('assets/frexp_1.png')

    exercicio3(imagem,'3_antes_pb')

    #print("Fatiamento...")
    # print(imagem.size)
    #limite_inferior = 145
    #limite_superior = 210
    #fatiamento1(imagem, limite_inferior, limite_superior)
    #fatiamento2(imagem, limite_inferior, limite_superior)

    print("Convolução...")
    #imagem = Image.open('assets/lena.tif')

    #Filtro: Original
    Constante_Original_3x3 = 1
    Filtro_Original_3x3 = [[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]]

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

    Constante_Teste_3x3 = 1
    Filtro_Teste_3x3 = [[0, 1, 2],
                           [3, 4, 5],
                           [6, 7, 8]]       

    #convolucao3x3(imagem,Filtro_Original_3x3,Constante_Original_3x3,"Original_3x3")
    #convolucao3x3(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"Passa-baixas_3x3")
    #convolucao3x3(imagem,Filtro_Gaussiano_3x3,Constante_Gaussiano_3x3,"Gaussiano_3x3")
    #convolucao3x3(imagem,Filtro_Laplaciano_3x3,Constante_Laplaciano_3x3,"Laplaciano_3x3")
    #convolucao3x3(imagem,Filtro_Laplaciano_3x3_45g,Constante_Laplaciano_3x3_45g,"Laplaciano_45g_3x3")
    
    convolucaonxn(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"Passa-baixas_3x3",3)
    convolucaonxn(imagem,Filtro_Laplaciano_3x3,Constante_Laplaciano_3x3,"ex03",3)

    imagem = Image.open('output/convolucao_ex03.jpg')

    exercicio3(imagem,'3_apos_pb')
    
    return 0
    mascara_de_nitidez(imagem)


    #Filtro: Passa-Baixa 3x3
    Constante_Passa_Baixa_11x11 = 1/121
    Filtro_Passa_Baixa_11x11 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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

    # imagem = Image.open('assets/ruidosa1.tif')
    # filtro_mediana(imagem, 3, 'output/ruidosa1')
    # filtro_mediana(imagem, 11, 'output/ruidosa1')
    # #convolucao3x3(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"ruidosa1_Passa-baixas_3x3")
    # convolucaonxn(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"ruidosa1_Passa-baixas_3x3_n",3)
    # convolucaonxn(imagem,Filtro_Passa_Baixa_11x11,Constante_Passa_Baixa_11x11,"ruidosa1_Passa-baixas_11x11_n",11)

    # imagem = Image.open('assets/ruidosa2.tif')
    # filtro_mediana(imagem, 3, 'output/ruidosa2')
    # filtro_mediana(imagem, 5, 'output/ruidosa2')
    # filtro_mediana(imagem, 7, 'output/ruidosa2')
    # filtro_mediana(imagem, 9, 'output/ruidosa2')
    # filtro_mediana(imagem, 11, 'output/ruidosa2')

    # #convolucao3x3(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"ruidosa2_Passa-baixas_3x3")
    # convolucaonxn(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"ruidosa2_Passa-baixas_3x3_n",3)
    # convolucaonxn(imagem,Filtro_Passa_Baixa_11x11,Constante_Passa_Baixa_11x11,"ruidosa2_Passa-baixas_11x11_n",11)

    # imagem = Image.open('assets/lena_ruido.jpg')
    # convolucaonxn(imagem,Filtro_Passa_Baixa_3x3,Constante_Passa_Baixa_3x3,"lena_ruido_Passa-baixas_3x3_n",3)
    # convolucaonxn(imagem,Filtro_Passa_Baixa_11x11,Constante_Passa_Baixa_11x11,"lena_ruido_Passa-baixas_11x11_n",11)
    # filtro_mediana(imagem, 3, 'output/lena_ruido')
    # filtro_mediana(imagem, 11, 'output/lena_ruido')

    imagem = Image.open('output/lena_ruido_filtro_mediana11x11.jpg')
    mascara_de_nitidez(imagem)
    print("Fim do programa")

if __name__ == '__main__':
   main()