from .model import Model

class UsersModel(Model):
    table_name = 'users'
    col_id = 'id'
    col_name = 'name'
    col_age = 'age'

    def __init__(self, name, age, id=None):
        self.id = id
        self.name = name
        self.age = age
    
    @property
    def birthday_year(self):
        return 2019 - self.age
    
    def insert(self):
        sql = (f'INSERT INTO {self.table_name} ({self.col_name},{self.col_age})' 
                'VALUES (%s, %s) RETURNING id')
        result = self.connector.execute_sql(sql, (self.name, self.age))
        self.id = result[0]['id']
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}

    def find_by_id(id):
        result = UsersModel.connector.execute_sql(
            f'SELECT * FROM {UsersModel.table_name} WHERE {UsersModel.col_id}={id}'
        )
        return UsersModel.instantiate_rows(result)
    
    def get_all():
        result = UsersModel.connector.execute_sql(
            f'SELECT * FROM {UsersModel.table_name};'
        )
        return UsersModel.instantiate_rows(result)
