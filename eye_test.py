import cv2 
from longest_word import get_words

word_obj = get_words()
word_list = word_obj.words
word_index = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
cap = cv2.VideoCapture(0) 
print_thresh = False
switch = False
thresh = False
thresh_val=0
font = cv2.FONT_HERSHEY_SIMPLEX
while 1: 
    ret, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    if(word_index<=len(word_list)-1):
        cv2.putText(img,word_list[word_index],(200,200), font, 3, (255,0,0),2, cv2.LINE_AA)
    else:
        cv2.putText(img,"Out of words",(200,200), font, 1, (255,0,0),2, cv2.LINE_AA)       
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray) 
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
        
        if(abs(thresh_val-y)>20 and thresh==True and switch == False):
            print('Will switch')
            switch = True
            word_index+=1
        elif(abs(thresh_val-y)<10 and switch==True and thresh==True):
            print('Back to normal')
            switch = False
    cv2.imshow('img',img) 



    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
    #If key input is an 'm'
    elif k == 109:
        print_thresh = True
        thresh_val = y
        thresh = True
        print('pressed')
    if(print_thresh==True):
        #print(y)
        #print(x)
        pass
cap.release() 
cv2.destroyAllWindows() 