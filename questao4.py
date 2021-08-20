"""
Lista 1 de Processamento Digital de Imagens
Questão 04
Aluno: Heitor Schulz
Matricula: 2016101758
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import cmath
from math import sqrt, exp

def centralizar(a_fft):
    b_fft = np.zeros((a_fft.shape[0],a_fft.shape[1]),dtype=complex)
    for i in range(a_fft.shape[0]):
        for j in range(a_fft.shape[1]):
            b_fft[i,j] = a_fft[i,j] * (-1)**(i+j)
    return b_fft

def descentralizar(a_fft):
    return centralizar(a_fft)

def exercicio4(imagem1, imagem2, nome):

    plt.figure(figsize=(32, 24), constrained_layout=False)

    img_centralizada_1 = centralizar(imagem1)
    img_centralizada_2 = centralizar(imagem2)

    img_fft_1 = np.fft.fft2(img_centralizada_1)
    img_fft_2 = np.fft.fft2(img_centralizada_2)

    plt.subplot(231), plt.imshow(imagem1, "gray"), plt.title("Imagem Original")
    plt.subplot(232), plt.imshow(np.log(np.abs(img_fft_1)), "gray"), plt.title("Espectro Original")
    plt.subplot(233), plt.imshow(np.angle(img_fft_1), "gray"), plt.title("Angulo de Fase Original")

    # Mudar a fase sem mudar o módulo
    for index in range(512*512):
        #primeiro passa para a forma polar, mais fácil trabalhar com o valor de módulo e fase
        img1_forma_polar = cmath.polar(img_fft_1[int(index/512),index%512])
        img2_forma_polar = cmath.polar(img_fft_2[int(index/512),index%512])

        #pega o valor de módulo da primeira imagem e o valor de fase da segunda imagem
        novo_valor=(img1_forma_polar[0],img2_forma_polar[1])

        #volta para a forma retangular com números complexos
        img_fft_1[int(index/512),index%512] = cmath.rect(novo_valor[0],novo_valor[1])


    plt.subplot(235), plt.imshow(np.log(np.abs(img_fft_1)), "gray"), plt.title("Espectro Modificado")
    plt.subplot(236), plt.imshow(np.angle(img_fft_1), "gray"), plt.title("Angulo de Fase Modificado")

    img_inversa_fft = np.fft.ifft2(img_fft_1)

    img_final = descentralizar(img_inversa_fft)

    plt.subplot(234), plt.imshow(np.abs(img_final), "gray"), plt.title("Imagem Processada")

    img_out = np.abs(img_final)
    cv2.imwrite("output/"+nome+".jpg", img_out)
   
    plt.savefig("output/"+nome+"_info.png",dpi=300)
    plt.show()
    

    

def main():

    img1=cv2.imread("assets/lena.tif", 0)
    img2=cv2.imread("assets/elaine.tiff", 0)

    exercicio4(img1,img2,"4A-Lena_modificada")
    exercicio4(img2,img1,"4B-Elaine_modificada")

    return


if __name__ == '__main__':
    main()
