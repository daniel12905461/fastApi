from fastapi import APIRouter
from config.db import conectar_db
from schemas.funcionario import Funcionario
import json
import mysql.connector

funcionario = APIRouter()

@funcionario.get("/funcionarios")
async def getall(ubicacion_id: int = 0):
  cnx = conectar_db()

  cursor = cnx.cursor()
  
  consulta = ("SELECT f.nombres, f.apellidos, f.ci, f.foto, f.celular, f.fecha_nac, f.id, f.user, f.password, f.id_rols, f.id_ubicaciones FROM funcionarios f ")
  
  if ubicacion_id != 0:
    consulta = consulta + ("JOIN ubicaciones u ON f.id_ubicaciones = u.id " +
      "AND u.id = " + str(ubicacion_id) + " ")
  
  consulta = consulta + "ORDER BY f.nombres ASC"
  
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

@funcionario.get("/funcionarios/{id}")
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

@funcionario.post("/funcionarios")
async def create(funcionario: Funcionario):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "INSERT INTO funcionarios (nombres, apellidos, ci, foto, celular, fecha_nac, user, password, id_rols, id_ubicaciones) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  valores = (funcionario.nombres, funcionario.apellidos, funcionario.ci, funcionario.foto, funcionario.celular, funcionario.fecha_nac, funcionario.user, funcionario.password, funcionario.id_rols, funcionario.id_ubicaciones)

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

@funcionario.put("/funcionarios/{id}")
async def update(id: int, funcionario: Funcionario):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "UPDATE funcionarios SET nombres = '"+funcionario.nombres+"', apellidos = '"+funcionario.apellidos+"', ci = '"+funcionario.ci+"', foto = '"+funcionario.foto+"', celular = '"+funcionario.celular+"', fecha_nac = '"+funcionario.fecha_nac+"', user = '"+funcionario.user+"', password = '"+funcionario.password+"', id_rols = '"+funcionario.id_rols+"', id_ubicaciones = '"+funcionario.id_ubicaciones+"' WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor

@funcionario.delete("/funcionarios/{id}")
async def delete(id: int):
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "DELETE FROM funcionarios WHERE id = "+str(id)

  cursor.execute(sentencia)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor

@funcionario.get("/funcionarios/dias-trabajados/{id}")
async def getbyid(id: int, id_ubicacion: int):
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT f.nombres, f.apellidos, f.ci, f.foto, f.celular, f.fecha_nac, f.id, f.user, f.password, f.id_rols, f.id_ubicaciones " +
              "FROM funcionarios f JOIN ubicaciones u ON f.id_ubicaciones = u.id " +
              "AND u.id = " + str(id_ubicacion) + " " +
              "ORDER BY f.nombres ASC ")
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  json_resultados = {"data": []}

  i=0
  for fila in resultados:
    json_resultados["data"].append({
      "nombres": fila[0],
      "apellidos": fila[1],
      "ci": fila[2],
      "foto": fila[3],
      "celular": fila[4],
      "fecha_nac": fila[5],
      "id": fila[6],
      "user": fila[7],
      "password": fila[8],
      "id_rols": fila[9],
      "id_ubicaciones": fila[10]
    })
    json_resultados["ok"] = True

    consulta = ("SELECT nombre, numero, estado, detalle, fecha, hora_inicio, hora_inicio_reseso, hora_fin_reseso, hora_fin, posicion, hora_retrasos, id_funcionarios, id_mes, id FROM dia WHERE id_funcionarios = "+str(fila[6])+" AND id_mes = "+str(id))
    cursor.execute(consulta)
    resultados_aux = cursor.fetchall()

    json_resultados["data"][i]["dias"] = []

    for fila_aux in resultados_aux:
      json_resultados["data"][i]["dias"].append({
        "nombre": fila_aux[0],
        "numero": fila_aux[1],
        "estado": fila_aux[2],
        "detalle": fila_aux[3],
        "fecha": fila_aux[4],
        "hora_inicio": str(fila_aux[5]),
        "hora_inicio_reseso": str(fila_aux[6]),
        "hora_fin_reseso": str(fila_aux[7]),
        "hora_fin": str(fila_aux[8]),
        "posicion": fila_aux[9],
        "hora_retrasos": str(fila_aux[10]),
        "id_funcionarios": fila_aux[11],
        "id_mes": fila_aux[12],
        "id": fila_aux[13]
      })

    consulta = ("SELECT h.hora_inicio, h.hora_inicio_reseso, h.hora_fin_reseso, h.hora_fin, h.domingo, h.lunes, h.martes, h.miercoles, h.jueves, h.viernes, h.sabado, h.id, r.nombre, r.id_horarios FROM horarios h JOIN rols r ON h.id = r.id_horarios AND r.id = " + str(fila[9]))
    cursor.execute(consulta)
    resultados_aux = cursor.fetchall()

    json_resultados["data"][i]["rol"] = {}
    json_resultados["data"][i]["rol"]['horario'] = {}

    for fila_aux in resultados_aux:
      json_resultados["data"][i]["rol"] = {
        "id": fila[9],
        "nombre": fila_aux[12],
        "id_horarios": fila_aux[13],
      }

      json_resultados["data"][i]["rol"]['horario'] = {
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

    i=i+1

  if len(json_resultados["data"]) == 0:
    json_resultados["mensaje"] = "No se encontraron resultados para la consulta."
    json_resultados["ok"] = False

  cursor.close()
  cnx.close()

  return json_resultados
