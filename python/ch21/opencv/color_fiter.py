import cv2
import numpy as np
image=cv2.imread(r"ch21\opencv\sample.jpg")

green_lower=np.array([35,100,100]) #초록색 하한값 (H: 35, S: 100, V: 100)
green_upper=np.array([85,255,255]) #초록색 상한값 (H: 85, S: 255, V: 255)

# 3. BGR 이미지를 HSV 색상 공간으로 변환
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# 4. HSV 이미지에서 초록색 범위에 해당하는 영역을 마스크로 생성
mask=cv2.inRange(hsv,green_lower,green_upper)

# 5. 원본 이미지와 마스크를 비트 연산하여 초록색만 추출
result=cv2.bitwise_and(image,image,mask=mask)

cv2.imshow("Green Color Filtering",result)
cv2.waitKey(0)
cv2.destroyAllWindows()