from cv2 import cv2
import numpy as np
from pyzbar import pyzbar
import os

p=cv2.VideoCapture(0)
printList = []
while True:
	ret, m1=p.read()
	if ret==True:
		cv2.imshow("Image 1.png",m1)
		r=pyzbar.decode(m1)
		if len(r)>0:
			#os.system("cls")
			for i,d in enumerate(r):
				if d.data not in printList:
					printList.append(d.data)
					print("第",len(printList),"個條碼，類型：",d.type,"，內容：",d.data.decode("UTF-8"))
					print(printList[-1].decode("UTF-8"))
	cv2.waitKey(50)
cv2.destroyAllWindows()
