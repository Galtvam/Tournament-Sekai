from . import Controller
from ..prompt import *
from ..api import BadRequest

@Controller
def main(api):
    print(api.user)