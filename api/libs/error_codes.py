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
        13: 'Usuário não possui permissão',
        14: 'Usuário não encontrado',
        15: 'Time não encontrado',
        16: 'Nenhum time encontrado com as palavras chave',
        17: 'Esse usuário já está no time ou não existe',
        18: 'Time ou Torneio não encontrado',
        19: 'Time já registrado',
        20: 'Esse time não está registrado no Torneio'
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