#_IMPORTACIONES
import sqlite3
import os
from colorama import Fore, init, Style
from datetime import datetime
#from phatlib import path

#_CONFIGURACIÓN 
RUTA_DB = "inventario.db"
CARPETA_LOGS="LOGS"
RUTA_LOG=f"{CARPETA_LOGS}/inventario.log"

os.makedirs(CARPETA_LOGS, exist_ok=True)

def registrt_log():
    """agrega una línea al archivo.log"""
    fecha_hora = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    


#if_name__=="__main__":

#condición para ejecutar el módulo 
#como modulo principal que no entre en loop 