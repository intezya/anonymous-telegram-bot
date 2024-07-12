from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    hashed_id: str


class UserSchemaAdd(BaseModel):
    id: int
