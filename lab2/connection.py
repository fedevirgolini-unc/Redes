# encoding: utf-8
# Revisión 2019 (a Python 3 y base64): Pablo Ventura
# Copyright 2014 Carlos Bederián
# $Id: connection.py 455 2011-05-01 00:32:09Z carlos $

from email.policy import default
from nis import match
import socket
from unittest import case
from constants import *
from base64 import b64encode

import logging

class Connection(object):
    """
    Conexión punto a punto entre el servidor y un cliente.
    Se encarga de satisfacer los pedidos del cliente hasta
    que termina la conexión.
    """

    def __init__(self, socket, directory):
        # FALTA: Inicializar atributos de Connection
        self.s = socket
        self.dir = directory

    def handle(self):
        """
        Atiende eventos de la conexión hasta que termina.
        """

        data = self.s.recv(1024)
        if data == "get_file_listing\r\n".encode("ascii")
            self.send(f"{CODE_OK} OK")
            #Enviar archivo por archivo los disponibles
            self.send("")
        data = self.s.recv(1024)


        # while True:
        #     data = self.s.recv(1024)
        #     if not data:
        #         print("Conexión cerrada")
        #         break
        #     print(data)
        #     self.send(f"{CODE_OK} OK")
        #     #Enviar archivo por archivo los disponibles
        #     self.send("")


    def send(self, message, timeout=None):
        """
        Envía el mensaje 'message' al cliente, seguido por el terminador de
        línea del protocolo.

        Si se da un timeout, puede abortar con una excepción socket.timeout.

        También puede fallar con otras excepciones de socket.
        """
        self.s.settimeout(timeout)
        message += EOL  # Completar el mensaje con un fin de línea
        while message:
            logging.debug("Enviando el (resto del) mensaje %s."
                          % repr(message))
            bytes_sent = self.s.send(message.encode("ascii"))
            assert bytes_sent > 0
            message = message[bytes_sent:]

    def file_lookup(self):
        """
        Obtener el listado de archivos disponibles. Devuelve una lista
        de strings.
        """
        result = []
        return result