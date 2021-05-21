import cv2
# RGB 는 openCV에서 BGR로 읽고 nump로 처리한다.(빠르게 연산하기 위해서)
# 이미지 읽기
img = cv2.imread('1.png', 1)
print(img)
 
# 이미지 화면에 표시
cv2.imshow('Test Image', img)
cv2.waitKey(0)
# 이미지 윈도우 삭제
cv2.destroyAllWindows()