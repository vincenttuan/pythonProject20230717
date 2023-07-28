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

    # 偵測人臉, 得到臉部的(x, y, w, h)
    #--------------------------------------------------------------------------
    faces = face_cascade.detectMultiScale(
        frame,  # 目標圖片
        scaleFactor=1.1,  # 檢測粒度(數字越小越精準(但速度慢), 反之數字越大越模糊(速度快))
        minNeighbors=5,  # 檢測次數(每個目標至少要檢測通過幾次才算成功，才被認定是 face)
        minSize=(30, 30),  # 搜尋比對最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE  # 比對類型: 影像
    )

    # 在 face 上畫矩形
    for (x, y, w, h) in faces:
        # 繪製參數 frame, 左上角座標, 右下角座標, BGR色碼, 框線的寬度
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # --------------------------------------------------------------------------

    # 將 frame 顯示
    cv2.imshow('My Face', frame)
    # 按下 q 離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()





