import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy import linspace, exp
from scipy.special import gamma



# load image and shrink - it's massive
num = 6
img = cv2.imread('C:/Users/SungHyeon/Desktop/t/'+str(num)+'.jpg')
height, width = img.shape[:2]

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
part5_height = (part3_height - part1_height)//2 + part4_height

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


# find point 13
for i in range(width):
    B = img.item(part5_height, i, 0)
    G = img.item(part5_height, i, 1)
    R = img.item(part5_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part5_height])
        break

# find point 14
for i in range(width-1, -1, -1):
    B = img.item(part5_height, i, 0)
    G = img.item(part5_height, i, 1)
    R = img.item(part5_height, i, 2)
    if B+G+R > threshold:
        point.append([i,part5_height])
        break


#황태는 따로 처리함.
lowerBound = np.array([20, 100, 100])
upperBound = np.array([30, 255, 255])
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_mask = cv2.inRange(img_hsv, lowerBound, upperBound)
img_result = cv2.bitwise_and(img, img, mask = img_mask)

# %구하는 코드
coa_img = cv2.imread('C:/Users/SungHyeon/Desktop/t/'+str(num)+'_coated_tongue.jpg')
ori_img = cv2.imread('C:/Users/SungHyeon/Desktop/t/'+str(num)+'_origin_color.jpg')

height, width = img.shape[:2]
print('width: ', width, ' height: ', height)

coa_count = 0
ori_count = 0
yellow_count = 0

for i in range(height):
    for j in range(width):

        b = coa_img.item(i,j,0)
        g = coa_img.item(i,j,1)
        r = coa_img.item(i,j,2)
        
        bb = ori_img.item(i,j,0)
        gg = ori_img.item(i,j,1)
        rr = ori_img.item(i,j,2)

        if (b!=bb and g!=gg and R!=rr):
            if (bb+gg+rr<=threshold):
                coa_count += 1
            else: ori_count += 1

percent  = "%0.2f" % (coa_count / (coa_count+ori_count) * 100)


for i in range(height):
    for j in range(width):

        B = img_result.item(i,j,0)
        G = img_result.item(i,j,1)
        R = img_result.item(i,j,2)

        if(B+G+R > threshold):
            yellow_count += 1


#find coated tongue area(origin color)
pts = np.array([[point[3][0],point[3][1]], [point[12][0],point[12][1]], [point[13][0], point[13][1]]])
## (1) Crop the bounding rect
rect = cv2.boundingRect(pts)
x,y,w,h = rect
croped = img[y:y+h, x:x+w].copy()

## (2) make mask
pts = pts - pts.min(axis=0)

mask = np.zeros(croped.shape[:2], np.uint8)
cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

## (3) do bit-op
dst = cv2.bitwise_and(croped, croped, mask=mask)
dst_height, dst_width = dst.shape[:2]
count = 0
sum_B = 0
sum_G = 0
sum_R = 0
for i in range(dst_height):
    for j in range(dst_width):
        B = dst.item(i, j, 0)
        G = dst.item(i, j, 1)
        R = dst.item(i, j, 2)
        if B+G+R > threshold:
            sum_B += B
            sum_G += G
            sum_R += R
            count += 1
color = [sum_B//count, sum_G//count, sum_R//count]

print(color)
print(yellow_count)

b = [96, 60, 136]
a = [103, 97, 214]
c = [117, 117, 224]

if yellow_count >= 1000:
    print('황태입니다')
elif float(percent) >= 50:
    print('설태는 '+ percent +'%')
else:
    if np.sum(color) > np.sum(c):
        print('담백설 입니다')
        print('설태 주의')
    elif np.sum(color) < np.sum(b):
        print('심한홍설입니다')
        print('심장병주의')
    elif np.sum(color) < np.sum(a)-15:
        print('홍설일 가능성 있음')
    elif np.sum(color) > np.sum(a)+15:
        print('담백설일 가능성 있음')
        print('설태 주의')
    else:
        print('건강한 혀입니다')







shape = float(percent)
scale = 1
x = linspace(0, 100, 101)
y = x ** (shape - 1) * exp(-x / scale) / (scale ** shape * gamma(shape))


plt.figure(figsize=(12, 8))
plt.plot(x, y, label = 'num : '+str(num))
plt.xlabel('Coated-Rate')
plt.ylabel('Gamma-Value')
plt.title('Gamma Distribution(coated = '+str(shape)+'%, scale = 1, loc = 0)')
plt.grid()


plt.show()





cv2.waitKey(0)
cv2.destroyAllWindows()
