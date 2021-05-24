from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np
import cv2

# 숫자 파일 만들기
# 구글에서 수집하고 정제한 것을 이미지화
(train_images, train_labels), (test_images, test_labels) = mnist.load_data() #keras.datasets 로드 (인터넷 다운로드)
for i,img in enumerate(test_images):
    test = test_labels[i]
    print(str(test))
    
    #cv2.imwrite("test/"+str(test)+"_"+str(i)+".jpg", img)
    if i > 5:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()