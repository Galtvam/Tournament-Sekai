from flask import jsonify, request

from controllers import Controller
from models import StatisticsModel

class StatisticsController(Controller):

    @Controller.route('/statistics/periodic-tournament-partcipant', methods=['POST'])
    @Controller.json_request
    def get_periodic_tournament_participant():
        data = request.get_json()
        result = StatisticsModel.periodic_tournament_participant(data['start_data'], data['end_data'])
        return Controller.format_response(result, status_code=200)

    
    @Controller.route('/statistics/most-diferent-team-participation', methods=['POST'])
    def get_most_diferent_team_participation():
        result = StatisticsModel.most_diferent_team_participation()
        return Controller.format_response(result, status_code=200)
    

    @Controller.route('/statistics/biggest-winners', methods=['POST'])
    def get_biggest_winners():
        result = StatisticsModel.biggest_winners()
        return Controller.format_response(result, status_code=200)

    
    @Controller.route('/statistics/biggest-winners-teams', methods=['POST'])
    def get_biggest_winners_teams():
        result = StatisticsModel.biggest_winners_teams()
        return Controller.format_response(result, status_code=200)
    

    @Controller.route('/statistics/biggest-match-winners', methods=['POST'])
    def get_biggest_match_winners():
        result = StatisticsModel.biggest_match_winners()
        return Controller.format_response(result, status_code=200)
    

    @Controller.route('/statistics/biggest-match-winners-teams', methods=['POST'])
    def get_biggest_match_winners_teams():
        result = StatisticsModel.biggest_match_winners_teams()
        return Controller.format_response(result, status_code=200)
    

    @Controller.route('/statistics/participants-one-attribute', methods=['POST'])
    def get_participants_information_one_attribute():
        data = request.get_json()
        result = StatisticsModel.participants_information_one_attribute(data['attribute'], data['cod_tournament'])
        return Controller.format_response(result, status_code=200)
    
    
    @Controller.route('/statistics/best-participants-one-attribute', methods=['POST'])
    def get_best_participants_information_one_attribute():
        data = request.get_json()
        result = StatisticsModel.best_participants_information_one_attribute(data['attribute'], data['cod_tournament'])
        return Controller.format_response(result, status_code=200)
    

    @Controller.route('/statistics/worst-participants-one-attribute', methods=['POST'])
    def get_worst_participants_information_one_attribute():
        data = request.get_json()
        result = StatisticsModel.worst_participants_information_one_attribute(data['attribute'], data['cod_tournament'])
        return Controller.format_response(result, status_code=200)