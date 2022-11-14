import numpy as np
from operator import xor
import matplotlib.image as img
import matplotlib.pyplot as plt

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 1-(0.2989 * r + 0.5870 * g + 0.1140 * b)

    return gray


def regulate(arr,sizex,sizey,cfconstant):
    arr1=arr
    for i in range(sizex):
        for j in range(sizey):
            if arr1[i,j]<cfconstant:
                arr1[i,j]=0
    return arr1

def normalize(arr,sizex,sizey):
    arr1=arr
    arr1max=np.amax(arr1)
    arr1min=np.amin(arr1)
    arr1=(arr1+abs(arr1min))/(arr1max+abs(arr1min))
    return arr1

def binarize(arr,sizex,sizey,c2,c3):
    arr1=arr
    for i in range(sizex):
        for j in range(sizey):
            if arr1[i,j]>c2:
                arr1[i,j]=1
            else:
                arr1[i,j]=0
    return arr1

def showimg(arr):
    arr1=arr
    plt.imshow(arr1);
    plt.colorbar()
    plt.show()
    return

def ditherimg(arr,dithercnt,sizex,sizey):
    arr1=arr
    for cnt in range(dithercnt):
        for i in range(sizex-1):
            for j in range(sizey-1):
                arr1[i,j]=(arr1[i,j]+arr1[i,j+1])/2
                arr1[i,j]=(arr1[i,j]+arr1[i+1,j])/2
    return arr1
def fftswap(arr,sizex,sizey):
     arr1=np.zeros((sizex,sizey))
     arr1[0:int(sizex/2),0:int(sizey/2)]=arr[int(sizex/2):sizex,int(sizey/2):sizey];
     arr1[0:int(sizex/2),int(sizey/2):sizey]=arr[int(sizex/2):sizex,0:int(sizey/2)];
     arr1[int(sizex/2):sizex,0:int(sizey/2)]=arr[0:int(sizex/2),int(sizey/2):sizey];
     arr1[int(sizex/2):sizex,int(sizey/2):sizey]=arr[0:int(sizex/2),0:int(sizey/2)];
     return arr1

image = img.imread('C:/Users/xjian/Desktop/wtest0730.png')
imggray=rgb2gray(image)
print(imggray.shape)

lenx=len(imggray)
leny=len(imggray[0])
print(lenx)
print(leny)
cf1=0.0001
cf2=0.18
cf3=0.5
dithercnt=10

ditherimg(imggray,dithercnt,lenx,leny)
showimg(imggray)

hol=np.fft.ifft2(imggray)*np.sqrt(100)
hol=np.real(hol)

hol=fftswap(hol,lenx,leny)
showimg(hol)

hol=regulate(hol,lenx,leny,cf1)
#showimg(hol)
hol=normalize(hol,lenx,leny)
#showimg(hol)
hol=binarize(hol,lenx,leny,cf2,cf3)
showimg(hol)

imgreal=abs(np.fft.fft2(hol)/(100))**2
imgreal=fftswap(imgreal,lenx,leny)
showimg(imgreal)
