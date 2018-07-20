from flask import Flask, request
import os
import socket
import ast
import json
import re
import requests
import base64

app = Flask(__name__)

@app.route("/image/recognite", methods=['POST'])
def recognite_image():
    image = base64.b64decode(request.json['image']['body'])
    if os.path.isdir('/storage/images'):
        newFile = open('/storage/images/'+request.json['image']['name'], "wb")
        newFile.write(image)
    res = requests.post(url=os.environ['IMAGE_PROCESSOR_PATH'], data=image, headers={'Content-Type': 'application/octet-stream'})
    return json.dumps(res.json())



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)