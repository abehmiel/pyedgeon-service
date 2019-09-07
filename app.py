#!/usr/bin/python3
#Service that receives SMS from twilio and turns the body text into an optical
# illusion button with pyedgeon, then uploading that image to imgur, using the
# public imgur link as an image source, and then sending that image via MMS to
# the client

import requests
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from pyedgeon import Pyedgeon
from src.validate_sms import validate_sms
from src.imgur_lib import *
from pathlib import Path
import logging

# create staic and logs folders if they don't exist
for f in ['static', 'logs']
    if not os.path.exists(f):
        os.makedirs(f)

logging.basicConfig(filename='logs/app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.debug = True

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming with a simple text message."""

    resp = MessagingResponse()
    # validate input and prepare txt, msg_id
    rq = request.form.to_dict()
    logging.info(str(rq))
    try:
        clean_request = validate_sms(rq)
    except:
        # TODO: handle errors
        pass

    text = clean_request['Body']
    msg_id = clean_request['MessageSid']
    # create illusion object & save to file
    ill = Pyedgeon(illusion_text=text,
                   file_path='static/',
                   file_name=msg_id,
                   file_ext='.png')
    ill.create()
    # take created file and push to imgur anonymously
    res = img_upload(ill.get_file_path(), ill.illusion_text, msg_id)
    img_link = str(res["link"])
    msg = resp.message("Thanks for using pyedgeon!")
    msg.media(img_link)
    logging.info('link:{link} text:{text} file:{fi} from:{fr}, to:{to} sid:{s}'
                 .format(link=img_link,
                         text=text,
                         fi=ill.get_file_path(),
                         fr=clean_request['From'],
                         to=clean_request['To'],
                         s=msg_id,
                         )
                 )
    return str(resp)

if __name__ == "__main__":
    app.run(port=5069)
