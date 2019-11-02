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
    $loginForm.submit();
});

//Event Listeners
$loginForm.submit(function(event) {
    event.preventDefault();
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
    $signupForm.submit();
});

//Event Listeners
$signupForm.submit(function(event) {
    event.preventDefault();
});
