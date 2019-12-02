from . import Controller
from ..prompt import *
from ..api import BadRequest

@Controller
def main(api):
    def _header():
        clear_screen()
        section_title('Menu Principal')
    
    menu = [
        ('Ver meu perfil', 'profile'),
        ('Procurar um usuário', 'find_user'),
        ('Criar um time', 'create_team'),
        ('Ver meus times', 'my_teams'),
        ('Procurar por um time', 'find_team'),
        ('Criar um torneio', 'create_tournament'),
        ('Procurar por um torneio', 'find_tournament'),
        ('Ranking', 'ranking'),
        ('Deslogar', 'logout')
    ]
    Menu(api, menu, 'logout', before_show=_header)
