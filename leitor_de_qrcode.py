import cv2
from pyzbar.pyzbar import decode
import time
#####################################

cap = cv2.VideoCapture(0)
cap.set(3, 640) #largura
cap.set(4, 480) #altura
codigos_usados=[]

camera=True
while camera == True:
        sucess, frame = cap.read()
        for code in decode (frame):
            if code.data.decode('utf-8') not in codigos_usados:
                print("Pode passar")
                print(code.data.decode('utf-8'))
                codigos_usados.append(code.data.decode('utf-8'))
                time.sleep(5)
            
            elif code.data.decode('utf-8') in codigos_usados:
                print("Esse QR já foi usado")
                print(code.data.decode('utf-8'))
                time.sleep(5)
           
               
           
            # print(code.type)
            # print(code.data.decode('utf-8'))
 
        cv2.imshow('Testando o Scanner de QR code', frame)
        cv2.waitKey(1)


