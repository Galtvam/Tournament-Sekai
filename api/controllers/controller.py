from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

import json

from enum import Enum
from functools import wraps

from models import UsersModel
from libs import ErrorCodes


class Controller:
	routes = []
	content_type = 'application/json; charset=utf-8'
	application = None
	bycrpt = None
	jwt = None

	@staticmethod
	def route(rule, **options):
		def decorator(f):
			route_parameters = rule, options, f
			Controller.routes.append(route_parameters)
			resource_name = rule.strip('/').split('/')[0]
			f.__name__ = f'{resource_name}_{f.__name__}'
		return decorator

	@staticmethod
	def set_application(app):
		Controller.application = app
	
	@staticmethod
	def set_bcrypt(bycrpt):
		Controller.bycrpt = bycrpt
	
	@staticmethod
	def apply_routes(app):
		for route in Controller.routes:
			rule, options, f = route
			app.route(rule, **options)(Controller.wrapper_request(f))
	
	@staticmethod
	def wrapper_request(original_callback):
		def wrapper(*args, **kwargs):
			return original_callback(*args, **kwargs)
		wrapper.__name__ = original_callback.__name__
		return wrapper

	@staticmethod
	def json_request(f):
		def wrapper(*args, **kwargs):
			try:
				conditions = [
					'Content-Type' in request.headers,
					request.headers['Content-Type'] == 'application/json',
					json.loads(request.data) is not None
				]
				if not all(conditions):
					raise Exception(conditions)
			except:
				return Controller.format_response(errors=3, status_code=400)
			return f(*args, **kwargs)
		return wrapper
	
	@staticmethod
	def set_jwt_rules(jwt):
		Controller.jwt = jwt
		jwt.unauthorized_loader(Controller.unauthorized_response)
		jwt.invalid_token_loader(
			lambda callback: Controller.format_response(errors=12, status_code=401)
		)
	
	@staticmethod
	def authenticate_user(f):
		return jwt_required(f)
	
	@staticmethod
	def authenticated_user():
		return UsersModel.find_by_login(get_jwt_identity())[0]

	@staticmethod
	def unauthorized_response(callback):
		return Controller.format_response(errors=1, status_code=401)
	
	@staticmethod
	def format_response(data=None, errors=None, status_code=200):
		response_errors = []
		if isinstance(errors, list):
			response_errors = []
			for err in errors:
				if isinstance(err, tuple):
					response_errors.append(ErrorCodes.get_error(*err))
				else:
					response_errors.append(ErrorCodes.get_error(err))
		elif isinstance(errors, tuple):
			response_errors = [ErrorCodes.get_error(*errors)]
		elif isinstance(errors, int):
			response_errors = [ErrorCodes.get_error(errors)]
		response = dict(data=data, errors=response_errors)
		return jsonify(response), status_code
	
	@staticmethod
	def validate_params(*params):
		def decorator(f):
			def wrapper(*args, **kwargs):
				params_values = dict()
				params_values.update(request.args)
				if request.is_json:
					params_values.update(request.json)
				errors = []
				for param, validations in params:
					for validation, error_code in validations:
						if param not in params_values:
							return Controller.format_response(errors=(8, param), status_code=400)
						try:
							is_valid = bool(validation(params_values[param]))
						except:
							is_valid = False
						if not is_valid:
							errors.append((error_code, param))
				if errors:
					return Controller.format_response(errors=errors, status_code=400)
				return f(*args, **kwargs)
			return wrapper
		return decorator
