import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('main/lemon.h5')

class_names = ['bad_quality', 'empty_background', 'good_quality']
def predict_quality(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(300, 300))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = tf.expand_dims(image_array, 0)
    
    prediction = model.predict(image_array)
    
    predicted_class = np.argmax(prediction[0])
    predicted_class_name = class_names[predicted_class]
    
    return{
        'predicted_class': predicted_class_name
    }