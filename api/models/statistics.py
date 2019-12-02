from .model import Model

class StatisticsModel(Model):
    table_integrate = 'integrate'
    table_team = 'team'
    table_play = 'play'
    table_att_participant = 'attribute_participant'
    table_attribute = 'attribute'
    table_match = 'match'
    table_tournament = 'tournament'


    @staticmethod
    def periodic_tournament_participant(start_date, end_date):
        sql = (f'SELECT DISTINCT i.participant_login '
            f'FROM {StatisticsModel.table_integrate} AS i '
            f'JOIN {StatisticsModel.table_tournament} AS t ON i.cod_tournament = t.cod_tournament '
            'WHERE t.start_date >= %s AND t.end_date <= %s'
        )
        result = StatisticsModel.connector.execute_sql(
            sql, (start_date, end_date,)
        )
        return StatisticsModel._best_player_list(result)
    
    #esse
    @staticmethod
    def most_diferent_team_participation():
        sql = (f'SELECT "participant_login", COUNT("cod_tournament") '
            f'FROM {StatisticsModel.table_integrate} '
            'GROUP BY "participant_login"'
        )
        result = StatisticsModel.connector.execute_sql(sql)
        return StatisticsModel._best_player_list(result)
    
    #esse
    @staticmethod
    def biggest_winners():
        sql = (f'SELECT i.participant_login, COUNT(t.winner) '
            f'FROM {StatisticsModel.table_integrate} AS i '
            f'JOIN {StatisticsModel.table_tournament} AS t ON i.cod_tournament = t.cod_tournament '
            'WHERE i.initials = t.winner '
            'GROUP BY i.participant_login '
            'ORDER BY COUNT(t.winner) DESC'
        )
        result = StatisticsModel.connector.execute_sql(sql)
        return StatisticsModel._best_player_list(result)
    
    #esse
    @staticmethod
    def biggest_winners_teams():
        sql = (f'SELECT te.initials, COUNT(tor.winner) '
            f'FROM {StatisticsModel.table_team} AS te '
            f'JOIN {StatisticsModel.table_tournament} AS tor ON te.initials=tor.winner '
            'GROUP BY te.initials '
            'ORDER BY COUNT(tor.winner) DESC'
        )
        result = StatisticsModel.connector.execute_sql(sql)
        return StatisticsModel._best_player_list(result)

    #esse
    @staticmethod
    def biggest_match_winners():
        sql = (f'SELECT  i.participant_login, COUNT(i.participant_login) '
            f'FROM {StatisticsModel.table_integrate} AS i '
            f'WHERE EXISTS ( SELECT NULL FROM {StatisticsModel.table_play} AS p '
            f'JOIN {StatisticsModel.table_match} as m ON p.id_match = m.id_match '
            f'WHERE i.initials = p.initials AND i.initials = m.winner) '
            'GROUP BY i.participant_login '
            'ORDER BY COUNT(i.participant_login) DESC'
        )
        result = StatisticsModel.connector.execute_sql(sql)
        return StatisticsModel._best_player_list(result)
    
    #esse
    @staticmethod
    def biggest_match_winners_teams():
        sql = (f'SELECT te.initials, COUNT(ma.winner) '
            f'FROM {StatisticsModel.table_team} AS te '
            f'JOIN {StatisticsModel.table_match} AS ma ON ma.winner=te.initials '
            'GROUP BY te.initials '
            'ORDER BY COUNT(ma.winner) DESC '
        )
        result = StatisticsModel.connector.execute_sql(sql)
        return StatisticsModel._best_player_list(result)
    
    #esse
    @staticmethod
    def participants_information_one_attribute(id_attribute, cod_tournament):
        sql = (f'SELECT ap.participant_login, ap.value ' 
            f'FROM {StatisticsModel.table_att_participant} AS ap '
            f'JOIN {StatisticsModel.table_attribute} AS a ON a.id_attribute=ap.id_attribute '
            'WHERE a.cod_tournament= %s ' 
            'AND a.id_attribute= %s'
        )
        result = StatisticsModel.connector.execute_sql(
            sql, (cod_tournament, id_attribute,)
        )
        return StatisticsModel._best_player_list(result)
    
    #esse
    @staticmethod
    def best_participants_information_one_attribute(id_attribute, cod_tournament):
        sql = ('SELECT DISTINCT i.participant_login, a.value '
            f'FROM {StatisticsModel.table_att_participant} AS a '
            f'INNER JOIN {StatisticsModel.table_integrate} AS i ON i.participant_login = a.participant_login '
            'WHERE a.cod_tournament=%s  AND a.id_attribute=%s '
            'ORDER BY a.value DESC'
        )
        result = StatisticsModel.connector.execute_sql(
            sql, (cod_tournament, id_attribute,)
        )
        return StatisticsModel._best_player_list(result)
    
    #esse
    @staticmethod
    def worst_participants_information_one_attribute(id_attribute, cod_tournament):
        sql = ('SELECT DISTINCT i.participant_login, a.value '
            f'FROM {StatisticsModel.table_att_participant} AS a '
            f'INNER JOIN {StatisticsModel.table_integrate} AS i ON i.participant_login = a.participant_login '
            'WHERE a.cod_tournament=%s AND a.id_attribute=%s '
            'ORDER BY a.value ASC'
        )
        result = StatisticsModel.connector.execute_sql(
            sql, (cod_tournament, id_attribute,)
        )
        return StatisticsModel._best_player_list(result)



    # Ajustes de retorno
    def _best_player_list(result):
        participants = []
        for login in result:
            participants.append(login['login'])
        return participants