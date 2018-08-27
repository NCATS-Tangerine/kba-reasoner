"""
 Customized delegate logic for connecting the front end Reasoner 
 to the back end the Knowledge Beacon Aggregator client
"""

from __future__ import absolute_import

from swagger_server.models.response import Response
from swagger_server.models.result   import Result

from datetime import date, datetime  # noqa: F401

class KBA():
    """
    Service middle ware to access Knowledge Beacon Aggregator client
    """

    def __init__(self):
        pass
    
    @classmethod
    def processQuery(cls,body):
        response = Response()
        # stupid stub here just to get started, since body JSON 
        # is not going to be the same as Response JSON
        return response.from_dict(body) 