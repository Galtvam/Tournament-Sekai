from . import Controller
from ..prompt import *
from ..api import BadRequest

@Controller
def ranking(api):
    def _header():
        clear_screen()
        section_title('Ranking')
    menu = [
        ('Ranking de Times', 'ranking_team'),
        ('Ranking de Jogadores', 'ranking_players'),
    ]
    Menu(api, menu, before_show=_header)


@Controller
def ranking_team(api):
    def _header():
        clear_screen()
        section_title('Ranking de Times')
    menu = [
        ('Times com mais mais partidas vencidas', 'ranking_teams_win_tournament_match'),
        ('Times com mais vitórias em torneios', 'ranking_teams_win_tournament')
    ]
    Menu(api, menu, before_show=_header)


@Controller
def ranking_players(api):
    def _header():
        clear_screen()
        section_title('Ranking de Jogadores')
    menu = [
        ('Jogadores com mais particição em torneios', 'ranking_players_sub_tournament'),
        ('Jogadores com mais alianças à times', 'ranking_players_sub_teams'),
        ('Jogadores com mais partidas vencidas', 'ranking_players_win_tournament_match'),
        ('Jogadores com mais vitórias em torneios', 'ranking_players_win_tournament')
    ]
    Menu(api, menu, before_show=_header)
