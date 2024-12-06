import requests
import logging


def crear_mensaje(usuario, contrasena, id_lista, asunto, cuerpo):
    """
    Crea un mensaje de correo electrónico en una lista específica.
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

        # Paso 2: Crear el mensaje
        logging.info(f"Creando un mensaje en la lista {id_lista}...")
        headers = {'Authorization': f'Bearer {access_token}'}
        mensaje_data = {
            "Subject": asunto,
            "Content": cuerpo,
            "UseDynamicFields": False,  # No se usan campos dinámicos
            "Embed": False,  # No se incrustan imágenes
            "IsConfirmation": False,  # No es un mensaje de confirmación
            "TrackingInfo": {
                "TrackLinks": True,  # Seguimiento de clics en enlaces
                "TrackReads": True,  # Seguimiento de apertura de correos
                "Enabled": True,  # Habilitar seguimiento
                "CustomParams": "",  # Sin parámetros personalizados
                "Protocols": {
                    "Http": True,  # Seguimiento HTTP
                    "Https": True  # Seguimiento HTTPS
                }
            }
        }
        response = requests.post(
            f'{base_api_url}/Console/List/{id_lista}/Email',
            headers=headers,
            json=mensaje_data
        )
        if response.status_code != 200:
            logging.error(f"Error al crear el mensaje: {response.status_code} - {response.text}")
            return
        mensaje_creado = response.json()
        print("hola")
        logging.info(f"Mensaje creado con éxito: {mensaje_creado}")
        return mensaje_creado

    except Exception as e:
        logging.error(f"Error en el proceso: {e}")

# Ejemplo de uso
usuario = "."
contrasena = "."
id_lista = 1  # ID de la lista existente
asunto = "Boletín mensual de ESPAE"
cuerpo = """
<html>
    <body>
        <h1>Bienvenidos al Boletín Mensual de ESPAE</h1>
        <p>Estamos encantados de compartir las últimas noticias y eventos contigo.</p>
    </body>
</html>
"""
mensaje = crear_mensaje(usuario, contrasena, id_lista, asunto, cuerpo)

