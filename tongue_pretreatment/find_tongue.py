import numpy as np
import cv2

click = False     # Mouse 클릭된 상태 (false = 클릭 x / true = 클릭 o) : 마우스 눌렀을때 true로, 뗏을때 false로
x1,y1 = -1,-1
x2,y2 = -1,-1

# Mouse Callback함수 : 파라미터는 고정됨.
def draw_rectangle(event, x, y, flags, param):
    global x1,y1,x2,y2, click                                     # 전역변수 사용

    if event == cv2.EVENT_LBUTTONDOWN:                      # 마우스를 누른 상태
        click = True 
        x1, y1 = x,y
        print("사각형의 왼쪽위 설정 : (" + str(x1) + ", " + str(y1) + ")")
		
    elif event == cv2.EVENT_MOUSEMOVE:                      # 마우스 이동
        if click == True:                                   # 마우스를 누른 상태 일경우
            #cv2.rectangle(img,(x1,y1),(x,y),(255,0,0),3)
            #cv2.circle(img,(x,y),5,(0,255,0),-1)
            print("(" + str(x1) + ", " + str(y1) + "), (" + str(x) + ", " + str(y) + ")")

    elif event == cv2.EVENT_LBUTTONUP:
        click = False;                                      # 마우스를 떼면 상태 변경
        cv2.rectangle(img,(x1,y1),(x,y),(255,0,0),3)
        x2, y2 = x, y                                       # 마우스 떼어냈을 때의 좌표를 x2, y2에 설정
        print("(" + str(x1) + ", " + str(y1) + "), (" + str(x) + ", " + str(y) + ")")
	#cv2.circle(img,(x,y),5,(0,255,0),-1)
num = 11
img_dir = "C:/Users/SungHyeon/Desktop/tongue/"
img = cv2.imread(img_dir+str(num)+".JPG")
img2 = cv2.imread(img_dir+str(num)+".JPG")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle)                # 마우스 이벤트 후 callback 수행하는 함수 지정

# main문 : 키보드로 esc를 받을때까지 화면을 계속 보여준다.
while True:
    cv2.imshow('image', img)    # 화면을 보여준다.
    
    k = cv2.waitKey(1) & 0xFF   # 키보드 입력값을 받고
        
    if k == 27 or k ==ord('q'):               # esc를 누르면 종료
        break

    mask = np.zeros(img2.shape[:2],np.uint8)

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    if k==ord(' '):
        img2 = cv2.imread(img_dir+str(num)+".JPG")
        rect = (x1, y1, x2, y2)
        print("rect : ", rect)
        cv2.grabCut(img2,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        img2 = img2*mask2[:,:,np.newaxis]
        cv2.imshow('image2', img2)
        cv2.imwrite(img_dir+'trim_'+str(num)+'.JPG', img2)
        x1, y1, x2, y2 = -1, -1, -1, -1
        cv2.waitKey(0)
        
cv2.destroyAllWindows()