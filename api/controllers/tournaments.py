from flask import jsonify, request

from controllers import Controller
from models import TournamentsModel

class TournamentsController(Controller):


    #/tournaments?code=&name=
    @Controller.route('/tournaments')
    def get():
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
    
    @Controller.route('/tournaments', methods=['POST'])
    @Controller.authenticate_user
    def create():
        current_user = Controller.authenticated_user()
        data = request.get_json()
        tournament = TournamentsModel(data['name'], data['description'],
        data['start_date'], data['end_date'], current_user.login)

        tournament.insert()
        return Controller.format_response(status_code=201)

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
            return Controller.format_response(status_code=200)
        
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

    @Controller.route('/<cod_tournaments>/<initials>/members', methods=['GET'])   
    def view_members(cod_tournament, initials):
        tournament = TournamentsModel.find_by_cod_tournament(int(code))
        team = TeamsModel.find_by_initials(initials)
        if tournament and team:
            pass #falta
        else:
            return Controller.format_response(status_code=404)  

    @Controller.route('/<cod_tournaments>/<initials>/members', methods=['POST'])
    def add_member(cod_tournament,initials):
        tournament = TournamentsModel.find_by_cod_tournament(int(code))
        team = TeamsModel.find_by_initials(initials)
        if tournament and team:
            pass #falta

        else:
            return Controller.format_response(status_code=404)  

