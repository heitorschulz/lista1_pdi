import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import sqrt, exp



def printaimg():

    img1 = cv2.imread("assets/lena.tif", 0)
    img2 = cv2.imread("output/2A-Passa-baixas.jpg", 0)
    img3 = cv2.imread("output/2B-Laplaciano.jpg", 0)
    img4 = cv2.imread("output/2C-Mascara-de-Nitidez.jpg", 0)

    plt.figure(figsize=(6.4*5, 4.8*5),constrained_layout=False)

    #plt.subplot(121), plt.imshow(img1, "gray"), plt.title("Imagem Original")
    #plt.subplot(122), plt.imshow(img2, "gray"), plt.title("Filtro Passa-baixas")
    plt.subplot(121), plt.imshow(img3, "gray"), plt.title("Filtro Laplaciano")
    plt.subplot(122), plt.imshow(img4, "gray"), plt.title("Máscara de Nitidez (c=1)")





    plt.show()
    return



def main():

    printaimg()
    return


if __name__ == '__main__':
    main()