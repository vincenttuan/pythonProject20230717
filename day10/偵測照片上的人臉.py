import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
# 眼睛特徵檔
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')
# 微笑特徵檔
smile_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml')

# 讀取影像檔
frame = cv2.imread('sample_image/test.jpg')
# print(frame)
# 將彩色圖片(BGR)進行(GRAY)處理以增加效率
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# print(gray)

# 偵測人臉, 得到臉部的(x, y, w, h)
faces = face_cascade.detectMultiScale(
    gray,  # 目標圖片
    scaleFactor=1.1,  # 檢測粒度(數字越小越精準(但速度慢), 反之數字越大越模糊(速度快))
    minNeighbors=5,  # 檢測次數(每個目標至少要檢測通過幾次才算成功，才被認定是 face)
    minSize=(30, 30), # 搜尋比對最小尺寸
    flags=cv2.CASCADE_SCALE_IMAGE  # 比對類型: 影像
)
print('臉部座標 (x, y, w, h)', faces)

# 在 face 上畫矩形
for (x, y, w, h) in faces:
    # 繪製參數 frame, 左上角座標, 右下角座標, BGR色碼, 框線的寬度
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # 在 face 內進行眼睛偵測
    # 建立 roi 人臉區域
    roi_color = frame[y:y+h, x:x+w]  # 人臉區域-彩色(y, x)
    roi_gray = gray[y:y+h, x:x+w]  # 人臉區域-灰階(y, x)
    # 進行眼睛偵測
    eyes = eye_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # 進行眼睛框線繪製
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    # 微笑偵測
    smile = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # 進行微笑區域框線繪製
    for (sx, sy, sw, sh) in smile:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)


# 顯示圖片
cv2.imshow('My Image', frame)  # frame: 彩色, gray: 灰色

# 在圖上按下任意鍵離開
c = cv2.waitKey(0)
print(c)


