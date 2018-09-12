# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from reasoner_server.models.query import Query  # noqa: E501
from reasoner_server.models.response import Response  # noqa: E501
from reasoner_server.test import BaseTestCase


class TestQueryController(BaseTestCase):
    """QueryController integration test stubs"""

    def test_query(self):
        """Test case for query

        Query using a predefined query type
        """
        query = Query()
        response = self.client.open(
            '//query',
            method='POST',
            data=json.dumps(query),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
