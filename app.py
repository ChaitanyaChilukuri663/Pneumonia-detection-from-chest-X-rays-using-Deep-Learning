from flask import Flask, request, render_template
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)
model = load_model('model.h5')

# Preprocess function
def preprocess_image(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (150, 150))
    img = img.reshape(1, 150, 150, 1)
    img = img / 255.0
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        file_path = "static/" + file.filename
        file.save(file_path)
        img = preprocess_image(file_path)
        prediction = model.predict(img)
        prediction = 'Pneumonia Positive' if prediction[0][0] > 0.5 else 'Pneumonia Negative'
        return render_template('index.html', prediction=prediction, image=file_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
