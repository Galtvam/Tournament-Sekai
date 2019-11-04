import jwt
import requests

class BadRequest(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
            self._user = self.authenticated_request('GET', f'{self.host}/users/{login}').json()['data']
        return self._user

    def login(self, username, password):
        credentials = {
            'login': username,
            'password': password
        }
        response = requests.post(f'{self.host}/sign-in', json=credentials).json()
        data = response['data']
        errors = response['errors']
        if errors:
            raise BadRequest(errors)
        self.auth_token = data['token']
    
    def register(self, name, email, username, birthday, password):
        data = {
            'name': name,
            'login': username,
            'email': email,
            'birthday': birthday,
            'password': password
        }
        response = requests.post(f'{self.host}/sign-up', json=data).json()
        errors = response['errors']
        if errors:
            raise BadRequest(errors)
    
    def authenticated_request(self, method, url, *args, **kwargs):
        headers = kwargs.get('headers', {})
        headers.update({'Authorization': f'Bearer {self.auth_token}'})
        kwargs.update({'headers': headers})
        return requests.request(method, url, *args, **kwargs)
