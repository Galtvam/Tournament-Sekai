import inquirer

from colorama import init, Fore, Style

CHAR_PIXEL = "█"

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
                      choices=menu_options)
        if option and option != exit_option:
            call_controller(option, api=api, *args, **kwargs)

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

def red_text(text):
    return Fore.RED + text + Style.RESET_ALL

def green_text(text):
    return Fore.GREEN + text + Style.RESET_ALL

def section_title(title):
    section_width = 45
    print('\n' + '#'*section_width)
    print(bright(title.center(section_width)))
    print('#'*section_width + '\n')

def escape_color(rgb):
    colors = [str(i) for i in rgb]
    return "\033[38;2;" + ";".join(colors) + "m"

def reset_color():
    print("\033[0m", end="")
    return "\033[0m"

def string_color(rgb, string):
    return escape_color(rgb) + string + reset_color()

def move_cursor(x, y):
    print("\033[%d;%dH" % (y, x), end="")

def set_pixel(x, y, rgb):
	string_pixel = string_color(rgb, CHAR_PIXEL)
	move_cursor(x, y)
	print(string_pixel)

def clear_pixel(x, y):
    set_pixel(x, y, CONSOLE_BACKGROUND)

def clear_screen():
    print("\033c", end="")
