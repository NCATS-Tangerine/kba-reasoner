import connexion
from swagger_server.bio.knowledge.server.model.feedback import Feedback
from swagger_server.bio.knowledge.server.model.result import Result
from swagger_server.bio.knowledge.server.model.result_feedback import ResultFeedback
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_result(result_id):
    """
    Request stored result
    
    :param result_id: Integer identifier of the result to return
    :type result_id: int

    :rtype: Result
    """
    return 'do some magic!'


def get_result_feedback(result_id):
    """
    Request stored feedback for this result
    
    :param result_id: Integer identifier of the result to return
    :type result_id: int

    :rtype: ResultFeedback
    """
    return 'do some magic!'


def post_result_feedback(result_id, body):
    """
    Store feedback for a particular result
    
    :param result_id: Integer identifier of the result to return
    :type result_id: int
    :param body: Comment information
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Feedback.from_dict(connexion.request.get_json())
    return 'do some magic!'
