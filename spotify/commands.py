from spotify.config import auth_header
import requests

def get_new_releases(token):
    url = "https://api.spotify.com/v1/browse/new-releases"
    query = "?country=US&limit=10&offset=1"
    headers = auth_header(token)

    query_url = url + query
    result = requests.get(query_url, headers=headers)
    albums = result.json()
    return albums

def get_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name}&type=artist&limit=1"
    headers = auth_header(token)

    url_query = url + query
    result = requests.get(url_query, headers=headers)
    result_json = result.json()
    artist = result_json["artists"]["items"]
    if len(artist) > 0:
        return artist[0]
    
    print("No Artist Found.")
    return None

def get_recommendations(token, artist_ids):
    url = "https://api.spotify.com/v1/recommendations?"
    query = f"?market=US&seed_artists={artist_ids}"
    headers = auth_header(token)

    url_query = url + query
    result = requests.get(url_query, headers=headers)
    result_json = result.json()
    recommendations = result_json["tracks"]
    if len(recommendations) > 0:
        for idx, track in enumerate(recommendations):
            print(f"{idx + 1}.\tArtist: {track['artists'][0]['name']}\n\tAlbum: {track['album']['name']}\n\tTrack: {track['name']}")
    else:
        print("No Recommendations Found.")