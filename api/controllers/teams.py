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
    def create(): 
        data = request.get_json()
        current_user = Controller.authenticated_user()
        team = TeamsModel(data['initials'], data['name'], current_user.login)

        team.insert()
        return Controller.format_response(team.to_dict(), status_code=201)

    @Controller.route('/teams/<initials>', methods=['PUT'])
    @Controller.authenticate_user
    def update(initials): 
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
            return Controller.format_response(errors=15, status_code=404)

    
    @Controller.route('/teams/<initials>', methods=['DELETE'])
    @Controller.authenticate_user
    def delete(initials): 
        team = TeamsModel.find_by_initials(initials)
        team = team[0]
        current_user = Controller.authenticated_user()
        
        if not current_user.login == team.owner_login:
            return Controller.format_response(errors=13, status_code=403) 

        if team:
            team = team[0]
            team.delete()
            return Controller.format_response(status_code=200)
        else:
            return Controller.format_response(errors=15, status_code=404)


    @Controller.route('/teams/<initials>/members', methods=['POST'])
    @Controller.authenticate_user
    def add_member_to_team(initials):
        data = request.get_json()
        team = TeamsModel.find_by_initials(initials)
        team = team[0]
        current_user = Controller.authenticated_user()

        if not current_user.login == team.owner_login:
            return Controller.format_response(errors=13, status_code=403) 
        
        if team:
            try:
                team.add_member_to_team(data['login'])
                return Controller.format_response(status_code=201) 
            except:
                return Controller.format_response(errors=17 ,status_code=404)

        else:
            return Controller.format_response(errors=15, status_code=404)



    @Controller.route('/teams/<initials>/members', methods=['GET'])
    @Controller.authenticate_user
    def view_members(initials):
        team = TeamsModel.find_by_initials(initials)
        if team:
            team = team[0]
            members = team.view_members_in_team()
            return Controller.format_response(members, status_code=200)
        else:
            return Controller.format_response(errors=14, status_code=404)

