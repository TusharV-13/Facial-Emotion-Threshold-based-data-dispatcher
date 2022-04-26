from keras.preprocessing.image import img_to_array
import imutils
import cv2
from tensorflow.keras.models import load_model
import numpy as np
from datetime import datetime

# import geocoder
# import gmplot
import time
# parameters for loading data and images
detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'

# hyper-parameters for bounding boxes shape
# loading models
face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised","neutral"]

f = open("Statistics.txt","w+")
f.truncate(0)

flag=0
# starting video streaming
cv2.namedWindow('Emotion Predictor')
camera = cv2.VideoCapture(0)
# count=0
count=[0]*7
start_time=time.time()
while(flag==0):
    frame = camera.read()[1]
    #reading the frame
    frame = imutils.resize(frame,width=300)
    frame = imutils.resize(frame,height=250)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    
    canvas = np.zeros((250, 300, 3), dtype="uint8")
    frameClone = frame.copy()

    end_time=time.time()

   
    if len(faces) > 0:
        for j in range(len(faces)):
            # faces = sorted(faces, reverse=True,key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = faces[j]
                # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
                # the ROI for classification via the CNN
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            
            
            preds = emotion_classifier.predict(roi)[0]
            emotion_probability = np.max(preds)
            label = EMOTIONS[preds.argmax()]
            
            if(label=="happy"):
                count[3]+=1
            elif(label=="neutral"):
                count[6]+=1
            elif(label=='sad'):
                count[4]+=1
            elif(label=="surprised"):
                count[5]+=1
            elif(label=="angry"):
                count[0]+=1
            elif(label=="disguist"):
                count[1]+=1
            elif(label=="scared"):
                count[2]+=1

            f.write("\nExpression Probabilities: ")
            for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                # construct the label text
                text = "{}: {:.2f}%".format(emotion, prob * 100)

                # draw the label + probability bar on the canvas
                # emoji_face = feelings_faces[np.argmax(preds)]

                w = int(prob * 300)
                cv2.rectangle(canvas, (7, (i * 35) + 5),(w, (i * 35) + 35), (0, 0, 255), -1)
                cv2.putText(canvas, text, (10, (i * 35) + 23),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45,(255, 255, 255), 2)
                cv2.putText(frameClone, label, (fX, fY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),(0, 0, 255), 2)
                print(label)
                f.write("("+text+" : "+str(w)+") ")
            f.write("\nExpression:"+str(label)+"\n")
            f.write("Time: "+str(datetime.now())+"\n")

            if(end_time-start_time>10):
              
                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                from email.mime.base import MIMEBase
                from email import encoders
                import os.path
                from collections import defaultdict as dd
                d=dd(int)

                for i in range(len(EMOTIONS)):
                    d[EMOTIONS[i]]=count[i]

                # print(d)
                f2 = open("emotions.txt","w+")
                f2.truncate(0)
                f2.write("Emotions:"+"\n"+str(d))
                f2.close()
                print(d)


                email = 'messagetusharverma@gmail.com'
                password ='kvhucttdeqjnklfj'
                send_to_email = 'herestushar@gmail.com'
                subject = '******EMOTION RECOGNITION******'
                message = '*****RESULTS****'
                file_location = 'Statistics.txt'
                # file_location1 = 'Location.txt'
                # file_location2 = 'Map.html'
                file_location3='details.txt'
                file_location4='emotions.txt'
                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" %filename)
                msg.attach(part)
               
                filename3= os.path.basename(file_location3)
                attachment3 = open(file_location3, "rb")
                part3 = MIMEBase('application', 'octet-stream')
                part3.set_payload((attachment3).read())
                encoders.encode_base64(part3)
                part3.add_header('Content-Disposition', "attachment; filename= %s" %filename3)
                msg.attach(part3)
                
                filename4= os.path.basename(file_location4)
                attachment4 = open(file_location4, "rb")
                part4 = MIMEBase('application', 'octet-stream')
                part4.set_payload((attachment4).read())
                encoders.encode_base64(part4)
                part4.add_header('Content-Disposition', "attachment; filename= %s" %filename4)
                msg.attach(part4)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                flag=1
    both = np.hstack((canvas,frameClone))
    cv2.imshow('Emotion Predictor', both)
    #cv2.imshow('Emotion Predictor', frameClone)
    #cv2.imshow("Probabilities", canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        f.close()
        break
f.close()
camera.release()
cv2.destroyAllWindows()