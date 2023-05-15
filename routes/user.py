from fastapi import APIRouter
# from config.db import conn
from config.db import conectar_db
# from models.user import users
from schemas.user import User

user = APIRouter()

@user.get("/users")
async def getall():
    # conexion = conectar_db()
    # cursor = conexion.cursor()
    # return cursor.execute("SELECT * FROM tu_tabla").fetchall()
    # conexion.close()
    # return await conn.execute(users.select()).fetchall()
    # return "dasdasdasdasd"
    # return {"message": "Hola mundo"}
  # Obtiene la conexión a la base de datos
  cnx = conectar_db()

  cursor = cnx.cursor()

  consulta = ("SELECT name,user,password FROM users")
  cursor.execute(consulta)

  # Recupera los resultados de la consulta
  for (name, user, password) in cursor:
    # print(columna1, columna2)
    new_user = {"name": name, "user": user, "password": password}

  # Cierra el cursor y la conexión
  cursor.close()
  cnx.close()

  return new_user

@user.post("/users")
async def createAux(userAux: User):
  # new_user = {"name": userAux.name, "user": userAux.user, "password": userAux.password}
  cnx = conectar_db()
  cursor = cnx.cursor()

  sentencia = "INSERT INTO users (name, user, password) VALUES (%s, %s, %s)"
  valores = (userAux.name, userAux.user, userAux.password)

  cursor.execute(sentencia, valores)
  cnx.commit()

  cursor.close()
  cnx.close()

  return cursor
