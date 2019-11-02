from flask import jsonify, request

from controllers import Controller
from models import UsersModel

class UsersController(Controller):

	@Controller.route('/users')
	def index():
		all_users = UsersModel.get_all()
		result = []
		for user in all_users:
			result.append(user.to_dict())
		return Controller.format_response(result, status_code=200)

	@Controller.route('/users/<id>')
	@Controller.authenticate_user
	def get(id):
		user = UsersModel.find_by_id(id)[0]
		return Controller.format_response(user.to_dict(), status_code=200)
	
	@Controller.route('/users', methods=['POST'])
	def create():
		data = request.get_json()
		user = UsersModel(data['name'], data['age'])
		user.insert()
		return Controller.format_response(status_code=201)