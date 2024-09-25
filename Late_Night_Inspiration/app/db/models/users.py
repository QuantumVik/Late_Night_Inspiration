from pydantic import BaseModel
import bcrypt


class Userinfo(BaseModel):
    username :str
    password  : str

