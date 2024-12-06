import requests
import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_email(usuario, contrasena):
    """
    Autentica, obtiene la zona horaria GMT -5 y crea una nueva lista en MailUp.
    """
    try:
        # Configuración de credenciales y URLs
        client_id = '.'
        client_secret = '.'
        token_url = 'https://services.mailup.com/Authorization/OAuth/Token'
        base_api_url = 'https://services.mailup.com/API/v1.1/Rest/ConsoleService.svc'

        # Paso 1: Autenticación
        logging.info("Autenticando con usuario y contraseña...")
        data = {
            'grant_type': 'password',
            'username': usuario,
            'password': contrasena,
            'client_id': client_id,
            'client_secret': client_secret,
        }
        response = requests.post(token_url, data=data)
        if response.status_code != 200:
            logging.error(f"Error en la autenticación: {response.status_code} - {response.text}")
            return
        access_token = response.json().get('access_token')
        logging.info("Autenticación exitosa. Token obtenido.")

        # Paso 2: Obtener lista de zonas horarias
        logging.info("Solicitando lista de zonas horarias...")
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(f'{base_api_url}/Console/TimeZones', headers=headers)
        if response.status_code != 200:
            logging.error(f"Error al obtener zonas horarias: {response.status_code} - {response.text}")
            return
        zonas_horarias = response.json()
        logging.info("Lista de zonas horarias obtenida con éxito.")

        # Paso 3: Filtrar zona horaria GMT -5
        logging.info("Filtrando zona horaria para GMT -5...")
        zona_horaria_gmt_menos_5 = next(
            (zona for zona in zonas_horarias if zona['OffsetFromUTC'] == '-05:00:00'),
            None
        )
        if not zona_horaria_gmt_menos_5:
            logging.warning("No se encontró una zona horaria con GMT -5.")
            return

        logging.info(f"Zona horaria GMT -5 encontrada: {zona_horaria_gmt_menos_5}")

        # Paso 4: Crear una nueva lista
        logging.info("Creando una nueva lista en MailUp...")
        nueva_lista = {
            "Name": "New ESPAE List",
            "Business": True,
            "Customer": True,
            "OwnerEmail": "espae@espol.edu.ec",
            "ReplyTo": "espae@espol.edu.ec",
            "NLSenderName": "ESPAE",
            "CompanyName": "ESPAE",
            "ContactName": "María Rivera",
            "Address": "Km 30.5 Vía Perimetral Guayaquil",
            "City": "Guayaquil",
            "CountryCode": "EC",
            "PermissionReminder": "You subscribed to our ESPAE newsletter.",
            "WebSiteUrl": "https://www.espae.edu.ec/",
            "UseDefaultSettings": True,
            "TimeZoneCode": zona_horaria_gmt_menos_5['TimeZoneCode']
        }
        response = requests.post(f'{base_api_url}/Console/List', headers=headers, json=nueva_lista)
        if response.status_code != 200:
            logging.error(f"Error al crear la lista: {response.status_code} - {response.text}")
            return
        lista_creada = response.json()
        logging.info(f"Lista creada con éxito: {lista_creada}")

    except Exception as e:
        logging.error(f"Error en el proceso: {e}")

# Ejemplo de uso
usuario = "."
contrasena = "."
send_email(usuario, contrasena)
