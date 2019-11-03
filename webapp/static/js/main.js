function notify(message, actionText, actionHandler, timeout) {
    let notification = document.querySelector('.mdl-js-snackbar');
    let data = {
        message: message,
        actionText: actionText,
        actionHandler: actionHandler,
        timeout: timeout || 3000
    };
    notification.MaterialSnackbar.showSnackbar(data);
}

function getJWTToken() {
    return Cookies.get('jwt_token');
}

function getCurrentLogin() {
    let token = getJWTToken();
    if (token) {
        return jwt_decode(token).identity;
    }
    return null;
}

function setJWTToken(token) {
    Cookies.set('jwt_token', token);
}