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


def exercicio4(imagem1, imagem2):

    
    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    img_c1 = imagem1
    img2_c1 = imagem2

    img_c2 = np.fft.fft2(img_c1)
    img2_c2 = np.fft.fft2(img2_c1)

    img_c3 = np.fft.fftshift(img_c2)
    img2_c3 = np.fft.fftshift(img2_c2)

    plt.subplot(231), plt.imshow(img_c1, "gray"), plt.title("Original Image")
    plt.subplot(232), plt.imshow(np.log(np.abs(img_c3)), "gray"), plt.title("Spectrum Original")
    plt.subplot(233), plt.imshow(np.angle(img_c3), "gray"), plt.title("Phase Angle Original")

    # Muda a fase sem mudar o módulo
    for index in range(512*512):
        #primeiro passa para a forma polar, mais fácil trabalhar com o valor de módulo e fase
        img1_forma_polar = cmath.polar(img_c3[int(index/512),index%512])
        img2_forma_polar = cmath.polar(img2_c3[int(index/512),index%512])

        #pega o valor de módulo da primeira imagem e o valor de fase da segunda imagem
        novo_valor=(img1_forma_polar[0],img2_forma_polar[1])

        #volta para a forma retangular com números complexos
        img_c3[int(index/512),index%512] = cmath.rect(novo_valor[0],novo_valor[1])


    plt.subplot(235), plt.imshow(np.log(np.abs(img_c3)), "gray"), plt.title("Spectrum Modified")
    plt.subplot(236), plt.imshow(np.angle(img_c3), "gray"), plt.title("Phase Angle Modified")

    img_c4 = np.fft.ifftshift(img_c3)
    img_c5 = np.fft.ifft2(img_c4)

    plt.subplot(234), plt.imshow(np.abs(img_c5), "gray"), plt.title("Processed Image")
   
    plt.show()

def main():

    img1=cv2.imread("assets/lena.tif", 0)
    img2=cv2.imread("assets/elaine.tiff", 0)

    exercicio4(img1,img2)
    exercicio4(img2,img1)

    return


if __name__ == '__main__':
    main()
