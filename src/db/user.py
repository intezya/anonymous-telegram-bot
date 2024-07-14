from models.users import Users
from db.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = Users
