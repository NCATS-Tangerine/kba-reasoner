# coding: utf-8

from __future__ import absolute_import

from swagger_server.bio.knowledge.server.model.feedback import Feedback
from swagger_server.bio.knowledge.server.model.result import Result
from swagger_server.bio.knowledge.server.model.result_feedback import ResultFeedback
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestResultController(BaseTestCase):
    """ ResultController integration test stubs """

    def test_get_result(self):
        """
        Test case for get_result

        Request stored result
        """
        response = self.client.open('/api/rtx/v1/result/{result_id}'.format(result_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_result_feedback(self):
        """
        Test case for get_result_feedback

        Request stored feedback for this result
        """
        response = self.client.open('/api/rtx/v1/result/{result_id}/feedback'.format(result_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_post_result_feedback(self):
        """
        Test case for post_result_feedback

        Store feedback for a particular result
        """
        body = Feedback()
        response = self.client.open('/api/rtx/v1/result/{result_id}/feedback'.format(result_id=56),
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
