import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

client_id = '90a2b01df2ef44b3a468ae6433ade20a'
client_secret = 'eae24e7a15d84220a2947c2a8023d4e2'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API
name = "Halsey" #chosen artist
result = sp.search(name) #search query
result['tracks']['items'][0]['artists']