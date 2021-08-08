"""
Lista 1 de Processamento Digital de Imagens
Questão 05
Aluno: Heitor Schulz
Matricula: 2016101758
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import sqrt, exp

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def butterworthLP(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

def main():

    img = cv2.imread("assets/lena.tif", 0)
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    D0=10
    n=1

    LowPassCenter = center * butterworthLP(D0,img.shape,n)
    LowPass = np.fft.ifftshift(LowPassCenter)
    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(221), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Butterworth Low Pass (D0="+str(D0)+",n="+str(n)+")")

    D0=50
    n=1

    LowPassCenter = center * butterworthLP(50,img.shape,1)
    LowPass = np.fft.ifftshift(LowPassCenter)
    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(222), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Butterworth Low Pass (D0="+str(D0)+",n="+str(n)+")")

    D0=10
    n=8

    LowPassCenter = center * butterworthLP(10,img.shape,8)
    LowPass = np.fft.ifftshift(LowPassCenter)
    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(223), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Butterworth Low Pass (D0="+str(D0)+",n="+str(n)+")")

    D0=50

    LowPassCenter = center * butterworthLP(50,img.shape,8)
    LowPass = np.fft.ifftshift(LowPassCenter)
    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(224), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Butterworth Low Pass (D0="+str(D0)+",n="+str(n)+")")

    plt.show()

    return


if __name__ == '__main__':
    main()
