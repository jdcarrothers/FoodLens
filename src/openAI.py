import cv2
import base64
import os
import requests
from flask_cors import CORS
import json
import textwrap
from flask import Flask,jsonify,request
app = Flask(__name__)
CORS(app)
api_key = "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"

def capture_and_save_frame():
    cap = cv2.VideoCapture(2)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Webcam Preview', frame)
        # Press 's' to save
        if cv2.waitKey(1) & 0xFF == ord('s'):
            resized_frame = cv2.resize(frame, (512, 512))
            cv2.imwrite('captured_frame.jpg', resized_frame)
            break
    cap.release()
    return 'captured_frame.jpg'

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = capture_and_save_frame()
base64_image = encode_image(image_path)

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
                    "text": "What am i showing you will be ingredients, they will probably be random ingredients, provide a quick description of the ingredients you see and what you can make with them. You must come up with something that is a real recipe, but something that is possible to make with the ingredients you see."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
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
def wrap_text(text, width):
    return textwrap.wrap(text, width=width)

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    height, width = frame.shape[:2]
    wrapped_text = wrap_text(ai_response, int(width / 20))
    for i, line in enumerate(wrapped_text):
        cv2.putText(frame, line, (20, height - 20 * (len(wrapped_text) - i)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('Webcam Preview', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
os.remove(image_path)
