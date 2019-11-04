from . import Controller, call_controller
from ..prompt import *
from ..api import BadRequest

@Controller
def main(api):
    menu = [
        ('Ver meu perfil', 'profile'),
        ('Procurar um usuário', 'find_user'),
        ('Criar um torneio', 'create_tournament'),
        ('Procurar por um torneio', 'find_tournament'),
        ('Criar um time', 'create_team'),
        ('Procurar por uma equipe', 'find_team'),
        ('Deslogar', 'logout')
    ]
    option = True
    while option not in (None, 'logout'):
        option = Menu(choices=menu)
        if option and option != 'logout':
            call_controller(option, api=api)
        print()