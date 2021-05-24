from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical


(train_images, train_labels), (test_images, test_labels) = mnist.load_data() #keras.datasets 로드 (인터넷 다운로드)

# print(train_images[0])
#
# print(train_images.shape)# (60000, 28, 28) 3차원 배열
# print(train_labels.shape)# (60000,) 1차원 배열
#
# print(test_images.shape)
print(train_labels.shape)
print(train_labels[1])

#2차원 배열로 변경
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255 # nump는 255까지인데 255로 나누면 0~1사이의 수만 나옴. => 시그모이드 함수는 0~1숫자가 놀아야 됨.
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# print(train_images[0]) # 1차원 배열
#
# print(train_images.shape)
# print(train_labels.shape)
#
# print(test_images.shape)
# print(test_labels.shape)

# out 0~9
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

print(train_labels.shape)
print(train_labels[1])

model = models.Sequential() # 신경망이라고 생각
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,))) # 신경 512개, input 784
model.add(layers.Dense(10, activation='softmax')) # output 10 (0~9)

# 컴파일
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128) # 5번 반복하면서 batch_size를 128로 신호를 제어함.

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)