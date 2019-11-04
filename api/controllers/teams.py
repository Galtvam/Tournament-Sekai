from flask import jsonify, request

from controllers import Controller
from models import TeamsModel

class TeamsController(Controller):

    @Controller.route('/teams')
    def index():
        all_teams = TeamsModel.get_all()
        result = []
        for team in all_teams:
            result.append(team.to_dict())
        return Controller.format_response(result, status_code=200)

    @Controller.route('/teams/<initials>')
    def get(initials):
        team = TeamsModel.find_by_initials(initials) 
        if team: #Verifica se possui conteúdo
            team = team[0]
            return Controller.format_response(team.to_dict(), status_code=200)

        else:
            return Controller.format_response(status_code=404)
            
    @Controller.route('/teams', methods=['POST'])
    def create():
        data = request.get_json()
        team = TeamsModel(data['initials'], data['name'])
        team.insert()
        return Controller.format_response(status_code=201)

    @Controller.route('/teams/<initials>', methods=['PUT'])
    def update(initials):
        team = TeamsModel.find_by_initials(initials)
        if team: #Verifica se possui conteúdo
            team = team[0]
            data = request.get_json()
            if 'name' in data:
                team.name = data['name']
                team.update()
                return Controller.format_response(status_code=200)

            if 'initials' in data:
                team.initials = data['initials']
                team.update()
                return Controller.format_response(status_code=200)
        else:
            return Controller.format_response(status_code=404)

    
    @Controller.route('/teams/<initials>', methods=['DELETE'])
    def delete(initials):
        team = TeamsModel.find_by_initials(initials)
        if team:
            team = team[0]
            team.delete()
            return Controller.format_response(status_code=200)
        else:
            return Controller.format_response(status_code=404)