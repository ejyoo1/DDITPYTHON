import cv2

original = cv2.imread('uin.png', cv2.IMREAD_COLOR)
 
img90 = cv2.rotate(original, cv2.ROTATE_90_CLOCKWISE) # 시계방향으로 90도 회전
img180 = cv2.rotate(original, cv2.ROTATE_180) # 180도 회전
img270 = cv2.rotate(original, cv2.ROTATE_90_COUNTERCLOCKWISE) # 반시계방향으로 90도 회전 
                                                         # = 시계방향으로 270도 회전
# 이미지 각도 기준 회전
#height, width, channel = src.shape #channel : RGB 정보 / Channel = Filter로 나오기도 함.
height, width, channel = original.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 10, 1) # 중심점 설정 후 10도 변환
dst = cv2.warpAffine(original, matrix, (width, height)) # 회전 동작 수행

cv2.imshow('original', original)
cv2.imshow('rotate90', img90)
cv2.imshow('rotate180', img180)
cv2.imshow('rotate270', img270)
cv2.imshow('matrix', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()