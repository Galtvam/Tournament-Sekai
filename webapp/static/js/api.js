var API_HOST = 'http://localhost:8080/'

class API {
    static login(credentials, callback) {
        API.request('sign-in', 'POST', credentials, callback);
    }

    static register(data, callback) {
        API.request('sign-up', 'POST', data, callback);
    }

    static getUser(login, callback) {
        API.request('users/' + login, 'GET', {}, callback);
    }

    static getTournament(cod, callback) {
        if (cod == 1) {
            callback(null, null);
        } else {
            callback(null, {cod_tournament: cod, name: 'Melhor Torneio de Yu-gi-oh'});
        }
    }

    static request(route, method, data, callback) {
        $.ajax({
            type: method,
            url: API_HOST + route,
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(data),
            dataType: 'json',
            beforeSend: function(request) {
                let authorizationToken = getJWTToken();
                if (authorizationToken) {
                    request.setRequestHeader('Authorization', 'Bearer ' + authorizationToken);
                }
            },
            success: function(data) {
                callback(null, data);
            },
            error: function(request, error) {
                callback(request, null);
            }
        });
    }
}