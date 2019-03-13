import re
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def Check_First_Name(first_name):
    first_name = first_name.strip()
    message = ""
    if first_name == "":
        message = "Please Enter the First Name"
        return {'check': False, 'error': message}

    for c in first_name:
        if c.isalpha() == False:
            message = "First Name can contain only alphabets"
            return {'check': False, 'error': message}
            break
    return {'check': True, 'error': message}

def Check_Last_Name(last_name):
    last_name = last_name.strip()
    message = ""
    if last_name == "":
        message = "Please Enter the Last Name"
        return {'check': False, 'error': message}

    for c in last_name:
        if c.isalpha() == False:
            message = "Last Name can contain only alphabets"
            return {'check': False, 'error': message}
            break
    return {'check': True, 'error': message}

def Check_User_Name(user_name):
    user_name = user_name.strip()
    message = ""
    if user_name == "":
        message = "Please Enter the User Name"
        return {'check': False, 'error': message}

    for c in first_name:
        if c.isalnum() == False and c != '_':
            message = "User Name can contain only alphanumeric characters and underscore"
            return {'check': False, 'error': message}
            break
    return {'check': True, 'error': message}

def Check_Email(email):
    email = email.strip()
    message = ""
    if email == "":
        message = "Please Enter the Email"
        return {'check': False, 'error': message}
    if not EMAIL_REGEX.match(email):
        message = "Invalid Email"
        return {'check': False, 'error': message}
    return {'check': True, 'error': message}


def Check_Password(password):
    message=""
    for c in password:
        if c.isspace()==True:
            message="Password can't contain white spaces"
            return {'check': False, 'error': message}
    if len(password) < 8:
        message = "Password should contain a minimum of 8 characters"
        return {'check': False, 'error': message}
    return {'check': True, 'error': message}

def Confirm_Password(password1,password2):
    message = ""
    if password1 != password2:
        message = "Password and Confirm Password not matching"
        return {'check': False, 'error': message}
    return {'check': True, 'error': message}


def Check_Contact(contact):
    message = ""
    for c in contact:
        if c.isdigit() == False:
            message = "Contact No. should only contain digits"
            return {'check': False, 'error': message}
    if len(contact) != 10:
        message = "Contact No. should contain exactly 10 digits"
        return {'check': False, 'error': message}
    return {'check': True, 'error': message}
