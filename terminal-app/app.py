from libs.prompt import *
from libs.controllers import *

from libs.api import Api

api = Api()

menu = [
    ('Fazer login', 'login'), 
    ('Criar uma conta', 'signup'), 
    ('Sair', 'exit')
]

option = True
while option not in (None, 'exit'):
    option = Menu(choices=menu)
    if option and option != 'exit':
        call_controller(option, api=api)
    print()
