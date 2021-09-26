import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhooks', methods=['POST'])
def webhooks():
    body = request.json

    print(body)

    print ("******************************")

    print (body['data']['payload']['from']['phone_number'])
    print (body['data']['payload']['text'])
    print (body['data']['payload']['to']['phone_number'])

    return '', 200

if __name__ == "__main__":
    app.run(port=8001)