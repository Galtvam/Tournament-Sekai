from . import Controller, call_controller
from .find_team import view_team, print_team
from ..prompt import *
from ..api import ApiError
from ..validations import validate_required


from datetime import datetime


@Controller
def create_team(api):
    clear_screen()
    section_title('Criar um time')
    
    team_data = {
        'initials': Text(message='Qual será as inicias do seu time?', validate=validate_required),
        'name': Text(message='Que nome você quer dar para o time?', validate=validate_required)
    }

    if all(value is not None for value in team_data.values()):
        team = api.create_team(**team_data)
        print_team(api, team['initials'])
        print_success('Time criado com sucesso')
        Back()

