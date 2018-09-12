# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from reasoner_server.models.query import Query  # noqa: E501
from reasoner_server.models.question import Question  # noqa: E501
from reasoner_server.test import BaseTestCase


class TestTranslateController(BaseTestCase):
    """TranslateController integration test stubs"""

    def test_translate(self):
        """Test case for translate

        Translate natural language question into a standardized query
        """
        question = Question()
        response = self.client.open(
            '//translate',
            method='POST',
            data=json.dumps(question),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
