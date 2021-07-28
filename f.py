import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def idealFilterLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 1
    return base

def idealFilterHP(D0,imgShape):
    base = np.ones(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 0
    return base

def butterworthLP(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

def butterworthHP(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1-1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

def gaussianLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

def gaussianHP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1 - exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

def teste():
    plt.figure(figsize=(6.4*5,4.8*5), constrained_layout=False)

    img_c1 = cv2.imread("testes/left01.jpg", 0)
    img_c2 = np.fft.fft2(img_c1)
    img_c3 = np.fft.fftshift(img_c2)
    img_c4 = np.fft.ifftshift(img_c3)
    img_c5 = np.fft.ifft2(img_c4)

    plt.subplot(151), plt.imshow(img_c1, "gray"), plt.title("Original Image")
    plt.subplot(152), plt.imshow(np.log(1+np.abs(img_c2)), "gray"), plt.title("Spectrum")
    plt.subplot(153), plt.imshow(np.log(1+np.abs(img_c3)), "gray"), plt.title("Centered Spectrum")
    plt.subplot(154), plt.imshow(np.log(1+np.abs(img_c4)), "gray"), plt.title("Decentralized")
    plt.subplot(155), plt.imshow(np.abs(img_c5), "gray"), plt.title("Processed Image")

    plt.show()



    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    img = cv2.imread("testes/left01.jpg", 0)

    original = np.fft.fft2(img)
    plt.subplot(131), plt.imshow(np.log(np.abs(original)), "gray"), plt.title("Spectrum")

    plt.subplot(132), plt.imshow(np.angle(original), "gray"), plt.title("Phase Angle")
    plt.show()


def testesLowPass():

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    img = cv2.imread("testes/left01.jpg", 0)
    plt.subplot(161), plt.imshow(img, "gray"), plt.title("Original Image")

    original = np.fft.fft2(img)
    plt.subplot(162), plt.imshow(np.log(1+np.abs(original)), "gray"), plt.title("Spectrum")

    center = np.fft.fftshift(original)
    plt.subplot(163), plt.imshow(np.log(1+np.abs(center)), "gray"), plt.title("Centered Spectrum")

    LowPassCenter = center * idealFilterLP(50,img.shape)
    plt.subplot(164), plt.imshow(np.log(1+np.abs(LowPassCenter)), "gray"), plt.title("Centered Spectrum multiply Low Pass Filter")

    LowPass = np.fft.ifftshift(LowPassCenter)
    plt.subplot(165), plt.imshow(np.log(1+np.abs(LowPass)), "gray"), plt.title("Decentralize")

    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(166), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Processed Image")

    plt.show()


    img = cv2.imread("testes/left01.jpg", 0)
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    plt.subplot(151), plt.imshow(np.log(1+np.abs(center)), "gray"), plt.title("Spectrum")

    LowPass = idealFilterLP(50,img.shape)
    plt.subplot(152), plt.imshow(np.abs(LowPass), "gray"), plt.title("Low Pass Filter")

    LowPassCenter = center * idealFilterLP(50,img.shape)
    plt.subplot(153), plt.imshow(np.log(1+np.abs(LowPassCenter)), "gray"), plt.title("Centered Spectrum multiply Low Pass Filter")

    LowPass = np.fft.ifftshift(LowPassCenter)
    plt.subplot(154), plt.imshow(np.log(1+np.abs(LowPass)), "gray"), plt.title("Decentralize")

    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(155), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Processed Image")

    plt.show()




def testesHighPass():

    img = cv2.imread("testes/left01.jpg", 0)
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    plt.subplot(151), plt.imshow(np.log(1+np.abs(center)), "gray"), plt.title("Spectrum")

    HighPass = idealFilterHP(50,img.shape)
    plt.subplot(152), plt.imshow(np.abs(HighPass), "gray"), plt.title("High Pass Filter")

    HighPassCenter = center * idealFilterHP(50,img.shape)
    plt.subplot(153), plt.imshow(np.log(1+np.abs(HighPassCenter)), "gray"), plt.title("Centered Spectrum multiply High Pass Filter")

    HighPass = np.fft.ifftshift(HighPassCenter)
    plt.subplot(154), plt.imshow(np.log(1+np.abs(HighPass)), "gray"), plt.title("Decentralize")

    inverse_HighPass = np.fft.ifft2(HighPass)
    plt.subplot(155), plt.imshow(np.abs(inverse_HighPass), "gray"), plt.title("Processed Image")

    plt.show()


def testesFiltros():

    img = cv2.imread("testes/left01.jpg", 0)

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    LowPass = idealFilterLP(50,img.shape)
    plt.subplot(131), plt.imshow(LowPass, "gray"), plt.title("Ideal Low Pass Filter")

    HighPass = idealFilterHP(50,img.shape)
    plt.subplot(132), plt.imshow(HighPass, "gray"), plt.title("Ideal High Pass Filter")

    plt.show()

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    LowPass = butterworthLP(50,img.shape,20)
    plt.subplot(131), plt.imshow(LowPass, "gray"), plt.title("Butterworth Low Pass Filter (n=20)")

    HighPass = butterworthHP(50,img.shape,20)
    plt.subplot(132), plt.imshow(HighPass, "gray"), plt.title("Butterworth High Pass Filter (n=20)")

    plt.show()

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    LowPass = butterworthLP(50,img.shape,3)
    plt.subplot(131), plt.imshow(LowPass, "gray"), plt.title("Butterworth Low Pass Filter (n=3)")

    HighPass = butterworthHP(50,img.shape,3)
    plt.subplot(132), plt.imshow(HighPass, "gray"), plt.title("Butterworth High Pass Filter (n=3)")

    plt.show()

    
    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    LowPass = gaussianLP(50,img.shape)
    plt.subplot(131), plt.imshow(LowPass, "gray"), plt.title("Gaussian Low Pass Filter")

    HighPass = gaussianHP(50,img.shape)
    plt.subplot(132), plt.imshow(HighPass, "gray"), plt.title("Gaussian High Pass Filter")

    plt.show()

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    IdealLP = idealFilterLP(50,img.shape)
    plt.subplot(131), plt.imshow(IdealLP, "gray"), plt.title("Ideal Low Pass Filter")

    ButterLP = butterworthLP(50,img.shape,10)
    plt.subplot(132), plt.imshow(ButterLP, "gray"), plt.title("Butterworth Low Pass Filter (n=10)")

    GaussianLP = gaussianLP(50,img.shape)
    plt.subplot(133), plt.imshow(GaussianLP, "gray"), plt.title("Gaussian Low Pass Filter")

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)
    IdealHP = idealFilterHP(50,img.shape)
    plt.subplot(231), plt.imshow(IdealHP, "gray"), plt.title("Ideal High Pass Filter")

    ButterHP = butterworthHP(50,img.shape,10)
    plt.subplot(232), plt.imshow(ButterHP, "gray"), plt.title("Butterworth High Pass Filter (n=10)")

    GaussianHP = gaussianHP(50,img.shape)
    plt.subplot(233), plt.imshow(GaussianHP, "gray"), plt.title("Gaussian High Pass Filter")

    plt.show()



def testesFiltrosImagem():
    img = cv2.imread("testes/left01.jpg", 0)
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    LowPassCenter = center * idealFilterLP(50,img.shape)
    LowPass = np.fft.ifftshift(LowPassCenter)
    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(131), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Ideal Low Pass")

    LowPassCenter = center * butterworthLP(50,img.shape,10)
    LowPass = np.fft.ifftshift(LowPassCenter)
    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(132), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Butterworth Low Pass (n=10)")

    LowPassCenter = center * gaussianLP(50,img.shape)
    LowPass = np.fft.ifftshift(LowPassCenter)
    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(133), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Gaussian Low Pass")

    plt.show()

    img = cv2.imread("testes/left01.jpg", 0)
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    HighPassCenter = center * idealFilterHP(50,img.shape)
    HighPass = np.fft.ifftshift(HighPassCenter)
    inverse_HighPass = np.fft.ifft2(HighPass)
    plt.subplot(131), plt.imshow(np.abs(inverse_HighPass), "gray"), plt.title("Ideal High Pass")

    HighPassCenter = center * butterworthHP(50,img.shape,10)
    HighPass = np.fft.ifftshift(HighPassCenter)
    inverse_HighPass = np.fft.ifft2(HighPass)
    plt.subplot(132), plt.imshow(np.abs(inverse_HighPass), "gray"), plt.title("Butterworth High Pass (n=10)")

    HighPassCenter = center * gaussianHP(50,img.shape)
    HighPass = np.fft.ifftshift(HighPassCenter)
    inverse_HighPass = np.fft.ifft2(HighPass)
    plt.subplot(133), plt.imshow(np.abs(inverse_HighPass), "gray"), plt.title("Gaussian High Pass")

    plt.show()

    img = cv2.imread("testes/left01.jpg", 0)
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)

    plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

    plt.subplot(131), plt.imshow(img, "gray"), plt.title("Original Image")

    LowPassCenter = center * gaussianLP(50,img.shape)
    LowPass = np.fft.ifftshift(LowPassCenter)
    inverse_LowPass = np.fft.ifft2(LowPass)
    plt.subplot(132), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Gaussian Low Pass")

    HighPassCenter = center * gaussianHP(50,img.shape)
    HighPass = np.fft.ifftshift(HighPassCenter)
    inverse_HighPass = np.fft.ifft2(HighPass)
    plt.subplot(133), plt.imshow(np.abs(inverse_HighPass), "gray"), plt.title("Gaussian High Pass")

    plt.show()


def main():
    
    teste()
    testesLowPass()
    testesHighPass()
    testesFiltros()
    testesFiltrosImagem()











if __name__ == '__main__':
    main()