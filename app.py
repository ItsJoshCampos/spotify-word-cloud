import spotify
import json

spotify_token = spotify.get_api_token()
#print(spotify_token)

# albums = spotify.get_new_releases(spotify_token)
# print(albums)
artist = spotify.get_artist(spotify_token, "redimi2")
#print(artist)

spotify.get_recommendations(spotify_token, artist["id"])


# # Serializing json
# json_object = json.dumps(albums, indent=4)
 
# # Writing to sample.json
# with open("spotify_payload.json", "w") as outfile:
#     outfile.write(json_object)