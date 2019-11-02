from .environment import Environment

class DevelopmentEnvironment(Environment):
    name = 'development'

    @staticmethod
    def setup(connector):
        pass