import sys
import cv2
import numpy
import math
import random


Himg = cv2.imread("sceinic.jpg",0)
cv2.imwrite("Ex1.jpg",Himg)

Nx = Himg.shape[0] # high resolution image's width
Ny = Himg.shape[1] # high resolution image's height

print(Nx,Ny)

Lx = 300 # high resolution image's margin for x
Ly = 300 # high resolution image's margin for y

Mx = int(((Nx) - 2*Lx)/4) # low resolution image's width
My = int(((Ny) - 2*Ly)/4) # low resolution image's height

print(Mx,My)

Limg = numpy.zeros(shape=(Mx-1,My-1)) # make empty matrix for low resolution image

# -------------------- parameter
theta = math.radians(random.randint(-5,5))
print(theta)
sin=math.sin(theta)
cos=math.cos(theta)
tranx = 0
trany = 0
sigma = 0.8
ux = numpy.zeros(shape=(4,4))
uy = numpy.zeros(shape=(4,4))
d = numpy.zeros(shape=(4,4))
# --------------------
i=0
j=0

for i in range(0,Mx-1):
    for j in range(0,My-1):
        sum=0
        x = Nx/2 + ((Lx+2)+4*i-Nx/2-1/2)*math.cos(theta)+((Ly+2)+4*j-Ny/2-1/2)*math.sin(theta)+tranx
        y = Ny/2 - ((Lx+2)+4*i-Nx/2-1/2)*math.sin(theta)+((Ly+2)+4*j-Ny/2-1/2)*math.cos(theta)+trany
        for q in range(1,5):
            for w in range(1,5):     
                ux[q-1,w-1] =round(Nx/2 + ((Lx+2)+4*i-Nx/2-3+q)*math.cos(theta)+((Ly+2)+4*j-Ny/2-3+w)*math.sin(theta)+tranx)
                uy[q-1,w-1] =round(Ny/2 - ((Lx+2)+4*i-Nx/2-3+w)*math.sin(theta)+((Ly+2)+4*j-Ny/2-3+q)*math.cos(theta)+trany)
                d[q-1,w-1] = math.exp(-((ux[q-1,w-1]-x)**2+(uy[q-1,w-1]-y)**2)/2*sigma**2)/math.sqrt((2*math.pi)*sigma)
        d = d/numpy.sum(d)

        for q in range(1,5):
            for w in range(1,5):
                sum = sum +d[q-1,w-1]*Himg[int(ux[q-1,w-1]),int(uy[q-1,w-1])]
        Limg[i,j] = sum

        # for q in range(ux-2,ux+2):
        #     for w in range(uy-2,uy+2):
        #         # --------------
        #         sum=sum+(1/(math.sqrt(2*math.pi)*sigma)*math.exp(-((ux-q)**2+(uy-w)**2)/2*sigma**2))*Himg[q,w]
        #         # --------------
        
        # Limg[i,j] = sum 

cv2.imwrite("Ex4.jpg",Limg)

    


