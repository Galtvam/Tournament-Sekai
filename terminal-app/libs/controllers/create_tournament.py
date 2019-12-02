from . import Controller, call_controller
from .find_tournament import view_tournament, print_tournament
from ..prompt import *
from ..api import ApiError
from ..validations import validate_required, validate_start_date, validate_end_date


from datetime import datetime


@Controller
def create_tournament(api):
    clear_screen()
    section_title('Criar um Torneio')
    
    tournament_data = {
        'name': Text(message='Qual será o nome do seu torneio?', validate=validate_required),
        'start_date': Text(message='Data de início (dd/mm/YYYY)', validate=validate_start_date),
        'description': Text(message='Dê uma descrição para o torneio'),
    }
    tournament_data['end_date'] = Text(message='Data de encerramento (dd/mm/YYYY)', 
                                       validate=validate_end_date(tournament_data['start_date']))

    if all(value is not None for value in tournament_data.values()):
        tournament_data['start_date'] = datetime.strptime(tournament_data['start_date'], '%d/%m/%Y')
        tournament_data['start_date'] = tournament_data['start_date'].strftime('%m/%d/%Y')

        tournament_data['end_date'] = datetime.strptime(tournament_data['end_date'], '%d/%m/%Y')
        tournament_data['end_date'] = tournament_data['end_date'].strftime('%m/%d/%Y')
    
        tournament = api.create_tournament(tournament_data)
        print_tournament(api, cod)
        print_success('Torneio criado com sucesso')
        Back()

