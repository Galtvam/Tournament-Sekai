from .environment import Environment

class ProductionEnvironment(Environment):
    name = 'production'

    @staticmethod
    def setup(application, connector):
        pass