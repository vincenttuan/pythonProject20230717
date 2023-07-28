import cv2

def load_cascades():
    # 加載特徵檔
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml')
    return face_cascade, eye_cascade, smile_cascade

def detect_faces(face_cascade, gray, frame):
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return faces, frame

def detect_eyes(eye_cascade, gray, frame, faces):
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
    return frame

def detect_smiles(smile_cascade, gray, frame, faces):
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
    return frame

def main():
    face_cascade, eye_cascade, smile_cascade = load_cascades()

    # 讀取影像檔
    frame = cv2.imread('sample_image/test.jpg')
    if frame is None:
        print("Failed to read image")
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces, frame = detect_faces(face_cascade, gray, frame)
    frame = detect_eyes(eye_cascade, gray, frame, faces)
    frame = detect_smiles(smile_cascade, gray, frame, faces)

    cv2.imshow('My Image', frame)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
