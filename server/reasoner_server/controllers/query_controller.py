import connexion
import six

from reasoner_server.models.query import Query  # noqa: E501
from reasoner_server.models.response import Response  # noqa: E501
from reasoner_server import util


def query(query):  # noqa: E501
    """Query using a predefined query type

     # noqa: E501

    :param query: Query information to be submitted
    :type query: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        query = Query.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
