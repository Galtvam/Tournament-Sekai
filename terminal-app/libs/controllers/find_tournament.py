from . import Controller
from ..prompt import *
from ..api import BadRequest
from ..validations import validate_required

from datetime import datetime


@Controller
def find_tournament(api):
    while True:
        clear_screen()
        section_title('Procurar por um Torneio')
        
        search_tournament = Text(message='Nome do torneio', validate=validate_required)
        if not search_tournament:
            return
        
        found_tournaments = api.find_tournaments(search_tournament)
        
        if len(found_tournaments) == 0:
            tournament = '__exit__'
        elif len(found_tournaments) == 1:
            tournament = found_tournaments[0]['cod_tournament']
        elif len(found_tournaments) > 1:
            print(f"\nEncontramos {len(found_tournaments)} times com as palavras chave\n")
            tournaments = [(f"{t['name']}", t['cod_tournament']) for t in found_tournaments]
            options = teams + [('Nenhum desses', '__exit__')]
            tournament = List(message="Por qual torneio você está procurando?", choices=options)
            if not tournament:
                return
        
        if tournament == '__exit__':
            try_again = Confirm(message='Quer tentar pesquisar usando outro termo?')

            if not try_again:
                break
        else:
            view_tournament(api, tournament)
            Back()
            break


def view_tournament(api, cod):
    def _header():
        print_tournament(api, cod)
    tournament = api.get_tournament(cod)
    if api.user['login'] == tournament['owner']:
        menu = [
            ('Atualizar informações do torneio', 'update_tournament'),
        ]
    else:
        menu += [

        ]
    Menu(api, menu, before_show=_header, cod=cod)


def print_tournament(api, cod):
    clear_screen()
    team = api.get_tournament(cod)
    section_title(f"#{team['cod_tournament']} {team['name']}")
    tournament_info = (f"{bright('Criado por:')} {team['owner']}\n"
                 f"{bright('Data de início:')} {team['start_date']}\t"
                 f"{bright('Data de encerramento:')} {team['end_date']}\n"
                 f"{bright('Descrição:')} {team['description']}\n")
    team_participants = api.get_tournament_teams(cod)
    print(tournament_info)
