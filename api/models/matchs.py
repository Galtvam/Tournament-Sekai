from .model import Model

class MatchsModel(Model):
    table_name = 'match'
    col_id_match = 'id_match'
    col_date = 'date'
    col_winner = 'winner'
    col_cod_tournament = 'cod_tournament'

    def __init__(self, id_match, date, cod_tournament, winner=None):

        self.id_match = id_match
        self.date = date
        self.winner = winner
        self.cod_tournament = cod_tournament

    
    def insert(self):
        sql = (f'INSERT INTO {self.table_name} ' 
                'VALUES (%s, %s, %s, %s) RETURNING id_match')
        result = self.connector.execute_sql(sql, (self.id_match, self.date, self.winner,
                                            self.cod_tournament))
        self.id_match = result[0]['id_match']
    
    def to_dict(self):
        return {'id_match': self.id_match, 'date': self.date, 'winner': self.winner,
                'cod_tournament': self.cod_tournament}

    @staticmethod
    def find_by_id_match(id_match, cod_tournament):
        result = MatchsModel.connector.execute_sql(
            f'SELECT * FROM {MatchsModel.table_name} '
            "WHERE " + MatchsModel.col_id_match +"='%s' and "+ col_cod_tournament" ='%s'",
            (id_match,)
        )
        return MatchsModel.instantiate_rows(result)
    
    @staticmethod
    def get_all():
        result = MatchsModel.connector.execute_sql(
            f'SELECT * FROM {MatchsModel.table_name};'
        )
        return MatchsModel.instantiate_rows(result)


    def update(self):
        sql = (f"UPDATE {self.table_name} SET date = '{self.date}', "
        f"winner = '{self.winner}' WHERE id_match = '{self.id_match}'")
        self.connector.execute_sql(sql)

    def delete(self):
        sql = (f"DELETE FROM {self.table_name} WHERE id_match = '{self.id_match}'")
        self.connector.execute_sql(sql)

