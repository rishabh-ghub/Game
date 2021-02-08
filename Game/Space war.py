import cv2
import copy
import time

bg=cv2.imread(r'gamebg.png')
reset=copy.copy(bg)
p1=cv2.imread(r'p1.png')
p2=cv2.imread(r'p2.png')

x=700
y=25


a=200
b=1313


h1=100
h2=100

s1=cv2.imread(r'spaceship1.png')
s2=cv2.imread(r'spaceship2.png')

while(1):
    if(h1<=0):
        cv2.imshow('test',p2)
        while(1):
            k=cv2.waitKey(0)
            if(k==ord('q')):
                cv2.destroyAllWindows()
                break
        h1=100
        h2=100
        bg=copy.copy(reset)
    if(h2<=0):
        cv2.imshow('test',p1)
        while(1):
            k=cv2.waitKey(0)
            if(k==ord('q')):
                cv2.destroyAllWindows()
                break
        h1=100
        h2=100
        bg=copy.copy(reset)
    
#bounds
    if(x<=125):
        x=x+10
        pass
    if(x>=716):
        x=x-10
        pass
    if(a<=125):
        a=a+10
        pass
    if(a>=716):
        a=a-10
        pass

    bg[65:75,30:30+h1*4,:]=255 #health 1
    bg[65:75,1308-h2*4:1308,:]=255 #health 2
    bg[x-25:x+25,y-25:y+25,:]=copy.copy(s1[:50,:50,:]) 
    bg[a-25:a+25,b-25:b+25,:]=copy.copy(s2[:50,:50,:])
    
    cv2.imshow('test',bg)
        
    k=cv2.waitKey(0)
    
    if(k==ord('w')):
        bg=copy.copy(reset)
        x=x-10
        pass
    
    elif(k==ord('z')):
        bg=copy.copy(reset)
        x=x+10
        pass

    elif(k==ord('s')):          
        bg[x-2:x+2,y+25:1338,:]=[0,0,255]
        if(a<=x+25):
            if(a>=x-25):
                h2=h2-5
                bg=copy.copy(reset)
                bg[x-2:x+2,y+25:1338,:]=[0,0,255]
                bg[65:75,1308-h2*4:1308,:]=255 #health 2
                cv2.imshow('test',bg)
        cv2.imshow('test',bg)
    
    elif(k==ord('i')):
        bg=copy.copy(reset)
        a=a-10
        pass
    
    elif(k==ord('m')):
        bg=copy.copy(reset)
        a=a+10
        pass

    elif(k==ord('j')):
        bg[a-2:a+2,0:b-25,:]=[0,255,0]
        if(x<=a+25):
            if(x>=a-25):
                h1=h1-5
                bg=copy.copy(reset)
                bg[a-2:a+2,0:b-25,:]=[0,255,0]
                bg[65:75,30:30+h1*4,:]=255 #health 1
                cv2.imshow('test',bg)
        cv2.imshow('test',bg)
    
    elif(k==ord('q')):
        cv2.destroyAllWindows()
        break
    
    else:
        bg=copy.copy(reset)
        

