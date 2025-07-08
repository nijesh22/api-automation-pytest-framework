

def create_post_payload(title="new title", body="new body"):
    return {
        "title": title,
        "body": body
    }

def create_login_payload(email=None, password=None):
    payload = {}
    if email is not None:
        payload["email"] = email
    if password is not None:
        payload["password"] = password
    return payload

def create_user_payload(name="John", job="QA Engineer"):

    return {
        "name": name,
        "job": job
    }

def create_register_payload(email="eve.holt@reqres.in", password="pistol"):

    return {
        "email": email,
        "password": password
    }

def create_update_post_payload(title="updated title", body="updated body"):

    return {
        "title": title,
        "body": body
    }


def create_update_user_payload(name="morpheus updated", job="zion resident updated"):

    return {
        "name": name,
        "job": job
    }

def create_user_payloads(name="John", job="Engineer", age=None, isAdmin=None):

    payload = {
        "name": name,
        "job": job
    }
    if age is not None:
        payload["age"] = age
    if isAdmin is not None:
        payload["isAdmin"] = isAdmin
    return payload