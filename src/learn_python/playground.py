from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str

data = {
    'id': 1,
    'name': 'Bo'
    #'email' : 'bo.george@gmail.com'
}

try:
    user = User(**data)
    print(user.email) 
except ValidationError as e:
    print(e.errors())