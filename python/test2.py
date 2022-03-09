import cv2 as cv


# img = cv.imread("../cards/card_to_detect/test_image.png")
img = cv.imread(
    "/Users/beka/Documents/GitHub/my_project/cards/card_to_detect/test_image.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.data.haarcascades +
card = cv.CascadeClassifier(
    "/Users/beka/Documents/GitHub/my_project/python/cascades/haarcascade_number.xml")
cards = card.detectMultiScale(img, 1.1, 4)

for x, y, w, h in cards:
    cv.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 255), 10)

cv.imshow("dfjhas", gray)
cv.waitKey(0)
