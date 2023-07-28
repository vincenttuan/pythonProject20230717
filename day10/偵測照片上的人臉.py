import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
# 讀取影像檔
frame = cv2.imread('sample_image/test.jpg')
# print(frame)
# 將彩色圖片(BGR)進行(GRAY)處理以增加效率
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# print(gray)

# 顯示圖片
cv2.imshow('My Image', gray)  # frame: 彩色, gray: 灰色

# 在圖上按下任意鍵離開
c = cv2.waitKey(0)
print(c)


