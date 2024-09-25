from dataclasses import Field

from pydantic import BaseModel , constr



class Idea(BaseModel):
    content: constr(min_length=5, max_length=225) = "Idea must be between 5 and 225 characters"

class Clarification(BaseModel):
    clarification: constr(min_length=5, max_length=225) = "Idea must be between 5 and 225 characters"

class UpdateIdea(BaseModel):
    content: constr(min_length=5, max_length=225) = "Idea must be between 5 and 225 characters"
    clarification: constr(min_length=5, max_length=225) = "Idea must be between 5 and 225 characters"


# class UpadteIdea:
#     pass