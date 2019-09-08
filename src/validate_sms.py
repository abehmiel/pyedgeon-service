from flask import request
import logging

def validate_sms(request):
    """validate and clean data from SMS message.
    Input -> Dict of str:str
    Output -> Dict of {str: Bool, str:str}
    If validated, output . Otherwise, contains 'error' field and msg
    """

    try:
        text = request['Body']
    except IndexError as e:
        err = 'No "Body" field in request'
        errdict = {'validated': False, 'error': err}
        logging.warning(err)
        return errdict

    try:
        assert isinstance(text, str)
    except AssertionError as e:
        err = 'Input is not a string'
        errdict = {'validated': False, 'error': err}
        logging.warning(err)
        return errdict

    try:
        assert len(text) < 20
    except AssertionError as e:
        err = 'Text is longer than 20 characters. Try a shorter phrase.'
        errdict = {'validated': False, 'error': err}
        logging.warning(err)
        return errdict

    try:
        assert len(text) > 6
    except AssertionError as e:
        err = 'Text is shorter than 6 characters. Try a longer phrase.'
        errdict = {'validated': False, 'error': err}
        logging.warning(err)
        return errdict

    return {'validated': True, 'error': 'OK'}

