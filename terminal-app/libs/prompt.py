import inquirer

from colorama import init, Fore, Style


init()

def prompt(question):
    return inquirer.prompt([question])

def Text(*args, **kwargs):
    question = prompt(inquirer.Text('question', *args, **kwargs))
    return question.get('question') if question else None

def List(*args, **kwargs):
    question = prompt(inquirer.List('question', *args, **kwargs))
    return question.get('question') if question else None

def Checkbox(*args, **kwargs):
    question = prompt(inquirer.Checkbox('question', *args, **kwargs))
    return question.get('question') if question else None

def Password(*args, **kwargs):
    question = prompt(inquirer.Password('question', *args, **kwargs))
    return question.get('question') if question else None

def Confirm(*args, **kwargs):
    question = prompt(inquirer.Confirm('question', *args, **kwargs))
    return question.get('question') if question else None

def Editor(*args, **kwargs):
    question = prompt(inquirer.Editor('question', *args, **kwargs))
    return question.get('question') if question else None

def Path(*args, **kwargs):
    question = prompt(inquirer.Path('question', *args, **kwargs))
    return question.get('question') if question else None

def Menu(api, menu_options, exit_option=None, clear=True, 
         before_show=None, *args, **kwargs):
    from .controllers import call_controller
    if not exit_option:
        menu_options.append(('Voltar', 'back'))
        exit_option = 'back'
    if clear:
        clear_screen()
    option = True 
    while option not in (None, exit_option):
        print()
        if callable(before_show):
            before_show()
        option = List(message='O que você deseja fazer', 
                      choices=menu_options, *args, **kwargs)
        if option and option != exit_option:
            call_controller(option, api=api)

def Back(**kwargs):
    Menu(None, [], clear=False, **kwargs)

def print_errors(errors):
    print()
    for error in errors:
        message = f"Erro {error['code']}: {error['message']}"
        print(Fore.RED + message)
    print(Style.RESET_ALL)

def print_error(error):
    print()
    print(Fore.RED + error)
    print(Style.RESET_ALL)

def print_success(message):
    print()
    print(Fore.GREEN + message)
    print(Style.RESET_ALL)

def bright(message):
    return Style.BRIGHT + message + Style.RESET_ALL

def section_title(title):
    section_width = 45
    print('\n' + '#'*section_width)
    print(bright(title.center(section_width)))
    print('#'*section_width + '\n')

def clear_screen():
    print("\033c", end="")
