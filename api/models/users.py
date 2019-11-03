import re
import datetime

from .model import Model

class UsersModel(Model):
    table_name = 'user'
    col_login = 'login'
    col_name = 'name'
    col_email = 'email'
    col_birthday = 'birthday'
    col_password = 'password'

    def __init__(self, login, name, email, birthday, password):
        self.login = login
        self.name = name
        self.email = email
        self.birthday = birthday
        self.password = password
    
    def insert(self):
        sql = (f'INSERT INTO "{self.table_name}" '
               f'({self.col_login}, {self.col_password}, '
               f'{self.col_name}, {self.col_email}, {self.col_birthday}) '
                'VALUES (LOWER(%s), %s, LOWER(%s), %s, %s)')
        result = self.connector.execute_sql(
            sql, (self.login, self.password, self.name, self.email, self.birthday)
        )
    
    def to_dict(self):
        return {'login': self.login, 'name': self.name, 
                'email': self.email, 'birthday': self.birthday.strftime('%d/%m/%Y')}

    def find_by_login(login):
        sql = f'SELECT * FROM "{UsersModel.table_name}" WHERE {UsersModel.col_login}=''LOWER(%s)'
        result = UsersModel.connector.execute_sql(sql, (login,))
        return UsersModel.instantiate_rows(result)

    def find_by_email(email):
        sql = f'SELECT * FROM "{UsersModel.table_name}" WHERE {UsersModel.col_email}=''LOWER(%s)'
        result = UsersModel.connector.execute_sql(sql, (email,))
        return UsersModel.instantiate_rows(result)
    
    def get_all():
        result = UsersModel.connector.execute_sql(
            f'SELECT * FROM {UsersModel.table_name};'
        )
        return UsersModel.instantiate_rows(result)


    class Validation:
        login = [
            (lambda v: isinstance(v, str), 4),
            (lambda v: len(v) > 0, 4)
        ]
        name = [
            (lambda v: isinstance(v, str), 4),
            (lambda v: re.match(r'^([^\W\d_]+[ ]*)+$', v, re.UNICODE), 7),
        ]
        birthday = [
            (lambda v: isinstance(v, str), 4),
            (lambda v: datetime.datetime.strptime(v, '%d/%m/%Y'), 4),
        ]
        password = [
            (lambda v: isinstance(v, str), 4),
            (lambda v: len(v) >= 8, 5),
            (lambda v: len(v) <=16, 6)
        ]
