class NotFoundEnvironmentError(NotImplementedError):
    pass

class Environment:
    environment_class = None

    @staticmethod
    def set_environment(environment):
        subclasses = Environment.__subclasses__()
        envs = [cls for cls in subclasses if cls.name == environment]
        if not envs:
            raise NotFoundEnvironmentError
        Environment.environment_class = envs

    @staticmethod
    def setup(connector):
        if not Environment.environment_class:
            raise NotFoundEnvironmentError
        for environment in Environment.environment_class:
            print(f'Running {environment.name} setup...')
            environment.setup(connector)
