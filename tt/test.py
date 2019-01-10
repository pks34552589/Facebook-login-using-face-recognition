import face_recognition
import cv2

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
manoj_image = face_recognition.load_image_file("manoj.jpg")
manoj_face_encoding = face_recognition.face_encodings(manoj_image)[0]

# Load a second sample picture and learn how to recognize it.
rishi_image = face_recognition.load_image_file("rishi.jpg")
rishi_face_encoding = face_recognition.face_encodings(rishi_image)[0]

# Load a second sample picture and learn how to recognize it.
pks_image = face_recognition.load_image_file("pks.jpg")
pks_face_encoding = face_recognition.face_encodings(pks_image)[0]

# Load a second sample picture and learn how to recognize it.
abhi_image = face_recognition.load_image_file("abhi.jpg")
abhi_face_encoding = face_recognition.face_encodings(abhi_image)[0]

# Load a second sample picture and learn how to recognize it.
atul_image = face_recognition.load_image_file("atul.jpg")
atul_face_encoding = face_recognition.face_encodings(atul_image)[0]

# Load a second sample picture and learn how to recognize it.
pradip_image = face_recognition.load_image_file("pradip.jpg")
pradip_face_encoding = face_recognition.face_encodings(pradip_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    manoj_face_encoding,
    rishi_face_encoding,
    pks_face_encoding,
    abhi_face_encoding,
    atul_face_encoding,
    pradip_face_encoding,
]
known_face_names = [
    "manoj",
    "motu",
    "pranay",
    "abhi",
    "atul",
    "pradip"
]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Pata nhi"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (100, 0, 50), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - (int)((top-bottom)/10)), (right, bottom), (100, 0, 50), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 2, bottom), font, 1.0, (0,0,0), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()