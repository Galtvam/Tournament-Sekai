from . import Controller
from .profile import print_profile
from ..prompt import *
from ..api import BadRequest

from datetime import datetime


@Controller
def find_user(api):
    clear_screen()
    section_title('Procurar usuário')
    login = Text(message='Nome de usuário')
    try:
        user = api.get_user(login)
        print_profile(user)
    except BadRequest as exception:
        errors = exception.args[0]
        print_errors(errors)
