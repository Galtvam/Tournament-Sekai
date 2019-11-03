from flask import jsonify, request

from controllers import Controller
from models import UsersModel

class UsersController(Controller):
	@Controller.route('/users/<login>')
	@Controller.authenticate_user
	def get(login):
		user = UsersModel.find_by_login(login)
		if user:
			return Controller.format_response(user[0].to_dict(), status_code=200)
		return Controller.format_response(status_code=404)
