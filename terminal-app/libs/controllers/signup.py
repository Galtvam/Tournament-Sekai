from . import Controller
from ..prompt import *
from ..api import ApiError
from ..validations import *

from datetime import datetime

@Controller
def signup(api):
    while True:
        register_data = {
            'name': Text(message='Qual seu nome', validate=validate_required),
            'birthday': Text(message='Quando você nasceu (dd/mm/YYYY)', validate=validate_birthday),
            'username': Text(message='Digite um nome de usuário', validate=validate_username),
            'email': Text(message='Digite um e-mail', validate=validate_email)
        }

        password = False
        confirm_password = None

        while password != confirm_password:
            password = Password(message='Digite sua senha', validate=validate_password)
            confirm_password = Password(message='Confirme sua senha', validate=validate_password)
            if password != confirm_password:
                print_error('As senhas não coincidem')
        
        register_data['password'] = password

        try:
            register_data['birthday'] = datetime.strptime(register_data['birthday'], '%d/%m/%Y')
            register_data['birthday'] = register_data['birthday'].strftime('%m/%d/%Y')
            
            try:
                api.register(**register_data)
            except ApiError as exception:
                errors = exception.args[0]
                beatifier_param_names(errors)
                print_errors(errors)
            
                try_again = Confirm(message='Deseja tentar novamente?')

                if not try_again:
                    break
            else:
                print_success('Conta criada com sucesso')
                break
        except:
            break

def beatifier_param_names(errors):
    dict_ = {
        'login': 'Login',
        'name': 'Nome',
        'password': 'Senha',
        'birthday': 'Data de Nascimento'
    }
    for error in errors:
        for key, value in dict_.items():
            error['message'] = error['message'].replace(key, value)
