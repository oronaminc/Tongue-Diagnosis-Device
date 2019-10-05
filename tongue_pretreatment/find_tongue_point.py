import numpy as np
import cv2
# load image and shrink - it's massive
num = 1
img = cv2.imread('C:/Users/SungHyeon/Desktop/t/'+str(num)+'.jpg')
cv2.imshow('original',img)
height, width = img.shape[:2]
print('width: ', width, ' height: ', height)

threshold = 30
point = []
temp = []
flag1, flag2, flag3, flag4 = False, False, False, False
center_width = 0
part1_height = 0
part2_height = 0

# find point 1
for i in range(height):
    for j in range(width):
        B = img.item(i, j, 0)
        G = img.item(i, j, 1)
        R = img.item(i, j, 2)
        if B+G+R > threshold and j < width/2:
            flag1 = True
            temp.append([j,i])
            break
    if flag1 == True:
        break

for i in range(width):
    for j in range(height):
        B = img.item(j, i, 0)
        G = img.item(j, i, 1)
        R = img.item(j, i, 2)
        if B+G+R > threshold:
            flag2 = True
            temp.append([i,j])
            break
    if flag2 == True:
        break


i = temp[1][0]
j = temp[0][1]
while True:
    B = img.item(j, i, 0)
    G = img.item(j, i, 1)
    R = img.item(j, i, 2)
    if B+G+R > threshold:
        point.append([i,j])
        break
    i += 1
    j += 1
    
temp = []

# find point 2
for i in range(height):
    for j in range(width-1, -1, -1):
        B = img.item(i, j, 0)
        G = img.item(i, j, 1)
        R = img.item(i, j, 2)
        if B+G+R > threshold and j > width/2:
            flag3 = True
            temp.append([j,i])
            break
    if flag3 == True:
        break

for i in range(width-1, -1, -1):
    for j in range(height):
        B = img.item(j, i, 0)
        G = img.item(j, i, 1)
        R = img.item(j, i, 2)
        if B+G+R > threshold:
            flag4 = True
            temp.append([i,j])
            break
    if flag4 == True:
        break

i = temp[1][0]
j = temp[0][1]
while True:
    B = img.item(j, i, 0)
    G = img.item(j, i, 1)
    R = img.item(j, i, 2)
    if B+G+R > threshold:
        point.append([i,j])
        break
    i -= 1
    j += 1

center_width = (point[0][0]+point[1][0])//2
flag1, flag2, flag3, flag4 = False, False, False, False

# find point 3
for i in range(height):
    B = img.item(i, center_width, 0)
    G = img.item(i, center_width, 1)
    R = img.item(i, center_width, 2)
    if B+G+R > threshold:
        point.append([center_width,i])
        break

# find point 4
for i in range(height-1, -1, -1):
    B = img.item(i, center_width, 0)
    G = img.item(i, center_width, 1)
    R = img.item(i, center_width, 2)
    if B+G+R > threshold:
        point.append([center_width,i])
        break

part1_height = (point[3][1]-point[2][1])//3+point[2][1]
part2_height = (point[3][1]-point[2][1])//3*2+point[2][1]
part3_height = (part2_height + part1_height)//2
part4_height = (part3_height - part1_height) + part2_height

# find point 5
for i in range(width):
    B = img.item(part1_height, i, 0)
    G = img.item(part1_height, i, 1)
    R = img.item(part1_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part1_height])
        break

# find point 6
for i in range(width-1, -1, -1):
    B = img.item(part1_height, i, 0)
    G = img.item(part1_height, i, 1)
    R = img.item(part1_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part1_height])
        break

# find point 7
for i in range(width):
    B = img.item(part3_height, i, 0)
    G = img.item(part3_height, i, 1)
    R = img.item(part3_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part3_height])
        break

# find point 8
for i in range(width-1, -1, -1):
    B = img.item(part3_height, i, 0)
    G = img.item(part3_height, i, 1)
    R = img.item(part3_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part3_height])
        break

# find point 9
for i in range(width):
    B = img.item(part2_height, i, 0)
    G = img.item(part2_height, i, 1)
    R = img.item(part2_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part2_height])
        break

# find point 10
for i in range(width-1, -1, -1):
    B = img.item(part2_height, i, 0)
    G = img.item(part2_height, i, 1)
    R = img.item(part2_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part2_height])
        break

# find point 11
for i in range(width):
    B = img.item(part4_height, i, 0)
    G = img.item(part4_height, i, 1)
    R = img.item(part4_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part4_height])
        break

# find point 12
for i in range(width-1, -1, -1):
    B = img.item(part4_height, i, 0)
    G = img.item(part4_height, i, 1)
    R = img.item(part4_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part4_height])
        break




for i, pnt in enumerate(point):
    if (i+1)%2 == 0: val = pnt[0]-20
    else: val = pnt[0]
    cv2.putText(img, str(i+1), (val,pnt[1]-5), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255,255,255), 2)
    cv2.circle(img, (pnt[0], pnt[1]), 2, (255,255,255), 4)


print(point)
cv2.imshow('img', img)
cv2.imwrite('C:/Users/SungHyeon/Desktop/T/'+str(num)+'_point.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
