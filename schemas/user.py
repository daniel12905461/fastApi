from pydantic import BaseModel
# from typing import Optional

class User(BaseModel):
    # id: Optional[str]
    # name: str
    user: str
    password: str

# @app.get("/")
# def index():
#     return {"message": "Hola mundo"}

# @app.get("/libros/{id}")
# def get_libro(id: int):
#     return {"message": id}

# @app.post("/libro")
# def insert_libro(libro: Libro):
#     return {"message": libro}
