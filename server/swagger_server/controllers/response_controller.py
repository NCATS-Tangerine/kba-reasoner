import connexion
from swagger_server.bio.knowledge.server.model.response import Response
from swagger_server.bio.knowledge.server.model.response_feedback import ResponseFeedback
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_response(response_id):
    """
    Request stored responses and results
    
    :param response_id: Integer identifier of the response to return
    :type response_id: int

    :rtype: Response
    """
    return 'do some magic!'


def get_response_feedback(response_id):
    """
    Request stored feedback for this response
    
    :param response_id: Integer identifier of the response to return
    :type response_id: int

    :rtype: ResponseFeedback
    """
    return 'do some magic!'
