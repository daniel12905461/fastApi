from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

users = Table("users", meta, 
              Column("id", Integer, primary_key= True), 
              Column("name", String(225)),
              Column("user", String(225)),
              Column("password", String(225)))

meta.create_all(engine)