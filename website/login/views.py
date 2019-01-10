from django.http import HttpResponse
from .models import user
from django.shortcuts import render
import cv2 , time
import face_recognition
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
def index(Request) :
    all_users = user.objects.all()
    context = {
    'all_users' : all_users,
    }
    return render(Request,"login/index.html",context)

def details(Request, user_id) :
    return HttpResponse("<p>Details for user id : " + str(user_id) + "</p>")
 
def capture(Request):
	video = cv2.VideoCapture(0)
	check, frame = video.read()

	#gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
	cv2.imshow("Capturing" , frame)

	key = cv2.waitKey(1)
	#time.sleep(4)
	cv2.destroyWindow("Capturing")
	data = np.asarray(frame)
	frame = Image.fromarray(np.roll(data, 1, axis=-1))
	#frame=[frame[480][640][2] frame[480][640][1] frame[480][640][0]]
	
	#video.release()
	'''folder="login/known/"
	folder1="login/unknown/"
	#image = face_recognition.load_image_file(folder1)
	encoding = face_recognition.face_encodings(frame)[0]
	encoding= np.array(encoding)
	encoding=np.reshape(encoding,(128,1))
	print(encoding.shape)
	encodings=[]
	for filename in os.listdir(folder):
		img=cv2.imread(os.path.join(folder,filename))
		encode=face_recognition.face_encodings(img)[0]
		encode= np.array(encode)
		encode=np.reshape(encode,(128,1))
		print(encode.shape)
		encodings.append(encode)
	encodings= np.array(encodings)
	#encode=np.reshape(encode,(128,1)) 
	#print(encodings)
	encodings=np.squeeze(encodings)
	angle=cosine_similarity(encoding.T,encodings)'''
	return HttpResponse("<p>"+'''angle''' + str(frame.shape) +"</p>")
