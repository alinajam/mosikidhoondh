#For a given country, finds top playlists on Spotify with music from that country,
#and pulls however many songs desired from these playlists. ('Pakistan' is 
# starter case) 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

foreigntracks = [] 
client_id = '85725aa023e545729e6630b2a369cf90'
client_secret = '1abf0e31be774f2d9fb434adb538ae87'
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
rawresults = spotify.search(q='playlist:Pakistan', type='playlist', limit=2)
playlisturls = rawresults['playlists']['items']
trackone = spotify.playlist_tracks('39DYnMMo49JrKyum8WdBnl', limit=3)
for i in range(0, len(trackone['items'])) :
    foreigntracks.append(trackone['items'][i]['track']['id'])
print(foreigntracks)