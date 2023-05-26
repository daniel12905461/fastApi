from fastapi import APIRouter
from config.db import conectar_db
from schemas.hora import Hora
import mysql.connector

horas = APIRouter()

@horas.get("/horas")
async def getall():
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombres, apellidos, ci, foto, celular, fecha_nac, id, user, password, id_rols, id_ubicaciones FROM funcionarios")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({"nombres": fila[0], "apellidos": fila[1], "ci": fila[2], "foto": fila[3], "celular": fila[4], "fecha_nac": fila[5], "id": fila[6], "user": fila[7], "password": fila[8], "id_rols": fila[9], "id_ubicaciones": fila[10]})
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@horas.get("/horas/{id}")
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT nombres, apellidos, ci, foto, celular, fecha_nac, id, user, password, id_rols, id_ubicaciones FROM funcionarios WHERE id = "+str(id))
  # valores = (id)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {"nombres": fila[0], "apellidos": fila[1], "ci": fila[2], "foto": fila[3], "celular": fila[4], "fecha_nac": fila[5], "id": fila[6], "user": fila[7], "password": fila[8], "id_rols": fila[9], "id_ubicaciones": fila[10]}
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@horas.post("/horas")
async def create(hora: Hora):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "INSERT INTO ubicacion_hora (hora, latitud, longitud, id_dia) VALUES (%s, %s, %s, %s, %s, %s, %s)"
  valores = (hora.hora, hora.latitud, hora.longitud, hora.id_dia)

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

@horas.put("/horas/{id}")
async def update(id: int, funcionario: Hora):
  cnx = conectar_db()
  cursor = cnx.cursor()

  # sentencia = "UPDATE funcionarios SET nombres = '"+funcionario.nombres+"', apellidos = '"+funcionario.apellidos+"', ci = '"+funcionario.ci+"', foto = '"+funcionario.foto+"', celular = '"+funcionario.celular+"', fecha_nac = '"+funcionario.fecha_nac+"', user = '"+funcionario.user+"', password = '"+funcionario.password+"', id_rols = '"+funcionario.id_rols+"', id_ubicaciones = '"+funcionario.id_ubicaciones+"' WHERE id = "+str(id)

  # cursor.execute(sentencia)
  # cnx.commit()

  # cursor.close()
  # cnx.close()

  return cursor

@horas.delete("/horas/{id}")
async def delete(id: int):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "DELETE FROM funcionarios WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor
