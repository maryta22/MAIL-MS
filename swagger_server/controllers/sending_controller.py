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

        contacts = get_contacts_from_list(list_id)
        if not contacts:
            raise ValueError(f"No hay contactos en la lista {list_id} o la lista no existe.")

        recipient_emails = [{"email": contact["email"]} for contact in contacts]

        payload = {
            "sender": {
                "email": body.sender_email,
                "name": body.sender_name
            },
            "to": recipient_emails,
            "subject": body.subject,
            "htmlContent": body.html_content,
        }

        # Endpoint correcto para enviar emails masivos
        url = "https://api.brevo.com/v3/smtp/email"
        response = requests.post(url, headers=HEADERS, json=payload)
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


def get_contacts_from_list(list_id):
    """
    Obtiene los contactos asociados a una lista en Brevo.
    :param list_id: ID de la lista.
    :return: Lista de contactos (diccionarios con sus atributos).
    """
    try:
        url = f"https://api.brevo.com/v3/contacts/lists/{list_id}/contacts"
        response = requests.get(url, headers=HEADERS)
        print(f"Respuesta al obtener contactos de la lista {list_id}: {response.status_code}, {response.text}")

        if response.status_code != 200:
            raise ValueError(f"Error al obtener los contactos de la lista {list_id}: {response.text}")

        response_data = response.json()
        return response_data.get("contacts", [])
    except Exception as e:
        print(f"Error al obtener contactos de la lista {list_id}: {e}")
        raise


