# model training python script ran in google colab
# keras model saved into the same directory

# -*- coding: utf-8 -*-
"""trash.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BfDR7MeJZfyPMwSFPSU2ZQGGI3rgKFWb
"""

import os
from matplotlib import pyplot
from tensorflow.python.keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.layers import BatchNormalization
from tensorflow.python.keras.layers import Dropout
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Flatten
from tensorflow.python.keras.layers import MaxPooling2D
from tensorflow.python.keras.layers import Conv2D
from tensorflow.python.keras.models import Sequential
from tensorflow import keras
from tensorflow.python.keras.preprocessing import image
import numpy as np
import tensorflow_hub as hub
import tensorflow as tf
import matplotlib.pylab as plt
from google.colab import drive
drive.mount('/content/gdrive')


waste2 = Sequential()

waste2.add(Conv2D(64, (3, 3), input_shape=(64, 64, 3), activation='relu'))

waste2.add(MaxPooling2D(pool_size=(2, 2)))
# waste2.add(Dropout(0.2))

# waste.add(Conv2D(32,(3,3),activation='relu'))

# waste.add(MaxPooling2D(pool_size=(2,2)))
# waste.add(Dropout(0.2))

# waste2.add(Conv2D(32,(3,3),activation='relu'))
# waste2.add(MaxPooling2D(pool_size=(2,2)))
# waste2.add(Dropout(0.5))

waste2.add(Flatten())

waste2.add(Dense(units=64, activation="relu"))
# waste.add(BatchNormalization())
waste2.add(Dense(units=1, activation="sigmoid"))

opt = SGD(lr=0.001, momentum=0.9, decay=0.01)

waste2.compile(optimizer='adam', loss='binary_crossentropy',
               metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset-2/train',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset-2/test',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

history = waste2.fit_generator(training_set,
                               steps_per_epoch=500,
                               epochs=5,
                               validation_data=test_set,
                               validation_steps=100)

_, acc = waste2.evaluate_generator(test_set, steps=len(test_set), verbose=0)
print('> %.3f' % (acc * 100.0))


def summarize_diagnostics(history):
    pyplot.title('Cross Entropy Loss')
    pyplot.plot(history.history['loss'], color='blue', label='train')
    pyplot.plot(history.history['val_loss'], color='orange', label='test')

# 	filename = sys.argv[0].split('/')[-1]
# 	pyplot.savefig(filename + '_plot.png')
# 	pyplot.close()


summarize_diagnostics(history)

trash_filepaths = []
for (path, dirnames, filenames) in os.walk('dataset-3/test/trash'):
    trash_filepaths.extend(os.path.join(path, name) for name in filenames)

trash_count = len(trash_filepaths)
trash_filepaths_re = trash_filepaths[100:200]
print(trash_filepaths_re)
print(trash_count)

prediction_results = []
x = 0
y = 0
for i in trash_filepaths_re:
    if i != 'dataset-3/train/recycle/.DS_Store':
        test_image = image.load_img(i, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
#     test_image = test_image.reshape(64,64)
#     test_image = test_image.astype('float32')
#     test_image = test_image - [123.68, 116.779, 103.939]
        result = waste2.predict(test_image)
        training_set.class_indices
        if result[0][0] == 0:
            prediction = 'recycle'
            x = x+1
        else:
            prediction = 'trash'
            y = y+1
    prediction_results.append(prediction)

print(prediction_results)
print(training_set.class_indices)
print(test_set.class_indices)

print(result)
print(x)
print(y)

test_image = image.load_img('http://google.com', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
#     test_image = test_image.reshape(64,64)
#     test_image = test_image.astype('float32')
#     test_image = test_image - [123.68, 116.779, 103.939]
# result = waste2.predict(test_image)
# training_set.class_indices
# if result[0][0] == 0:
#   prediction = 'recycle'
# else:
#   prediction = 'trash'

print(test_image)
print(result)
print(prediction)

# Run this cell to mount your Google Drive.
drive.mount('/content/drive')

waste2.save('goodenough.h5')
