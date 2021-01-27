import cv2,time

print("1. Face detection Through Webcam\n2. Face detection in video.\n3. Face Detection in Image.")
x=int(input("Enter Choice :"))
if x==1:
    try:
        model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        video=cv2.VideoCapture(0)
        print("......... Press q for terminate.........!")
        while True:
            check,frame=video.read()
            gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face=model.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

            for x,y,w,h in face:
                frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),3)
            # time.sleep(3)
            cv2.imshow("WebCam-detecting faces",frame)
            if cv2.waitKey(1)==ord("q"):
                video.release()
                cv2.destroyAllWindows() 
                break
        print("congratulation...!!!!!!")
    except:
        print("!!! File Not found.or \nKeep the reference file in same directory.")


elif x==2:
    print("Enter path to video :")
    path =input(" path-  :")
    try:
        model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        video=cv2.VideoCapture(str(path))
        print("......... Press q for terminate.........!")
        while True:
            check,frame=video.read()
            gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face=model.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

            for x,y,w,h in face:
                frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),3)
            # time.sleep(3)
            cv2.imshow(str(path),frame)
            if cv2.waitKey(1)==ord("q"):
                video.release()
                cv2.destroyAllWindows() 
                break
        print("congratulation...!!!!!!")
    except:
        print("!!! File Not found.or \nKeep the reference file in same directory.")


elif x==3:
    print("Enter path to Image")
    path=input("path : ")
    try:
        model=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        img=cv2.imread(str(path))
        gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=model.detectMultiScale(gimg,scaleFactor=1.05,minNeighbors=5)
        for x,y,w,h in face:
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        print("..Faces are detected...")
        cv2.imshow(str(path),img)
        cv2.waitKey(0)
        
    except:

        print("!!! File Not found.\nKeep the reference file in same directory.")
        

else :print("Invalid Input")
            