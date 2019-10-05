import numpy as np
import cv2
# load image and shrink - it's massive
num = 1

img = cv2.imread('C:/Users/SungHyeon/Desktop/T/'+str(num)+'.jpg')
img_origin_color = cv2.imread('C:/Users/SungHyeon/Desktop/T/'+str(num)+'_origin_color.jpg')
img_coated = img.copy()
height, width = img.shape[:2]
print(img.shape)
for i in range(height):
    for j in range(width):
        B = img.item(i, j, 0)
        G = img.item(i, j, 1)
        R = img.item(i, j, 2)
        b = img_origin_color.item(i, j, 0)
        g = img_origin_color.item(i, j, 1)
        r = img_origin_color.item(i, j, 2)
        if B==b and G == g and R == r:
            img_coated[j,i] = [0,0,0]

cv2.show('hehe', img_coated)
