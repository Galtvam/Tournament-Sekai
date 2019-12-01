from flask import jsonify, request

from controllers import Controller
from models import TeamsModel

class TeamsController(Controller):

    # GET /teams?search=
    @Controller.route('/teams')
    def index():
        all_teams = TeamsModel.get_all()
        search_keyword = request.args.get('search')
        if search_keyword:
            k = search_keyword.lower()
            all_teams = [t for t in all_teams 
                         if k in t.to_dict()['initials'].lower() or k in t.to_dict()['name'].lower()]
        result = []
        for team in all_teams:
            result.append(team.to_dict())
        # Somente retornar erro se for uma pesquisa por palavra chave e não for encontrado nada
        if search_keyword and not result:
            return Controller.format_response(errors=16, status_code=404) 
        return Controller.format_response(result, status_code=200)

    @Controller.route('/teams/<initials>')
    def get(initials):
        team = TeamsModel.find_by_initials(initials) 
        if team: #Verifica se possui conteúdo
            team = team[0]
            return Controller.format_response(team.to_dict(), status_code=200)

        else:
            return Controller.format_response(errors=15, status_code=404)
            
    @Controller.route('/teams', methods=['POST'])
    @Controller.authenticate_user
    def create(): #TESTAR Adicionar owner_login
        data = request.get_json()
        current_user = Controller.authenticated_user()
        team = TeamsModel(data['initials'], data['name'], current_user.login)
        team.insert()
        return Controller.format_response(team.to_dict(), status_code=201)

    @Controller.route('/teams/<initials>', methods=['PUT'])
    @Controller.authenticate_user
    def update(initials): #TESTAR averiguar se o usuário autenticado é o dono do time
        team = TeamsModel.find_by_initials(initials)
        if team: #Verifica se possui conteúdo
            team = team[0]
            data = request.get_json()
            current_user = Controller.authenticated_user()
            
            if not current_user.login == team.owner_login:
                return Controller.format_response(errors=13, status_code=403) 

            for field in ('initials', 'name','owner_login'):
                if field in data:
                    setattr(team, field, data[field])
            team.update()
            return Controller.format_response(status_code=200)

        else:
            return Controller.format_response(status_code=404)

    
    @Controller.route('/teams/<initials>', methods=['DELETE'])
    @Controller.authenticate_user
    def delete(initials): #TESTAR averiguar se o usuário autenticado é o dono do time
        team = TeamsModel.find_by_initials(initials)
        current_user = Controller.authenticated_user()
        
        if not current_user.login == team.owner_login:
            return Controller.format_response(errors=13, status_code=403) 

        if team:
            team = team[0]
            team.delete()
            return Controller.format_response(status_code=200)
        else:
            return Controller.format_response(status_code=404)