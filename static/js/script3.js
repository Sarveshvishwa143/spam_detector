// JavaScript function to show the Sign-Up form and hide the Login form
function showSignUp() {
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('signup-container').style.display = 'block';
}

// JavaScript function to show the Login form and hide the Sign-Up form
function showLogin() {
    document.getElementById('signup-container').style.display = 'none';
    document.getElementById('login-container').style.display = 'block';
}
