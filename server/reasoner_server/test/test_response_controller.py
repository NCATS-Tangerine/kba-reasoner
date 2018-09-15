# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from reasoner_server.models.response import Response  # noqa: E501
from reasoner_server.models.response_feedback import ResponseFeedback  # noqa: E501
from reasoner_server.test import BaseTestCase


class TestResponseController(BaseTestCase):
    """ResponseController integration test stubs"""

    def test_get_response(self):
        """Test case for get_response

        Request stored responses and results
        """
        response = self.client.open(
            '//response/{response_id}'.format(response_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_response_feedback(self):
        """Test case for get_response_feedback

        Request stored feedback for this response
        """
        response = self.client.open(
            '//response/{response_id}/feedback'.format(response_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()