from .model import Model

class TournamentsModel(Model):
    table_name = 'tournament'
    col_cod_tournament = 'cod_tournament'
    col_name = 'name'
    col_description = 'description'
    col_start_date = 'start_date'
    col_end_date = 'end_date'
    col_owner_login = 'owner_login'

    def __init__(self, name, description, start_date, end_date, owner_login, cod_tournament=None):

        self.cod_tournament  = cod_tournament
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.owner_login = owner_login

    def insert(self):
        sql = (f'INSERT INTO {self.table_name} ' 
                'VALUES (DEFAULT,%s, %s, %s, %s, %s) RETURNING cod_tournament')
        result = self.connector.execute_sql(sql, (self.name,
        self.description, self.start_date, self.end_date, self.owner_login))
        self.initials = result[0]['cod_tournament']
    
    def to_dict(self):
        return {'cod_tournament': self.cod_tournament, 'name': self.name,
        'description': self.description, 'start_date': self.start_date.strftime('%d/%m/%Y'),
         'end_date': self.end_date.strftime('%d/%m/%Y'),
        'owner_login': self.owner_login}

    @staticmethod
    def find_by_cod_tournament(cod_tournament):
        result = TournamentsModel.connector.execute_sql(
            f'SELECT * FROM {TournamentsModel.table_name} '
            f'WHERE {TournamentsModel.col_cod_tournament} = {cod_tournament}'
            
        )
        
        return TournamentsModel.instantiate_rows(result)
    
    @staticmethod
    def search_by_name(name, limit=20, offset=0):
        result = TournamentsModel.connector.execute_sql(
            f'SELECT * FROM {TournamentsModel.table_name} '
            f"WHERE LOWER({TournamentsModel.col_name}) LIKE LOWER('%{name}%') "
            f'LIMIT {limit} OFFSET {offset}'
        )
            
        return TournamentsModel.instantiate_rows(result)


    @staticmethod
    def get_all(limit,offset):
        result = TournamentsModel.connector.execute_sql(
            f'SELECT * FROM {TournamentsModel.table_name} '
            f'LIMIT {limit} OFFSET {offset};'
        )
        return TournamentsModel.instantiate_rows(result)

    def update_by_code(self):
        sql = (f"UPDATE {self.table_name} SET name = '{self.name}', description = '{self.description}', "
        f"start_date = '{self.start_date}', end_date = '{self.end_date}', "
        f"owner_login = '{self.owner_login}' WHERE cod_tournament = '{self.cod_tournament}'")
        self.connector.execute_sql(sql)

    def delete_by_code(self):
        sql = (f"DELETE FROM {self.table_name} WHERE cod_tournament = '{self.cod_tournament}'")
        self.connector.execute_sql(sql)

    @staticmethod
    def add_member(cod_tournament, initials, login):
        '''
        Adiciona membro ao time naquele torneio
        '''
        sql = (f"INSERT INTO integrate VALUES ( '{cod_tournament}', '{initials}', '{login}'")
        self.connector.execute_sql(sql)
        
    @staticmethod
    def view_members(cod_tournament, initials, login):
        sql (f"SELECT login FROM integrate WHERE cod_tournament = '{cod_tournament}', "
        f"initials = '{initials}', participant_login = '{cod_tournament}'")
        self.connector.execute_sql(sql)