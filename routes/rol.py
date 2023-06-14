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

  consulta = ("SELECT nombre, id, id_horarios FROM rols")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({"nombre": fila[0], "id": fila[1], "id_horarios": fila[2]})
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

  consulta = ("SELECT nombre, id, id_horarios FROM rols WHERE id = "+str(id))
  # valores = (id)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {"nombre": fila[0], "id": fila[1], "id_horarios": fila[2]}
    json_resultados["ok"] = True

    consulta = ("SELECT h.hora_inicio, h.hora_inicio_reseso, h.hora_fin_reseso, h.hora_fin, h.domingo, h.lunes, h.martes, h.miercoles, h.jueves, h.viernes, h.sabado, h.id, r.nombre, r.id_horarios FROM horarios h JOIN rols r ON h.id = r.id_horarios AND r.id = " + str(id))
    cursor.execute(consulta)
    resultados_aux = cursor.fetchall()

    json_resultados["data"]['horario'] = {}

    for fila_aux in resultados_aux:
      json_resultados["data"]['horario'] = {
        "hora_inicio": str(fila_aux[0]),
        "hora_inicio_reseso": str(fila_aux[1]),
        "hora_fin_reseso": str(fila_aux[2]),
        "hora_fin": str(fila_aux[3]),
        "domingo": fila_aux[4],
        "lunes": fila_aux[5],
        "martes": fila_aux[6],
        "miercoles": fila_aux[7],
        "jueves": fila_aux[8],
        "viernes": fila_aux[9],
        "sabado": fila_aux[10],
        "id": fila_aux[11]
      }

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

  sentencia = "INSERT INTO rols (nombre, id_horarios) VALUES ('"+rol.nombre+"', "+rol.id_horarios+")"
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

  sentencia = "UPDATE rols SET nombre = '"+rol.nombre+"', id_horarios = '"+rol.id_horarios+"' WHERE id = "+str(id)

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
