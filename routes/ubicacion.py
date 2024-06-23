from fastapi import APIRouter
from config.db import conectar_db
from schemas.ubicacion import Ubicacion
import json
import mysql.connector

ubicacion = APIRouter()

@ubicacion.get("/ubicaciones")
async def getall():
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, latitud, longitud, id FROM ubicaciones")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({"nombre": fila[0], "latitud": fila[1], "longitud": fila[2], "id": fila[3]})
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@ubicacion.get("/ubicaciones/{id}")
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, latitud, longitud, id FROM ubicaciones WHERE id = "+str(id))
  # valores = (id)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {"nombre": fila[0], "latitud": fila[1], "longitud": fila[2], "id": fila[3]}
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@ubicacion.post("/ubicaciones")
async def create(ubicacion: Ubicacion):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "INSERT INTO ubicaciones (nombre, latitud, longitud) VALUES (%s, %s, %s)"
  valores = (ubicacion.nombre, ubicacion.latitud, ubicacion.longitud)

  try:
    cursor.execute(sentencia, valores)
    cnx.commit()

    num_filas_afectadas = cursor.rowcount

    json_respuesta = {"mensaje": "Inserción exitosa.", "filas_afectadas": num_filas_afectadas}

  except mysql.connector.Error as error:
    json_respuesta = {"mensaje": "Error al insertar en la base de datos: {}".format(error.msg)}

  finally:
    cursor.close()
    cnx.close()

  return json_respuesta

@ubicacion.put("/ubicaciones/{id}")
async def update(id: int, ubicacion: Ubicacion):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "UPDATE ubicaciones SET nombre = '"+ubicacion.nombre+"', latitud = "+str(ubicacion.latitud)+", longitud = "+str(ubicacion.longitud)+" WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return 'dda'

@ubicacion.delete("/ubicaciones/{id}")
async def delete(id: int):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "DELETE FROM ubicaciones WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor
