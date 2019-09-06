from imgurpython import ImgurClient
import urllib2
import os
import json
import logging

logging.basicConfig(filename='logs/imgur.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

client_id = '72437224179f262'
client_secret = 'e57c65c24a3c118921aec91b4cf65222a43184a3'
imgur_endpoint = 'https://api.imgur.com/3/'

def img_upload(file_path, text, msg_id):

	client = ImgurClient(client_id, client_secret)

	conf = {"album" : "pyedgeon-service-anon",
		 "description": text,
		 "title" : msg_id}
	res = client.upload_from_path(file_path, config = conf, anon = True)
	#print(res)
	#print(res["link"])
    return res
