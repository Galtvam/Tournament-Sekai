from flask import jsonify, request

from controllers import Controller
from models import TournamentsModel
from models import TeamsModel
from models import ModerationsModel

class TournamentsController(Controller):


    @Controller.route('/tournaments')
    def get_all():
        code = request.args.get('code')
        name = request.args.get('name')
        limit = request.args.get('limit','20')
        offset = request.args.get('offset','0')

        limit, offset = int(limit), int(offset)
        if name is not None:
            tournaments = TournamentsModel.search_by_name(name,limit,offset)

        elif code is not None:
            tournaments = TournamentsModel.find_by_cod_tournament(int(code))
            
        else:
            tournaments = TournamentsModel.get_all(limit,offset)
        result = []
        for tournament in tournaments:
            result.append(tournament.to_dict())
        return Controller.format_response(result, status_code=200)
    
    @Controller.route('/tournaments/<cod_tournament>')
    def get(cod_tournament):
        tournaments = TournamentsModel.find_by_cod_tournament(int(cod_tournament))
        if not tournaments:
            Controller.format_response(errors=21, status_code=200)
        return Controller.format_response(tournaments[0].to_dict(), status_code=200)

    @Controller.route('/tournaments', methods=['POST'])
    @Controller.authenticate_user
    def create():
        current_user = Controller.authenticated_user()
        data = request.get_json()
        tournament = TournamentsModel(data['name'], data['description'],
        data['start_date'], data['end_date'], current_user.login)

        tournament.insert()
        return Controller.format_response(tournament, status_code=201)

    @Controller.route('/tournaments/<code>', methods=['PUT'])
    @Controller.authenticate_user
    def update_by_code(code):
        data = request.get_json()
        tournament = TournamentsModel.find_by_cod_tournament(int(code))
        if tournament:
            tournament = tournament[0]

            current_user = Controller.authenticated_user()
            if not current_user.login == tournament.owner_login:
                return Controller.format_response(errors=13, status_code=403) 
            
            for field in ('name', 'description','start_date','end_date'):
                if field in data:
                    setattr(tournament, field, data[field])

            tournament.update_by_code()
            return Controller.format_response(tournament, status_code=200)
        
        else:
            return Controller.format_response(status_code=404)

    @Controller.route('/tournaments/<code>', methods=['DELETE'])
    @Controller.authenticate_user
    def delete_by_code(code):
        tournament = TournamentsModel.find_by_cod_tournament(int(code))
        if tournament:
            tournament = tournament[0]
            current_user = Controller.authenticated_user()

            if not current_user.login == tournament.owner_login:
                return Controller.format_response(errors=13, status_code=403)    

            tournament.delete_by_code()
            return Controller.format_response(status_code=200)
        else:
            return Controller.format_response(status_code=404)    

    @Controller.route('/tournaments/<cod_tournament>/<initials>/members', methods=['GET'])
    @Controller.authenticate_user 
    def view_members(cod_tournament, initials):
        tournament = TournamentsModel.find_by_cod_tournament(cod_tournament)
        team = TeamsModel.find_by_initials(initials)

        if tournament and team:
            tournament = tournament[0]
            members = tournament.view_members_in_tournament(initials)
            return Controller.format_response(members, status_code=200)

        else:
            return Controller.format_response(errors=18,status_code=404)  

    @Controller.route('/tournaments/<cod_tournament>/<initials>/members', methods=['POST'])
    @Controller.authenticate_user
    def add_team_to_tournament(cod_tournament,initials):
        tournament = TournamentsModel.find_by_cod_tournament(cod_tournament)
        team = TeamsModel.find_by_initials(initials)
        current_user = Controller.authenticated_user()
        #Verifica se existe o torneio e o time
        if tournament and team:
            team = team[0]
            tournament = tournament[0]
            moderator = ModerationsModel.find_moderation(current_user.login, cod_tournament)
            #Verifica se o usuário atual é moderador ou dono do torneio
            if moderator or current_user.login == tournament.owner_login:
                members = team.view_members_in_team()
                for member in members:
                    try:
                        tournament.add_member_to_tournament(member['participant_login'], initials, cod_tournament)
                    except:
                        return Controller.format_response(errors=19 ,status_code=404)
                return Controller.format_response(status_code=201)
            
            else:
                return Controller.format_response(errors=13, status_code=404)

        else:
            return Controller.format_response(errors=18, status_code=404)  


    @Controller.route('/tournaments/<cod_tournament>/<initials>/members', methods=['DELETE'])
    @Controller.authenticate_user
    def delete_team_to_tournament(cod_tournament,initials):
        tournament = TournamentsModel.find_by_cod_tournament(cod_tournament)
        team = TeamsModel.find_by_initials(initials)
        current_user = Controller.authenticated_user()
        #Verifica se existe o torneio e o time
        if tournament and team:
            team = team[0]
            tournament = tournament[0]
            moderator = ModerationsModel.find_moderation(current_user.login, cod_tournament)
            #Verifica se o usuário atual é moderador ou dono do torneio
            if moderator or current_user.login == tournament.owner_login:
                members = tournament.view_members_in_tournament(initials) #Pega os membros do time no torneio
                if members:
                    for member in members:
                        try:
                            tournament.delete_member_to_tournament(member['participant_login'], initials, cod_tournament)
                        except:
                            return Controller.format_response(errors=0 ,status_code=404)
                    return Controller.format_response(status_code=200)
                else:
                    return Controller.format_response(errors=20 ,status_code=404)
            
            else:
                return Controller.format_response(errors=13, status_code=404)

        else:
            return Controller.format_response(errors=18, status_code=404)  

    