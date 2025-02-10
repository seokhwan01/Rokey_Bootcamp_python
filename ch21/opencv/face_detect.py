import cv2
import matplotlib.pyplot as plt
print(cv2.data.haarcascades)
#이미지 로드
image=cv2.imread(r"ch21\opencv\sample.jpg")
face_path=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(face_path)
#흑백 변환
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#얼굴 검출 진행
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

#검출된 얼굴에 사각형 그리기
for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h),(255,0,0),2)
#결과 출력
cv2.imshow("Face detection",image)
cv2.waitKey(0)
cv2.destroyAllWindows()