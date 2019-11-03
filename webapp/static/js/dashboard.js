$(window).on('load', function() {
    if (!getCurrentLogin()) {
        document.location = '/';
    } else {
        API.getUser(getCurrentLogin(), function(request, data) {
            if (!data) {
                document.location = '/';
            } else {
                disableLoader();
                main(data.data);
            }
        })
    }
});

function disableLoader() {
    $('#loader').fadeOut('slow');
}

function main(user) {
    console.log(user);
    
}