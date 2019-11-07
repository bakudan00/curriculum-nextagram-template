from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(null=False, unique=True)
    password = pw.CharField(null=False)

    # def validate(self):
    #     if len(self.password) < 8:
    #         self.errors.append('Password length needs to be at least 8 character')
    #     else:
    #         self.password = generate_password_hash(self.password)
