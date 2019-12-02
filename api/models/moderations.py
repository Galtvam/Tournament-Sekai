import re
import datetime

from .model import Model

class ModerationsModel(Model):
    table_name = 'moderate'
    col_moderator_login = 'moderator_login'
    col_cod_tournament = 'cod_tournament'


    def __init__(self, moderator_login, cod_tournament):
        self.moderator_login = moderator_login
        self.cod_tournament = cod_tournament
  
    def insert(self):
        sql = (f'INSERT INTO "{self.table_name}" '
                'VALUES (%s, %s)')
        result = self.connector.execute_sql(
            sql, (self.moderator_login, self.cod_tournament)
        )


    def to_dict(self):
        return {'login': self.moderator_login, 'cod_tournament': self.cod_tournament}

    def find_moderation(login, cod_tournament):
        sql = (f"SELECT * FROM {ModerationsModel.table_name} WHERE {ModerationsModel.col_moderator_login} = '{login}' and "
        f"{ModerationsModel.col_cod_tournament} = {cod_tournament}")
        result = ModerationsModel.connector.execute_sql(sql)
        return ModerationsModel.instantiate_rows(result)


    def get_all():
        result = ModerationsModel.connector.execute_sql(
            f'SELECT * FROM {ModerationsModel.table_name};'
        )
        return ModerationsModel.instantiate_rows(result)
