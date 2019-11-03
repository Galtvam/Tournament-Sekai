from flask import jsonify, request

from controllers import Controller
from models import UsersModel

from flask_jwt_extended import create_access_token
from psycopg2.errors import UniqueViolation

class AuthController(Controller):
    login_param = 'login', UsersModel.Validation.login
    password_param = 'password', UsersModel.Validation.password
    name_param = 'name', UsersModel.Validation.name
    birthday_param = 'birthday', UsersModel.Validation.birthday

    @Controller.route('/sign-in', methods=['POST'])
    @Controller.json_request
    @Controller.validate_params(login_param, password_param)
    def sign_in():
        data = request.get_json()
        user = UsersModel.find_by_login(data['login'])
        if user and Controller.bycrpt.check_password_hash(user[0].password, data['password']):
            access_token = create_access_token(identity=user[0].login)
            return Controller.format_response({'token': access_token}, status_code=200)

        return Controller.format_response(errors=11, status_code=401)
    
    @Controller.route('/sign-up', methods=['POST'])
    @Controller.json_request
    @Controller.validate_params(login_param, name_param, birthday_param, password_param)
    def sign_up():
        data = request.get_json()
        password = Controller.bycrpt.generate_password_hash(data['password']).decode('utf-8')
        
        if UsersModel.find_by_login(data['login']):
            return Controller.format_response(errors=9, status_code=400)
        
        if UsersModel.find_by_email(data['email']):
            return Controller.format_response(errors=10, status_code=400)
        
        user = UsersModel(
            data['login'], data['name'], data['email'], data['birthday'], password
        )
        user.insert()
        
        return Controller.format_response(status_code=201)

