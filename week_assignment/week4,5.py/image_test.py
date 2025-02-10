import cv2
image=cv2.imread(r"week_assignment\week4,5.py\image.jpg")
(h,w)=image.shape[:2]
center=(w//2,h//2)
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows() 