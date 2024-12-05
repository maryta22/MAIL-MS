import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
from swagger_server.models.send_bulk_body import SendBulkBody  # noqa: E501
from swagger_server.models.send_individual_body import SendIndividualBody  # noqa: E501
from swagger_server import util


def send_bulk_message(body):  # noqa: E501
    """Send a message to multiple recipients

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = SendBulkBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def send_individual_message(body):  # noqa: E501
    """Send an individual message

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = SendIndividualBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
