from libs.prompt import *
from libs.controllers import *

from libs.api import Api
from libs.prompt import *

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

api = Api()

menu = [
    ('Fazer login', 'login'), 
    ('Criar uma conta', 'signup'), 
    ('Sair', 'exit')
]

Menu(api, menu, 'exit')
