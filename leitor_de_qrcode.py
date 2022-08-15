import imghdr
import cv2
import numpy as np
from pyzbar.pyzbar import decode
###########



# img = cv2.imread('confere_qr.png')
# pts2= barcode.rect
            # cv2.putText(img,myData,(pts2[0]),(pts2[1]),cv2.FONT_HERSHEY_COMPLEX,
            # 0.9,(255,0,255),2)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# while True:
#     for barcode in decode(img):
#         print(barcode.data)
sucess, img = cap.read()
myData= barcode.data.decode('utf-8')
if myData==str('ok'):
    print(myData,'opa lele')
    pts = np.array([barcode.polygon], np.int32)
    pts= pts.reshape((-1,1,2))
    cv2.polylines(img,[pts], True,(255,0,255),5)
    
    
else:
    print(myData,'acesso negado lele')
    pts = np.array([barcode.polygon], np.int32)
    pts= pts.reshape((-1,1,2))
    cv2.polylines(img,[pts], True,(255,0,255),5)
        

        

cv2.imshow('Result',img)
cv2.waitKey(1)
            # pts2= barcode.rect
            # cv2.putText(img,myData,(pts2[0]),(pts2[1]),cv2.FONT_HERSHEY_COMPLEX,
            # 0.9,(255,0,255),2)