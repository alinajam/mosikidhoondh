import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

def convertName(name):
    client_id = '85725aa023e545729e6630b2a369cf90'
    client_secret = '1abf0e31be774f2d9fb434adb538ae87'
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        print(artist['uri'])
        print(artist['name'], artist['images'][0]['url'])

convertName('Tame Impala')