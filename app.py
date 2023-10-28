import boto3
from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import tensorflow as tf
import io

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
S3_BUCKET = 'project-plant'
MODEL_PATH_1_S3_KEY = 'model_den.h5'

app = Flask(__name__)

# Initialize the S3 client
s3 = boto3.client(
    service_name='s3',
    region_name='me-central-1',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

BATCH_SIZE = 1

import tensorflow.keras.layers as L
import tempfile

def load_model_weights_from_s3(model, s3_bucket, s3_key):
    obj = s3.get_object(Bucket=s3_bucket, Key=s3_key)
    model_weights_data = obj['Body'].read()
    
    # Create a temporary file and write the model weights data to it
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        with open(tmp.name, 'wb') as f:
            f.write(model_weights_data)
        model.load_weights(tmp.name)
    
    return model

model1 = tf.keras.Sequential([
        tf.keras.applications.DenseNet201(
            input_shape=(768, 768, 3),
            weights='imagenet',
            include_top=False
        ),
        L.GlobalAveragePooling2D(),
        L.Dense(4, activation='softmax')
    ])

# model1 = load_model_weights_from_s3(model1, S3_BUCKET, MODEL_PATH_1_S3_KEY)
# model1.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['categorical_accuracy']
# )

def decode_image(filename, image_size=(768, 768)):
    bits = tf.io.read_file(filename)
    image = tf.image.decode_jpeg(bits, channels=3)
    image = tf.cast(image, tf.float32) / 255.0
    image = tf.image.resize(image, image_size)
    return image

def prepare_test_single_image_from_stream(image_stream, image_size=(768, 768)):
    image = tf.image.decode_jpeg(image_stream.read(), channels=3)
    image = tf.cast(image, tf.float32) / 255.0
    image = tf.image.resize(image, image_size)
    data = tf.data.Dataset.from_tensor_slices([image]).batch(BATCH_SIZE)
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return jsonify({'error': 'no file'}), 400
            file = request.files['file']
            if file.filename == '':
                return jsonify({'error': 'no file'}), 400

            # Use BytesIO to handle the image in-memory
            image_stream = io.BytesIO()
            file.save(image_stream)
            image_stream.seek(0)  # Reset stream position

            img_ds = prepare_test_single_image_from_stream(image_stream)
            # prediction, predicted_class = prepare_predictions(img_ds, model1)

            return jsonify({'prediction': f'{.5} is ddd'})

        return render_template('index.html')
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/s3-image/<path:image_name>')
def serve_s3_image(image_name):
    obj = s3.get_object(Bucket=S3_BUCKET, Key=image_name)
    image_data = obj['Body'].read()
    return app.response_class(image_data, content_type='image/jpeg')

def prepare_predictions(img_ds, model):
    classes = ['healthy', 'multiple_diseases', 'rust', 'scab']

    pred = model.predict(img_ds)

    max_value = np.max(pred) * 100
    max_index = np.argmax(pred)
    predicted_class = classes[max_index]
    formatted_max_value = "{:.3f}%".format(max_value)

    return formatted_max_value, predicted_class

if __name__ == '__main__':
    app.run(debug=True)
