import spotify

spotify_token = spotify.get_api_token()

# print(spotify_token)

albums = spotify.get_new_releases(spotify_token)

print(albums)