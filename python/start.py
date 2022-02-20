import cv2 as cv

def yle(path):
    img = cv.imread(path)
    print(path)
    imgg = cv.cvtColor(img,cv.COLOR_BGR2GRAY,)
    cv.imwrite(path,imgg)

path = 'C:/Users/User/Desktop/my_project/cards/Modern/'
cardnames = ('c','d','h','s')
i=0
while i < 4:
    k=1
    while k <=13:
        if k<10:
            name=path+cardnames[i]+'0'+str(k)+'.png'
        else:
            name=path+cardnames[i]+str(k)+'.png'
        yle(name)
        k+=1
    i+=1
