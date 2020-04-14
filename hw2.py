import cv2
import numpy as np


img = cv2.imread('G:\\imagetest\\hw2.jpg',0) 
#cv2.imshow('org', img)
#Binarization


#-------------sobel----------------     
blurred = cv2.GaussianBlur(img, (5, 5), 0)
sobelX = cv2.Sobel(blurred, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(blurred, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)


sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombinNoblur = cv2.bitwise_or(sobelX, sobelY)


#-------------canny----------------  
#img = opening(img)
#blurred = cv2.GaussianBlur(img, (3, 3), 0)

canny = cv2.Canny(img, 70, 210)




#cv2.imshow('sobelX', sobelX)
#cv2.imshow('sobelY', sobelY)
cv2.imshow('sobelCombined', sobelCombined)
cv2.imshow('sobelCombinNoblur', sobelCombinNoblur)
cv2.imshow('canny', canny)
cv2.imwrite('G:\\imagetest\\sobelCombined.jpg',sobelCombined)
cv2.imwrite('G:\\imagetest\\sobelCombinNoblur.jpg',sobelCombinNoblur)
cv2.imwrite('G:\\imagetest\\canny.jpg',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()


