import cv2
import numpy as np

# 캔버스 생성
img = np.zeros((400, 400, 3), np.uint8)

# 케이크 그리기
cv2.rectangle(img, (50, 150), (350, 250), (60, 60, 60), -1)
cv2.rectangle(img, (50, 150), (350, 200), (200, 200, 200), -1)

# 생크림 그리기
cv2.rectangle(img, (100, 180), (300, 200), (255, 255, 255), -1)

# 딸기 그리기
cv2.circle(img, (100, 100), 50, (0, 0, 255), -1)
cv2.circle(img, (300, 100), 50, (0, 0, 255), -1)

# 이미지 출력
cv2.imshow('Strawberry Cream Cake', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
