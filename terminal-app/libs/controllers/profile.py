from . import Controller
from ..prompt import *

from datetime import datetime

@Controller
def profile(api):
    clear_screen()
    section_title('Perfil')
    print_profile(api.user)
    menu = [
        ('Atualizar minhas informações', 'update_profile')
    ]
    Menu(api, menu, clear=False)

@Controller
def update_profile(api):
    clear_screen()
    section_title('Perfil')
    print_profile(api.user)
    input()

def print_profile(user):
    birthday = datetime.strptime(user['birthday'], '%d/%m/%Y').strftime('%d/%B/%Y')
    birthday = birthday.title().replace('/', ' de ')
    profile = (f"{bright('Nome:')} {user['name'].title()}\n"
              f"{bright('Nome de usuário:')} {user['login']}\n"
              f"{bright('E-mail:')} {user['email']}\n"
              f"{bright('Data de Nascimento:')} {birthday}")
    address = ''
    if user['street']:
        address = f"{bright('Endereço:')} {user['street']} {user['number']} {user['complement']}, {user['neighborhood']}" 
    locality = []
    if user['city']:
        locality.append(f"{bright('Cidade:')} {user['city']}")
    if user['state']:
        locality.append(f"{bright('Estado:')} {user['state']}")
    if user['country']:
        locality.append(f"{bright('País:')} {user['country']}")
    
    locality = '\t'.join(locality)
    sections = [s for s in (profile, address, locality) if s]
    print('\n'.join(sections))
