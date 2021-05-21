import cv2

original = cv2.imread('uin.png', cv2.IMREAD_COLOR)
gray = cv2.imread('uin.png',cv2.IMREAD_GRAYSCALE)
 
img_crop = original[10:300,150:450].copy() # 세로[어디서부터:자르는크기] 가로[어디서부터:자르는크기]

print(len(original)) # 세로
print(len(original[0])) # 가로

cv2.imshow('Original', img_crop)
#cv2.imshow('Gray', gray)

cv2.imwrite("target1.jpg", img_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()