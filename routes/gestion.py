from fastapi import APIRouter
from config.db import conectar_db
from schemas.gestion import Gestion
import mysql.connector

gestion = APIRouter()

@gestion.get("/gestion")
async def getall():
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre FROM gestion")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({"nombre": fila[0]})
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@gestion.get("/gestion/{id}")
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre FROM gestion WHERE id = "+str(id))
  # valores = (id)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {"nombre": fila[0]}
    json_resultados["ok"] = True

    consulta = ("SELECT nombre, id FROM mes WHERE id_gestion = "+str(id))

    cursor.execute(consulta)
    resultados_aux = cursor.fetchall()

    json_resultados["data"]["meses"] = []
    for fila_aux in resultados_aux:
      json_resultados["data"]["meses"].append({"nombre": fila_aux[0], "id": fila_aux[1]})

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados
