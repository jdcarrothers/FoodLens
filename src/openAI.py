import cv2
import base64
import os
import shutil
import requests
from flask_cors import CORS
import json
import textwrap
from flask import Flask,jsonify,request
app = Flask(__name__)
CORS(app)
api_key = "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"
@app.route ('/capture_and_save_frame', methods =['POST']) 
def capture_and_save_frame():
    imagePath, response, status_code = fetchFromJson() # gets the imageurl from the front end
    if imagePath:
        print(imagePath)#prints in log
        #enable the three commented methods for testing using image url relative to os system  
        # new_path = saveImageLocal(imagePath)    #saves the image to the local src in order for it to be acsessed by the python script
        # base64_image = encode_image(new_path)   #that new path gets incoded; allows chat gpt to process
        ai_response = AIReply(imagePath)     #ai responds with an answer regarding a possible recipe
        # removeImageLocal(new_path)              #removes the image after a response has been generated
        return jsonify({'result': ai_response}), 200 

    else:
        return response, status_code
    
def removeImageLocal(path):
    save_directory = 'src/'
    filename = os.path.basename(path)
    file_path = os.path.join(save_directory, filename)

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Image removed successfully from {file_path}")
            return True
        except OSError as e:
            print(f"Error removing image: {e}")
            return False
    else:
        print(f"Image not found at {file_path}")
        return False
    
def saveImageLocal(path):
    save_directory = 'src/'
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    filename = os.path.basename(path)
    new_path = os.path.join(save_directory, filename)

    try:
        shutil.copy(path, new_path)
        print(f"Image saved successfully to {new_path}")
        return new_path
    except IOError as e:
        print(f"Error saving image: {e}")
        return None
def fetchFromJson():
    try:
        data = request.get_json()
        imageFile = data.get('imageFile')
        if imageFile is None:
            return None, jsonify({'error': 'Missing the data'}), 400
        print("Gathered image data")
        return imageFile, None, 200
    except Exception as e:
        return None, jsonify({'error': str(e)}), 500

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def AIReply(base64_image):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What am i showing you will be ingredients, they will probably be random ingredients,start your response by provide a brief description of the ingredients you see and what you can make with them. You must come up with something that is a real recipe, but something that is possible to make with the ingredients you see. Keep the answer breif!"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_text = json.loads(response.text)

    if response_text.get('choices'):
        ai_response = response_text['choices'][0]['message']['content']
    else:
        ai_response = "No response received."
    print(ai_response)
    return ai_response

if __name__ == '__main__':
    app.run(debug=True)