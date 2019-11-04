from . import Controller
from ..prompt import *

from datetime import datetime

@Controller
def profile(api):
    section_title('Perfil')
    birthday = datetime.strptime(api.user['birthday'], '%d/%m/%Y').strftime('%d %B %Y')
    profile = (f"{bright('Nome:')} {api.user['name']}\n"
              f"{bright('Nome de usuário:')} {api.user['login']}\n"
              f"{bright('E-mail:')} {api.user['email']}\n"
              f"{bright('Data de Nascimento:')} {birthday}\n")
    print(profile)