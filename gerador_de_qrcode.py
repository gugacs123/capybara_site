from asyncore import ExitNow
from random import random
import qrcode
import random
import mysql.connector


resposta=str(input("Você deseja gerar um QRcode? S/N \n"))

if (resposta=="S") or (resposta=="s"):
    dado=random.randrange(1,1000,2)
    img=qrcode.make(dado)
    img.show()
elif (resposta=="N") or (resposta=="n"):
    exit




        
        


    
    