import cv2
image=cv2.imread(r"ch21\opencv\sample.jpg")
blurred = cv2.GaussianBlur(image, (51, 51), 0)
cv2.imshow('Gaussian Blur', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
 