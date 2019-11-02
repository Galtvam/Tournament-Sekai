from flask import jsonify, request
from flask_jwt_extended import jwt_required
from libs import ErrorCodes

class Controller:
	routes = []
	content_type = 'application/json; charset=utf-8'
	jwt = None

	@staticmethod
	def route(rule, **options):
		def decorator(f, *args, **kwargs):
			parameters = (args, kwargs)
			route_parameters = rule, options, f, parameters
			Controller.routes.append(route_parameters)
			resource_name = rule.strip('/').split('/')[0]
			f.__name__ = f'{resource_name}_{f.__name__}'
		return decorator

	@staticmethod
	def apply_routes(app):
		for route in Controller.routes:
			rule, options, f, parameters = route
			args, kwargs = parameters
			app.route(rule, **options)(f, *args, **kwargs)
	
	@staticmethod
	def set_jwt_rules(jwt):
		Controller.jwt = jwt
		jwt.unauthorized_loader(Controller.unauthorized_response)

	@staticmethod
	def authenticate_user(f):
		return jwt_required(f)

	@staticmethod
	def unauthorized_response(callback):
		return Controller.format_response(errors=1, status_code=401)
	
	@staticmethod
	def format_response(data=None, errors=None, status_code=200):
		response_errors = []
		if isinstance(errors, list):
			response_errors = [ErrorCodes.get_error(err) for err in errors]
		elif isinstance(errors, int):
			response_errors = [ErrorCodes.get_error(errors)]
		response = dict(data=data, errors=response_errors)
		return jsonify(response), status_code

