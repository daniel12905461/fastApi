from fastapi import APIRouter, Request
from config.db import conectar_db
from schemas.horario import Horario
import mysql.connector

horario = APIRouter()

@horario.get("/horarios")
async def getall():
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, domingo, lunes, martes, miercoles, jueves, viernes, sabado, id FROM horarios")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"].append({
      "hora_inicio": str(fila[0]),
      "hora_inicio_reseso": str(fila[1]),
      "hora_fin_reseso": str(fila[2]),
      "hora_fin": str(fila[3]),
      "domingo": fila[4],
      "lunes": fila[5],
      "martes": fila[6],
      "miercoles": fila[7],
      "jueves": fila[8],
      "viernes": fila[9],
      "sabado": fila[10],
      "id": fila[11]
    })
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@horario.get("/horarios/{id}")
async def getbyid(id: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, domingo, lunes, martes, miercoles, jueves, viernes, sabado, id FROM horarios WHERE id = "+str(id))
  # valores = (id)
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  for fila in resultados:
    json_resultados["data"] = {
      "hora_inicio": str(fila[0]),
      "hora_inicio_reseso": str(fila[1]),
      "hora_fin_reseso": str(fila[2]),
      "hora_fin": str(fila[3]),
      "domingo": fila[4],
      "lunes": fila[5],
      "martes": fila[6],
      "miercoles": fila[7],
      "jueves": fila[8],
      "viernes": fila[9],
      "sabado": fila[10],
      "id": fila[11]
    }
    json_resultados["ok"] = True

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados

@horario.post("/horarios")
async def create(horario: Horario):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "INSERT INTO horarios (hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, domingo, lunes, martes, miercoles, jueves, viernes, sabado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  valores = (
    horario.hora_inicio,
    horario.hora_inicio_reseso,
    horario.hora_fin_reseso,
    horario.hora_fin,
    horario.domingo,
    horario.lunes,
    horario.martes,
    horario.miercoles,
    horario.jueves,
    horario.viernes,
    horario.sabado,
  )

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

@horario.put("/horarios/{id}")
async def update(id: int, horario: Horario):
  cnx = conectar_db()
  cursor = cnx.cursor()

  # sentencia = "UPDATE horarios SET hora_inicio = '"+horario.hora_inicio+"', hora_inicio_reseso = '"+horario.hora_inicio_reseso+"', hora_fin_reseso = '"+horario.hora_fin_reseso+"', hora_fin = '"+horario.hora_fin+"', domingo = "+horario.domingo+", lunes = "+horario.lunes+", martes = "+horario.martes+", miercoles = "+horario.miercoles+", jueves = "+horario.jueves+", viernes = "+horario.viernes+", sabado = "+horario.sabado+" WHERE id = "+str(id)
  sentencia = "UPDATE horarios SET hora_inicio = '"+horario.hora_inicio+"', hora_inicio_reseso = '"+horario.hora_inicio_reseso+"', hora_fin_reseso = '"+horario.hora_fin_reseso+"', hora_fin = '"+horario.hora_fin+"', domingo = %s, lunes = %s, martes = %s, miercoles = %s, jueves = %s, viernes = %s, sabado = %s WHERE id = "+str(id)
  valores = (
    horario.domingo,
    horario.lunes,
    horario.martes,
    horario.miercoles,
    horario.jueves,
    horario.viernes,
    horario.sabado
  )

  cursor.execute(sentencia, valores)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor

@horario.delete("/horarios/{id}")
async def delete(id: int):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "DELETE FROM horarios WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor
