import cv2 as cv

def yle(path,path2):
    img = cv.imread(path)
    print(path)
    imgg = cv.cvtColor(img,cv.COLOR_BGR2GRAY,)
    cv.imwrite(path2,imgg)

path = 'C:/Users/User/Desktop/my_project/cards/PNG-cards/'
path2 = 'C:/Users/User/Desktop/my_project/cards/muteli/'
cardnames = ('c','d','h','s')
ylenames = ('_of_clubs','_of_diamonds','_of_hearts','_of_spades')
meore = ('jack','queen','king','ace')
i=0
while i < 4:
    k=1
    while k <=12:
        if k<2:
            name=path2+cardnames[i]+'0'+str(k)+'.png'
            oldname = path + meore[3]+ylenames[i]+'.png'
        elif k>1 and k<=10:
            name=path2+cardnames[i]+'0'+str(k)+'.png'
            oldname = path + str(k)+ylenames[i]+'.png' 
        else:
            name=path2+cardnames[i]+str(k)+'.png'
            oldname = path + meore[k-10]+ylenames[i]+'.png' 
        yle(oldname,name)
        k+=1
    i+=1
