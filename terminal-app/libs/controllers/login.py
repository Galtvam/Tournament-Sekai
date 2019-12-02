from . import Controller, call_controller
from ..prompt import *
from ..api import ApiError

@Controller
def login(api):
    while True:
        #TODO: Remover usuário padrão conlcuir o desenvovlimento
        username = Text(message='Digite seu login')
        password = Password(message='Digite sua senha')

        try:
            api.login(username, password)
        except ApiError as exception:
            errors = exception.args[0]
            beatifier_param_names(errors)
            print_errors(errors)
        
            try_again = Confirm(message='Deseja tentar novamente?')

            if not try_again:
                break
        else:
            call_controller('main', api)
            break

def beatifier_param_names(errors):
    dict_ = {
        'login': 'Login',
        'password': 'Senha'
    }
    for error in errors:
        for key, value in dict_.items():
            error['message'] = error['message'].replace(key, value)