from .model import Model

class TeamsModel(Model):
    table_name = 'team'
    col_initials = 'initials'
    col_name = 'name'

    def __init__(self, initials, name, owner_login):

        self.initials = initials
        self.name = name
        self.owner_login = owner_login
    
    def insert(self):
        sql = (f'INSERT INTO {self.table_name} ' 
                'VALUES (%s, %s, %s) RETURNING initials')
        result = self.connector.execute_sql(sql, (self.initials, self.name, self.owner_login))
        self.initials = result[0]['initials']
    
    def to_dict(self):
        return {'initials': self.initials, 'name': self.name, 'owner': self.owner_login }

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
    
    @staticmethod
    def user_teams(login):
        result = TeamsModel.connector.execute_sql(
            'SELECT DISTINCT * FROM team_member t ' 
            f'RIGHT JOIN {TeamsModel.table_name} m ON t.initials = m.initials ' 
            'WHERE LOWER("participant_login")=LOWER(%s) OR LOWER("owner_login")=LOWER(%s)',
            (login, login)
        )
        return TeamsModel.instantiate_rows(result)

    def update(self, initials=None):
        initials = initials or self.initials
        sql = (f"UPDATE {self.table_name} SET initials = '{self.initials}', "
        f"name = '{self.name}', owner_login = '{self.owner_login}' WHERE initials = '{initials}'")
        self.connector.execute_sql(sql)

    def delete(self):
        sql = (f"DELETE FROM {self.table_name} WHERE initials = '{self.initials}'")
        self.connector.execute_sql(sql)


    def add_member_to_team(self, login):
        sql = (f"INSERT INTO team_member VALUES('{login}', '{self.initials}')")
        self.connector.execute_sql(sql)

    def view_members_in_team(self):
        sql = (f"SELECT participant_login FROM team_member WHERE initials = '{self.initials}'")
        result = self.connector.execute_sql(sql)
        return result

    def remove_member_to_team(self, login):
        sql = (f"DELETE FROM team_member WHERE initials='{self.initials}' AND participant_login='{login}'")
        self.connector.execute_sql(sql)