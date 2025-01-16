from sib_api_v3_sdk import Configuration, ApiClient, ContactsApi, TransactionalEmailsApi
from sib_api_v3_sdk.models.create_contact import CreateContact
from sib_api_v3_sdk.models.update_contact import UpdateContact
from sib_api_v3_sdk.models.send_smtp_email import SendSmtpEmail
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('TOKEN')

def send_email(to_email, to_name, sender_email, sender_name, subject, html_content, list_ids=None):
    """
    Crea o actualiza un contacto en Brevo y envía un correo electrónico.

    :param to_email: Email del destinatario.
    :param to_name: Nombre completo del destinatario.
    :param sender_email: Email del remitente.
    :param sender_name: Nombre del remitente.
    :param subject: Asunto del correo.
    :param html_content: Contenido HTML del correo.
    :param list_ids: Lista de IDs donde se añadirá el contacto (opcional).
    :return: Resultado final de creación/actualización y envío del correo.
    """
    # Configuración de la API
    configuration = Configuration()
    configuration.api_key["api-key"] = API_KEY

    # Inicializar clientes de API
    api_client = ApiClient(configuration)
    contacts_api = ContactsApi(api_client)
    email_api = TransactionalEmailsApi(api_client)

    try:
        print("Enviando correo...")
        send_email = SendSmtpEmail(
            sender={"email": sender_email, "name": sender_name},
            to=[{"email": to_email, "name": to_name}],
            subject=subject,
            html_content=html_content
        )
        send_response = email_api.send_transac_email(send_email)
        print("Correo enviado:", send_response)
        return {
            "status": "Contacto creado/actualizado y correo enviado exitosamente",
            "email_details": send_response.to_dict()
        }
    except Exception as e:
        return {"error": str(e), "message": "Error al enviar el correo"}
