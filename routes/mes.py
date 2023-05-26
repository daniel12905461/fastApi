# from fastapi import APIRouter
from config.db import conectar_db
# import json
import mysql.connector
import math

async def getIdMes(numero: str, id_gestion: str):
  cnx = conectar_db()
  cursor = cnx.cursor()

  consulta = ("SELECT id FROM mes WHERE numero = " + numero + " AND id_gestion = " + id_gestion)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  id_mes = '0'

  for fila in resultados:
    id_mes = str(fila[0])

  cursor.close()
  cnx.close()

  return id_mes
