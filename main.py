import cv2
#영상 이미지 읽기
src= cv2.imread("pictures/picture01.jpg")


#영상 디스플레이


dst1=cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
cv2.imshow('dst1', dst1)
dst2=src.copy()
_ , dst2= cv2.threshold(dst2, 127,255, cv2.THRESH_BINARY)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed = cv2.morphologyEx(dst2, cv2.MORPH_CLOSE, kernel)

edges = cv2.Canny(closed, 100, 200)
cv2.imshow('dst2', edges)

#마무리
cv2.waitkey(0)
cv2.destroyAllWindows()



