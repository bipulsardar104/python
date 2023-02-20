# import io
# import os
# from flask import Flask, request, jsonify
# from google.cloud import vision
# from google.cloud.vision_v1 import types
# from google.oauth2 import service_account

# app = Flask(__name__)

# # Set the path to your service account key file
# key_path = './text.json'

# # Authenticate the client
# credentials = service_account.Credentials.from_service_account_file(key_path)
# client = vision.ImageAnnotatorClient(credentials=credentials)

# @app.route('/api/analyze_image', methods=['POST'])
# def analyze_image():
#     # Get the image file from the request
#     image_file = request.files['image']

#     # Load the image into memory
#     content = image_file.read()

#     image = types.Image(content=content)

#     # Analyze the image
#     response = client.label_detection(image=image)
#     labels = response.label_annotations

#     # Print the labels
#     results = []
#     for label in labels:
#         results.append(label.description)

#     # Return the results as a JSON object
#     return jsonify({'results': results})

# if __name__ == '__main__':
#     app.run(debug=True)


import io
import os
from flask import Flask, request, jsonify
from google.cloud import vision
from google.cloud.vision_v1 import types
from google.oauth2 import service_account

app = Flask(__name__)

# Set the path to your service account key file
key_path = './text.json'

# Authenticate the client
credentials = service_account.Credentials.from_service_account_file(key_path)
client = vision.ImageAnnotatorClient(credentials=credentials)

@app.route('/api/analyze_image', methods=['POST'])
def analyze_image():
    # Get the image file from the request
    image_file = request.files['image']

    # Load the image into memory
    content = image_file.read()

    image = types.Image(content=content)

    try:
        # Analyze the image
        response = client.label_detection(image=image)
        labels = response.label_annotations

        # Print the labels to the console
        results = []
        for label in labels:
            results.append(label.description)
            print(label.description)

        # Return the results as a JSON object
        return jsonify({'results': results})

    except Exception as e:
        # Return an error message if an exception occurs
        error_message = str(e)
        print(error_message)
        return jsonify({'error': error_message})

if __name__ == '__main__':
    app.run(debug=True)

