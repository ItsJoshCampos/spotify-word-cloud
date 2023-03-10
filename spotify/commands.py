from spotify.config import auth_header
from requests import get

def get_new_releases(token):
    url = "https://api.spotify.com/v1/browse/new-releases"
    query = "?country=US&limit=10&offset=1"
    headers = auth_header(token)

    query_url = url + query
    result = get(query_url, headers=headers)
    albums = result.json()
    return albums