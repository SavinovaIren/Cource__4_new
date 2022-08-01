from typing import List, Optional

from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO, T
from project.models import Genre, Movie, Director, User
from project.tools.security import generate_password_hash


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

# Вывода фильмов с применение фильтра по годам (с сортировкой от большего к меньшему)
    def get_all_order_by(self, page: Optional[int] = None, filter=None) -> List[T]:
        stmt = self._db_session.query(self.__model__)
        if filter:
            stmt = stmt.order_by(desc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


class UsersDAO(BaseDAO[User]):
    __model__ = User

# добавляет нового пользователя с email и захэшированным паролем
    def create(self, login, password):
        try:
            self._db_session.add(
                User(
                    email=login,
                    password_hash=generate_password_hash(password)
                )
            )
            self._db_session.commit()
            print("Пользователь добавлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()

# получение пользователя по переданному логину
    def get_user_by_login(self, login):
        try:
            stmt = self._db_session.query(self.__model__).filter(self.__model__.email == login).one()
            return stmt
        except Exception as e:
            print(e)
            return {}

# обнавляет данные, которые были изменены
    def update(self, login, data):
        try:
            self._db_session.query(self.__model__).filter(self.__model__.email == login).update(
                data
            )
            self._db_session.commit()
            print("Пользователь обновлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()


