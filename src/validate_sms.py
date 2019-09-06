from flask import request
import logging

logging.basicConfig(filename='logs/validation.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

def validate_sms(request):
    """validate and clean data from SMS message"""
    text = request['body']
    if not isinstance(text, str):
        logging.warning('input is not a string')
    if len(text) > 20:
        logging.warning('text is longer than 20 characters')
    if len(text) < 6:
        logging.warning('text is shorter than 6 characters')

    return request

