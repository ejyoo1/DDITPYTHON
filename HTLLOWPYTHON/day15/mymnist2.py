from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np
import cv2


(train_images, train_labels), (test_images, test_labels) = mnist.load_data() #keras.datasets 로드 (인터넷 다운로드)

print(train_images)
print(len(train_images))
print(len(train_labels))

print(test_labels)
print(len(test_images))
print(len(test_labels))

print(train_images[1]) # 이미지
print(train_labels[1]) # 트레이닝 숫자 번호

arr2d = train_images[1]
print(arr2d)
for i in arr2d:
    for j in i:
        if j == 0:
            print("0",end="")
        else:
            print("1",end="")
    print()
    
arr2d_np = np.array(arr2d,dtype=np.uint8)

print(arr2d_np.shape)
cv2.imshow('0', arr2d_np)

cv2.imwrite("train/0.jpg", arr2d_np)

cv2.waitKey(0)
cv2.destroyAllWindows()