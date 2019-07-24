function hasWhiteSpace(s){
    return s.indexOf(' ') >= 0;
}

function verifyCaptcha(){
    document.getElementById('g-recaptcha-error').innerHTML = '';
}

function validateForm(username_list, email_list, response){
    var first_name = document.forms["myForm"]["first_name"].value;
    var last_name = document.forms["myForm"]["last_name"].value;
    var username = document.forms["myForm"]["username"].value;
    var user_email = document.forms["myForm"]["user_email"].value;
    var password = document.forms["myForm"]["password"].value;
    var confirm_password = document.forms["myForm"]["confirm_password"].value;
    var contact = document.forms["myForm"]["contact"].value;

    first_name = first_name.trim();
    last_name = last_name.trim();
    username = username.trim();
    user_email = user_email.trim();
    contact = contact.trim();

    // Regular Expressions
    var reg_letters = /^[A-Za-z]+$/;
    var reg_username = /^[a-zA-Z0-9\_]+$/;
    var reg_user_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var reg_contact = /^[0-9]{10}$/;

    // First Name
    if (first_name == "") {
        document.getElementById('first_name').innerHTML = "Please enter your First Name";
        return false;
    }
    else if (!(first_name.match(reg_letters))) {
        document.getElementById('first_name').innerHTML = "First Name can contain only alphabets";
        return false;
    }
    else if(first_name.length > 100){
        document.getElementById('first_name').innerHTML = "Character limit exceeded";
        return false;
    }
    else {
        document.getElementById('first_name').innerHTML = "";
    }

    // Last Name
    if (last_name == "") {
        document.getElementById('last_name').innerHTML = "Please enter your Last Name";
        return false;
    }
    else if (!(last_name.match(reg_letters))) {
        document.getElementById('last_name').innerHTML = "Last Name can contain only alphabets";
        return false;
    }
    else if(last_name.length > 100){
        document.getElementById('last_name').innerHTML = "Character limit exceeded";
        return false;
    }
    else {
        document.getElementById('last_name').innerHTML = "";
    }

    // Username
    if(username == ""){
        document.getElementById('username').innerHTML = "Please enter your Username";
        return false;
    }
    else if(!(username.match(reg_username))) {
        document.getElementById('username').innerHTML = "UserName can contain only alphanumeric characters and Underscore";
        return false;
    }
    else if(username.length > 100) {
        document.getElementById('username').innerHTML = "Character limit exceeded";
        return false;
    }
    else {
        document.getElementById('username').innerHTML = "";
    }

    for (i = 0; i < username_list.length; i++) {
        if(username_list[i] == username){
            document.getElementById('username').innerHTML = "This username already exists.";
            return false;
        }
    }
    document.getElementById('username').innerHTML = "";

    // Email
    if (user_email == "") {
        document.getElementById('user_email').innerHTML = "Please enter your email";
        return false;
    }
    else if (!(user_email.match(reg_user_email))) {
        document.getElementById('user_email').innerHTML = "Invalid Email Address";
        return false;
    }
    else if (user_email.length > 100) {
        document.getElementById('user_email').innerHTML = "Character limit exceeded";
        return false;
    }
    else {
        document.getElementById('user_email').innerHTML = "";
    }

    for (i = 0; i < email_list.length; i++) {
        if(email_list[i] == user_email){
            document.getElementById('user_email').innerHTML = "This email is already used by another account.";
            return false;
        }
    }
    document.getElementById('user_email').innerHTML = "";

    // Password
    if (password == "") {
        document.getElementById('password').innerHTML = "Please enter the password";
        return false;
    }
    else if (hasWhiteSpace(password)){
        document.getElementById('password').innerHTML = "Password can't contain white spaces";
        return false;
    }
    else if (password.length < 8) {
        document.getElementById('password').innerHTML = "Password should contain a minimum of 8 characters";
        return false;
    }
    else if (password.length > 100) {
        document.getElementById('password').innerHTML = "Character limit exceeded";
        return false;
    }
    else {
        document.getElementById('password').innerHTML = "";
    }

    // Confirm Password
    if (confirm_password == "") {
        document.getElementById('confirm_password').innerHTML = "Please Confirm the password";
        return false;
    }
    else if (password != confirm_password) {
        document.getElementById('confirm_password').innerHTML = "Password and Confirm Password not matching";
        return false;
    }
    else {
        document.getElementById('confirm_password').innerHTML = "";
    }

    // Contact
    if (contact == "") {
        document.getElementById('contact').innerHTML = "Please enter your Contact Number";
        return false;
    }
    else if (!(contact.match(reg_contact))) {
        document.getElementById('contact').innerHTML = "Contact should contain exactly 10 digits";
        return false;
    }
    else {
        document.getElementById('contact').innerHTML = "";
    }

    if(typeof response == 'undefined') {
        document.getElementById('g-recaptcha-error').innerHTML = 'Validate captcha to signup';
        return false;
    }
    else{
        document.getElementById('g-recaptcha-error').innerHTML = '';
    }

    return true;
}
