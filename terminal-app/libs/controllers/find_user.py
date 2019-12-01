from . import Controller
from .profile import print_profile
from ..prompt import *
from ..api import ApiError

from datetime import datetime


@Controller
def find_user(api):
    clear_screen()
    section_title('Procurar usuário')
    login = Text(message='Nome de usuário')
    user = api.get_user(login)
    print_profile(user)

