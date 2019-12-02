from . import Controller
from ..prompt import *
from ..api import BadRequest
from ..validations import validate_date, validate_end_date

from prettytable import PrettyTable

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


@Controller
def ranking_players_sub_tournament(api):
    clear_screen()
    section_title('Jogadores com mais particição em torneios')
    start_date = Text(message='Data de início (dd/mm/YYYY)', validate=validate_date),
    end_date = Text(message='Data de fim (dd/mm/YYYY)', validate=validate_end_date(start_date))
    results = api.get_periodic_tournament_participant(start_date, end_date)

    table = PrettyTable()
    table.field_names = ["Posição", "Login", "Total"]
    for i, row in enumerate(results):
        table.add_row([f"{i + 1}º", row['participant_login'], row['count']])

    print(table)
    Back()

@Controller
def ranking_players_sub_teams(api):
    clear_screen()
    section_title('Jogadores com mais alianças à times')
    results = api.get_most_diferent_team_participation()
    table = PrettyTable()
    table.field_names = ["Posição", "Login"]
    for i, row in enumerate(results):
        table.add_row([f"{i + 1}º", row['participant_login']])

    print(table)
    Back()

@Controller
def ranking_players_win_tournament_match(api):
    clear_screen()
    section_title('Jogadores com mais partidas vencidas')
    results = api.get_biggest_match_winners()
    table = PrettyTable()
    table.field_names = ["Posição", "Login", "Total"]
    for i, row in enumerate(results):
        table.add_row([f"{i + 1}º", row['participant_login'], row['count']])

    print(table)
    Back()

@Controller
def ranking_players_win_tournament(api):
    clear_screen()
    section_title('Jogadores com mais vitórias em torneios')
    results = api.get_biggest_winners()
    table = PrettyTable()
    table.field_names = ["Posição", "Login", "Total"]
    for i, row in enumerate(results):
        table.add_row([f"{i + 1}º", row['participant_login'], row['count']])

    print(table)
    Back()