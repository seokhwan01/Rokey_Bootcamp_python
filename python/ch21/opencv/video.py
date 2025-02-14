import cv2
cap=cv2.VideoCapture(0)
#cv2.VideoCapture(0)를 사용하여 웹캠에서 영상을 가져오기

while True:
    ret,frame=cap.read()
    if not ret:
        break
    edge=cv2.Canny(frame,100,200)#cv2.Canny()를 이용해 실시간으로 엣지 검출을 수행
    cv2.imshow("Edge detection",edge)#cv2.imshow()를 사용하여 결과를 화면에 표시
    if cv2.waitKey(1)==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
