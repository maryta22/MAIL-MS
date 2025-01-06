import connexion
import six
from flask import request

from repository.message_repository import send_email
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.send_individual_request import SendIndividualRequest  # noqa: E501
from swagger_server.models.send_response import SendResponse  # noqa: E501
from swagger_server import util


def send_individual_message(body):  # noqa: E501
    """Send an individual message

    Sends a personalized message to a single recipient. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SendResponse
    """
    if request.is_json:
        body = SendIndividualRequest.from_dict(request.get_json())  # noqa: E501
        response = send_email(body.to_email, body.to_name, body.sender_email, body.sender_name, body.subject, body.message)
    return response

