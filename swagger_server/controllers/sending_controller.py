import connexion
import requests
import six
from flask import request

from repository.message_repository import send_email
from swagger_server.encoder import JSONEncoder
from swagger_server.models import SendEmailToListRequest
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.send_individual_request import SendIndividualRequest  # noqa: E501
from swagger_server.models.send_response import SendResponse  # noqa: E501
from swagger_server import util

# Configuración de la API
API_KEY = "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"
BASE_URL = "https://api.brevo.com/v3/smtp/email"
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "api-key": API_KEY,
}


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

def send_email_to_list(body, list_id):  # noqa: E501
    """Send an email to a list

    Sends a bulk email to all contacts in the specified list. # noqa: E501

    :param body:
    :type body: dict | bytes
    :param list_id: ID of the list to send emails to
    :type list_id: str

    :rtype: SendResponse
    """
    if request.is_json:
        body = SendEmailToListRequest.from_dict(request.get_json())  # noqa: E501
    try:
        print(f"Enviando email a la lista {list_id}")

        # Payload para el envío de correo
        payload = {
            "sender": {
                "email": body.sender_email,
                "name": body.sender_name
            },
            "subject": body.subject,
            "htmlContent": body.html_content,
            "listIds": [int(list_id)]  # Enviar directamente a la lista por su ID
        }

        # Realizar la solicitud POST
        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        print(f"Respuesta de la API: {response.status_code}, {response.text}")

        if response.status_code not in [200, 201]:
            raise ValueError(f"Error al enviar email: {response.text}")

        # Procesar la respuesta
        response_data = response.json()
        send_response = SendResponse(
            send_id=response_data.get("messageId"),
            status="Emails sent successfully"
        )
        return JSONEncoder().default(send_response), 200
    except Exception as e:
        print(f"Error al enviar email a la lista {list_id}: {e}")
        return JSONEncoder().default(ErrorResponse(error=str(e))), 500
