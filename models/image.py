import peewee as pw
import re
from models.base_model import BaseModel
from models.user import User

class Image(BaseModel):
    imageURL = pw.CharField(null=True)
    user_id = pw.ForeignKeyField(User, backref="users", unique=True)
