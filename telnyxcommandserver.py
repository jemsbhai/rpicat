import os
from flask import Flask, request
import telnyx

def sendsms(tonum, fromnum, msg):
    telnyx.api_key = "KEY017C1DC88EABF62211DC33AA838F213A_nQyoWbrBzChgaYkSM1feBI"

    your_telnyx_number = fromnum
    destination_number = tonum

    telnyx.Message.create(
        from_=your_telnyx_number,
        to=destination_number,
        text=msg,
    )



app = Flask(__name__)

@app.route('/webhooks', methods=['POST'])
def webhooks():
    body = request.json

    print(body)

    print ("******************************")

    print (body['data']['payload']['from']['phone_number'])
    print (body['data']['payload']['text'])
    print (body['data']['payload']['to'][0])
    # print (body['data']['payload']['to'][0][0]) 
    print (body['data']['payload']['to'][0]['phone_number'])

    print ("******************************")


    intext = body['data']['payload']['text']

    fromnum = body['data']['payload']['from']['phone_number']
    tonum = body['data']['payload']['to'][0]['phone_number']

    intext = intext.lower()

    if intext == "lastpic":
        sendsms(fromnum, tonum, "here is the last picture taken by rescuerover: https://storage.googleapis.com/hackybucket/last.jpg")
        return '', 200

    
    if intext == "latestpic":
        sendsms(fromnum, tonum, "here is the latest picture taken by rescuerover: https://storage.googleapis.com/hackybucket/latest.jpg")
        return '', 200

    if intext == "latestlocation":
        sendsms(fromnum, tonum, "here is the latest location of rescuerover: ")
        return '', 200

    if intext == "latestalarm":
        sendsms(fromnum, tonum, "here is the latest alarm detected by rescuerover: ")
        return '', 200

    if intext == "status":
        sendsms(fromnum, tonum, "rescuerover status: ")
        return '', 200


    if intext == "autoon":
        sendsms(fromnum, tonum, "rescuerover autonomous mode: on ")
        return '', 200

    if intext == "autooff":
        sendsms(fromnum, tonum, "rescuerover autonomous mode: off ")
        return '', 200

    if intext == "return":
        sendsms(fromnum, tonum, "rescurecover returning to base ")
        return '', 200

    if "notify" in intext:
        sendsms(fromnum, tonum, "rescurecover notification sent: " + intext)
        return '', 200


    sendsms(fromnum, tonum, "sorry, the command was not recognized")

    return '', 200

if __name__ == "__main__":
    app.run(port=8001)