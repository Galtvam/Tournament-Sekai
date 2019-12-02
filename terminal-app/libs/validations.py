import re
from inquirer.errors import ValidationError
from datetime import datetime


def validate_password(answers, current):
    if len(current) < 8:
        raise ValidationError('', reason='Senha precisa ter no mínimo 8 caracateres')
    if len(current) > 16:
        raise ValidationError('', reason='Senha pode ter no máximo 16 caracateres')
    return True

def validate_required(answers, current):
    if len(current) == 0:
        raise ValidationError('', reason=f'O campo é obrigatório')
    return True

def validate_email(answers, current):
    if not re.match(r'^(\w+[.|\w])*@(\w+[.])*\w+$', current, re.IGNORECASE):
        raise ValidationError('', reason='E-mail inválido')
    return True

def validate_name(answers, current):
    if not re.match(r'^([^\W\d_]+[ ]*)+$', current, re.UNICODE):
        raise ValidationError('', reason='Nome só pode conter letras')
    return True

def validate_date(answers, current):
    try:
        datetime.strptime(current, '%d/%m/%Y')
    except:
        raise ValidationError('', reason='Data inválida, o formato deve ser "dd/mm/YYYY"')
    return True

def validate_start_date(answers, current):
    validate_date(answers, current)
    start_date = datetime.strptime(current, '%d/%m/%Y')
    if start_date < datetime.now():
        raise ValidationError('', reason='A data não pode ser no passado')
    return True

def validate_end_date(start_date):
    if not start_date:
        start_date = datetime.strptime(start_date, '%d/%m/%Y')
    else:
        return lambda answers, current: True 
    def validation(answers, current):
        validate_date(answers, current)
        end_date = datetime.strptime(current, '%d/%m/%Y')
        if end_date < start_date:
            raise ValidationError('', reason='O encerramento deve ser depois da data de início')
        return True
    return validation

def validate_is_digit(answers, current):
    if not current.isdigit():
        raise ValidationError('', reason='O campo não é um número')
    return True