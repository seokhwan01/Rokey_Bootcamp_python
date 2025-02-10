import cv2
image=cv2.imread(r"ch21\opencv\sample.jpg")
(h,w)=image.shape[:2]
center=(w//2,h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
 