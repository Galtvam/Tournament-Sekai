$(window).on('load', function() {
    if (!getCurrentLogin()) {
        document.location = '/';
    } else {
        API.getUser(getCurrentLogin(), function(request, data) {
            if (!data) {
                document.location = '/';
            } else {
                $(window).trigger('ready', [data.data]);
            }
        })
    }
});

function disableLoader() {
    $('#loader').fadeOut('slow');
}

function setDashboardTitle(title) {
    $('#toolbar-title').html(title);
}