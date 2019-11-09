import peewee as pw
import re
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash

class User(BaseModel):
    
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(null=False, unique=True)
    password = pw.CharField(null=False)

    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)
        duplicate_email = User.get_or_none(User.email == self.email)

        #validation for duplicate username
        if duplicate_username:
            self.errors.append('Username exist, please use other username')
        else:
            self.username = self.username

        #validation for duplicate email
        if duplicate_email:
            self.errors.append('Email exist, please use other email')
        else:
            self.email = self.email
        
        #validation for password (Uppercasem, Lowercase, Special char, no longer than 6)
        if re.match(r"^(?:(?=.*[a-z])(?:(?=.*[A-Z])(?=.*[\d\W])|(?=.*\W)(?=.*\d))|(?=.*\W)(?=.*[A-Z])(?=.*\d)).{8,}$", self.password):
            self.password = generate_password_hash(self.password)
        else:
            self.errors.append('Password length needs to have both uppercase and lowercase character, password should have at least one special character and no longer than 6 char')
    
            
    
    

    
    
