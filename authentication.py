import requests

def authenticate_user(username, password):
    response = requests.post('https://api.example.com/auth', json={'username': username, 'password': password})
    if response.status_code == 200:
        return True
    return False

