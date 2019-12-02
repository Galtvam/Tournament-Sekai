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
            teams = [(f"{team['initials']} - {team['name']}", team['initials']) for team in found_teams]
            options = teams + [('Nenhum desses', '__exit__')]
            team = List(message="Por qual time você está procurando?", choices=options)
            if not team:
                return
        
        if team == '__exit__':
            try_again = Confirm(message='Quer tentar pesquisar usando outro termo?')

            if not try_again:
                break
        else:
            view_team(api, team)
            Back()
            break

@Controller
def my_teams(api):
    clear_screen()
    section_title('Meus Times')
    teams = api.user_teams(api.user['login'])
    team_choices = [(f"{team['initials']} - {team['name']}", team['initials']) for team in teams]
    if not teams:
        print_error('Você ainda não participa de nenhum time\n')
    options = team_choices + [('Voltar', '__exit__')]
    choose = List(message='Você participa dos seguinte times', choices=options)
    if choose != '__exit__':
        team = [t for t in teams if t['initials'] == choose]
        if team:
            team[0]
            view_team(api, team['initials'])


@Controller
def change_team_initials(api, initials):
    new_initials = Text(message='Para quais iniciais você deseja alterar?', validate=validate_required)
    team = api.update_team(initials, new_initials=new_initials)
    print_success('Iniciais do time alterada com sucesso')
    Back()

@Controller
def change_team_name(api, initials):
    new_name = Text(message='Qual o novo nome do seu time?', validate=validate_required)
    team = api.update_team(initials, new_name=new_name)
    print_success('Nome do time alterada com sucesso')
    Back()

@Controller
def team_new_member(api, initials):
    login = Text(message='Qual o login do usuário que você deseja adicionar?', validate=validate_required)
    user = api.get_user(login)
    api.add_team_member(initials, login)
    print_success('Usuário adicionado como membro com sucesso')
    Back()

@Controller
def delete_team(api, initials):
    confirm = Confirm(message='Você tem certeza que quer deletar o time?')
    if confirm:
        api.delete_team(initials)
        print_success('Time removido com sucesso')
        Back()


def view_team(api, initials):
    def _header():
        print_team(api, initials)
    team = api.get_team(initials)
    if api.user['login'] == team['owner']:
        menu = [
            ('Alterar iniciais do time', 'change_team_initials'),
            ('Alterar nome do time', 'change_team_name'),
            ('Adicionar novo membro', 'team_new_member'),
            ('Apagar o time', 'delete_team'),
        ]
        try:
            Menu(api, menu, before_show=_header, initials=initials)
        except BadRequest as exception:
            errors = exception.args[0]
            if errors[0]['code'] != 15:
                raise exception

def print_team(api, initials):
    clear_screen()
    team = api.get_team(initials)
    section_title(f"{team['initials']} - {team['name']}")
    members = api.team_members(team['initials'])
    members = ', '.join(m['login'] for m in members)
    team_info = (f"{bright('Criado por:')} {team['owner']}\n"
                 f"{bright('Membros:')} {members}\n")
    print(team_info)
