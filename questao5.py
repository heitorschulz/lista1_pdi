"""
Lista 1 de Processamento Digital de Imagens
Questão 05
Aluno: Heitor Schulz
Matricula: 2016101758
"""

def centralizar(a_fft):
    b_fft = np.zeros((a_fft.shape[0],a_fft.shape[1]),dtype=complex)
    for i in range(a_fft.shape[0]):
        for j in range(a_fft.shape[1]):
            b_fft[i,j] = a_fft[i,j] * (-1)**(i+j)
    return b_fft

def descentralizar(a_fft):
    return centralizar(a_fft)

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import sqrt, exp

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def filtroButterworthPassaBaixa(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

def main():

    imagem = cv2.imread("assets/lena.tif", 0)
    imagem_centralizada = centralizar(imagem)
    fft_da_imagem = np.fft.fft2(imagem_centralizada)
    
    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    #para D0=10 e n = 1
    D0=10
    n=1
    fft_com_filtro = fft_da_imagem * filtroButterworthPassaBaixa(D0,imagem.shape,n)
    inversa_da_fft = np.fft.ifft2(fft_com_filtro)
    imagem_descentralizada = descentralizar(inversa_da_fft)
    plt.subplot(221), plt.imshow(np.abs(imagem_descentralizada), "gray"), plt.title("Butterworth Passa Baixa (D0="+str(D0)+",n="+str(n)+")")

    #para D0=50 e n = 1
    D0=50
    n=1
    fft_com_filtro = fft_da_imagem * filtroButterworthPassaBaixa(D0,imagem.shape,n)
    inversa_da_fft = np.fft.ifft2(fft_com_filtro)
    imagem_descentralizada = descentralizar(inversa_da_fft)
    plt.subplot(222), plt.imshow(np.abs(imagem_descentralizada), "gray"), plt.title("Butterworth Passa Baixa (D0="+str(D0)+",n="+str(n)+")")

    #para D0=10 e n = 8
    D0=10
    n=8
    fft_com_filtro = fft_da_imagem * filtroButterworthPassaBaixa(D0,imagem.shape,n)
    inversa_da_fft = np.fft.ifft2(fft_com_filtro)
    imagem_descentralizada = descentralizar(inversa_da_fft)
    plt.subplot(223), plt.imshow(np.abs(imagem_descentralizada), "gray"), plt.title("Butterworth Passa Baixa (D0="+str(D0)+",n="+str(n)+")")

    #para D0=50 e n = 8
    D0=50
    n=8
    fft_com_filtro = fft_da_imagem * filtroButterworthPassaBaixa(D0,imagem.shape,n)
    inversa_da_fft = np.fft.ifft2(fft_com_filtro)
    imagem_descentralizada = descentralizar(inversa_da_fft)
    plt.subplot(224), plt.imshow(np.abs(imagem_descentralizada), "gray"), plt.title("Butterworth Passa Baixa (D0="+str(D0)+",n="+str(n)+")")

    plt.show()

    return


if __name__ == '__main__':
    main()