# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
from swagger_server.models.send_bulk_body import SendBulkBody  # noqa: E501
from swagger_server.models.send_individual_body import SendIndividualBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSendingController(BaseTestCase):
    """SendingController integration test stubs"""

    def test_send_bulk_message(self):
        """Test case for send_bulk_message

        Send a message to multiple recipients
        """
        body = SendBulkBody()
        response = self.client.open(
            '/send/bulk',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_individual_message(self):
        """Test case for send_individual_message

        Send an individual message
        """
        body = SendIndividualBody()
        response = self.client.open(
            '/send/individual',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
