import connexion
import six

from reasoner_server.models.query import Query  # noqa: E501
from reasoner_server.models.question import Question  # noqa: E501
from reasoner_server import util


def translate(question):  # noqa: E501
    """Translate natural language question into a standardized query

     # noqa: E501

    :param question: Question object that needs to be translated
    :type question: dict | bytes

    :rtype: List[Query]
    """
    if connexion.request.is_json:
        question = Question.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
