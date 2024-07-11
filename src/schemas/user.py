from pydantic import BaseModel


class UserSchema(BaseModel):
    tg_id: int
    hashed_tg_id: str


class UserSchemaAdd(BaseModel):
    tg_id: int
