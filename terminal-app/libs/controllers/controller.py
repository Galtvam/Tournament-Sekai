from ..prompt import clear_screen, print_error, print_errors

registred_controllers = {}
controllers_api = None

def Controller(f):
    registred_controllers[f.__name__] = f
    def controller_wrapper(*args, **kwargs):
        kwrags.update({api: controllers_api})
        return f(*args, **kwargs)
    return controller_wrapper

def call_controller(controller, *args, **kwargs):
    from ..api import ApiError
    if controller not in registred_controllers:
        clear_screen()
        print_error('Seção em Manutenção')
    else:
        try:
            registred_controllers[controller](*args, **kwargs)
        except ApiError as exception:
            errors = exception.args[0]
            print_errors(errors)
