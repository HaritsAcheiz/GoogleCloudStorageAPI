from flask import Flask, render_template, request
from google.cloud import storage

app = Flask(__name__)

# Configure the Google Cloud Storage client
storage_client = storage.Client()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    # Get the uploaded image file
    image_file = request.files['image']

    # Create a new bucket and specify its name
    bucket_name = 'googlecloudstoragebucket'
    bucket = storage_client.create_bucket(bucket_name)

    # Generate unique filename for the uploaded image
    image_filename = image_file.filename
    blob_name = f'uploads/{image_filename}'

    # Upload the image file to the bucket
    blob = bucket.blob(blob_name)
    blob.upload_from_file(image_file)

    return 'Image uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)