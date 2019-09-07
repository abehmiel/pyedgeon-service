from flask import request
import logging

def validate_sms(request):
    """validate and clean data from SMS message"""
    try:
        text = request['Body']
    except:
        logging.warning('no body in request')
    try:
        assert isinstance(text, str)
    except:
        logging.warning('input is not a string')

    try:
        assert len(text) > 20
    except:
        logging.warning('text is longer than 20 characters')

    try:
        assert len(text) < 6
    except:
        logging.warning('text is shorter than 6 characters')

    return request

