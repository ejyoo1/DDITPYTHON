import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0

# 모델 복원
loaded_model = tf.keras.models.load_model('model1.h5')
loaded_model.summary()

loss, acc = loaded_model.evaluate(x_test, y_test, verbose=2)
print('Loss: ', loss)
print('Acc: ', acc)