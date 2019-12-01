from . import Controller
from .profile import print_profile
from ..prompt import *
from ..api import BadRequest
from ..validations import validate_required

from datetime import datetime


@Controller
def find_team(api):
    while True:
        clear_screen()
        section_title('Procurar por um time')
        
        search_team = Text(message='Quais as iniciais ou o nome do time?', validate=validate_required)
        if not search_team:
            return
        try:
            found_teams = api.find_team(search_team)
        except BadRequest as exception:
            errors = exception.args[0]
            if errors[0]['code'] == 16:
                print_errors(errors)
                found_teams = []
                team = '__exit__'
            else:
                raise exception
        
        if len(found_teams) == 1:
            team = found_teams[0]
        elif len(found_teams) > 1:
            print(f"\nEncontramos {len(found_teams)} times com as palavras chave\n")
            teams = [(f"{team['initials']} - {team['name']}", team) for team in found_teams]
            options = teams + [('Nenhum desses', '__exit__')]
            team = List(message="Por qual time você está procurando?", choices=options)
            if not team:
                return
        
        if team == '__exit__':
            try_again = Confirm(message='Quer tentar pesquisar usando outro termo?')

            if not try_again:
                break
        else:
            print_team(team)
            Back()
            break

def print_team(team):
    # TODO: Implementar membros quando for disponibilizado pela API
    clear_screen()
    section_title(f"{team['initials']} - {team['name']}")
    members = []
    team_info = (f"{bright('Criado por:')} {team['owner']}\n"
                 f"{bright('Membros:')}")
    print(team_info)
