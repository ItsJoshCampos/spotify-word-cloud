import spotify.settings
from requests import post
import base64

def get_api_token():
    url = "https://accounts.spotify.com/api/token"

    auth_requirement = f"{spotify.settings.CLIENT_ID}:{spotify.settings.CLIENT_SECRET}"
    auth_bytes = auth_requirement.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes)
    auth = auth_base64.decode('utf-8')

    headers = {
        "Authorization": "Basic " + auth,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    token = result.json()['access_token']
    return token

def auth_header(token):
    return {"Authorization": "Bearer " + token}
