import connexion
import six

from swagger_server.bio.knowledge.server.model.response import Response  # noqa: E501
from swagger_server.bio.knowledge.server.model.response_feedback import ResponseFeedback  # noqa: E501
from swagger_server import util


def get_response(response_id):  # noqa: E501
    """Request stored responses and results

     # noqa: E501

    :param response_id: Integer identifier of the response to return
    :type response_id: int

    :rtype: Response
    """
    return 'do some magic!'


def get_response_feedback(response_id):  # noqa: E501
    """Request stored feedback for this response

     # noqa: E501

    :param response_id: Integer identifier of the response to return
    :type response_id: int

    :rtype: ResponseFeedback
    """
    return 'do some magic!'
