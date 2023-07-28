#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2

face_cascade =  cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
#num_people = set()

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    num_people = len(faces)
    cv2.putText(frame, f'Heads: {num_people}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('Frame', frame)
    
    #num_people.add(len(faces))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()


# In[ ]:




