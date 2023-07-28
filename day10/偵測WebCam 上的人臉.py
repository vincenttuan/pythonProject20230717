import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

# 設定 Webcam
cap = cv2.VideoCapture(0)  # 0 或 1, 2, ... 表示設備 id

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    ret, frame = cap.read()
    print(ret, frame)

    # 將 frame 顯示
    cv2.imshow('My Face', frame)
    # 按下 q 離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()





