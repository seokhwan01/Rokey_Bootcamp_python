import cv2

image=cv2.imread(r"ch21\opencv\sample.jpg")
resized=cv2.resize(image,(300,300))
cv2.imshow('Resized image',resized) #cv2.imread() : 이미지 로드
cv2.waitKey(0) #cv2.imshow() : 이미지를 OpenCV 창에서 표시
cv2.destroyAllWindows()
 