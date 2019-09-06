#Service that receives SMS from twilio and turns the body text into an optical
# illusion button with pyedgeon, then uploading that image to imgur, using the
# public imgur link as an image source, and then sending that image via MMS to
# the client

import requests
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from pyedgeon import Pyedgeon
from src.validate_sms import validate_sms
from src.imgur_lib import *
from pathlib import Path
import logging

logging.basicConfig(filename='logs/app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# twilio credential go here

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming with a simple text message."""

    resp = MessagingResponse()
    # validate input and prepare txt, msg_id
    clean_request = validate_sms(request)
    text = clean_request.values['body']
    msg_id = clean_request.values['sid']
    # create illusion object & save to file
    ill = Pyedgeon(illusion_text=text,
                   file_path='static/',
                   filename=msg_id,
                   file_ext='.png')
    ill.create()
    # take created file and push to imgur anonymously
    res = img_upload(ill.get_file_path(), ill.illusion_text, msg_id)
    img_link = res["link"]
    resp.messages(body="Thanks for using pyedgeon!",
                  media_url=img_link)

    return resp

if __name__ == "__main__":
    app.run(debug=True)
