from . import Controller
from ..prompt import *
from ..validations import *

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
    user = api.user
    print_profile(user)
    
    address_data = {
        'street': Text(message='Qual o nome da rua onde você mora?', 
                       default=user['street']),
        'number': Text(message='Qual o número da sua residência?', 
                       default=user['number']),
        'complement': Text(message='Qual o complemento do seu endereço?', 
                           default=user['complement']),
        'neighborhood': Text(message='Em que bairro você mora?', 
                             default=user['neighborhood']),
        'city': Text(message='Em que cidade você mora?', 
                    default=user['city']),
        'state': Text(message='Em que estado você mora?', 
                      default=user['state']),
        'country': Text(message='Em que país você mora?', 
                        default=user['country'])
    }
    api.update_user(user['login'], address_data)

    # Mostrar perfil com as informações atualizadas
    clear_screen()
    section_title('Perfil')
    print_profile(api.user)

    print_success('Informações atualizadas com sucesso')
    Back()

def print_profile(user):
    birthday = datetime.strptime(user['birthday'], '%d/%m/%Y').strftime('%d/%B/%Y')
    birthday = birthday.title().replace('/', ' de ')
    profile = (f"\n{bright('Nome:')} {user['name'].title()}\n"
              f"{bright('Nome de usuário:')} {user['login']}\n"
              f"{bright('E-mail:')} {user['email']}\n"
              f"{bright('Data de Nascimento:')} {birthday}")
    
    street = user['street'] if user['street'] else 'Não definido'
    number = user['number'] if user['number'] else ''
    complement = user['complement'] if user['complement'] else ''
    neighborhood = f", {user['neighborhood']}" if user['neighborhood'] else ''
    address = f"{bright('Endereço:')} {street} {number} {complement}{neighborhood}" 
    
    city = user['city'] if user['city'] else 'Não definido'
    state = user['state'] if user['state'] else 'Não definido'
    country = user['country'] if user['country'] else 'Não definido'
    locality = (f"{bright('Cidade:')} {city}\t"
                f"{bright('Estado:')} {state}\t"
                f"{bright('País:')} {country}")
    sections = [s for s in (profile, address, locality) if s]
    print('\n'.join(sections), '\n')
