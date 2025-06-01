from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import os
from PIL import Image
import uuid
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Load TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load labels
with open('labels.txt', 'r') as f:
    labels = [line.strip() for line in f.readlines()]

def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((input_details[0]['shape'][2], input_details[0]['shape'][1]))
    input_data = np.expand_dims(img, axis=0)
    if input_details[0]['dtype'] == np.float32:
        input_data = (np.float32(input_data) - 127.5) / 127.5  # Normalize if model expects float input
    return input_data

@app.route('/', methods=['GET', 'POST'])
def upload_and_classify():
    results_path = "results.json"
    results = {}

    # Load existing results if any
    if os.path.exists(results_path):
        with open(results_path, "r") as f:
            results = json.load(f)

    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            input_data = preprocess_image(filepath)
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])
            predicted_label = labels[np.argmax(output_data)]

            # Save result to JSON
            results[filename] = predicted_label
            with open(results_path, "w") as f:
                json.dump(results, f)

            return render_template('result.html', label=predicted_label, image_url=filepath)

    # List uploaded files with labels
    uploads = sorted(results.items(), key=lambda x: x[0], reverse=True)
    return render_template('index.html', uploads=uploads)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
