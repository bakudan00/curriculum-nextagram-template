import peewee as pw
import re
from models.base_model import BaseModel
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash

class User(UserMixin, BaseModel):
    
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(null=False, unique=True)
    password = pw.CharField(null=False)
    role = pw.TextField(default='user')
    img_Profile = pw.TextField(null=True)

    #validation on sign up page
    # @staticmethod
    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)
        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_username:
            self.errors.append('Username exist, please use other username')
        elif duplicate_email:
            self.errors.append('Email exist, please use other email')
        elif not re.match(r"^(?:(?=.*[a-z])(?:(?=.*[A-Z])(?=.*[\d\W])|(?=.*\W)(?=.*\d))|(?=.*\W)(?=.*[A-Z])(?=.*\d)).{8,}$", self.password):
            self.errors.append('Password length needs to have both uppercase and lowercase character, password should have at least one special character and no longer than 6 char')      
        else:
            self.password = generate_password_hash(self.password)

        




            
        
       
    
            
    
    

    
    
