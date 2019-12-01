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
    col_country = 'country'
    col_state = 'state'
    col_city = 'city'
    col_neighborhood = 'neighborhood'
    col_street = 'street'
    col_number = 'number'
    col_complement = 'complement'

    def __init__(
        self, login, name, email, birthday, password,
        country=None, state=None, city=None,
        neighborhood=None, street=None,
        number=None, complement=None
    ):
        self.login = login
        self.name = name
        self.email = email
        self.birthday = birthday
        self.password = password
        self.country = country
        self.state = state
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.number = number
        self.complement = complement


    def insert(self):
        sql = (f'INSERT INTO "{self.table_name}" '
               f'({self.col_login}, {self.col_password}, '
               f'{self.col_name}, {self.col_email}, {self.col_birthday}) '
                'VALUES (LOWER(%s), %s, LOWER(%s), %s, %s)')
        result = self.connector.execute_sql(
            sql, (self.login, self.password, self.name, self.email, self.birthday)
        )

    def update(self):
        empty = []
        for field in (
            'country', 'state', 'city', 'neighborhood',
            'street', 'number', 'complement'
        ):
            value = getattr(self, field)
            if field == 'number' and value == None:
                setattr(self, field, 'NAN')
                empty.append(field)
            elif value == None:
                empty.append(field)
                setattr(self, field, 'NULL')
        sql = (f'UPDATE "{self.table_name}" '
        f"SET name = '{self.name}', email = '{self.email}', "
        f"birthday = '{self.birthday}', password = '{self.password}', country = '{self.country}', "
        f"state = '{self.state}', city = '{self.city}', neighborhood = '{self.neighborhood}', street = '{self.street}', "
        f"number = '{self.number}', complement = '{self.complement}' WHERE login = '{self.login}'")
        result = self.connector.execute_sql(sql)
        for field in empty:
            setattr(self, field, None)

    def to_dict(self):
        return {
                'login': self.login, 'name': self.name,
                'email': self.email, 'birthday': self.birthday.strftime('%d/%m/%Y'),
                'street': self.street, 'number': self.number, 'complement': self.complement,
                'neighborhood': self.neighborhood, 'city': self.city,
                'state': self.state, 'country': self.country
                }

    def find_by_login(login):
        sql = f'SELECT * FROM "{UsersModel.table_name}" WHERE LOWER({UsersModel.col_login})=''LOWER(%s)'
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
            (lambda v: datetime.datetime.strptime(v, '%m/%d/%Y'), 4),
        ]
        password = [
            (lambda v: isinstance(v, str), 4),
            (lambda v: len(v) >= 8, 5),
            (lambda v: len(v) <=16, 6)
        ]
