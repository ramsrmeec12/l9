
import cv2

img = cv2.imread("download.jpeg")
if img is None: exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")\
        .detectMultiScale(gray, 1.1, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

