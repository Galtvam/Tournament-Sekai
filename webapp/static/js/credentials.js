// #############################
//            Login
// #############################

//Elements
$loginForm = $('#loginForm');
$loginFields = $('#loginForm input');
$loginFormSubmitButton = $('#loginFormSubmitButton');

$loginFormSubmitButton.click(function() {
    $loginFields.each(function() {
        if ($(this).is('[data-required]')) {
            $(this).prop('required', true);
            if (!$(this).val()) {
                $(this).parent().addClass('is-invalid');
            }
        }
    });
});

//Event Listeners
$loginForm.submit(function(event) {
    event.preventDefault();
    let data = $loginForm.serializeObject();
    
    API.login(data, function(request, data){
        if (request != null) {
            request.responseJSON.errors.forEach(error => {
                notify(error.message);
            });
        } else {
            data = data.data;
            setJWTToken(data.token);
            document.location = '/dashboard';
        }
    });
    return false;
});


// #############################
//            Signup
// #############################

//Elements
$signupForm = $('#signupForm');
$signupFields = $('#signupForm input');
$signupFormSubmitButton = $('#signupFormSubmitButton');

$signupFormSubmitButton.click(function() {
    $signupFields.each(function() {
        if ($(this).is('[data-required]')) {
            $(this).prop('required', true);
            if (!$(this).val()) {
                $(this).parent().addClass('is-invalid');
            }
        }
    });
});

//Event Listeners
$signupForm.submit(function(event) {
    event.preventDefault();

    let data = $signupForm.serializeObject();
    data.birthday = formatDate($signupForm.find('input[name="birthday"]')[0].valueAsDate);

    if (data.password != data.confirm_password) {
        notify('As senhas não coincidiem');
    } else {
        API.register(data, function(request, data){
            if (request != null) {
                request.responseJSON.errors.forEach(error => {
                    notify(error.message);
                });
            } else {
                document.location = '/';
            }
        });
    }
});
