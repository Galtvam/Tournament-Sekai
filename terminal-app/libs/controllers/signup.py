from . import Controller, call_controller
from ..prompt import *
from ..api import BadRequest

import re

from inquirer.errors import ValidationError

from datetime import datetime

@Controller
def signup(api):
    while True:
        register_data = {
            'name': Text(message='Qual seu nome', validate=validate_name),
            'birthday': Text(message='Quando você nasceu (dd/mm/YYYY)', validate=validate_birthday),
            'username': Text(message='Digite um nome de usuário', validate=True),
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
            except BadRequest as exception:
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

def validate_password(answers, current):
    if len(current) < 8:
        raise ValidationError('', reason='Senha precisa ter no mínimo 8 caracateres')
    if len(current) > 16:
        raise ValidationError('', reason='Senha pode ter no máximo 16 caracateres')
    return True

def validate_email(answers, current):
    if not re.match(r'^(\w+[.|\w])*@(\w+[.])*\w+$', current, re.IGNORECASE):
        raise ValidationError('', reason='E-mail inválido')
    return True

def validate_name(answers, current):
    if not re.match(r'^([^\W\d_]+[ ]*)+$', current, re.UNICODE):
        raise ValidationError('', reason='Nome só pode conter letras')
    return True

def validate_birthday(answers, current):
    try:
        datetime.strptime(current, '%d/%m/%Y')
    except:
        raise ValidationError('', reason='Data inválida, o formato deve ser "dd/mm/YYYY"')
    return True
