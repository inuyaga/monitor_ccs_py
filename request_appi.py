
import requests
import json
import logging
from requests.exceptions import RequestException
from pathlib import Path
class AppiResponseMonitor:
    """
    Clase definida para monitor de ventas
    """
    def __init__(self, ruta_archivo:Path, url:str='http://127.0.0.1:8000/almacen/crear/'):
        """
        Args:
            ruta_archivo (str): Ruta absoluta
            url (str, optional): url hacia donde se hara la peticion. Defaults to 'http://127.0.0.1:8000/almacen/crear/'.
        """
        self.ruta_file=ruta_archivo
        self.url_request = url
    def send(self):
        """Envio de venta hacia el servidor

        Returns:
            request: respuesta del servidor
        """
        request_server=None
        try:
            with open(self.ruta_file) as file:
                json_read = json.load(file)
                request_server = requests.post(self.url_request, json=json_read)
            if request_server.status_code == 200 or request_server.status_code == 201:
                self.ruta_file.unlink()
        except FileNotFoundError as error:
            logging.error(str(error))
        except RequestException as r_error:
            logging.fatal(f"{self.ruta_file} error al enviar al servidor")
        return request_server



# apicacion = AppiResponseMonitor(ruta_archivo='venta.txt')
# apicacion.send()
# apicacion.ruta_file='venta2.txt'
# apicacion.send()