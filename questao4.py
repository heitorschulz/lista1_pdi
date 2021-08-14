"""
Lista 1 de Processamento Digital de Imagens
Questão 04
Aluno: Heitor Schulz
Matricula: 2016101758
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp


def exercicio4(imagem):

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    img_c1 = cv2.imread("assets/lena.tif", 0)
    img2_c1 = cv2.imread("assets/elaine.tiff", 0)

    # img_c1 = cv2.imread("assets/elaine.tiff", 0)
    # img2_c1 = cv2.imread("assets/lena.tif", 0)

    img_c2 = np.fft.fft2(img_c1)
    img2_c2 = np.fft.fft2(img2_c1)

    img_c3 = np.fft.fftshift(img_c2)
    img2_c3 = np.fft.fftshift(img2_c2)

  

    plt.subplot(231), plt.imshow(img_c1, "gray"), plt.title("Original Image")
    plt.subplot(232), plt.imshow(np.log(np.abs(img_c2)), "gray"), plt.title("Spectrum Original")
    plt.subplot(233), plt.imshow(np.angle(img_c2), "gray"), plt.title("Phase Angle Original")

    #print(img_c2)

    for index in range(512*512):
        #print("\nX:"+str(int(index/512))+",Y:"+str(index%512))
        #print(str(img_c2[int(index/512),index%512].real)+"|"+str(img_c2[int(index/512),index%512].imag))
        #print(str(img_c2[int(index/512),index%512].real)+"|"+str(img2_c2[int(index/512),index%512].imag))
        #print("Valor_B:"+str(img_c2[int(index/512),index%512]))
        #img_c2[int(index/512),index%512] = complex(img_c2[int(index/512),index%512].real, img2_c2[int(index/512),index%512].imag)
        #img_c2[int(index/512),index%512] = complex(img_c2[int(index/512),index%512].real, 0)
        #img_c3[int(index/512),index%512] = complex(img_c3[int(index/512),index%512].real, img2_c3[int(index/512),index%512].imag)
        img_c3[int(index/512),index%512] = complex(img_c3[int(index/512),index%512].real, 0)
        #print("Valor_A:"+str(img_c2[int(index/512),index%512]))

    #print(img_c2)

    plt.subplot(235), plt.imshow(np.log(np.abs(img_c3)), "gray"), plt.title("Spectrum Modified")
    plt.subplot(236), plt.imshow(np.angle(img_c3), "gray"), plt.title("Phase Angle Modified")


    img_c4 = np.fft.ifftshift(img_c3)
    img2_c4 = np.fft.ifftshift(img2_c3)

    img_c5 = np.fft.ifft2(img_c4)

    plt.subplot(234), plt.imshow(np.abs(img_c5), "gray"), plt.title("Processed Image")

    plt.show()

def main():

    exercicio4("")
    return


if __name__ == '__main__':
    main()
