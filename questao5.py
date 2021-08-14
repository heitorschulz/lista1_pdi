"""
Lista 1 de Processamento Digital de Imagens
Questão 05
Aluno: Heitor Schulz
Matricula: 2016101758
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp


def centralizar(a_fft):
    b_fft = np.zeros((a_fft.shape[0],a_fft.shape[1]),dtype=complex)
    for i in range(a_fft.shape[0]):
        for j in range(a_fft.shape[1]):
            b_fft[i,j] = a_fft[i,j] * (-1)**(i+j)
    return b_fft

def descentralizar(a_fft):
    return centralizar(a_fft)

def distancia(ponto1,ponto2):
    return sqrt((ponto1[0]-ponto2[0])**2 + (ponto1[1]-ponto2[1])**2)

def filtroButterworthPassaBaixa(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    linhas, colunas = imgShape[:2]
    centro = (linhas/2,colunas/2)
    for x in range(colunas):
        for y in range(linhas):
            base[y,x] = 1/(1+(distancia((y,x),centro)/D0)**(2*n))
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
    img_out = np.abs(imagem_descentralizada)
    cv2.imwrite("output/5A-Butterworth_D0-10_e_n-1.jpg", img_out)
    
    #para D0=50 e n = 1
    D0=50
    n=1
    fft_com_filtro = fft_da_imagem * filtroButterworthPassaBaixa(D0,imagem.shape,n)
    inversa_da_fft = np.fft.ifft2(fft_com_filtro)
    imagem_descentralizada = descentralizar(inversa_da_fft)
    plt.subplot(222), plt.imshow(np.abs(imagem_descentralizada), "gray"), plt.title("Butterworth Passa Baixa (D0="+str(D0)+",n="+str(n)+")")
    img_out = np.abs(imagem_descentralizada)
    cv2.imwrite("output/5B-Butterworth_D0-50_e_n-1.jpg", img_out)
    
    #para D0=10 e n = 8
    D0=10
    n=8
    fft_com_filtro = fft_da_imagem * filtroButterworthPassaBaixa(D0,imagem.shape,n)
    inversa_da_fft = np.fft.ifft2(fft_com_filtro)
    imagem_descentralizada = descentralizar(inversa_da_fft)
    plt.subplot(223), plt.imshow(np.abs(imagem_descentralizada), "gray"), plt.title("Butterworth Passa Baixa (D0="+str(D0)+",n="+str(n)+")")
    img_out = np.abs(imagem_descentralizada)
    cv2.imwrite("output/5C-Butterworth_D0-10_e_n-8.jpg", img_out)
    
    #para D0=50 e n = 8
    D0=50
    n=8
    fft_com_filtro = fft_da_imagem * filtroButterworthPassaBaixa(D0,imagem.shape,n)
    inversa_da_fft = np.fft.ifft2(fft_com_filtro)
    imagem_descentralizada = descentralizar(inversa_da_fft)
    plt.subplot(224), plt.imshow(np.abs(imagem_descentralizada), "gray"), plt.title("Butterworth Passa Baixa (D0="+str(D0)+",n="+str(n)+")")
    img_out = np.abs(imagem_descentralizada)
    cv2.imwrite("output/5D-Butterworth_D0-50_e_n-8.jpg", img_out)
    plt.show()

    return


if __name__ == '__main__':
    main()