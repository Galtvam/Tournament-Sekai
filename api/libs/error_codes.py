class ErrorCodes:
    errors = {
        0: 'Ocorreu um erro desconhecido',
        1: 'Usuário não autenticado',
        3: 'A requisição precisa ser um JSON',
        4: 'Paramêtros inválidos: {}',
        5: 'Senha precisa ter no mínimo 8 caracateres',
        6: 'Senha pode ter no máximo 16 caracateres',
        7: 'Nome só pode conter letras',
        8: 'Parâmetro {} não está presente',
        9: 'O Login já foi utilizado',
        10: 'O Email já foi utilizado',
        11: 'Usuário ou senha incorreta',
        12: 'Token de Autenticação inválido',
        13: 'Usuário não possui permissão para alterar informações',
        14: 'Usuário não encontrado'
    }

    @staticmethod
    def get_error_message(error_code, args):
        try:
            return ErrorCodes.errors.get(error_code, ErrorCodes.errors[0]).format(', '.join(args))
        except TypeError:
            return ErrorCodes.errors.get(error_code, ErrorCodes.errors[0])
    
    @staticmethod
    def get_error(error_code, *args):
        return {'code': error_code, 'message': ErrorCodes.get_error_message(error_code, args)}