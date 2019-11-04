$(window).on('ready', function(event, user){
    paths = document.location.toString().split('/');
    cod = paths[paths.length - 1];
    API.getTournament(cod, function(request, data) {
        if (!data) {
            notFoundTournament();
        } else {
            tournamentMain(data);
        }
        
    });
});

function notFoundTournament() {
    disableLoader();
    $('.tournament-not-found').show();
}

function tournamentMain(tournament) {
    disableLoader();
    setTitle(tournament.name + ' - Torneio');
    $('.tournament-info-card').show();
}