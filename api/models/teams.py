from .model import Model

class TeamsModel(Model):
    table_name = 'team'
    col_initials = 'initials'
    col_name = 'name'

    def __init__(self, initials, name):

        self.initials = initials
        self.name = name
    
    def insert(self):
        sql = (f'INSERT INTO {self.table_name} ' 
                'VALUES (%s, %s) RETURNING initials')
        result = self.connector.execute_sql(sql, (self.initials, self.name))
        self.initials = result[0]['initials']
    
    def to_dict(self):
        return {'initials': self.initials, 'name': self.name}

    @staticmethod
    def find_by_initials(initials):
        result = TeamsModel.connector.execute_sql(
            f'SELECT * FROM {TeamsModel.table_name} '
            'WHERE ' + TeamsModel.col_initials +'=%s',
            (initials,)
        )
        return TeamsModel.instantiate_rows(result)
    
    @staticmethod
    def get_all():
        result = TeamsModel.connector.execute_sql(
            f'SELECT * FROM {TeamsModel.table_name};'
        )
        return TeamsModel.instantiate_rows(result)


    def update(self):
        sql = (f"UPDATE {self.table_name} SET initials = '{self.initials}', "
        f"name = '{self.name}' WHERE initials = '{self.initials}'")
        self.connector.execute_sql(sql)

    def delete(self):
        sql = (f"DELETE FROM {self.table_name} WHERE initials = '{self.initials}'")
        self.connector.execute_sql(sql)

