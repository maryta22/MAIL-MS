import requests
from flask import request
from swagger_server.models.create_folder_request import CreateFolderRequest  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.folder_response import FolderResponse  # noqa: E501
from swagger_server.encoder import JSONEncoder
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('TOKEN')
BASE_URL = "https://api.brevo.com/v3/contacts/folders"


def create_folder(body):  # noqa: E501
    """Create a new folder

    Creates a new folder for grouping lists. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: FolderResponse
    """
    if request.is_json:
        body = CreateFolderRequest.from_dict(request.get_json())  # noqa: E501
    try:
        print(f"Creando nueva carpeta: {body.name}")
        response = requests.post(
            "https://api.brevo.com/v3/contacts/folders",
            headers={
                "accept": "application/json",
                "content-type": "application/json",
                "api-key": API_KEY,
            },
            json={"name": body.name},
        )
        print(f"Respuesta de la API: {response.status_code}, {response.text}")

        if response.status_code != 201:
            raise ValueError(f"Error al crear la carpeta: {response.text}")

        response_data = response.json()
        print(response_data)
        folder_response = FolderResponse(
            id=str(response_data["id"]), name=body.name
        )

        return JSONEncoder().default(folder_response), 200
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")
        return JSONEncoder().default(ErrorResponse(error=str(e))), 500



def get_all_folders():  # noqa: E501
    """Get all folders

    Retrieves all available folders. # noqa: E501

    :rtype: List[FolderResponse]
    """
    try:
        print("Obteniendo todas las carpetas disponibles")
        headers = {
            "accept": "application/json",
            "api-key": API_KEY,
        }

        response = requests.get(BASE_URL, headers=headers)
        print(f"Respuesta de la API: {response.status_code}, {response.text}")

        if response.status_code != 200:
            raise ValueError(f"Error al obtener las carpetas: {response.text}")

        response_body = response.json()
        folders = [
            FolderResponse(id=str(folder["id"]), name=folder["name"])
            for folder in response_body.get("folders", [])
        ]

        return [JSONEncoder().default(folder) for folder in folders], 200

    except Exception as e:
        print(f"Error al obtener las carpetas: {e}")
        return JSONEncoder().default(ErrorResponse(error=str(e))), 500
