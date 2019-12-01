import jwt
import requests


class ApiError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BadRequest(ApiError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ConnectionError(ApiError):
    def __init__(self):
        errors = [{'code': -1, 'message': 'Não foi possível conectar-se à API'}]
        super().__init__(errors)

class Api:
    HOST = 'http://localhost:8080'

    def __init__(self):
        self.host = Api.HOST
        self.auth_token = None

        self._user = None
    
    @property
    def user(self):
        if not self._user:
            login = jwt.decode(self.auth_token, verify=False)['identity']
            self._user = self.authenticated_request('GET', f'{self.host}/users/{login}')
        return self._user

    def login(self, username, password):
        credentials = {
            'login': username,
            'password': password
        }
        try:
            response = requests.post(f'{self.host}/sign-in', json=credentials).json()
            data = response['data']
            errors = response['errors']
            if errors:
                raise BadRequest(errors)
            self.auth_token = data['token']
        except requests.exceptions.ConnectionError:
            raise ConnectionError
    
    def register(self, name, email, username, birthday, password):
        data = {
            'name': name,
            'login': username,
            'email': email,
            'birthday': birthday,
            'password': password
        }
        try:
            response = requests.post(f'{self.host}/sign-up', json=data).json()
            errors = response['errors']
            if errors:
                raise BadRequest(errors)
        except requests.exceptions.ConnectionError:
            raise ConnectionError
    
    def get_user(self, login):
        data = {'login': login}
        return self.authenticated_request('GET', f'{self.host}/users/{login}', json=data)
    
    def update_user(self, login, payload):
        response = self.authenticated_request('PUT', f'{self.host}/users/{login}', json=payload)
        # Forçar atualização das informações de cache do usuário logado
        if self._user and self._user['login'] == login:
            self._user = None
        return response

    def authenticated_request(self, method, url, *args, **kwargs):
        headers = kwargs.get('headers', {})
        headers.update({'Authorization': f'Bearer {self.auth_token}'})
        kwargs.update({'headers': headers})
        try:
            response = requests.request(method, url, *args, **kwargs).json()
            errors = response['errors']
            if errors:
                raise BadRequest(errors)
            return response['data']
        except requests.exceptions.ConnectionError:
            raise ConnectionError