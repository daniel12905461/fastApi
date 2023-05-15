from fastapi import APIRouter
from config.db import conectar_db
from schemas.rol import Rol
import json
import mysql.connector

rol = APIRouter()

@rol.get("/rols")
async def getall():
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, id FROM rols")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({"nombre": fila[0], "id": fila[1]})
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@rol.get("/rols/{id}")
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombre, id FROM rols WHERE id = "+str(id))
  # valores = (id)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {"nombre": fila[0], "id": fila[1]}
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@rol.post("/rols")
async def create(rol: Rol):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "INSERT INTO rols (nombre) VALUES ('"+rol.nombre+"')"
  # valores = (rol.nombre)

  try:
    # cursor.execute(sentencia, valores)
    cursor.execute(sentencia)
    cnx.commit()

    num_filas_afectadas = cursor.rowcount

    json_respuesta = {"mensaje": "Inserción exitosa.", "filas_afectadas": num_filas_afectadas}

  except mysql.connector.Error as error:
    json_respuesta = {"mensaje": "Error al insertar en la base de datos: {}".format(error.msg)}

  finally:
    cursor.close()
    cnx.close()

  return json_respuesta

@rol.put("/rols/{id}")
async def update(id: int, rol: Rol):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "UPDATE rols SET nombre = '"+rol.nombre+"' WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor

@rol.delete("/rols/{id}")
async def delete(id: int):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "DELETE FROM rols WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor
