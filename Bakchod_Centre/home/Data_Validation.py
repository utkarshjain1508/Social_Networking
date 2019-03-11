import re
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def Check_First_Name(first_name):
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
    message = ""
    if email == "":
        message = "Please Enter the Email"
        return {'check': False, 'error': message}
    if not EMAIL_REGEX.match(email):
        message = "Invalid Email"
        return {'check': False, 'error': message}
    return {'check': True, 'error': message}
