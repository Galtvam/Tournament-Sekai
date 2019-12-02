from flask import jsonify, request

from controllers import Controller
from models import UsersModel, TeamsModel, TournamentsModel

class UsersController(Controller):
	@Controller.route('/users/<login>')
	@Controller.authenticate_user
	def get(login):
		user = UsersModel.find_by_login(login)
		if user:
			return Controller.format_response(user[0].to_dict(), status_code=200)
		return Controller.format_response(errors=14, status_code=404)


	@Controller.route('/users/<login>', methods=['PUT'])
	@Controller.authenticate_user
	@Controller.json_request
	def put(login):
		data = request.get_json()

		logged_user = Controller.authenticated_user()
		if logged_user.login == login:
			for field in (
				'name', 'email', 'birthday', 'password',
		        'country', 'state', 'city',
		        'neighborhood', 'street',
		        'number', 'complement', 'phone'
			):
				if field in data:
					setattr(logged_user, field, data[field])
			logged_user.update()
			return Controller.format_response(status_code=200)
		return Controller.format_response(errors=10, status_code=400)
	
	
	@Controller.route('/users/<login>/teams')
	@Controller.authenticate_user
	def user_teams(login):
		teams = TeamsModel.user_teams(login)
		result = []
		for team in teams:
			result.append(team.to_dict())
		return Controller.format_response(result, status_code=404)

	@Controller.route('/users/<login>/tournaments')
	@Controller.authenticate_user
	def user_tournaments(login):
		tournaments = TournamentsModel.user_tournaments(login)
		result = []
		for tournament in tournaments:
			result.append(tournament.to_dict())
		return Controller.format_response(result, status_code=404)

