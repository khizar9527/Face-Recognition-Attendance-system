import cv2
import numpy as np
import face_recognition
import os
import tkinter 
from tkinter import *
from PIL import  Image,ImageTk
import pandas  as pd
from datetime import datetime


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
def qt():
    
    cv2.destroyAllWindows()
    

def face_recogn1():
    path = 'imagesAttendence'
   
   
    images = []
    classNames = []
    myList = os.listdir(path)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)
    while TRUE:
        
       
        success,img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesFrame = face_recognition.face_locations(imgS)
        encodesFrame = face_recognition.face_encodings(imgS,facesFrame)
       
        for encodeFace,faceLoc in zip(encodesFrame,facesFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            print(matches)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex] and faceDis[matchIndex]<=0.47:
                name = classNames[matchIndex].upper()
                print(name)
                
                y1,x2,y2,x1=faceLoc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                
                enter(name)
            else:
                y1,x2,y2,x1=faceLoc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(img,"Press Esc button to quit",(10,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,0),1)
        cv2.imshow('Face Recognition',img)
        key=cv2.waitKey(1)
       
        if key%256==27:
            cap.release()
            cv2.destroyAllWindows()
            break
          
   
        

def face_recogn2():
    path = 'imagesAttendence'
    images = []
    classNames = []
    myList = os.listdir(path)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)
    while TRUE:
        success,img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesFrame = face_recognition.face_locations(imgS)
        encodesFrame = face_recognition.face_encodings(imgS,facesFrame)
        for encodeFace,faceLoc in zip(encodesFrame,facesFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            print(matches)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex] and faceDis[matchIndex]<=0.47:
                name = classNames[matchIndex].upper()
                print(name)
                y1,x2,y2,x1=faceLoc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3)
                exit(name)
            else:
                y1,x2,y2,x1=faceLoc
                y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.imshow('Face Recognition',img)
        key=cv2.waitKey(1)
        if key%256==27:
            break
def readfile():
    namelist=[]
    entrylist=[]
    f=open('attendance.csv','r')
    for i in f:
        entry=i.split(',')
        namelist.append(entry[0])
        entrylist.append(entry[3])
    f.close()
    print(entrylist)
    return namelist,entrylist

def enter(name):
    print("start of enter process")
    count=0
    namelist,entrylist=readfile()
    for i,j in zip(namelist,entrylist):
        print(i,j)
        if name==i:
            if j=='Enter' or j=='Enter\n':
                count=1
            if j=='Exit' or j=='Exit\n':
                count=0
    if count==0:
        now=datetime.now()
        timestring=now.strftime('%H:%M:%S')
        datestring=str(now.date())
        b=open('attendance.csv',"a")
        b.writelines(f'\n{name},{timestring},{datestring},{"Enter"}')  
        b.close()
    print("over of enter process")

def exit(name):
    print("start of exit process")
    count=0
    namelist,entrylist=readfile()
    for i,j in zip(namelist,entrylist):
        print(i,j)
        if name==i:
            if j=='Enter' or j=='Enter\n':
                count=1
            if j=='Exit' or j=='Exit\n':
                count=0
    if count==1:
        now=datetime.now()
        timestring=now.strftime('%H:%M:%S')
        datestring=str(now.date())
        b=open('attendance.csv',"a")
        b.writelines(f'\n{name},{timestring},{datestring},{"Exit"}')  
        b.close()
    print("over of exit process")
    
def attend():
    exc2=pd.read_csv('attendance.csv')
    print(exc2)

# stop=False
# def stop():
#     if stop==True:
#         break

def frame():
    window=Tk()
    window.geometry('1360x728')
    window.title("FACE RECOGNITION")
   
    canvass=Canvas(window,width=1700,height=900)
    canvass.place(x=0,y=0)
    image=Image.open("upload_image//image5.jpg")
    image2=image.resize((1750,850))
    photo=ImageTk.PhotoImage(image2)
    photo2=canvass.create_image(0,0,image=photo,anchor=NW)
    iconA=Image.open("upload_image//image3.jpg")
    iconA2=ImageTk.PhotoImage(iconA)
    window_button1=Button(window,command=face_recogn1,width=164,height=120,image=iconA2)
    window_button1.pack()
    window_button1.place(x=217,y=310)
    window_button2=Button(window,text="ENTER",command=face_recogn1,width=18,height=2,bg='green',fg='white',activebackground='green',activeforeground='gold',font='time')
    window_button2.pack()
    window_button2.place(x=216,y=436)
    iconc=Image.open("upload_image//image4.jpg")
    iconc2=ImageTk.PhotoImage(iconc)
    window_button5=Button(window,command=face_recogn2,width=164,height=120,image=iconc2)
    window_button5.pack()
    window_button5.place(x=648,y=310)
    window_button6=Button(window,text="EXIT",command=face_recogn2,width=18,height=2,bg='red',fg='white',activebackground='red',activeforeground='gold',font='time')
    window_button6.pack()
    window_button6.place(x=647,y=436)
    iconB=Image.open("upload_image//image7.jpg")
    iconB2=ImageTk.PhotoImage(iconB)
    window_button3=Button(window,command=attend,width=164,height=120,image=iconB2)
    window_button3.pack()
    window_button3.place(x=1070,y=310)
    window_button4=Button(window,text="ATTENDANCE SHEET",command=attend,width=18,height=2,bg="#252525",fg='white',activebackground='#252525',activeforeground='gold',font='time')
    window_button4.pack()
    window_button4.place(x=1069,y=436)
    window.mainloop()

frame()

