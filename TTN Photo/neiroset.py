# Импортируем

import numpy
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
%matplotlib inline
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras import utils
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import PIL.ImageOps

# делим дата сет на тестовую и обучающую выборку

(x_train, y_train), (x_test, y_test) = mnist.load_data()


class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Предварительная обработка данных

plt.figure()
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)

# нормализация данных

x_train = x_train / 255
x_test = x_test / 255

plt.figure()
plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)

# Создание модели нейронной сети

model = keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),
                          keras.layers.Dense(128, activation ="relu"),
                          keras.layers.Dense(10, activation="softmax")
                          ])

model.compile(optimizer=tf.keras.optimizers.SGD(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.summary()

# Обучение нейросети

model.fit(x_train,y_train, epochs=10)
model.save('mnist.h5')
print("Модель сохранена как mnist.h5")

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Результаты теста: ', test_acc)

predictions = model.predict(x_train)
predictions[7]

np.argmax(predictions[7])

y_train[7]

plt.figure()
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)

class_names[np.argmax(predictions[1])]

img = Image.open('tri.jpeg')
img = img.resize((28, 28))

img = img.convert('L')
img.save('greyscale.png')
new_new_image = Image.open('greyscale.png')
new_new_image = np.array(new_new_image)
new_new_image = new_new_image.reshape(28,28,1)
new_new_image = new_new_image/255.0

plt.figure()
plt.imshow(np.squeeze(new_new_image,))
# plt.imshow(new_new_image,cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)

res = model.predict(new_new_image)[0]
print(np.argmax(res), max(res))