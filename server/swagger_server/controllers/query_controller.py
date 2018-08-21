import connexion
from swagger_server.bio.knowledge.server.model.query import Query
from swagger_server.bio.knowledge.server.model.response import Response
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def query(body):
    """
    Query using a predefined query type
    
    :param body: Query information to be submitted
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = Query.from_dict(connexion.request.get_json())
    return 'do some magic!'
