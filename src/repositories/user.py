from models.users import Users
from repositories.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = Users
