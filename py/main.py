import base64
import numpy as np
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.models import load_model

# warnings.filterwarnings('ignore')
name = sys.argv[1]  # name of file
data = sys.argv[2]  # base64 data


def predictTrash(name, data):

    # load model
    trash = load_model('py/keras.h5')

    # convert and save the image
    filename = name
    with open(filename, 'wb') as f:
        data = base64.b64decode(data)
        f.write(data)

    # interpret the image
    test_image = image.load_img(filename, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    result = trash.predict(test_image)
    if result[0][0] == 0:
        prediction = 'recycle'
    else:
        prediction = 'trash'

    print(prediction)


predictTrash(name, data)
