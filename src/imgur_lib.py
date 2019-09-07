from imgurpython import ImgurClient
import os
import json
import logging


client_id = os.environ['IMGUR_ID']
client_secret = os.environ['IMGUR_SECRET']

def img_upload(file_path, text, msg_id):
    """ uploads a file to imgur anonymously using the API keys
    stored as environment variables"""
    client = ImgurClient(client_id, client_secret)
    conf = {"description": text,
            "title" : msg_id}
    res = client.upload_from_path(file_path, config=conf, anon = True)
    return res
