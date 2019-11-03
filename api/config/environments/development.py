from flask_cors import CORS

from .environment import Environment

class DevelopmentEnvironment(Environment):
    name = 'development'

    @staticmethod
    def setup(application, connector):
        CORS(application)
