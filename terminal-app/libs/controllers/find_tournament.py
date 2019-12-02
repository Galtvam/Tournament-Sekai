from . import Controller
from ..prompt import *
from ..api import BadRequest
from .find_team import view_team
from ..validations import validate_required, validate_start_date, validate_end_date


from datetime import datetime


@Controller
def find_tournament(api):
    while True:
        clear_screen()
        section_title('Procurar por um Torneio')
        
        search_tournament = Text(message='Pesquise por um nome (deixe para ver todos)')
        if not search_tournament:
            found_tournaments = api.all_tournaments()
        else:
            found_tournaments = api.find_tournaments(search_tournament)
        
        if len(found_tournaments) == 0:
            print_error('Nenhum torneio encontrado')
            tournament = '__exit__'
        elif len(found_tournaments) == 1:
            tournament = found_tournaments[0]['cod_tournament']
        elif len(found_tournaments) > 1:
            print(f"\nEncontramos {len(found_tournaments)} torneios\n")
            tournaments = [(f"{t['name']}", t['cod_tournament']) for t in found_tournaments]
            options = tournaments + [('Nenhum desses', '__exit__')]
            tournament = List(message="Por qual torneio você está procurando?", choices=options)
            if not tournament:
                return
        
        if tournament == '__exit__':
            try_again = Confirm(message='Quer tentar pesquisar usando outro termo?')

            if not try_again:
                break
        else:
            view_tournament(api, tournament)
            break

@Controller
def my_tournaments(api):
    clear_screen()
    section_title('Ver meus torneios')
    tournaments = api.user_tournaments(api.user['login'])
    tournament_choices = []
    for tournament in tournaments:
        owner_text = ' (Dono)' if tournament['owner'] == api.user['login'] else ''
        option = (f"{tournament['name']}{owner_text}", tournament['cod_tournament'])
        tournament_choices.append(option)
    if not tournaments:
        print_error('Você ainda não participa/criou um torneio\n')
    options = tournament_choices + [('Voltar', '__exit__')]
    choose = List(message='Você participa dos seguinte times', choices=options)
    if choose != '__exit__':
        tournament = [t for t in tournaments if t['cod_tournament'] == choose]
        if tournament:
            tournament = tournament[0]
            view_tournament(api, tournament['cod_tournament'])


def view_tournament(api, cod):
    def _header():
        print_tournament(api, cod)
    tournament = api.get_tournament(cod)
    menu = []
    if api.user['login'] == tournament['owner']:
        menu += [
            ('Atualizar informações do torneio', 'update_tournament'),
            ('Deletar o torneio', 'delete_tournament')
        ]
    else:
        menu += [
            ('Inscrever-se para o torneio', 'subscribe_tournament')
        ]
    menu += [
        ('Ver times do torneio', 'tournament_teams'),
    ]
    try:
        Menu(api, menu, before_show=_header, cod=cod)
    except BadRequest as exception:
        errors = exception.args[0]
        if errors[0]['code'] != 21:
            raise exception

@Controller
def subscribe_tournament(api, cod):
    teams = api.user_teams(api.user['login'])

    # Filterar somente os que o usuário é dono
    teams = [t for t in teams if t['owner'] == api.user['login']]
    if not teams:
        print_error('Você ainda não participa de nenhum time')
        Back()
        return

    team_choices = [(f"{t['initials']} - {t['name']}", t['initials']) for t in teams]
    options = team_choices + [('Voltar', '__exit__')]
    choose = List(message='Qual time você quer inscrever para o torneio', choices=options)
    if choose != '__exit__':
        team = [t for t in teams if t['initials'] == choose]
        if team:
            team = team[0]
            api.add_team_to_tournament(cod, team['initials'])
            print_success('Inscrito com sucesso')
            Back()


@Controller   
def update_tournament(api, cod):
    clear_screen()
    section_title('Atualizar Torneio')
    tournament = api.get_tournament(cod)
    print_tournament(api, cod)

    new_name = Text(message='Para qual nome você deseja alterar?', validate=validate_required, default=tournament['name'])

    new_description = Text(message='Qual a nova descrição que você deseja inserir?', validate=validate_required, default=tournament['description'])

    new_start_date = Text(message='Data de início (dd/mm/YYYY)', validate=validate_start_date, default=tournament['start_date'])

    new_end_date = Text(message='Data de encerramento (dd/mm/YYYY)', 
                    validate=validate_end_date(new_start_date), default=tournament['end_date'])


    json_dict = {'name': new_name, 'description': new_description, 'start_date': new_start_date, 'end_date': new_start_date}
    tournament = api.update_tournament(cod, json_dict)
    print_success('Informações do Torneio alteradas com sucesso')
    Back()

@Controller   
def delete_tournament(api, cod):
    confirm = Confirm(message='Você tem certeza que quer deletar o Torneio?')
    if confirm:
        api.delete_tournament(cod)
        print_success('Torneio removido com sucesso')
        Back()

@Controller   
def tournament_teams(api, cod):
    clear_screen()
    section_title('Times do Torneio ')
    teams = api.tournament_teams(cod)
    team_choices = [(f"{team['initials']} - {team['name']}", team['initials']) for team in teams]
    if not teams:
        print_error('Este torneio não possui times registrados ainda')

    options = team_choices + [('Voltar', '__exit__')]
    choose = List(message='Selecione um time para visualizar', choices=options)
    if choose != '__exit__':
        team = [t for t in teams if t['initials'] == choose]
        if team:
            team = team[0]
            view_team(api, team['initials'])




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
