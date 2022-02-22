import cv2 as cv


img = cv.imread("python/img1.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

card = cv.CascadeClassifier("C:/Users/User/Desktop/my_project/python/cascades/c05.xml")
cards = card.detectMultyScale(gray,1.1,4)

for x,y,w,h in card:
    cv.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),10)

cv.imshow("dfjhas",gray)
cv.waitKey(0)