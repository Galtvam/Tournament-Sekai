class ErrorCodes:
    errors = {
        0: 'Ocorreu um erro desconhecido',
        1: 'Usuário não autenticado'
    }

    @staticmethod
    def get_error_message(error_code):
        return ErrorCodes.errors.get(error_code, ErrorCodes.errors[0])
    
    @staticmethod
    def get_error(error_code):
        return {'code': error_code, 'message': ErrorCodes.get_error_message(error_code)}