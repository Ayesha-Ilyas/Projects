import cv2
import numpy as np
import face_recognition

imgobama=face_recognition.load_image_file("bacisImgs/obama.jpg")
imgobama= cv2.cvtColor(imgobama,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file("bacisImgs/donald3.jpg")
imgTest= cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc= face_recognition.face_locations(imgobama)[0]
encodeobama= face_recognition.face_encodings(imgobama)[0]
cv2.rectangle(imgobama,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest= face_recognition.face_locations(imgTest)[0]
encodeTest= face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results= face_recognition.compare_faces([encodeobama],encodeTest)
faceDis= face_recognition.face_distance([encodeobama],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,225),2)

cv2.imshow("obama ",imgobama)
cv2.imshow("obama test",imgTest)
cv2.waitKey(0)
