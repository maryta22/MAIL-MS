import requests
from flask import request
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.list_response import ListResponse  # noqa: E501
from swagger_server.models.add_contact_request import AddContactRequest  # noqa: E501
from swagger_server.models.contact_response import ContactResponse  # noqa: E501
from swagger_server.models.create_list_request import CreateListRequest  # noqa: E501
from swagger_server.models.delete_response import DeleteResponse  # noqa: E501
from swagger_server.encoder import JSONEncoder

# Configuración de la API
API_KEY = "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"
BASE_URL = "https://api.brevo.com/v3/contacts"
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "api-key": API_KEY,
}

def add_contact_to_list(body, list_id):  # noqa: E501
    """Add a contact to a list

    Adds a new contact to an existing list. # noqa: E501

    :param body:
    :type body: dict | bytes
    :param list_id: ID of the list to add the contact to
    :type list_id: str

    :rtype: ContactResponse
    """
    if request.is_json:
        body = AddContactRequest.from_dict(request.get_json())  # noqa: E501
    try:
        print(f"Añadiendo contacto {body.email} a la lista {list_id}")
        payload = {
            "emails": [body.email]
        }

        response = requests.post(f"{BASE_URL}/lists/{list_id}/contacts", headers=HEADERS, json=payload)
        print(f"Respuesta de la API: {response.status_code}, {response.text}")

        if response.status_code != 200:
            raise ValueError(f"Error al añadir contacto: {response.text}")

        contact_response = ContactResponse(email=body.email, list_id=list_id)
        return JSONEncoder().default(contact_response), 200
    except Exception as e:
        print(f"Error al añadir contacto: {e}")
        return JSONEncoder().default(ErrorResponse(error=str(e))), 500



def create_list(body):  # noqa: E501
    """Create a new list

    Creates a new list for storing contacts in a specified folder. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: ListResponse
    """
    if request.is_json:
        body = CreateListRequest.from_dict(request.get_json())  # noqa: E501
    try:
        print(f"Creando nueva lista: {body.name}")

        # Validar si el folder_id está presente en el cuerpo de la solicitud
        folder_id = body.folder_id
        if not folder_id:
            raise ValueError("El campo 'folder_id' es obligatorio.")

        # Datos para la creación de la lista
        payload = {
            "name": body.name,
            "folderId": int(folder_id)
        }

        # Realizar la solicitud para crear la lista
        response = requests.post(f"{BASE_URL}/lists", headers=HEADERS, json=payload)
        print(f"Respuesta de la API: {response.status_code}, {response.text}")

        if response.status_code != 201:
            raise ValueError(f"Error al crear la lista: {response.text}")

        # Procesar la respuesta de la API
        response_data = response.json()
        list_id = response_data["id"]
        print(f"Lista creada exitosamente con ID: {list_id}")

        # Si se incluyen contactos, agregarlos a la lista
        if body.emails:
            print("Añadiendo contactos a la lista...")
            for email in body.emails:
                create_contact_if_not_exists(email)
            add_contacts_to_list(list_id, body.emails)

        # Crear la respuesta final
        list_response = ListResponse(id=str(list_id), name=body.name)
        return JSONEncoder().default(list_response), 200
    except Exception as e:
        print(f"Error al crear la lista: {e}")
        return JSONEncoder().default(ErrorResponse(error=str(e))), 500


def is_contact_exist(email):
    """Verifica si un contacto existe en Brevo."""
    try:
        response = requests.get(
            f"{BASE_URL}/contacts/{email}", headers=HEADERS
        )
        print(f"Comprobando si el contacto {email} existe: {response.status_code}")
        return response.status_code == 200  # Devuelve True si el contacto existe
    except Exception as e:
        print(f"Error al verificar existencia del contacto {email}: {e}")
        return False


def create_contact(email):
    """Crea un nuevo contacto en Brevo."""
    try:
        url = "https://api.brevo.com/v3/contacts"  # URL correcta para crear contactos
        payload = {
            "email": email,
            "attributes": {
                "FNAME": "Default",  # Puedes cambiar esto si tienes nombres específicos
                "LNAME": "Default"
            },
            "emailBlacklisted": False,
            "smsBlacklisted": False,
            "updateEnabled": True  # Esto asegura que si el contacto existe, se actualice
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": API_KEY,
        }
        response = requests.post(url, headers=headers, json=payload)
        print(f"Respuesta al crear contacto {email}: {response.status_code}, {response.text}")
        if response.status_code not in [200, 201]:
            # Capturar errores específicos de la API
            try:
                error_detail = response.json()
                raise ValueError(f"Error al crear el contacto {email}: {error_detail.get('message', response.text)}")
            except Exception:
                raise ValueError(f"Error al crear el contacto {email}: {response.text}")
    except Exception as e:
        print(f"Error al crear el contacto {email}: {e}")
        raise

def get_contact(email):
    """Obtiene un contacto de Brevo por su email."""
    try:
        url = f"https://api.brevo.com/v3/contacts/{email}"
        headers = {
            "accept": "application/json",
            "api-key": API_KEY,
        }
        response = requests.get(url, headers=headers)
        print(f"Respuesta al obtener contacto {email}: {response.status_code}, {response.text}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None  # Contacto no existe
        else:
            raise ValueError(f"Error al obtener el contacto {email}: {response.text}")
    except Exception as e:
        print(f"Error al obtener el contacto {email}: {e}")
        raise


def add_contacts_to_list(list_id, emails):
    """Añade contactos existentes a una lista específica."""
    errores = []
    try:
        print(f"Añadiendo contactos a la lista {list_id}")
        for email in emails:
            try:
                payload = {"emails": [email]}
                response = requests.post(
                    f"{BASE_URL}/lists/{list_id}/contacts/add",
                    headers=HEADERS,
                    json=payload
                )
                print(f"Respuesta de la API al añadir {email}: {response.status_code}, {response.text}")
                if response.status_code != 200:
                    errores.append({email: response.json().get("message", "Error desconocido")})
            except Exception as e:
                errores.append({email: str(e)})

        if errores:
            print(f"Errores al añadir algunos contactos: {errores}")
        return errores
    except Exception as e:
        print(f"Error general al añadir contactos: {e}")
        raise


def create_contact_if_not_exists(email):
    """Crea un nuevo contacto solo si no existe."""
    try:
        contact = get_contact(email)
        if contact:
            print(f"El contacto {email} ya existe.")
            return contact  # Devolver los detalles del contacto existente
        # Crear el contacto si no existe
        create_contact(email)
        print(f"El contacto {email} fue creado exitosamente.")
    except Exception as e:
        print(f"Error al verificar/crear el contacto {email}: {e}")
        raise


def delete_contact_from_list(list_id, contact_id):  # noqa: E501
    """Delete a contact from a list

    Deletes a contact from an existing list. # noqa: E501

    :param list_id: ID of the list
    :type list_id: str
    :param contact_id: ID of the contact to delete
    :type contact_id: str

    :rtype: DeleteResponse
    """
    try:
        print(f"Eliminando contacto {contact_id} de la lista {list_id}")

        # URL para la eliminación del contacto
        url = f"{BASE_URL}/lists/{list_id}/contacts/{contact_id}"

        # Realizar la solicitud DELETE
        response = requests.delete(url, headers=HEADERS)
        print(f"Respuesta de la API: {response.status_code}, {response.text}")

        if response.status_code != 204:
            raise ValueError(f"Error al eliminar el contacto: {response.text}")

        # Crear una instancia de DeleteResponse
        delete_response = DeleteResponse(
            success=True,
            message=f"Contacto {contact_id} eliminado de la lista {list_id}"
        )

        return JSONEncoder().default(delete_response), 200

    except Exception as e:
        print(f"Error al eliminar el contacto: {e}")
        return JSONEncoder().default(ErrorResponse(error=str(e))), 500

def delete_list(list_id):  # noqa: E501
    """Delete a list

    Deletes a list and all its contacts. # noqa: E501

    :param list_id: ID of the list to delete
    :type list_id: str

    :rtype: DeleteResponse
    """
    try:
        print(f"Eliminando lista {list_id}")
        response = requests.delete(f"{BASE_URL}/lists/{list_id}", headers=HEADERS)
        print(f"Respuesta de la API: {response.status_code}, {response.text}")

        if response.status_code != 204:
            raise ValueError(f"Error al eliminar la lista: {response.text}")

        delete_response = DeleteResponse(
            success=True,
            message=f"Lista {list_id} eliminada exitosamente"
        )
        return JSONEncoder().default(delete_response), 200
    except Exception as e:
        print(f"Error al eliminar la lista: {e}")
        return JSONEncoder().default(ErrorResponse(error=str(e))), 500


def get_all_lists():  # noqa: E501
    """Get all lists

    Retrieves all available lists. # noqa: E501

    :rtype: List[ListResponse]
    """
    try:
        print("Obteniendo todas las listas disponibles")
        response = requests.get(f"{BASE_URL}/lists", headers=HEADERS)
        print(f"Respuesta de la API: {response.status_code}, {response.text}")

        if response.status_code != 200:
            raise ValueError(f"Error al obtener las listas: {response.text}")

        response_data = response.json()

        # Modificar para incluir folder_id
        lists = [
            ListResponse(
                id=str(lista["id"]),
                name=lista["name"],
                folder_id=lista.get("folderId", None)  # Obtener folder_id si está disponible
            )
            for lista in response_data.get("lists", [])
        ]

        return [JSONEncoder().default(lista) for lista in lists], 200
    except Exception as e:
        print(f"Error al obtener las listas: {e}")
        return JSONEncoder().default(ErrorResponse(error=str(e))), 500

