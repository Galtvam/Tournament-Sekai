registred_controllers = {}
controllers_api = None

def Controller(f):
    registred_controllers[f.__name__] = f
    def wrapper(*args, **kwargs):
        kwrags.update({api: controllers_api})
        return f(*args, **kwargs)
    return Controller

def call_controller(controller, *args, **kwargs):
    registred_controllers[controller](*args, **kwargs)
